---
name: signal-card
description: >
  Name the signal an agent should learn from, in one line ("My agent gets better when ___ goes
  up"), then lay out the self-improvement loop around it: act, take a signal, search for a better
  version, apply it. Fills the three choosable slots (signal, search, artifact) with options found
  in the codebase or the operator's description. Read-only. Link 2 of the SIA audit chain; reads
  the learning-check envelope. Use after learning-check, when an agent has no signal, or when
  "I edit the prompt" is the only improvement path.
license: MIT
---

# Signal Card

Most agents improve only when a person reads output, judges it, and edits the prompt. That
works until it has to scale, run unattended, or survive an audit. This skill writes down the
signal that would let the agent run that loop itself, and the slots around it.

The loop vocabulary (act → signal → search → apply) follows Micheal Lanham's *Self-Improving
Agents* (Manning).

## Rules

- **Read-only.** No edits, no agent runs, no model or API calls.
- **The signal comes from outside the model.** A score from a test, a preference between two
  outputs, written feedback from a person, or a confidence value that something external checks.
- **One signal first.** Propose up to three candidates, then recommend one and say why.
- **Cite what exists.** For each slot, prefer options already present in the code (path:line).
  Mark anything new as "to build".
- **Never invent an upstream verdict.** If a field you read is missing, ask for it or reconstruct
  it and list it under `out.reconstructed`.

## Step 0: Read upstream and place the agent

If a `learning-check` envelope is in context, read `deploymentType`, `verdicts.signal` and
`firstFix`, and reuse its evidence. Otherwise place the agent in one deployment type yourself:

| type | where signals usually are |
|---|---|
| `coding-harness` | PR review outcomes, reverted diffs, CI results |
| `gateway-agent` | corrections in the channel |
| `framework-app` | thumbs, escalations, task outcomes in the app |
| `prompt-program` | labeled examples and existing metric functions |
| `hosted-nocode` | ratings, edits people make before using an output |

## Step 1: Current loop

Describe how the agent improves today in four nodes: agent runs → who reads the output → who
judges it → what gets edited. If a person fills the middle two, say "you are the loop".

## Step 2: Candidate signals

List up to three candidates. For each: what is measured, where it would come from, how often it
arrives, what it costs, and its type: **score**, **preference**, **feedback**, or **confidence**.

## Step 3: The one line

Write: **"My agent gets better when ___ goes up."** The blank names one measurable quantity on a
defined set of examples.

## Step 4: The slots

| Slot | Options | Pick for now |
|---|---|---|
| Signal | score · preference · feedback · confidence | the recommended candidate's type |
| Search | hill-climbing · an evolutionary optimizer such as GEPA · person reviewing proposals | the cheapest that fits |
| Artifact | instructions · demos · skill file · memory · code | what the search will change |

## Output

```markdown
# Signal Card: <agent name>

**Today:** <four-node loop; "you are the loop" if applicable>

**My agent gets better when <quantity> goes up.**

| Candidate | Type | Source | Frequency | Cost |
|---|---|---|---|---|

**Slots:** Signal = … · Search = … · Artifact = …
```

Then the envelope as the last fenced block, then the footer line.

```yaml
sia:
  skill: signal-card
  version: 1
  agent: { name: "<name>", summary: "<one line>" }
  deploymentType: <type>
  in_ref: learning-check#v1       # or "none"
  out:
    candidates:
      - { quantity: "<what is measured>", type: preference, source: "<path:line or system>", frequency: "per PR", cost: "free; already recorded" }
    chosenSignal: "<the recommended candidate's quantity>"
    oneLine: "My agent gets better when <quantity> goes up."
    slots: { signal: preference, search: "person reviewing proposals", artifact: "skill file" }
  recommendations:
    - id: sc-1
      title: <imperative, one line>
      why: <one line tied to evidence>
      do: <a step an agent or engineer can do without rereading the report>
      effort: S                   # S | M | L
      impact: high                # high | medium | low
      evidence: ["<path:line>"]   # or "unknown (ask: <question>)"
      next_skill: metric-signature
      links: []
```

> Series and help: peleke.me · LinkedIn

**Recommendations:** at most seven, ordered by leverage, each with evidence or
`unknown (ask: …)`. No pitching.

## Gotchas

- "User satisfaction" is not a signal until you say how it's recorded per output.
- A signal that arrives once a quarter can't drive search; pair it with a faster proxy and say so.
- If the honest answer is "when I edit the prompt", that is the finding. Don't dress it up.
- `slots.signal` is the type (score, preference, feedback, confidence), not the quantity.

## Examples

- Code-review bot: "My agent gets better when the share of its comments that authors resolve
  (not dismiss) goes up." Type: preference. Search: person reviews proposed instruction changes.
  Artifact: skill file.
- Changelog summarizer: "…when the share of summary quotes found verbatim in the source goes up."
  Type: score. Search: bootstrap demos. Artifact: demos.
