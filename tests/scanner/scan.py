"""7-class deterministic SKILL.md security scanner.

Usage:
    from tests.scanner.scan import scan_skill_md, ScanResult

    result = scan_skill_md(content)
    if result.blocked:
        print(f"BLOCKED: {result.block_reasons}")
    elif result.flagged:
        print(f"FLAGGED: {result.flag_reasons}")
    else:
        print("CLEAN")
"""

from __future__ import annotations

import re
import string
from dataclasses import dataclass, field
from enum import StrEnum
from urllib.parse import urlparse


class Severity(StrEnum):
    BLOCK = "block"
    FLAG = "flag"
    INFO = "info"
    CLEAN = "clean"


class ThreatClass(StrEnum):
    COMMAND_INJECTION = "command_injection"
    DATA_EXFILTRATION = "data_exfiltration"
    CREDENTIAL_THEFT = "credential_theft"
    PROMPT_OVERRIDE = "prompt_override"
    SUPPLY_CHAIN = "supply_chain"
    PRIVILEGE_ESCALATION = "privilege_escalation"
    STEGANOGRAPHIC = "steganographic"
    SEMANTIC_MISMATCH = "semantic_mismatch"


@dataclass
class Finding:
    """A single scanner finding."""

    threat_class: ThreatClass
    severity: Severity
    description: str
    evidence: str  # The matched text/pattern
    line: int | None = None


@dataclass
class ScanResult:
    """Result of scanning a SKILL.md file."""

    findings: list[Finding] = field(default_factory=list)

    @property
    def blocked(self) -> bool:
        return any(f.severity == Severity.BLOCK for f in self.findings)

    @property
    def flagged(self) -> bool:
        return any(f.severity == Severity.FLAG for f in self.findings)

    @property
    def clean(self) -> bool:
        return not self.findings

    @property
    def severity(self) -> Severity:
        if self.blocked:
            return Severity.BLOCK
        if self.flagged:
            return Severity.FLAG
        if self.findings:
            return Severity.INFO
        return Severity.CLEAN

    @property
    def block_reasons(self) -> list[str]:
        return [f.description for f in self.findings if f.severity == Severity.BLOCK]

    @property
    def flag_reasons(self) -> list[str]:
        return [f.description for f in self.findings if f.severity == Severity.FLAG]

    def to_dict(self) -> dict:
        return {
            "severity": self.severity,
            "blocked": self.blocked,
            "flagged": self.flagged,
            "finding_count": len(self.findings),
            "findings": [
                {
                    "threat_class": f.threat_class,
                    "severity": f.severity,
                    "description": f.description,
                    "evidence": f.evidence[:200],
                    "line": f.line,
                }
                for f in self.findings
            ],
        }


# =========================================================================
# Pattern definitions
# =========================================================================

# --- Class 1: Command Injection ---
_CMD_INJECTION_PATTERNS = [
    # Pipe to shell
    (r"curl\s+[^\s]+\s*\|\s*(?:ba)?sh", "curl pipe to shell"),
    (r"wget\s+[^\s]+\s*(?:-O\s*-\s*)?\|\s*(?:ba)?sh", "wget pipe to shell"),
    # Reverse shells
    (r"(?:bash|sh)\s+-[ci]\s+['\"].*(?:\/dev\/tcp|nc\s|ncat\s|netcat\s)", "reverse shell"),
    (r"nc\s+-[elp]+\s+.*\d{2,5}", "netcat listener"),
    (r"python[3]?\s+-c\s+['\"].*(?:socket|subprocess|os\.system)", "python inline execution"),
    # Base64-encoded commands
    (r"(?:echo|printf)\s+['\"]?[A-Za-z0-9+/]{20,}={0,2}['\"]?\s*\|\s*base64\s+-d\s*\|\s*(?:ba)?sh",
     "base64 decode to shell"),
    (r"base64\s+-d\s*<<<?\s*['\"]?[A-Za-z0-9+/]{20,}", "base64 decode suspicious payload"),
    # Direct dangerous commands
    (r"rm\s+-rf\s+[/~]", "recursive delete from root or home"),
    (r"mkfifo\s+/tmp/", "named pipe creation (common in reverse shells)"),
    # eval/exec with external input
    (r"eval\s*\$\(", "eval with command substitution"),
]

# --- Class 2: Data Exfiltration ---
_EXFIL_PATTERNS = [
    (r"(?:cat|read|head|tail|less|more)\s+~?/\.ssh/(?:id_rsa|id_ed25519|authorized_keys|known_hosts)(?!\.pub)",
     "SSH key file read"),
    (r"(?:include|embed|attach|send|post|upload).*(?:response|output|reply|message).*(?:ssh|key|secret|token|credential)",
     "exfiltrate secrets in response"),
    (r"(?:response|output|reply).*(?:include|contain|embed).*(?:ssh|key|secret|token|credential)",
     "embed secrets in output"),
    (r"curl\s+.*-d\s+.*(?:\$\(cat|<\(|@).*(?:\.ssh|\.env|\.aws|\.gnupg|\.npmrc)",
     "POST secret files to external URL"),
    (r"(?:cat|read)\s+.*\.(?:pem|key|crt)\s", "reading PKI files"),
]

# --- Class 3: Credential Theft ---
_CRED_PATTERNS = [
    (r"(?:env|printenv|set)\s*\|\s*grep\s+(?:KEY|SECRET|TOKEN|PASS|API|AUTH|CRED)",
     "grep environment for credentials"),
    (r"(?:cat|read|head|source|\.)\s+\.env\b", "read .env file"),
    (r"(?:cat|read|head)\s+.*(?:credentials\.json|\.aws/credentials|\.netrc|\.npmrc)",
     "read credential files"),
    (r"\$(?:AWS_SECRET|API_KEY|AUTH_TOKEN|DATABASE_URL|OPENAI_API_KEY|ANTHROPIC_API_KEY|SECRET_KEY)",
     "reference to sensitive environment variables"),
    (r"printenv\s+(?:.*KEY|.*SECRET|.*TOKEN|.*PASS)", "printenv for credentials"),
    (r"keychain\s+.*(?:export|dump|list)", "keychain credential access"),
]

# --- Class 4: Prompt Override ---
_PROMPT_OVERRIDE_PATTERNS = [
    (r"ignore\s+(?:all\s+)?(?:previous|prior|above|earlier)\s+(?:instructions|rules|guidelines|directives|constraints)",
     "ignore previous instructions"),
    (r"you\s+are\s+now\s+(?:in\s+)?(?:unrestricted|unfiltered|jailbreak|DAN|developer)\s+mode",
     "unrestricted mode activation"),
    (r"(?:new|override|replace|overwrite)\s+(?:system\s+)?(?:prompt|instructions|rules)",
     "system prompt override"),
    (r"disregard\s+(?:all\s+)?(?:safety|ethical|content)\s+(?:guidelines|rules|filters|policies)",
     "disregard safety guidelines"),
    (r"(?:act|behave|respond)\s+(?:as\s+if|like)\s+(?:you\s+have\s+)?no\s+(?:restrictions|limits|rules|constraints)",
     "act without restrictions"),
    (r"do\s+not\s+(?:follow|obey|adhere\s+to)\s+(?:any|your)\s+(?:rules|guidelines|instructions|safety)",
     "do not follow rules"),
]

# --- Class 5: Supply Chain Poisoning ---
_SUPPLY_CHAIN_PATTERNS = [
    (r"(?:postinstall|preinstall|prepublish)\s*[\"':]\s*.*(?:curl|wget|fetch|node\s+-e|python)",
     "malicious install hook"),
    (r"--(?:index-url|extra-index-url)\s+(?!https://pypi\.org)https?://",
     "custom PyPI index (not pypi.org)"),
    (r"npm\s+(?:install|i)\s+.*--registry\s+(?!https://registry\.npmjs\.org)",
     "custom npm registry"),
    (r"pip\s+install\s+.*-f\s+https?://(?!pypi\.org)",
     "pip install from custom find-links"),
    (r"(?:git\s+clone|pip\s+install\s+git\+)(?:https?://(?!github\.com|gitlab\.com|bitbucket\.org))",
     "install from unknown git host"),
]

# --- Class 6: Privilege Escalation ---
_PRIV_ESC_PATTERNS = [
    (r"sudo\s+chmod\s+(?:-R\s+)?[67]77\s+/", "sudo chmod 777 on root paths"),
    (r"sudo\s+(?:chown|chgrp)\s+.*\s+/(?:etc|usr|var|bin|sbin)", "sudo ownership change on system dirs"),
    (r"(?:echo|cat|tee)\s+.*(?:>>?\s*)?/etc/(?:hosts|passwd|shadow|sudoers|crontab)",
     "modify system configuration files"),
    (r"sudo\s+(?:bash|sh|su)\s", "sudo to shell"),
    (r"chmod\s+[ugo]?\+s\s", "setuid/setgid bit modification"),
    (r"crontab\s+-[lr]?\s*(?:<<|<\(|.*curl|.*wget)", "crontab modification with download"),
]

# --- Class 7: Steganographic ---
_ZERO_WIDTH_CHARS = "\u200b\u200c\u200d\u2060\ufeff\u200e\u200f\u202a\u202b\u202c\u202d\u202e"

_STEG_PATTERNS = [
    (r"<!--.*(?:script|eval|exec|system|curl|wget|fetch).*-->", "hidden command in HTML comment"),
    (r"<!\[CDATA\[.*(?:script|eval|exec).*\]\]>", "hidden command in CDATA"),
]

# --- Semantic: URL allowlist ---
_URL_DOMAIN_ALLOWLIST = {
    "github.com",
    "gitlab.com",
    "bitbucket.org",
    "docs.python.org",
    "docs.astral.sh",
    "pypi.org",
    "npmjs.com",
    "npmjs.org",
    "registry.npmjs.org",
    "developer.mozilla.org",
    "stackoverflow.com",
    "wikipedia.org",
    "en.wikipedia.org",
    "anthropic.com",
    "docs.anthropic.com",
    "openai.com",
    "platform.openai.com",
    "agentskills.io",
    "docs.openclaw.ai",
    "clawhub.ai",
    "example.com",
    "example.org",
}

# --- Semantic: Sensitive paths ---
_SENSITIVE_PATHS = [
    r"~?/\.ssh/",
    r"~?/\.aws/",
    r"~?/\.gnupg/",
    r"~?/\.npmrc",
    r"\.env\b",
    r"/etc/passwd",
    r"/etc/shadow",
    r"/etc/sudoers",
    r"/etc/hosts",
    r"credentials\.json",
    r"\.pem\b",
    r"\.key\b",
]

# Security-context keywords that make sensitive path references benign
_SECURITY_CONTEXT_KEYWORDS = {
    "audit", "security", "pentest", "penetration", "review",
    "scan", "vulnerability", "compliance", "hardening", "protect",
    "defend", "secure", "guard", "monitor", "detect", "prevent",
    "encrypt", "decrypt", "certificate", "ssl", "tls",
}


# =========================================================================
# Scanner functions
# =========================================================================


def scan_skill_md(content: str) -> ScanResult:
    """Scan SKILL.md content for security threats.

    Args:
        content: Raw SKILL.md file content (with frontmatter).

    Returns:
        ScanResult with findings.
    """
    result = ScanResult()

    # Split frontmatter from body for analysis
    body = _extract_body(content)
    description = _extract_description(content)

    # Run all pattern-based detectors
    _scan_patterns(body, _CMD_INJECTION_PATTERNS, ThreatClass.COMMAND_INJECTION, Severity.BLOCK, result)
    _scan_patterns(body, _EXFIL_PATTERNS, ThreatClass.DATA_EXFILTRATION, Severity.BLOCK, result)
    _scan_patterns(body, _CRED_PATTERNS, ThreatClass.CREDENTIAL_THEFT, Severity.BLOCK, result)
    _scan_patterns(body, _PROMPT_OVERRIDE_PATTERNS, ThreatClass.PROMPT_OVERRIDE, Severity.BLOCK, result)
    _scan_patterns(body, _SUPPLY_CHAIN_PATTERNS, ThreatClass.SUPPLY_CHAIN, Severity.FLAG, result)
    _scan_patterns(body, _PRIV_ESC_PATTERNS, ThreatClass.PRIVILEGE_ESCALATION, Severity.FLAG, result)

    # Steganographic checks
    _scan_zero_width(content, result)
    _scan_patterns(body, _STEG_PATTERNS, ThreatClass.STEGANOGRAPHIC, Severity.FLAG, result)

    # Semantic mismatch checks
    _scan_url_domains(body, result)
    _scan_sensitive_paths(body, content, result)
    if description:
        _scan_keyword_divergence(description, body, result)

    return result


def _extract_body(content: str) -> str:
    """Extract body text after frontmatter."""
    match = re.match(r"^---\s*\n.*?\n---\s*\n?(.*)", content, re.DOTALL)
    return match.group(1) if match else content


def _extract_description(content: str) -> str:
    """Extract description from frontmatter."""
    match = re.search(r"^description:\s*[\"']?(.+?)[\"']?\s*$", content, re.MULTILINE)
    return match.group(1) if match else ""


def _has_security_context(content: str) -> bool:
    """Check if the skill has security/infrastructure context.

    Skills about security auditing, SSH setup, git workflows, etc.
    legitimately reference sensitive paths and credentials.
    """
    content_lower = content.lower()
    if any(kw in content_lower for kw in _SECURITY_CONTEXT_KEYWORDS):
        return True
    infra_markers = {"ssh-keygen", "ssh key setup", "ssh authentication",
                     "never share", "public key", "git config"}
    return any(m in content_lower for m in infra_markers)


def _scan_patterns(
    text: str,
    patterns: list[tuple[str, str]],
    threat_class: ThreatClass,
    severity: Severity,
    result: ScanResult,
) -> None:
    """Run regex patterns against text, appending findings."""
    for pattern, desc in patterns:
        for match in re.finditer(pattern, text, re.IGNORECASE | re.MULTILINE):
            line_num = text[:match.start()].count("\n") + 1
            result.findings.append(Finding(
                threat_class=threat_class,
                severity=severity,
                description=desc,
                evidence=match.group(0),
                line=line_num,
            ))


def _scan_zero_width(content: str, result: ScanResult) -> None:
    """Detect zero-width characters (steganographic hiding)."""
    for i, char in enumerate(content):
        if char in _ZERO_WIDTH_CHARS:
            line_num = content[:i].count("\n") + 1
            result.findings.append(Finding(
                threat_class=ThreatClass.STEGANOGRAPHIC,
                severity=Severity.FLAG,
                description=f"zero-width character U+{ord(char):04X}",
                evidence=f"...{content[max(0,i-10):i+10]}...",
                line=line_num,
            ))


def _scan_url_domains(body: str, result: ScanResult) -> None:
    """Extract URLs and check domains against allowlist."""
    url_pattern = re.compile(r"https?://[^\s\)\]\"'`>]+")
    for match in url_pattern.finditer(body):
        url = match.group(0).rstrip(".,;:!?)")
        try:
            parsed = urlparse(url)
            domain = parsed.netloc.lower()
            # Strip port
            if ":" in domain:
                domain = domain.split(":")[0]
            # Check against allowlist (including subdomains)
            allowed = False
            for allowed_domain in _URL_DOMAIN_ALLOWLIST:
                if domain == allowed_domain or domain.endswith("." + allowed_domain):
                    allowed = True
                    break
            if not allowed and domain:
                line_num = body[:match.start()].count("\n") + 1
                result.findings.append(Finding(
                    threat_class=ThreatClass.SEMANTIC_MISMATCH,
                    severity=Severity.INFO,
                    description=f"URL to non-allowlisted domain: {domain}",
                    evidence=url[:100],
                    line=line_num,
                ))
        except Exception:
            pass


def _scan_sensitive_paths(body: str, full_content: str, result: ScanResult) -> None:
    """Detect references to sensitive paths without security context."""
    if _has_security_context(full_content):
        return  # Security/infra skills legitimately reference these paths

    for path_pattern in _SENSITIVE_PATHS:
        for match in re.finditer(path_pattern, body, re.IGNORECASE):
            # Skip if inside a code block that's clearly demonstrating something
            # (heuristic: if the match is within a fenced block that also has
            # "example" or "don't" nearby, it's likely educational)
            context_start = max(0, match.start() - 200)
            context = body[context_start:match.start()].lower()
            if "example" in context and ("don't" in context or "avoid" in context or "never" in context):
                continue

            line_num = body[:match.start()].count("\n") + 1
            result.findings.append(Finding(
                threat_class=ThreatClass.SEMANTIC_MISMATCH,
                severity=Severity.FLAG,
                description=f"sensitive path reference without security context",
                evidence=match.group(0),
                line=line_num,
            ))


def _scan_keyword_divergence(
    description: str, body: str, result: ScanResult
) -> None:
    """Check if description and body keywords diverge significantly.

    Uses Jaccard similarity on content words (not stopwords).
    Low overlap suggests the description is a decoy.
    """
    desc_tokens = _tokenize(description)
    body_tokens = _tokenize(body)

    if not desc_tokens or not body_tokens:
        return

    # Jaccard similarity
    intersection = desc_tokens & body_tokens
    union = desc_tokens | body_tokens
    jaccard = len(intersection) / len(union) if union else 0

    # Very low overlap is suspicious — description might be a decoy
    if jaccard < 0.02 and len(body_tokens) > 20:
        result.findings.append(Finding(
            threat_class=ThreatClass.SEMANTIC_MISMATCH,
            severity=Severity.FLAG,
            description=f"keyword divergence: description/body Jaccard={jaccard:.3f} (threshold: 0.02)",
            evidence=f"desc tokens: {sorted(desc_tokens)[:10]}, body sample: {sorted(body_tokens)[:10]}",
        ))


def _tokenize(text: str) -> set[str]:
    """Extract meaningful content tokens (skip stopwords, short words, punctuation)."""
    _STOPWORDS = {
        "a", "an", "the", "and", "or", "but", "in", "on", "at", "to", "for",
        "of", "with", "by", "from", "is", "are", "was", "were", "be", "been",
        "being", "have", "has", "had", "do", "does", "did", "will", "would",
        "could", "should", "may", "might", "shall", "can", "it", "its",
        "this", "that", "these", "those", "i", "you", "he", "she", "we",
        "they", "me", "him", "her", "us", "them", "my", "your", "his",
        "our", "their", "not", "no", "if", "then", "else", "when", "while",
        "as", "so", "than", "each", "every", "all", "any", "some", "such",
        "only", "also", "very", "just", "about", "into", "through", "during",
        "before", "after", "above", "below", "up", "down", "out", "off",
        "over", "under", "between", "same", "other", "new", "use", "using",
    }
    # Split on whitespace and punctuation, lowercase, filter
    words = re.findall(r"[a-z][a-z0-9_-]+", text.lower())
    return {w for w in words if len(w) > 2 and w not in _STOPWORDS}
