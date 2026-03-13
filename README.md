<div align="center">

<img src="https://raw.githubusercontent.com/Peleke/brunnr/main/assets/hero.png" alt="brunnr — the well agents drink from" width="100%" />

# brunnr

**The well agents drink from.**

*Security scanner and skills marketplace for Claude Code.*

[![PyPI](https://img.shields.io/pypi/v/brunnr)](https://pypi.org/project/brunnr/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-3-4ade80)](skills/)

</div>

---

> *Beneath the world tree there is a well. Odin gave an eye to drink from it.*
>
>*Your agent won't need to. We bottled the water.*

---

## What this is

**brunnr** is a security scanner and skills marketplace for [Claude Code](https://docs.anthropic.com/en/docs/claude-code).

- **Scan** — a deterministic, zero-dependency scanner that checks SKILL.md files for prompt injection, credential theft, data exfiltration, supply chain poisoning, and 4 other threat classes. No LLM in the scan loop.
- **Install** — fetch skills from the registry with review-before-install defaults. You see what you're installing before it touches your project.
- **Eval** — validate skill quality by running test fixtures against Claude. Structured assertions on scores, format, and criteria.
- **Pipeline** — scan + eval in one command with CI-ready exit codes.

---

## Install

### Option 1 — Claude Code (recommended)

```bash
# Add the brunnr marketplace
/plugin marketplace add Peleke/brunnr

# Install a skill
/plugin install ax-rubric@brunnr-skills

# Use it
/ax-rubric
```

### Option 2 — CLI

```bash
# uv (recommended)
uv tool install brunnr

# or pipx
pipx install brunnr

# or pip
pip install brunnr
```

```bash
# Install a skill from the registry
brunnr install ax-rubric

# Scan your skills for threats
brunnr scan skills/

# Run the eval harness
brunnr eval ax-rubric --dry-run
```

---

## Skills

| Skill | What it does | Based on |
|-------|-------------|----------|
| **[ax-rubric](skills/ax-rubric/)** | Score tool descriptions 0-5 on agent discoverability. Five criteria, pass/fail, rewrite. | [I Don't Deliberate About This](https://peleke.me/writing/ax-04-tool-descriptions) |
| **[ax-interview](skills/ax-interview/)** | Run a structured AX Interview on agent-tool sessions. Gricean maxim analysis, implicature detection, CoT faithfulness check, Pragmatic Coherence Score with ranked fixes. | [The AX Interview](https://peleke.me/writing/ax-07-the-ax-interview) |
| **[runlet](skills/runlet/)** | Turn a braindump into an ND-adapted daily runlist. Classifies by activation energy and focus axis. | — |

---

## Why "brunnr"

Old Norse *brunnr*: well, spring.

As in *Mímisbrunnr* — the Well of Mímir beneath Yggdrasil. Odin sacrificed an eye to drink from it and gain wisdom. The well doesn't give you answers. It gives you the capacity to see what was always there.

Your agent doesn't need to sacrifice anything. It just needs tool descriptions that don't waste its context window.

---

## Contributing

Have an agent-facing tool? Run `/ax-rubric` on your own descriptions first. If they score 4+, you're ahead of 90% of the field.

Want to add a skill? Open a PR. The rubric applies to skill descriptions too.

---

## License

[MIT](LICENSE)
