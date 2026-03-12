# AX Description Rubric

The AX Description Rubric is the first skill in the brunnr registry. It scores agent-facing tool descriptions against five criteria that determine whether an agent will ever call the tool.

Based on ["I Don't Deliberate About This"](https://peleke.me/writing/ax-04-tool-descriptions) from the Agent Experience (AX) series.

---

## What it does

You give it a tool description. It returns:

1. A **score** from 0 to 5 (binary pass/fail on each criterion)
2. A **criteria table** showing which criteria passed and why others failed
3. A **rewrite** that scores 5/5

---

## The five criteria

| # | Criterion | Pass | Fail |
|---|-----------|------|------|
| 1 | **Output shape** | You can picture the response before calling (count, format, structure stated) | "Returns relevant results" -- what shape? how many? |
| 2 | **Cost signal** | Token count, response size, or item count stated | No indication of response size |
| 3 | **Trigger clarity** | You know exactly when to call this (specific event, phase, condition) | "When relevant" -- always true, never actionable |
| 4 | **Specificity** | Solves one named problem | Lists categories ("learnings, patterns, skills, ...") |
| 5 | **Differentiation** | Distinguishable from every other tool in the set | Generic language shared by multiple tools |

### Scoring bands

- **0-1 pass** -- Invisible. Agent will never call it voluntarily.
- **2-3 pass** -- Marginal. Agent might call it if specifically looking.
- **4-5 pass** -- Habitual. Agent calls it every session without prompting.

---

## Example

### Input (invisible tool, 1/5)

> "Query the knowledge base for structured learnings, patterns, and skills relevant to your current work context."

### Output

```
### knowledge_base_query

**Score: 1/5**

| Criterion | Result | Notes |
|-----------|--------|-------|
| Output shape | fail | "structured learnings, patterns, and skills" -- how many? |
| Cost signal | fail | No indication of response size |
| Trigger clarity | fail | "relevant to your current work context" -- always true |
| Specificity | fail | Lists categories, solves no named problem |
| Differentiation | fail | Half your tools say "relevant to current context" |

**Original:**
> "Query the knowledge base for structured learnings, patterns, and skills relevant to your current work context."

**Rewritten (5/5):**
> "Check for known pitfalls before starting work. Returns 3-5 specific warnings for your tech stack. ~500 tokens. Call once at session start."

**Key changes:**
Led with the problem (pitfalls) instead of the mechanism (query).
Added output shape (3-5 warnings), cost signal (~500 tokens),
and a specific trigger (session start, once).
```

---

## Usage

### As a Claude Code slash command

```
/ax-rubric
```

Paste your tool description when prompted. Or pass it inline:

```
/ax-rubric "Query the knowledge base for structured learnings."
```

### File mode

Point it at a file containing tool definitions:

```
/ax-rubric path/to/mcp-server.py
```

The skill extracts tool descriptions from:

- MCP tool definitions (JSON with `name` and `description`)
- Python docstrings on `@tool` or `@mcp.tool()` decorators
- OpenAPI/Swagger `description` fields
- SKILL.md frontmatter `description` fields

### Batch mode

When given multiple descriptions, the skill produces a summary table first:

```
| Tool | Score | Worst gap |
|------|-------|-----------|
| tool_a | 2/5 | No cost signal, no trigger |
| tool_b | 4/5 | Generic differentiation |
| tool_c | 1/5 | Everything |
```

Then provides individual breakdowns for tools scoring below 4/5.

---

## The seven rewrite principles

The skill follows these principles when rewriting descriptions:

1. **Lead with the problem, not the action.** "Check for known pitfalls" not "Query the knowledge base."
2. **State the cost.** Token count, response size, number of items.
3. **Specify the trigger.** "Call at session start" not "when relevant."
4. **Bound the output.** "Returns 3-5 items" not "returns relevant results."
5. **Include `so_what`.** Not just the fact -- the decision it implies.
6. **Report actual cost in the response.** `"token_cost": 487` lets the agent verify the promise.
7. **Don't assume the agent will figure it out.** The description is the only context. Every session. Forever.

---

## Installing

```bash
brunnr install ax-rubric
```

Or with test fixtures:

```bash
brunnr install ax-rubric --with-tests
```

---

## Evaluating

```bash
# Validate fixtures
brunnr eval ax-rubric --dry-run

# Full evaluation
brunnr eval ax-rubric
```
