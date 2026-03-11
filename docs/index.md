# brunnr

**The well agents drink from.**

brunnr is a security scanner and skill registry CLI for agent tool descriptions. It scans SKILL.md files for security threats, installs skills from a registry, and evaluates skill quality with an LLM harness.

---

## The problem

Agent-facing tools ship with descriptions that determine whether the agent ever calls them. Most tool descriptions score 1-2 out of 5 on discoverability. The tool might be excellent. The agent will never know.

Worse: third-party skills can contain hidden threats. A SKILL.md file that looks like a helpful code formatter might contain embedded reverse shells, credential theft patterns, or prompt injection attacks. Without automated scanning, you're trusting that every skill author is honest and competent.

brunnr solves both problems:

1. **Security scanning** -- A deterministic, zero-dependency, 7+1 threat class scanner that catches command injection, data exfiltration, credential theft, prompt overrides, supply chain poisoning, privilege escalation, steganographic hiding, and semantic mismatch.

2. **Skill registry** -- Install skills from a curated registry with review-before-install defaults. Every skill is scanned before it reaches your agent.

3. **Eval harness** -- Validate that skills produce correct, high-quality output by running test fixtures against Claude models.

---

## Why "brunnr"

Old Norse *brunnr*: well, spring.

As in *Mimisbrunnr* -- the Well of Mimir beneath Yggdrasil. Odin sacrificed an eye to drink from it and gain wisdom. The well doesn't give you answers. It gives you the capacity to see what was always there.

Your agent doesn't need to sacrifice anything. It needs tool descriptions that don't waste its context window, and a scanner that catches threats before they reach the model.

---

## Quick example

```bash
# Install brunnr
pip install brunnr

# Scan your skills for threats
brunnr scan skills/

# Install a skill from the registry
brunnr install ax-rubric

# Run the eval harness
brunnr eval ax-rubric --dry-run
```

---

## Features at a glance

| Feature | Description |
|---------|-------------|
| **Zero dependencies** | Core scanner uses only Python stdlib. No third-party packages required. |
| **7+1 threat classes** | Command injection, data exfil, credential theft, prompt override, supply chain, privilege escalation, steganographic, semantic mismatch. |
| **Deterministic** | Regex-based scanning. Same input, same output, every time. No LLM in the scan loop. |
| **Review-before-install** | Shows you the first 30 lines of a skill before installing. You approve or abort. |
| **Eval harness** | Test skills against Claude models with structured assertions (score ranges, format checks, criteria matching). |
| **Pipeline mode** | Run scan + eval in one command. CI-ready exit codes. |

---

## What's next

- [Getting Started](getting-started.md) -- Install brunnr and run your first scan.
- [Commands](commands/scan.md) -- Full reference for every subcommand.
- [Threat Classes](security/threat-classes.md) -- What the scanner catches and why.
- [Writing Skills](skills/writing-skills.md) -- How to write SKILL.md files that pass the scanner.

!!! note "Dev dependency"
    To build and preview these docs locally, install MkDocs:
    ```bash
    pip install mkdocs pymdown-extensions
    mkdocs serve
    ```
