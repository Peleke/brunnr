<div align="center">

# brunnr

**The well agents drink from.**

*Skills marketplace for Claude Code and agent-facing tools.*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-1-4ade80)](skills/)
[![AX Rubric](https://img.shields.io/badge/ax--rubric-v1.0-e88072)](skills/ax-rubric/)

</div>

---

> *Beneath the world tree there is a well. Odin gave an eye to drink from it.*
>
> *Your agent just needs a good tool description.*

---

## What this is

**brunnr** is a skills marketplace for [Claude Code](https://docs.anthropic.com/en/docs/claude-code). Install it once, get access to every skill in the collection.

The first skill is the **AX Description Rubric** — a tool that scores your agent-facing tool descriptions against [five criteria](https://peleke.me/writing/ax-04-tool-descriptions) that determine whether an agent will ever call your tool.

Most tool descriptions score 1-2 out of 5. The rubric tells you why, then rewrites them to score 5.

## Install

```bash
# Add the marketplace
/plugin marketplace add Peleke/brunnr

# Use the skill
/ax-rubric
```

Paste your tool description when prompted. Or pass it inline:

```
/ax-rubric "Query the knowledge base for structured learnings, patterns, and skills relevant to your current work context."
```

## What you get

```
### knowledge_base_query

Score: 1/5

| Criterion       | Result | Notes                                                        |
|-----------------|--------|--------------------------------------------------------------|
| Output shape    | fail   | "structured learnings, patterns, and skills" — how many?     |
| Cost signal     | fail   | No indication of response size                               |
| Trigger clarity | fail   | "relevant to your current work context" — always true        |
| Specificity     | fail   | Lists categories, solves no named problem                    |
| Differentiation | fail   | Half your tools say "relevant to current context"            |

Rewritten (5/5):
> "Check for known pitfalls before starting work. Returns 3-5 specific
> warnings for your tech stack. ~500 tokens. Call once at session start."
```

One input, five scores, one rewrite. The rewrite is ready to paste into your tool definition.

---

## The rubric

Five criteria. Binary pass/fail. Most descriptions fail.

| # | Criterion | What agents need |
|---|-----------|------------------|
| 1 | **Output shape** | Can the agent picture the response before calling? |
| 2 | **Cost signal** | Does the agent know what this costs in tokens? |
| 3 | **Trigger clarity** | Does the agent know exactly when to call this? |
| 4 | **Specificity** | Does this solve one named problem? |
| 5 | **Differentiation** | Can the agent distinguish this from every other tool? |

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
