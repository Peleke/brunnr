"""Sensitive path detection — flags references without security context."""

from __future__ import annotations

import re

from brunnr.scanner.context import ScanContext
from brunnr.scanner.types import Finding, Severity, ThreatClass

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

_SECURITY_CONTEXT_KEYWORDS = {
    "audit", "security", "pentest", "penetration", "review",
    "scan", "vulnerability", "compliance", "hardening", "protect",
    "defend", "secure", "guard", "monitor", "detect", "prevent",
    "encrypt", "decrypt", "certificate", "ssl", "tls",
}

_INFRA_MARKERS = {
    "ssh-keygen", "ssh key setup", "ssh authentication",
    "never share", "public key", "git config",
}


def _has_security_context(content: str) -> bool:
    content_lower = content.lower()
    if any(kw in content_lower for kw in _SECURITY_CONTEXT_KEYWORDS):
        return True
    return any(m in content_lower for m in _INFRA_MARKERS)


class SensitivePathRule:
    name = "sensitive_paths"

    def scan(self, ctx: ScanContext) -> list[Finding]:
        if _has_security_context(ctx.raw):
            return []

        findings: list[Finding] = []
        for path_pattern in _SENSITIVE_PATHS:
            for match in re.finditer(path_pattern, ctx.body, re.IGNORECASE):
                context_start = max(0, match.start() - 200)
                context = ctx.body[context_start : match.start()].lower()
                if "example" in context and (
                    "don't" in context or "avoid" in context or "never" in context
                ):
                    continue

                line_num = ctx.body[: match.start()].count("\n") + 1
                findings.append(
                    Finding(
                        threat_class=ThreatClass.SEMANTIC_MISMATCH,
                        severity=Severity.FLAG,
                        description="sensitive path reference without security context",
                        evidence=match.group(0),
                        line=line_num,
                    )
                )
        return findings
