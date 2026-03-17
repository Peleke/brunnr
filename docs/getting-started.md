# Getting Started

Install brunnr, scan your first skill, and understand the output.

---

## Installation

brunnr is a Python package with zero core dependencies. It requires Python 3.12 or later.

```bash
# pip
pip install brunnr

# pipx (isolated environment)
pipx install brunnr

# uv
uv pip install brunnr
```

If you plan to use the `eval` command (LLM-based skill evaluation), install with the eval extra:

```bash
pip install brunnr[eval]
```

This adds the `anthropic` SDK as a dependency. You will also need an `ANTHROPIC_API_KEY` environment variable set.

### From source

```bash
git clone https://github.com/Peleke/brunnr.git
cd brunnr
pip install -e .
```

---

## The flow

The typical brunnr workflow: install, scan your skills directory, review results.

<div style="max-width: 520px; margin: 2em auto;">
<svg viewBox="0 0 500 340" aria-label="brunnr getting started flow: install, scan, review">
  <defs>
    <filter id="gs-glow">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <linearGradient id="gs-flow-down" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#4ade80" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#4ade80" stop-opacity="0.15"/>
    </linearGradient>
    <pattern id="gs-grid" width="25" height="25" patternUnits="userSpaceOnUse">
      <path d="M 25 0 L 0 0 0 25" fill="none" stroke="#cbd5e1" stroke-width="0.4" opacity="0.25"/>
    </pattern>
  </defs>

  <!-- Background grid -->
  <rect width="100%" height="100%" fill="url(#gs-grid)" opacity="0.4"/>

  <!-- Step 1: Install -->
  <g data-step="install">
    <rect x="110" y="20" width="280" height="70" rx="8"
          fill="#f8fafc" stroke="#4ade80" stroke-width="2" filter="url(#gs-glow)"/>
    <text x="140" y="44" font-family="'JetBrains Mono', 'Fira Code', monospace" font-size="9"
          fill="#64748b" letter-spacing="0.05em">01 &middot; INSTALL</text>
    <text x="140" y="68" font-family="system-ui, sans-serif" font-size="14" fill="#1e293b">
      pip install brunnr
    </text>
    <text x="380" y="68" font-family="'JetBrains Mono', monospace" font-size="8"
          fill="#94a3b8" text-anchor="end" opacity="0.6">zero deps</text>
  </g>

  <!-- Arrow 1→2 -->
  <line x1="250" y1="90" x2="250" y2="130"
        stroke="url(#gs-flow-down)" stroke-width="1.5" stroke-dasharray="4 3">
    <animate attributeName="stroke-dashoffset" from="0" to="-14" dur="2s" repeatCount="indefinite"/>
  </line>
  <polygon points="250,128 246,122 254,122" fill="#4ade80" opacity="0.5"/>

  <!-- Step 2: Scan -->
  <g data-step="scan">
    <rect x="110" y="135" width="280" height="70" rx="8"
          fill="#f8fafc" stroke="#94a3b8" stroke-width="1"/>
    <text x="140" y="159" font-family="'JetBrains Mono', 'Fira Code', monospace" font-size="9"
          fill="#64748b" letter-spacing="0.05em">02 &middot; SCAN</text>
    <text x="140" y="183" font-family="system-ui, sans-serif" font-size="14" fill="#1e293b">
      brunnr scan skills/
    </text>
    <text x="380" y="183" font-family="'JetBrains Mono', monospace" font-size="8"
          fill="#94a3b8" text-anchor="end" opacity="0.6">7+1 classes</text>
  </g>

  <!-- Arrow 2→3 -->
  <line x1="250" y1="205" x2="250" y2="245"
        stroke="url(#gs-flow-down)" stroke-width="1.5" stroke-dasharray="4 3">
    <animate attributeName="stroke-dashoffset" from="0" to="-14" dur="2s" repeatCount="indefinite"/>
  </line>
  <polygon points="250,243 246,237 254,237" fill="#4ade80" opacity="0.5"/>

  <!-- Step 3: Review -->
  <g data-step="review">
    <rect x="110" y="250" width="280" height="70" rx="8"
          fill="#f8fafc" stroke="#94a3b8" stroke-width="1"/>
    <text x="140" y="274" font-family="'JetBrains Mono', 'Fira Code', monospace" font-size="9"
          fill="#64748b" letter-spacing="0.05em">03 &middot; REVIEW</text>
    <text x="140" y="298" font-family="system-ui, sans-serif" font-size="14" fill="#1e293b">
      CLEAN / FLAG / BLOCK
    </text>
    <text x="380" y="298" font-family="'JetBrains Mono', monospace" font-size="8"
          fill="#94a3b8" text-anchor="end" opacity="0.6">exit codes</text>
  </g>
</svg>
</div>

---

## Your first scan

brunnr scans SKILL.md files for security threats. If you have a `skills/` directory, it will find them automatically.

```bash
brunnr scan
```

If your skills are elsewhere, pass the path:

```bash
brunnr scan path/to/skills/
```

You can also scan a single file:

```bash
brunnr scan my-skill/SKILL.md
```

### Understanding the output

```
=== brunnr scan ===

  CLEAN  ax-rubric

  Scanned 1 files: 1 clean, 0 flagged, 0 blocked
```

Each file gets one of three verdicts:

| Verdict | Meaning | Exit code |
|---------|---------|-----------|
| **CLEAN** | No threats detected. Safe to use. | `0` |
| **FLAG** | Suspicious patterns found. Review recommended. | `0` (or `1` with `--strict`) |
| **BLOCK** | Dangerous patterns detected. Do not use. | `1` |

For more detail, add `-v` (verbose):

```bash
brunnr scan -v
```

```
=== brunnr scan ===

  FLAG   suspicious-skill -- 2 findings
         FLAG: [supply_chain] custom PyPI index (not pypi.org)
               --index-url https://evil.example.com/simple
         FLAG: [steganographic] zero-width character U+200B
               ...some hidden​text...

  Scanned 1 files: 0 clean, 1 flagged, 0 blocked
```

---

## Install a skill

Browse available skills:

```bash
brunnr install --list
```

```
Available skills:
  - ax-rubric
```

Install one:

```bash
brunnr install ax-rubric
```

brunnr shows you the first 30 lines of the SKILL.md before installing. Review the content, then confirm:

```
--- ax-rubric/SKILL.md (first 30 of 142 lines) ---
---
name: ax-rubric
description: Score agent-facing tool descriptions against the AX Description Rubric...
---
...

Full source: https://github.com/Peleke/brunnr/tree/main/skills/ax-rubric

Install ax-rubric to ./skills/ax-rubric/? [y/N] y
  -> skills/ax-rubric/SKILL.md (142 lines)

Installed ax-rubric to ./skills/ax-rubric/

Tip: Run `brunnr eval ax-rubric --dry-run` to validate locally.
```

---

## Run an eval

If the skill has test fixtures (in `tests/<slug>/test-spec.json`), you can validate it:

```bash
# Dry run: validate fixtures without API calls
brunnr eval ax-rubric --dry-run

# Full run: call Claude and check assertions
brunnr eval ax-rubric
```

```
=== brunnr eval: ax-rubric ===
  2 test cases, model: claude-sonnet-4-20250514

  [case-1] Score a bad description
    PASS: [score_range] Score 1 in [1, 2]
    PASS: [has_table] Table found
    PASS: [has_rewrite] Rewrite found

  [case-2] Score a good description
    PASS: [score_range] Score 5 in [4, 5]

=== 2/2 passed ===
```

---

## What's next

- [Commands Reference](commands/scan.md) -- Full docs for every subcommand.
- [Threat Classes](security/threat-classes.md) -- What the scanner detects.
- [Writing Skills](skills/writing-skills.md) -- How to write SKILL.md files that pass the scanner.
