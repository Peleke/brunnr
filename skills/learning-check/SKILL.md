---
name: learning-check
description: >
  Audit an agent (a repo, a service, or a written description) for the three properties of
  learning: a feedback signal from outside the model, an update rule you can write down, and
  measurable improvement on held-out examples. Read-only. Produces a three-row verdict table with
  evidence and the first thing to fix. Use when asking "does my agent actually learn?", before
  adding a memory feature, or before reaching for an optimizer.
license: MIT
---

# Learning Check

Answer three questions about one agent, with evidence for each answer. Memory features (the
model writes notes and reads them back) pass none of the three on their own: nothing is weighted
or scored, so a note confirmed a hundred times counts the same as one invented once.

## Rules

- **Read-only.** Do not edit files, run the agent, or make model or API calls.
- **Evidence or "no".** Every "yes" or "partial" cites a file path (with line numbers) or a
  quoted sentence from the operator's description. No evidence means the answer is "no".
- **The model grading itself is not a signal.** A self-critique or self-score from the same model
  counts only if something outside the model checks it.
- **A person editing the prompt is an update rule for the person, not the agent.** Record it as
  "operator is the loop".

## Step 1: Locate the agent

Find where the agent calls a model and what it produces:
- model client construction, prompt or signature definitions, tool definitions
- the outputs it returns or writes, and who reads them

If the input is a description rather than code, restate the agent in three lines and ask the
operator to confirm before continuing.

## Step 2: Question 1, the signal

*When it gets something wrong, what tells it?*

Look for outcomes captured from outside the model:
- tests or validators run on outputs; assertion failures that are logged
- user actions (accept, reject, edit, retry, churn) recorded against an output id
- eval scripts with labeled examples; review comments tied to outputs

Verdict: **yes** (outcomes are recorded and tied to specific outputs), **partial** (outcomes
exist but aren't tied to outputs, or are only in someone's head), **no**.

## Step 3: Question 2, the update rule

*When that happens, what changes, and by how much?*

Look for code that changes the agent's behavior because of a recorded outcome:
- demo or example sets rebuilt from scored outputs
- instructions rewritten by an optimizer (DSPy, Ax, GEPA, or similar)
- weights, rankings, or confidence on stored memories that move with outcomes
- fine-tuning jobs fed by outcome data

Verdict: **yes** (an update you could write down: this changed, by this much, because of that),
**partial** (memory accumulates but nothing is weighted, or updates are manual but logged),
**no** (only "operator is the loop").

## Step 4: Question 3, convergence

*Is it measurably better than last month, on examples it didn't train on?*

Look for a metric tracked over time on a held-out set: eval result files with dates, dashboards,
CI jobs that score a fixed set.

Verdict: **yes** (a number, a held-out set, at least two dated measurements), **partial** (a
metric exists but on training data, or measured once), **no**.

## Output

```markdown
# Learning Check: <agent name>

| # | Question | Verdict | Evidence |
|---|---|---|---|
| 1 | What tells it it was wrong? | yes / partial / no | path:line or quote |
| 2 | What changes when it's wrong? | yes / partial / no | path:line or quote |
| 3 | Is it measurably better over time? | yes / partial / no | path:line or quote |

**Memory vs learning:** <one sentence: does any "memory" feature here weight or score what it stores?>

**First fix:** <start at the first question that isn't "yes"; one concrete step>

**Next step:** run `signal-card` to name the signal this agent should learn from.
```

## Gotchas

- An eval that exists but never runs is "partial" on question 3, not "yes".
- Logging every output is not a signal unless something marks outputs right or wrong.
- Don't count the optimizer's training score as convergence; only held-out scores count.

## Examples

- "Run a learning check on this repo" → locate the agent in code, fill the table from the files.
- "My support bot saves summaries of past chats to a vector DB. Does it learn?" → Q1 no (no
  outcome recorded), Q2 partial (memory accumulates, unweighted), Q3 no. First fix: record
  whether each answer resolved the ticket.
