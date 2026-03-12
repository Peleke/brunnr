<div align="center">

<img src="https://raw.githubusercontent.com/Peleke/brunnr/main/assets/hero.png" alt="brunnr — the well agents drink from" width="100%" />

# brunnr

**The well agents drink from.**

*Skills marketplace for Claude Code and agent-facing tools.*

[![PyPI](https://img.shields.io/pypi/v/brunnr)](https://pypi.org/project/brunnr/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-1-4ade80)](skills/)
[![AX Rubric](https://img.shields.io/badge/ax--rubric-v1.0-e88072)](skills/ax-rubric/)

</div>

---

> *Beneath the world tree there is a well. Odin gave an eye to drink from it.*
>
>*Your agent won't need to. We bottled the water.*

---

## Contents

- [AX Description Rubric](#ax-description-rubric) — score your tool descriptions
- [Install](#install) — one command
- [What you get](#what-you-get) — example output
- [The Rubric](#the-rubric) — five criteria, explained
- [Skills](#skills) — what's available
- [Why "brunnr"](#why-brunnr)
- [Contributing](#contributing)

---

## What this is

**brunnr** is a skills marketplace for [Claude Code](https://docs.anthropic.com/en/docs/claude-code). Install it once, get access to every skill in the collection.

### AX Description Rubric

The first skill: the **AX Description Rubric** — a tool that scores your agent-facing tool descriptions against [five criteria](https://peleke.me/writing/ax-04-tool-descriptions) that determine whether an agent will ever call your tool.

Most tool descriptions score 1-2 out of 5. The rubric tells you why, then rewrites them to score 5.

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

Paste your tool description when prompted. Or pass it inline:

```
/ax-rubric "Query the knowledge base for structured learnings, patterns, and skills relevant to your current work context."
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

## What you get

#### `knowledge_base_query`

**Score: 1/5**

| Criterion | Result | Notes |
|-----------|--------|-------|
| Output shape | fail | "structured learnings, patterns, and skills" — how many? |
| Cost signal | fail | No indication of response size |
| Trigger clarity | fail | "relevant to your current work context" — always true |
| Specificity | fail | Lists categories, solves no named problem |
| Differentiation | fail | Half your tools say "relevant to current context" |

**Rewritten (5/5):**

> "Check for known pitfalls before starting work. Returns 3-5 specific warnings for your tech stack. ~500 tokens. Call once at session start."

One input, five scores, one rewrite. The rewrite is ready to paste into your tool definition.

---

## The rubric

Five criteria. Binary pass/fail. Most descriptions fail.

<img src="https://raw.githubusercontent.com/Peleke/brunnr/main/assets/rubric.svg" alt="The AX Description Rubric — five criteria for agent-facing tool descriptions" width="100%" />

**0-1 pass** = invisible (agent will never call it). **2-3** = marginal. **4-5** = habitual.

The bar for habitual use is 4/5. Most tool descriptions in the wild score 1-2. The tool might be excellent. The agent will never know.

---

## Skills

| Skill | What it does | Based on |
|-------|-------------|----------|
| **[ax-rubric](skills/ax-rubric/)** | Score tool descriptions for agent discoverability. 5 criteria, pass/fail, rewrite. | [I Don't Deliberate About This](https://peleke.me/writing/ax-04-tool-descriptions) |

More skills coming. Each one ships alongside an article in the [AX series](https://peleke.me/writing/ax-series).

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

---

<div align="center">

*Part of the [Agent Experience (AX)](https://peleke.me/writing/ax-series) series*
*by [Peleke Sengstacke](https://peleke.me) and [Maren](https://peleke.me/writing/ax-01a-the-agent-has-opinions).*

</div>
