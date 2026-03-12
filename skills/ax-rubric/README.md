# ax-rubric

**Score agent-facing tool descriptions 0-5 on discoverability.**

Scores your tool descriptions against [five criteria](https://peleke.me/writing/ax-04-tool-descriptions) that determine whether an agent will ever call your tool. Most descriptions score 1-2 out of 5. The rubric tells you why, then rewrites them to score 5.

## Example

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
brunnr eval ax-rubric --dry-run
```

---

Based on [I Don't Deliberate About This](https://peleke.me/writing/ax-04-tool-descriptions) from the [AX series](https://peleke.me/writing/ax-series).
