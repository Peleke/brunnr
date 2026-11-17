# Field Table

**Before any optimizer, fill in this table.**

Before you reach for DSPy, Ax, GEPA or any optimizer, list every output your agent produces and fill in four columns for each one.

1. **Consumer:** what reads this output? Another step, a rule in code, or a metric.
2. **Definition:** what does the field mean, written down where the model and the code both use it?
3. **Examples:** do you have labeled examples of right and wrong?
4. **Metric:** what number tells you it improved?

An output with no consumer gets deleted. An output with no definition, examples or metric is a place where any "improvement" would be a guess.

## One real row

From a pipeline that extracts claims from changelog posts, built in Ax:

| Output | Consumer | Definition | Examples | Metric |
|---|---|---|---|---|
| quoteText | a check that the quote appears in the source; the evidence rules for tags | "verbatim span of sourceText that states the claim" | 5 labeled changelog entries | verbatim rate (1.00 on the current eval) |

That pipeline enforces the first column in CI: a contract test fails if any model output field has no named consumer.

## Your turn

| Output | Consumer | Definition | Examples | Metric |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |

## Run it with an agent

```bash
brunnr install field-table
```

Ask: *"Run a field table on this agent."* It finds every output shape (schemas, DSPy/Ax signatures, parsers, tool arguments), greps each field's readers, quotes its definition, counts its examples, finds or proposes a metric, and lists what to delete. Read-only.

## Where this sits

```
learning-check  →  signal-card  →  field-table  →  (your optimizer)
```

---

*Part of the SIA (self-improving agents) series. Drafted with AI assistance, edited by me.*
