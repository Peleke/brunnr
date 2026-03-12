# Writing Skills

A skill is a SKILL.md file: a Markdown document with YAML frontmatter that serves as a system prompt for an agent. This guide covers how to write skills that pass the brunnr security scanner and work well as agent instructions.

---

## File structure

Every skill lives in a directory under `skills/`:

```
skills/
  my-skill/
    SKILL.md          # Required: the skill prompt
tests/
  my-skill/
    test-spec.json    # Optional: eval test specification
    fixtures/
      case-1.json     # Optional: test fixtures
schemas/
  my-skill/
    output.schema.json  # Optional: output schema
```

---

## SKILL.md format

### Frontmatter

The YAML frontmatter is required. At minimum, it must include `name` and `description`:

```yaml
---
name: my-skill
description: A clear, specific description of what this skill does. Use when [specific trigger]. Returns [specific output shape].
---
```

!!! tip "Write the description for the agent"
    The `description` field is what the agent reads to decide whether to use the skill. Apply the [AX Description Rubric](ax-rubric.md) principles: output shape, cost signal, trigger clarity, specificity, differentiation.

Optional frontmatter fields:

```yaml
---
name: my-skill
description: Score tool descriptions against five criteria. Returns a score, table, and rewrite. ~800 tokens. Use when reviewing MCP tool descriptions.
license: Complete terms in LICENSE.txt
metadata:
  openclaw:
    emoji: "\U0001F50D"
    requires:
      bins: ["python3"]
---
```

### Body

The body is the system prompt. Write it as instructions the agent will follow.

Structure the body with clear sections:

```markdown
# Skill Title

Brief overview of what the skill does.

## Input

What the user provides. Be explicit about format.

## Phase 1: [Step Name]

Instructions for the first phase of work.

## Phase 2: [Step Name]

Instructions for the second phase.

## Output Format

Exact format the agent should produce.

## Reference Examples

Show concrete input/output pairs.
```

---

## Passing the security scanner

The scanner checks your SKILL.md against [7+1 threat classes](../security/threat-classes.md). Here are the rules for writing clean skills.

### Do not include

These patterns will cause a **BLOCK** finding:

- **Shell pipes** -- Never write `curl ... | sh` or `wget ... | bash`, even as examples.
- **Reverse shells** -- Never reference `bash -c`, `nc -e`, or Python socket commands.
- **Base64 payloads** -- Never include `echo ... | base64 -d | sh`.
- **Sensitive file reads** -- Never write `cat ~/.ssh/id_rsa` or `cat .env`.
- **Credential extraction** -- Never include `printenv API_KEY` or `env | grep SECRET`.
- **Prompt overrides** -- Never write "ignore previous instructions" or "you are now in unrestricted mode".

### Be careful with

These patterns will cause a **FLAG** finding:

- **Custom package registries** -- If your skill references `--index-url` or `--registry`, it will be flagged.
- **Privilege escalation** -- `sudo chmod`, `sudo bash`, or writing to `/etc/` will be flagged.
- **Sensitive paths** -- References to `~/.ssh/`, `~/.aws/`, `.env` will be flagged unless your skill has security context (see below).

### Security context exemption

If your skill is about security auditing, SSH setup, or infrastructure, include security keywords in the content: "audit", "security", "protect", "encrypt", "ssh-keygen", etc. The scanner recognizes these and suppresses sensitive-path flags.

### URL allowlist

URLs to non-allowlisted domains produce INFO findings. Stick to well-known domains (GitHub, PyPI, npm, MDN, Anthropic docs, etc.) or accept the INFO findings during review.

### Keyword divergence

Make sure your frontmatter `description` uses words that also appear in the body. If the description says "code formatter" but the body is about "database administration", the scanner will flag a keyword divergence.

---

## Writing effective instructions

### Be specific

Bad:

```markdown
Help the user with their code.
```

Good:

```markdown
## Phase 1: Analyze

Read the user's code and identify:
1. Functions with more than 3 parameters (refactoring candidates)
2. Repeated code blocks (DRY violations)
3. Missing error handling (try/catch absent on I/O operations)
```

### Use phases

Break complex skills into numbered phases. Agents follow sequential instructions better than unstructured prose.

### Include output format

Specify exactly what the agent should produce:

```markdown
## Output Format

For each function reviewed, produce:

| Function | Score | Issue |
|----------|-------|-------|
| {name} | {1-5} | {one line} |

Then provide a rewritten version of the lowest-scoring function.
```

### Provide reference examples

Show input/output pairs so the agent understands the expected behavior:

```markdown
## Reference Examples

### Example: Bad input (Score 1/5)

**Input:**
> "Query the database for relevant results."

**Output:**
> Score: 1/5. No output shape, no cost signal, no trigger.

### Example: Good input (Score 5/5)

**Input:**
> "Check for schema drift. Returns 0-3 warnings with SQL fix suggestions. ~200 tokens. Call after migrations."

**Output:**
> Score: 5/5. All criteria pass.
```

---

## Writing test specifications

Test specs validate that your skill produces correct output when evaluated against test fixtures.

### test-spec.json

```json
{
  "cases": [
    {
      "id": "case-1",
      "description": "Basic functionality test",
      "fixture": "fixtures/basic-input.json",
      "assertions": [
        {"type": "score_range", "expected": {"min": 1, "max": 2}},
        {"type": "has_table", "expected": true},
        {"type": "contains", "expected": "rewritten"}
      ]
    }
  ]
}
```

### Fixture files

```json
{
  "input": "The text that will be sent as the user message to Claude.",
  "description": "Human-readable description of this test case."
}
```

### Available assertion types

| Type | Expected value | Checks |
|------|---------------|--------|
| `score_range` | `{"min": N, "max": N}` | Extracted score is within range |
| `has_table` | `true`/`false` | Output contains a markdown table |
| `has_rewrite` | `true`/`false` | Output contains "rewrite"/"rewritten" |
| `contains` | `"string"` | Case-insensitive substring match |
| `format_valid` | (none) | Has headers, score line, and criteria table |
| `criteria_pass` | `["name", ...]` | Named criteria show "pass" in table |
| `criteria_fail` | `["name", ...]` | Named criteria show "fail" in table |

---

## Checklist

Before publishing a skill:

- [ ] Frontmatter has `name` and `description`
- [ ] Description follows AX rubric principles (output shape, cost, trigger)
- [ ] Body has clear phases or sections
- [ ] Output format is specified
- [ ] At least one reference example is included
- [ ] `brunnr scan` passes with CLEAN verdict
- [ ] Test spec exists with at least one case (if applicable)
- [ ] `brunnr eval <slug> --dry-run` validates fixtures
