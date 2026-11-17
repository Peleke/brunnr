---
name: field-table
description: >
  Before any optimizer, list every output an agent produces and fill four columns per output:
  consumer (what reads it), definition (written down where the model and the code both use it),
  labeled examples, and metric. Read-only. Flags outputs with no consumer for deletion and marks
  every gap where an "improvement" would be a guess. Use before DSPy, Ax, GEPA or any prompt
  optimization, or when an agent's output schema has grown without review.
license: MIT
---

# Field Table

An output with no consumer should be deleted. An output with no definition, examples, or metric
is a place where any optimizer "improvement" would be a guess. This skill builds the table that
shows which is which.

## Rules

- **Read-only.** No edits, no runs, no model or API calls.
- **Every model output field gets a row**, including nested fields and enum labels.
- **A consumer is code or a metric that reads the field.** Logging it or showing it in a debug
  view is not a consumer. Cite path:line for each consumer.
- **A definition counts only if both sides see it:** the text the model gets (schema description,
  signature field description, prompt) and the code that relies on it. One-sided definitions are
  "partial".

## Step 1: Enumerate outputs

Find every place the model's output is given a shape:
- structured-output schemas (JSON schema, zod, pydantic)
- DSPy or Ax signatures (output fields)
- parsers over free text (regex, `JSON.parse` of model text)
- tool-call arguments the model fills

List each field with its type and source location.

## Step 2: Consumer

Search for reads of each field outside the model call. Record the reader, or **none**. Fields
with no consumer go to the "delete" list.

## Step 3: Definition

Quote the definition the model sees, and note whether the code's use matches it. Overlapping enum
values with no definitions (for example `impact | change | action`) are a gap, even if the model
"usually gets it right".

## Step 4: Examples

Find labeled examples: gold files, fixtures, eval sets. Count them per field. Zero means there is
no ground truth for this field.

## Step 5: Metric

Find the function that scores this field against its examples. If none, propose the cheapest
honest one (exact match, set overlap, verbatim check, then an LLM judge only if nothing cheaper
works) and mark it "to build".

## Output

```markdown
# Field Table: <agent name>

| Output | Type | Consumer | Definition | Examples | Metric |
|---|---|---|---|---|---|
| quoteText | string | path:line | "verbatim span that states the claim" (model + code) | 5 | verbatim rate |

**Delete (no consumer):** …
**Gaps (no definition / examples / metric):** …
**Optimizable now:** outputs with all four columns filled.

**Optional:** a contract test that fails CI when an output field has no named consumer.
```

## Gotchas

- Don't treat "the model mostly gets it right" as a definition.
- A metric scored on the same examples used as demos is not a metric for that field; note the
  overlap.
- Enum fields often have the weakest definitions. Check every value, not just the field.

## Examples

- "Run field-table on src/flows" → enumerate signature outputs, grep each field's readers, fill
  the table, list deletions.
- A label field with four overlapping values, no definitions and no reader → delete list, with a
  note that any "accuracy" on it would have no answer key.
