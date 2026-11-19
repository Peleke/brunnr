# SIA chain conventions

Shared rules for the SIA (self-improving agent) audit chain. Every chain skill follows this file.
Each skill copies the parts its report needs, so it still works when installed without this file.

| link | skill | audits |
|---|---|---|
| 1 | `learning-check` | does the agent learn at all |
| 2 | `signal-card` | which signal it should learn from |
| 3 | `metric-signature` | the metric function for that signal |
| 3b | `field-table` | every output field (optional side link) |
| 4 | `gold-set` | the reference set the metric runs on |
| 5 | `eval-power` | whether the eval can detect a change |

## Deployment type

Every chain skill first places the target agent in one of five deployment types. The type says
where to look for evidence.

| `deploymentType` | examples | prompts / instructions | signals / feedback | traces / data |
|---|---|---|---|---|
| `coding-harness` | Claude Code, Codex, Cursor | CLAUDE.md / AGENTS.md, skills, rules | PR review outcomes, reverted diffs, hooks | session transcripts |
| `gateway-agent` | OpenClaw | workspace skills, memory files | user corrections in channel | channel logs |
| `framework-app` | LangGraph, CrewAI, OpenAI / Claude Agent SDK, Mastra, Google ADK | prompts in code | thumbs, escalations, task outcomes | LangSmith / Langfuse / OTel traces |
| `prompt-program` | DSPy, Ax | signatures | existing metrics | eval sets, optimizer logs |
| `hosted-nocode` | custom GPTs, n8n, Copilot Studio | instructions in the UI | ratings, edits | conversation exports |

If the agent fits none of them, pick the closest and say why in one line.

## Envelope

Every report ends with exactly one fenced YAML block, the **envelope**. It is the last fenced
block in the report. The next skill in the chain reads it.

```yaml
sia:
  skill: metric-signature
  version: 1
  agent: { name: "support-triage", summary: "LangGraph ticket router" }
  deploymentType: framework-app
  in_ref: signal-card#v1        # the envelope this run read, or "none"
  out: { }                      # skill-specific fields; see each skill
  recommendations: [ ]          # see below
```

**Reading upstream:**
- If an upstream envelope is in context (pasted, or in a file the user names), read it and set
  `in_ref` to `<skill>#v<version>`.
- Otherwise ask for the fields this skill reads, or reconstruct them from the code. Mark each
  reconstructed field by adding its name to `out.reconstructed: [...]`, and set `in_ref: none`.
- Never invent an upstream verdict. A field you can't find or reconstruct is `unknown`.

**Fields each link reads and writes** (`tests/sia-chain/chain.yaml` is the machine-readable copy,
and a test checks that every read has an upstream writer):

| link | reads (from upstream `out`) | writes (`out`) |
|---|---|---|
| 1 `learning-check` | none | `verdicts`, `loops`, `outcome`, `firstFix` |
| 2 `signal-card` | `verdicts.signal`, `firstFix` | `candidates`, `chosenSignal`, `oneLine`, `slots` |
| 3 `metric-signature` | `chosenSignal`, `slots.artifact` | `metrics`, `baseline`, `fieldsUnscored` |
| 3b `field-table` | `metrics[].outputField` | `fields` |
| 4 `gold-set` | `metrics[].labelsNeeded`, `metrics[].outputField` | `exampleSchema`, `sources`, `labelingPlan`, `split`, `leakageChecks` |
| 5 `eval-power` | `split`, `metrics` | `reps`, `interval`, `interpretation`, `claimVerdicts` |

`deploymentType` sits at the top level of every envelope, so every link reads it.

## Recommendations

The most important part of every report. YAML, inside the envelope:

```yaml
recommendations:
  - id: ms-1                       # <skill initials>-<n>, ordered by leverage
    effort: S                      # S | M | L
    impact: high                   # high | medium | low, spelled out
    title: "Score vendor IDs with exact match before trying a judge"
    why: "the chosen signal is a correct/incorrect vendor; a code metric is enough"
    do: "add metric(example, pred) -> float returning 1.0 on vendor match; run it on 30 invoices"
    evidence: ["src/ap/extract.py:41"]
    next_skill: gold-set
    links: []
```

**Rules:**
- Order by leverage: the item that unblocks the most comes first.
- Double-quote free-text values so the envelope parses as YAML.
- At most seven items.
- Every item has `evidence` (paths with line numbers, or quotes from the operator), or
  `evidence: "unknown (ask: <the question that would settle it>)"`.
- `do` is doable by an agent or an engineer without rereading the report.
- No pitching. The report states findings; it doesn't sell anything.

**File them as issues** (needs `yq` and `gh`; save the envelope as `report.yaml`):

```bash
yq -o=json '.sia.recommendations[]' report.yaml | jq -c '.' | while read -r r; do gh issue create --title "$(jq -r .title <<<"$r")" --body "$(jq -r '"Why: \(.why)\n\nDo: \(.do)\n\nEffort: \(.effort) · Impact: \(.impact)\nEvidence: \(.evidence|if type=="array" then join(", ") else . end)\nNext: \(.next_skill)"' <<<"$r")"; done
```

## Footer

One line after the envelope, in every report:

> Series and help: peleke.me · LinkedIn

## Rules shared by every chain skill

- **Read-only.** Don't edit files, run the agent, or make model or API calls.
- **Evidence or "unknown".** Every claim cites a file path with line numbers or a quote from the
  operator.
- **Specific to this agent.** Generic advice that would fit any agent doesn't belong in the report.
