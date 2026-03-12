# Scanner Architecture

brunnr's security scanner is deterministic, regex-based, and uses zero external dependencies. It runs entirely on Python's standard library -- no LLM in the scan loop, no network calls, no third-party packages.

---

## Design principles

1. **Deterministic** -- Same input produces the same output every time. No probabilistic models, no temperature settings, no API calls.
2. **Zero dependencies** -- The scanner uses only `re`, `string`, `dataclasses`, `enum`, and `urllib.parse` from Python's stdlib.
3. **Fast** -- Scanning a SKILL.md file takes milliseconds. The scanner can process hundreds of files in under a second.
4. **No false negatives by design** -- The scanner errs on the side of flagging. A legitimate skill that triggers a pattern gets reviewed. A malicious skill that evades all patterns is the failure mode to minimize.

---

## Pipeline flow

The scanner processes each SKILL.md file through a multi-stage pipeline. Every stage runs against the same content, and findings are accumulated into a single `ScanResult`.

<div style="max-width: 650px; margin: 2em auto;">
<svg viewBox="0 0 620 880" aria-label="brunnr scanner architecture: 8-stage pipeline from input to verdict">
  <defs>
    <filter id="sa-glow">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <linearGradient id="sa-flow" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#6366f1" stop-opacity="0.55"/>
      <stop offset="100%" stop-color="#6366f1" stop-opacity="0.12"/>
    </linearGradient>
    <pattern id="sa-grid" width="25" height="25" patternUnits="userSpaceOnUse">
      <path d="M 25 0 L 0 0 0 25" fill="none" stroke="#cbd5e1" stroke-width="0.4" opacity="0.2"/>
    </pattern>
  </defs>

  <!-- Background -->
  <rect width="100%" height="100%" fill="url(#sa-grid)" opacity="0.4"/>

  <!-- ===== INPUT ===== -->
  <g data-stage="input">
    <rect x="160" y="15" width="300" height="55" rx="8"
          fill="#f8fafc" stroke="#6366f1" stroke-width="2" filter="url(#sa-glow)"/>
    <text x="185" y="36" font-family="'JetBrains Mono', monospace" font-size="9"
          fill="#64748b" letter-spacing="0.05em">INPUT</text>
    <text x="185" y="56" font-family="system-ui, sans-serif" font-size="13" fill="#1e293b">
      SKILL.md raw content
    </text>
    <text x="448" y="56" font-family="'JetBrains Mono', monospace" font-size="8"
          fill="#94a3b8" text-anchor="end" opacity="0.6">frontmatter + body</text>
  </g>

  <!-- Arrow -->
  <line x1="310" y1="70" x2="310" y2="100" stroke="url(#sa-flow)" stroke-width="1.5" stroke-dasharray="4 3">
    <animate attributeName="stroke-dashoffset" from="0" to="-14" dur="2s" repeatCount="indefinite"/>
  </line>
  <polygon points="310,98 306,92 314,92" fill="#6366f1" opacity="0.4"/>

  <!-- ===== PARSE ===== -->
  <g data-stage="parse">
    <rect x="160" y="103" width="300" height="55" rx="8"
          fill="#f8fafc" stroke="#94a3b8" stroke-width="1"/>
    <text x="185" y="124" font-family="'JetBrains Mono', monospace" font-size="9"
          fill="#64748b" letter-spacing="0.05em">00 &middot; PARSE</text>
    <text x="185" y="144" font-family="system-ui, sans-serif" font-size="13" fill="#1e293b">
      Extract frontmatter + body
    </text>
    <text x="448" y="144" font-family="'JetBrains Mono', monospace" font-size="8"
          fill="#94a3b8" text-anchor="end" opacity="0.6">description, body</text>
  </g>

  <!-- Arrow -->
  <line x1="310" y1="158" x2="310" y2="188" stroke="url(#sa-flow)" stroke-width="1.5" stroke-dasharray="4 3">
    <animate attributeName="stroke-dashoffset" from="0" to="-14" dur="2s" repeatCount="indefinite"/>
  </line>
  <polygon points="310,186 306,180 314,180" fill="#6366f1" opacity="0.4"/>

  <!-- ===== CLASS 1: CMD INJECTION ===== -->
  <g data-stage="cmd-injection">
    <rect x="160" y="191" width="300" height="55" rx="8"
          fill="#fef2f2" stroke="#ef4444" stroke-width="1.5"/>
    <text x="185" y="212" font-family="'JetBrains Mono', monospace" font-size="9"
          fill="#b91c1c" letter-spacing="0.05em">01 &middot; COMMAND INJECTION</text>
    <text x="185" y="232" font-family="system-ui, sans-serif" font-size="12" fill="#1e293b">
      curl|sh, reverse shells, base64
    </text>
    <text x="448" y="232" font-family="'JetBrains Mono', monospace" font-size="8"
          fill="#ef4444" text-anchor="end">BLOCK</text>
  </g>

  <!-- Arrow -->
  <line x1="310" y1="246" x2="310" y2="262" stroke="url(#sa-flow)" stroke-width="1.5" stroke-dasharray="4 3">
    <animate attributeName="stroke-dashoffset" from="0" to="-14" dur="2s" repeatCount="indefinite"/>
  </line>
  <polygon points="310,260 306,254 314,254" fill="#6366f1" opacity="0.4"/>

  <!-- ===== CLASS 2: DATA EXFIL ===== -->
  <g data-stage="data-exfil">
    <rect x="160" y="265" width="300" height="55" rx="8"
          fill="#fef2f2" stroke="#ef4444" stroke-width="1.5"/>
    <text x="185" y="286" font-family="'JetBrains Mono', monospace" font-size="9"
          fill="#b91c1c" letter-spacing="0.05em">02 &middot; DATA EXFILTRATION</text>
    <text x="185" y="306" font-family="system-ui, sans-serif" font-size="12" fill="#1e293b">
      SSH keys, secrets in responses
    </text>
    <text x="448" y="306" font-family="'JetBrains Mono', monospace" font-size="8"
          fill="#ef4444" text-anchor="end">BLOCK</text>
  </g>

  <!-- Arrow -->
  <line x1="310" y1="320" x2="310" y2="336" stroke="url(#sa-flow)" stroke-width="1.5" stroke-dasharray="4 3">
    <animate attributeName="stroke-dashoffset" from="0" to="-14" dur="2s" repeatCount="indefinite"/>
  </line>
  <polygon points="310,334 306,328 314,328" fill="#6366f1" opacity="0.4"/>

  <!-- ===== CLASS 3: CREDENTIAL THEFT ===== -->
  <g data-stage="cred-theft">
    <rect x="160" y="339" width="300" height="55" rx="8"
          fill="#fef2f2" stroke="#ef4444" stroke-width="1.5"/>
    <text x="185" y="360" font-family="'JetBrains Mono', monospace" font-size="9"
          fill="#b91c1c" letter-spacing="0.05em">03 &middot; CREDENTIAL THEFT</text>
    <text x="185" y="380" font-family="system-ui, sans-serif" font-size="12" fill="#1e293b">
      .env, env vars, keychain access
    </text>
    <text x="448" y="380" font-family="'JetBrains Mono', monospace" font-size="8"
          fill="#ef4444" text-anchor="end">BLOCK</text>
  </g>

  <!-- Arrow -->
  <line x1="310" y1="394" x2="310" y2="410" stroke="url(#sa-flow)" stroke-width="1.5" stroke-dasharray="4 3">
    <animate attributeName="stroke-dashoffset" from="0" to="-14" dur="2s" repeatCount="indefinite"/>
  </line>
  <polygon points="310,408 306,402 314,402" fill="#6366f1" opacity="0.4"/>

  <!-- ===== CLASS 4: PROMPT OVERRIDE ===== -->
  <g data-stage="prompt-override">
    <rect x="160" y="413" width="300" height="55" rx="8"
          fill="#fef2f2" stroke="#ef4444" stroke-width="1.5"/>
    <text x="185" y="434" font-family="'JetBrains Mono', monospace" font-size="9"
          fill="#b91c1c" letter-spacing="0.05em">04 &middot; PROMPT OVERRIDE</text>
    <text x="185" y="454" font-family="system-ui, sans-serif" font-size="12" fill="#1e293b">
      Jailbreaks, instruction bypass
    </text>
    <text x="448" y="454" font-family="'JetBrains Mono', monospace" font-size="8"
          fill="#ef4444" text-anchor="end">BLOCK</text>
  </g>

  <!-- Arrow -->
  <line x1="310" y1="468" x2="310" y2="484" stroke="url(#sa-flow)" stroke-width="1.5" stroke-dasharray="4 3">
    <animate attributeName="stroke-dashoffset" from="0" to="-14" dur="2s" repeatCount="indefinite"/>
  </line>
  <polygon points="310,482 306,476 314,476" fill="#6366f1" opacity="0.4"/>

  <!-- ===== CLASS 5: SUPPLY CHAIN ===== -->
  <g data-stage="supply-chain">
    <rect x="160" y="487" width="300" height="55" rx="8"
          fill="#fffbeb" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="185" y="508" font-family="'JetBrains Mono', monospace" font-size="9"
          fill="#92400e" letter-spacing="0.05em">05 &middot; SUPPLY CHAIN</text>
    <text x="185" y="528" font-family="system-ui, sans-serif" font-size="12" fill="#1e293b">
      Custom registries, install hooks
    </text>
    <text x="448" y="528" font-family="'JetBrains Mono', monospace" font-size="8"
          fill="#f59e0b" text-anchor="end">FLAG</text>
  </g>

  <!-- Arrow -->
  <line x1="310" y1="542" x2="310" y2="558" stroke="url(#sa-flow)" stroke-width="1.5" stroke-dasharray="4 3">
    <animate attributeName="stroke-dashoffset" from="0" to="-14" dur="2s" repeatCount="indefinite"/>
  </line>
  <polygon points="310,556 306,550 314,550" fill="#6366f1" opacity="0.4"/>

  <!-- ===== CLASS 6: PRIV ESC ===== -->
  <g data-stage="priv-esc">
    <rect x="160" y="561" width="300" height="55" rx="8"
          fill="#fffbeb" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="185" y="582" font-family="'JetBrains Mono', monospace" font-size="9"
          fill="#92400e" letter-spacing="0.05em">06 &middot; PRIVILEGE ESCALATION</text>
    <text x="185" y="602" font-family="system-ui, sans-serif" font-size="12" fill="#1e293b">
      sudo abuse, chmod 777, setuid
    </text>
    <text x="448" y="602" font-family="'JetBrains Mono', monospace" font-size="8"
          fill="#f59e0b" text-anchor="end">FLAG</text>
  </g>

  <!-- Arrow -->
  <line x1="310" y1="616" x2="310" y2="632" stroke="url(#sa-flow)" stroke-width="1.5" stroke-dasharray="4 3">
    <animate attributeName="stroke-dashoffset" from="0" to="-14" dur="2s" repeatCount="indefinite"/>
  </line>
  <polygon points="310,630 306,624 314,624" fill="#6366f1" opacity="0.4"/>

  <!-- ===== CLASS 7: STEGANOGRAPHIC ===== -->
  <g data-stage="steg">
    <rect x="160" y="635" width="300" height="55" rx="8"
          fill="#fffbeb" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="185" y="656" font-family="'JetBrains Mono', monospace" font-size="9"
          fill="#92400e" letter-spacing="0.05em">07 &middot; STEGANOGRAPHIC</text>
    <text x="185" y="676" font-family="system-ui, sans-serif" font-size="12" fill="#1e293b">
      Zero-width chars, HTML comments
    </text>
    <text x="448" y="676" font-family="'JetBrains Mono', monospace" font-size="8"
          fill="#f59e0b" text-anchor="end">FLAG</text>
  </g>

  <!-- Arrow -->
  <line x1="310" y1="690" x2="310" y2="706" stroke="url(#sa-flow)" stroke-width="1.5" stroke-dasharray="4 3">
    <animate attributeName="stroke-dashoffset" from="0" to="-14" dur="2s" repeatCount="indefinite"/>
  </line>
  <polygon points="310,704 306,698 314,698" fill="#6366f1" opacity="0.4"/>

  <!-- ===== CLASS 8: SEMANTIC MISMATCH ===== -->
  <g data-stage="semantic">
    <rect x="160" y="709" width="300" height="55" rx="8"
          fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="185" y="730" font-family="'JetBrains Mono', monospace" font-size="9"
          fill="#1d4ed8" letter-spacing="0.05em">08 &middot; SEMANTIC MISMATCH</text>
    <text x="185" y="750" font-family="system-ui, sans-serif" font-size="12" fill="#1e293b">
      URL allowlist, keyword divergence
    </text>
    <text x="448" y="750" font-family="'JetBrains Mono', monospace" font-size="8"
          fill="#3b82f6" text-anchor="end">FLAG/INFO</text>
  </g>

  <!-- Arrow -->
  <line x1="310" y1="764" x2="310" y2="794" stroke="url(#sa-flow)" stroke-width="1.5" stroke-dasharray="4 3">
    <animate attributeName="stroke-dashoffset" from="0" to="-14" dur="2s" repeatCount="indefinite"/>
  </line>
  <polygon points="310,792 306,786 314,786" fill="#6366f1" opacity="0.4"/>

  <!-- ===== VERDICT ===== -->
  <g data-stage="verdict">
    <rect x="160" y="797" width="300" height="55" rx="8"
          fill="#f0fdf4" stroke="#4ade80" stroke-width="2" filter="url(#sa-glow)"/>
    <text x="185" y="818" font-family="'JetBrains Mono', monospace" font-size="9"
          fill="#166534" letter-spacing="0.05em">VERDICT</text>
    <text x="185" y="838" font-family="system-ui, sans-serif" font-size="13" fill="#1e293b">
      ScanResult (CLEAN / FLAG / BLOCK)
    </text>
  </g>

  <!-- Accumulator arrow on right side -->
  <path d="M 465 220 L 485 220 L 485 810 L 465 810"
        fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 2" opacity="0.4"/>
  <text x="498" y="520" font-family="'JetBrains Mono', monospace" font-size="8"
        fill="#94a3b8" opacity="0.5" transform="rotate(90, 498, 520)">findings accumulate</text>
</svg>
</div>

---

## Internal components

### ScanResult

The `ScanResult` dataclass accumulates all findings from a scan:

```python
@dataclass
class ScanResult:
    findings: list[Finding]

    @property
    def blocked(self) -> bool: ...   # Any BLOCK findings?
    @property
    def flagged(self) -> bool: ...   # Any FLAG findings?
    @property
    def clean(self) -> bool: ...     # No findings at all?
    @property
    def severity(self) -> Severity: ...  # Highest severity
```

### Finding

Each finding records the threat class, severity, a human-readable description, the matched evidence, and the line number:

```python
@dataclass
class Finding:
    threat_class: ThreatClass
    severity: Severity
    description: str
    evidence: str
    line: int | None = None
```

### Severity and ThreatClass enums

```python
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
```

---

## Scan stages in detail

### Stage 0: Parse

The scanner separates the YAML frontmatter from the body content. The `description` field from frontmatter is extracted for semantic mismatch analysis. The body (everything after `---`) is used for pattern matching.

### Stages 1-4: BLOCK-severity pattern checks

Command injection, data exfiltration, credential theft, and prompt override patterns are checked against the body text. Each regex match produces a BLOCK-severity finding with the matched text as evidence and the line number of the match.

### Stages 5-6: FLAG-severity pattern checks

Supply chain and privilege escalation patterns are checked with FLAG severity. These patterns have legitimate uses, so they warrant review rather than automatic rejection.

### Stage 7: Steganographic checks

Two sub-checks:

1. **Zero-width character scan** -- Iterates over every character in the full content (including frontmatter) and flags any zero-width Unicode characters (U+200B, U+200C, U+200D, U+2060, U+FEFF, and BiDi control characters).

2. **Hidden command scan** -- Regex check for commands hidden in HTML comments (`<!-- -->`) and CDATA sections.

### Stage 8: Semantic mismatch checks

Three sub-checks:

1. **URL domain allowlist** -- Extracts all URLs from the body and checks each domain against a curated allowlist. Non-allowlisted domains produce INFO findings.

2. **Sensitive path detection** -- Checks for references to sensitive paths (`~/.ssh/`, `~/.aws/`, `.env`, etc.). Findings are suppressed if the skill has security context (detected by keywords like "audit", "security", "encrypt", etc.).

3. **Keyword divergence** -- Computes Jaccard similarity between tokenized description and tokenized body. Similarity below 0.02 with a sufficiently large body suggests the description is a decoy.

---

## Security context detection

The scanner includes a special check for skills that legitimately discuss security topics. If the content contains keywords like "audit", "security", "pentest", "protect", "encrypt", "ssh-keygen", or "git config", sensitive path references are suppressed. This prevents false positives on skills about SSH setup, security hardening, or infrastructure automation.

---

## Using the scanner as a library

```python
from brunnr.scanner import scan_skill_md, ScanResult

content = open("skills/my-skill/SKILL.md").read()
result = scan_skill_md(content)

if result.blocked:
    print(f"BLOCKED: {result.block_reasons}")
elif result.flagged:
    print(f"FLAGGED: {result.flag_reasons}")
else:
    print("CLEAN")

# Get structured output
print(result.to_dict())
```
