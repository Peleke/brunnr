---
name: learning-check
description: >
  Audit an agent (a repo, a service, or a written description) for the three properties of
  learning: a feedback signal from outside the model, a lasting update, and measurable improvement
  on held-out examples. Answers per loop, gives each loop an outcome (no loop found, not learning,
  learning unmeasured, learning measured), and names the first thing to fix. Read-only. Link 1 of
  the SIA audit chain. Use when asking "does my agent actually learn?", before adding a memory
  feature, or before reaching for an optimizer.
license: MIT
---

# Learning Check

Answer three questions about each loop an agent has, with evidence for each answer. Memory
features (the model writes notes and reads them back) usually fail at least one: nothing records
how much a note changed, so a note confirmed a hundred times counts the same as one invented once.

## Rules

- **Read-only.** Do not edit files, run the agent, or make model or API calls.
- **Evidence or "no".** Every "yes" or "partial" cites a file path (with line numbers) or a
  quoted sentence from the operator's description. No evidence means the answer is "no"; say
  where you looked.
- **The model grading itself is not a signal.** A second call to the same model counts as the
  model reviewing itself.
- **A person carrying the signal or applying the change makes the answer "partial"**, not yes.

## Step 0: Job and deployment type

Write the agent's job in one sentence. Then place it in one deployment type; the type tells you
where to look.

| type | prompts / instructions | signals / feedback | traces / data |
|---|---|---|---|
| `coding-harness` (Claude Code, Codex, Cursor) | CLAUDE.md / AGENTS.md, skills, rules | PR review outcomes, reverted diffs, hooks | session transcripts |
| `gateway-agent` (OpenClaw) | workspace skills, memory files | user corrections in channel | channel logs |
| `framework-app` (LangGraph, CrewAI, agent SDKs) | prompts in code | thumbs, escalations, task outcomes | LangSmith / Langfuse / OTel traces |
| `prompt-program` (DSPy, Ax) | signatures | existing metrics | eval sets, optimizer logs |
| `hosted-nocode` (custom GPTs, n8n, Copilot Studio) | instructions in the UI | ratings, edits | conversation exports |

## Step 1: Find the loops

A **loop** is one signal source feeding one artifact that changes (user corrections → a memory
file; labeled examples → a demo set). Answer the three questions once per loop. Things that only
steer the next step inside one run (a tool loop, a retry, a self-check) get a one-line note, not a
loop. If nothing feeds any artifact, the outcome is **no loop found**: describe the loop you'd
want, mark it "proposed", and answer no to all three.

## Step 2: The three questions, per loop

| | yes | partial | no |
|---|---|---|---|
| **Q1** When it gets something wrong, what tells it? | A signal the model can't produce by reviewing itself (a test, CI, a tool's exit code, a user, a label, a human click) reaches the agent without anyone carrying it, and says whether the output was right | Such a signal exists but a person has to carry it to the agent; or the only judge is a separate LLM not checked against people | Only the model reviewing itself, or nothing |
| **Q2** When that happens, what changes, and how much? | A change survives across runs, is applied without a person, and is recorded in a unit you can diff | A change persists but its size isn't recorded; or it's computed once and never saved; or a person applies it | Nothing outlasts one run |
| **Q3** Is it measurably better over time? | A score on held-out examples, compared with a baseline, recorded more than once | A held-out set or a baseline exists, but they aren't run together | No held-out number |

## Step 3: Outcome per loop

- **not learning:** Q1 is no, or Q2 is no, or a person both carries the signal and applies the
  change and Q3 is no. That's the person learning, not the agent.
- **learning, unmeasured:** Q1 and Q2 are yes or partial; Q3 is no or partial.
- **learning, measured:** Q1 and Q2 are yes or partial; Q3 is yes.
- Add **(partial loop)** to a learning outcome when Q1 or Q2 is partial.

**Headline:** the best loop's outcome, naming the loop.

## Output

```markdown
# Learning Check: <agent name>

**Job:** <one sentence> · **Type:** <deploymentType>

## Loop: <name>

| # | Question | Verdict | Evidence |
|---|---|---|---|
| 1 | What tells it it was wrong? | yes / partial / no | path:line or quote |
| 2 | What changes when it's wrong? | yes / partial / no | path:line or quote |
| 3 | Is it measurably better over time? | yes / partial / no | path:line or quote |

**Outcome:** <outcome for this loop>

**Headline:** <best loop's outcome (loop name); other loops: …>

**Memory vs learning:** <one sentence: does any "memory" feature here record how much it changed?>

**First fix:** <start at the first question that isn't "yes" in the best loop; one concrete step>
```

Then the envelope as the last fenced block, then the footer line. `verdicts` are the headline
loop's answers; `loops` lists every loop.

```yaml
sia:
  skill: learning-check
  version: 1
  agent: { name: "<name>", summary: "<one line>" }
  deploymentType: <type>
  in_ref: none
  out:
    verdicts: { signal: partial, update: partial, convergence: "no" }
    loops:
      - { name: "<loop>", signal: partial, update: partial, convergence: "no", outcome: "not learning", evidence: ["<path:line>"] }
    outcome: "not learning"       # headline: no loop found | not learning | learning, unmeasured | learning, measured, plus " (partial loop)"
    firstFix: "<one concrete step>"
  recommendations:
    - id: lc-1
      title: <imperative, one line>
      why: <one line tied to evidence>
      do: <a step an agent or engineer can do without rereading the report>
      effort: S                   # S | M | L
      impact: high                # high | medium | low
      evidence: ["<path:line>"]   # or "unknown (ask: <question>)"
      next_skill: signal-card
      links: []
```

> Series and help: peleke.me · LinkedIn

**Recommendations:** at most seven, ordered by leverage, each with evidence or
`unknown (ask: …)`. No pitching. Quote `"no"` in YAML so it stays a string.

## Gotchas

- An eval that exists but never runs is "partial" on Q3, not "yes".
- Logging every output is not a signal unless something marks outputs right or wrong.
- Don't count the optimizer's training score as convergence; only held-out scores count.
- A person editing the prompt after noticing failures, with no eval, is "not learning": the person
  carries the signal and applies the change.

## Examples

- "Run a learning check on this repo" → locate the agent in code, find its loops, fill one table
  per loop from the files.
- "My assistant appends a line to its memory file when I correct it in chat. Does it learn?" →
  Q1 yes (corrections reach it), Q2 partial (the file persists; nothing records how much changed),
  Q3 no. Outcome: learning, unmeasured (partial loop). First fix: record per correction which
  memory line it added, and count repeat corrections.
