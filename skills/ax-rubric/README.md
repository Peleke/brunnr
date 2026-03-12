<div align="center">

# ax-rubric

**Score agent-facing tool descriptions 0-5 on discoverability.**

*One input. Five scores. One rewrite. Ready to paste.*

[![brunnr](https://img.shields.io/badge/brunnr-skill-4ade80)](https://github.com/Peleke/brunnr)
[![Version](https://img.shields.io/badge/v1.0.0-e88072)](https://github.com/Peleke/brunnr/tree/main/skills/ax-rubric)

</div>

---

> *Most tool descriptions score 1-2 out of 5. The tool might be excellent. The agent will never know.*

---

## What this does

Your agent picks tools based on their descriptions. If the description is vague, the agent skips it — no matter how good the tool is.

**ax-rubric** scores your tool descriptions against five criteria that determine whether an agent will ever call your tool. It explains every failure, then rewrites the description to pass.

<div align="center">
<img src="https://raw.githubusercontent.com/Peleke/brunnr/main/skills/ax-rubric/assets/flow.svg" alt="ax-rubric flow: input → score → rewrite" width="100%" />
</div>

---

## Install

### Claude Code

```bash
# If you haven't added the brunnr marketplace yet
/plugin marketplace add Peleke/brunnr

# Install
/plugin install ax-rubric@brunnr-skills
```

### CLI

```bash
# Install brunnr
uv tool install brunnr    # or: pipx install brunnr

# Install the skill
brunnr install ax-rubric
```

---

## Usage

### Claude Code

```bash
/ax-rubric
```

Paste your tool description when prompted. Or pass it inline:

```
/ax-rubric "Query the knowledge base for structured learnings, patterns, and skills relevant to your current work context."
```

### CLI

```bash
# Dry-run (validate test fixtures, no API calls)
brunnr eval ax-rubric --dry-run

# Full run (calls Claude, checks assertions)
brunnr eval ax-rubric
```

---

## The five criteria

<div align="center">
<img src="https://raw.githubusercontent.com/Peleke/brunnr/main/assets/rubric.svg" alt="The AX Description Rubric — five criteria" width="100%" />
</div>

| # | Criterion | The question it answers |
|---|-----------|----------------------|
| 1 | **Output shape** | Can the agent picture the response before calling? |
| 2 | **Cost signal** | Does the agent know what this costs in tokens? |
| 3 | **Trigger clarity** | Does the agent know *exactly* when to call this? |
| 4 | **Specificity** | Does this solve one named problem? |
| 5 | **Differentiation** | Can the agent distinguish this from every other tool? |

Each criterion is binary pass/fail. The scoring bands:

- **0-1 pass** — invisible. The agent will never call this tool.
- **2-3 pass** — marginal. The agent might call it, might not.
- **4-5 pass** — habitual. The agent reaches for this tool reliably.

The bar for habitual use is **4/5**. Most tool descriptions in the wild score 1-2.

---

## Example

### Before (1/5)

```
"Query the knowledge base for structured learnings, patterns, and skills
relevant to your current work context."
```

| Criterion | Result | Why |
|-----------|--------|-----|
| Output shape | **fail** | "structured learnings, patterns, and skills" — how many? what shape? |
| Cost signal | **fail** | No indication of response size |
| Trigger clarity | **fail** | "relevant to your current work context" — always true, never actionable |
| Specificity | **fail** | Lists categories, solves no named problem |
| Differentiation | **fail** | Half your tools say "relevant to current context" |

### After (5/5)

```
"Check for known pitfalls before starting work. Returns 3-5 specific warnings
for your tech stack. ~500 tokens. Call once at session start."
```

| Criterion | Result | Why |
|-----------|--------|-----|
| Output shape | **pass** | "3-5 specific warnings" — agent knows the count and shape |
| Cost signal | **pass** | "~500 tokens" — agent can budget |
| Trigger clarity | **pass** | "once at session start" — unambiguous trigger |
| Specificity | **pass** | "known pitfalls for your tech stack" — one named problem |
| Differentiation | **pass** | No other tool checks pitfalls at session start |

---

## How it works

1. You provide a tool description (any format — function docstring, OpenAPI summary, MCP tool description)
2. The rubric scores it against all five criteria
3. Each failure gets an explanation of *why* it fails and *what the agent sees*
4. A rewritten description is generated that passes all five criteria
5. The rewrite is ready to paste directly into your tool definition

No configuration. No setup. No training data. Just paste and go.

---

## Further reading

- [I Don't Deliberate About This](https://peleke.me/writing/ax-04-tool-descriptions) — the article behind the rubric
- [AX Series](https://peleke.me/writing/ax-series) — the full Agent Experience series
- [brunnr](https://github.com/Peleke/brunnr) — the skills marketplace
