---
name: metric-signature
description: >
  Turn an agent's chosen learning signal into metric functions: the cheapest check that can tell a
  good output from a bad one, written as a DSPy-style Python signature, an Ax-style TypeScript
  signature and plain language, normalized to 0..1, with a named do-nothing baseline. Read-only.
  Link 3 of the SIA audit chain; reads the signal-card envelope. Use after signal-card, before
  building a gold set, or when an optimizer needs a metric and nobody has written one.
license: MIT
---

# Metric Signature

An optimizer only climbs what the metric measures. This skill writes the metric down before
anyone builds a dataset or runs a search: which output fields it scores, how cheaply, on what
scale, and what "doing nothing" scores.

## Rules

- **Read-only.** Don't edit files, run the agent, or make model or API calls.
- **Evidence or "unknown".** Every claim cites `path:line` or a quote from the operator.
- **Cheapest adequate tier.** Use code before partial credit, and partial credit before a judge.
  Use an LLM judge only when nothing cheaper can tell good from bad, and say why.
- **Scores run from 0 to 1.** Higher is better.
- **Never invent an upstream verdict.** If a field you read is missing, ask for it or reconstruct
  it from the code and list it under `out.reconstructed`.

## Step 0: Deployment type

Place the agent in one type; it tells you where outputs and labels live.

| type | outputs are defined in | labels / outcomes live in |
|---|---|---|
| `coding-harness` | skill files, CLAUDE.md / AGENTS.md | PR review outcomes, reverted diffs |
| `gateway-agent` | workspace skills | corrections in the channel |
| `framework-app` | structured-output schemas in code | thumbs, escalations, task outcomes, traces |
| `prompt-program` | DSPy / Ax signatures | eval sets, existing metric functions |
| `hosted-nocode` | instructions in the UI | ratings, edits, conversation exports |

## Step 1: Read the signal

From the `signal-card` envelope read `chosenSignal` and `slots.artifact`. Without an envelope, ask
for the one line "My agent gets better when ___ goes up", or reconstruct it from the code.

## Step 2: List the output fields the signal touches

Name each output field (with `path:line` where it is defined) whose value changes the signal. A
field the signal doesn't touch goes in `fieldsUnscored`, with no metric.

## Step 3: Pick a tier per field

| tier | use when | examples |
|---|---|---|
| `code` | the right answer can be checked exactly | exact match, verbatim span, schema valid, label equality |
| `partial` | closeness matters more than exactness | token overlap, set F1, numeric tolerance |
| `judge` | only a reader can tell | an LLM grades against a written rubric |

For every `judge` metric, write the rubric (criteria and pass conditions) and one line on judge
bias: position, length, and self-preference when the judge shares a model with the agent.

## Step 4: Write the signature three ways

- **Python (DSPy shape):** `def metric(example, pred, trace=None) -> float`. DSPy accepts a
  float, int or bool; return a float in 0..1.
- **TypeScript (Ax shape):** `({ prediction, example }) => number`, normalized to 0..1.
- **Plain language:** one sentence a reviewer can check by hand.

For GEPA, say whether the metric can also return feedback text
(`dspy.Prediction(score=..., feedback=...)`). Code-tier metrics usually can: say which check failed.

## Step 5: Baseline and labels

- **Baseline:** what a do-nothing version scores (always the majority label, an empty answer, or the
  current prompt unchanged). Without a baseline, no gain can be claimed.
- **Labels needed:** for each metric, the reference values it compares against (`labelsNeeded`).
  `gold-set` plans how to collect them.

## Output

```markdown
# Metric Signature: <agent name>

**Signal:** <chosenSignal, and where it came from>

| Metric | Output field | Tier | Labels needed | Feedback text |
|---|---|---|---|---|

<for each metric: the Python, TypeScript and plain-language signatures>

**Baseline:** <do-nothing version and its expected score, or "unknown (ask: …)">
**Unscored fields:** <fields the signal doesn't touch>
```

Then the envelope as the last fenced block, then the footer line.

```yaml
sia:
  skill: metric-signature
  version: 1
  agent: { name: "<name>", summary: "<one line>" }
  deploymentType: <type>
  in_ref: signal-card#v1          # or "none"
  out:
    metrics:
      - name: queue_exact
        outputField: queue
        tier: code                # code | partial | judge
        range: "0..1"
        feedbackText: true
        labelsNeeded: [final_queue]
        signature:
          python: "def metric(example, pred, trace=None) -> float: return float(pred.queue == example.final_queue)"
          typescript: "({ prediction, example }) => (prediction.queue === example.final_queue ? 1 : 0)"
          plain: "1 when the routed queue equals the queue the ticket ended in, else 0"
    baseline: "always 'how-to' (most common queue)"
    fieldsUnscored: [urgency, tags]
  recommendations:
    - id: ms-1
      title: <imperative, one line>
      why: <one line tied to evidence>
      do: <a step an agent or engineer can do without rereading the report>
      effort: S                   # S | M | L
      impact: high                # high | medium | low
      evidence: ["<path:line>"]   # or "unknown (ask: <question>)"
      next_skill: gold-set
      links: []
```

> Series and help: peleke.me · LinkedIn

**Recommendations:** at most seven, ordered by leverage, each with evidence or
`unknown (ask: …)`. No pitching.

## Gotchas

- A metric on a field nothing reads optimizes nothing. Check `fieldsUnscored` against the consumers.
- Exact match on free text almost always reads as 0. Use partial credit or a verbatim span instead.
- A judge that shares a model with the agent tends to prefer its own outputs. Name that bias.
- A boolean metric is fine for DSPy demo bootstrapping, but averaging over examples needs floats.

## Examples

- Ticket router with a `queue` enum and a logged final queue → one `code` metric (queue exact
  match), labels = final queue, baseline = majority queue; `urgency` and `tags` unscored.
- Sales-email drafter whose reps edit drafts before sending → a `partial` metric (token overlap of
  the draft with the sent version); reply rate noted as a slower signal, not the metric.
