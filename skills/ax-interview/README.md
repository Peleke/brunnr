# ax-interview

**Run a structured AX Interview on any agent-tool interaction session.**

The AX Interview is a post-task research protocol that surfaces friction invisible to evals. It combines behavioral trace analysis with Gricean pragmatic theory to detect what your agent isn't telling you: the tools it silently avoided, the responses it worked around, the descriptions that never opened a frame.

> Engineering optimizes for what you already know to measure. Research discovers what you didn't know to ask.

## What it does

After an agent completes a real task, `ax-interview` runs a six-phase analysis:

```
Session traces ──→ Phase 1: Trace Analysis (maxim violations)
                ──→ Phase 2: Implicature Detection (behavioral signals)
                ──→ Phase 3: Dialog Probe (structured interview)
                ──→ Phase 4: Cross-Reference (faithfulness check)
                ──→ Phase 5: Pragmatic Coherence Score
                ──→ Phase 6: Structured Report + Ranked Fixes
```

The output is a **Pragmatic Coherence Score (PCS)** across five dimensions, an implicature index, and a ranked list of concrete fixes.

## The framework

### Gricean maxims applied to agent-tool interaction

| Maxim | What it measures | Tool-side violation | Agent-side violation |
|---|---|---|---|
| **Quantity** | Response completeness | 67KB payload (too much) | Agent requests everything |
| **Quality** | Response accuracy | Stale data, wrong format | Agent propagates bad data |
| **Relation** | Response relevance | 30% irrelevant content | Agent calls wrong tool |
| **Manner** | Response clarity | Opaque IDs, nested JSON | Agent retries, routes around |

### The implicature layer

What's communicated by what's *not* said:

- **Tool avoidance** = "this tool failed my cost-benefit calculation"
- **Silent routing-around** = "I found a better way and didn't tell you"
- **Unexplained retries** = "the response was unclear"
- **Context burn without output** = "I processed your response and got nothing useful"

### CoT faithfulness check

Cross-references what the agent *says* with what it *did*. Based on Anthropic's interpretability research showing models lack metacognitive access to their own reasoning:

| Agent says | Trace shows | Classification |
|---|---|---|
| Matches trace | Behavior confirms | **Genuine** — trust it |
| Plausible but unsupported | No evidence | **Fabricated** — discard explanation |
| Matches your framing | Ambiguous | **Backward** — contaminated |

## Example output

```
# AX Interview Report: buildlog gauntlet_loop

## Pragmatic Coherence Score

| Dimension        | Score | Signal                                        |
|------------------|-------|-----------------------------------------------|
| Quantity         | 0.17  | agent used 15 of 86 rules — 83% noise         |
| Quality          | 0.89  | 1 retry due to stale learning data             |
| Relation         | 0.71  | 2 of 7 calls were to irrelevant tool variants  |
| Manner           | 0.56  | hash IDs forced 4 lookup workarounds           |
| CoT Faithfulness | 0.60  | 2 of 5 explanations not corroborated by traces |
| **Composite PCS**| **0.55** |                                             |

## Implicature Index: 3 unresolved signals

1. Agent never called `gauntlet_learn` despite it being available (Relation)
2. Agent parsed JSON response via Python shell-out instead of using tool output (Manner)
3. Agent did not reference learning system in final summary (Quantity — learning void)
```

## Installation

```bash
# From the brunnr registry
brunnr install ax-interview

# Or via Claude Code marketplace
/plugin marketplace add Peleke/brunnr
/plugin install ax-interview@brunnr-skills
```

## Usage

After completing a task session:

```
Run an AX Interview on this session. The tools under evaluation are [tool names].
Here are the traces: [paste or reference trace data]
```

Or in dialog-only mode (no traces):

```
Run an AX Interview on the task I just completed. Focus on [tool names].
```

## The Pragmatic Coherence Score

PCS measures how well a tool-agent exchange adheres to the cooperative principle:

| Score | Interpretation |
|-------|---------------|
| **0.85+** | Strong coherence. The exchange is cooperative. |
| **0.60–0.84** | Moderate friction. Specific maxims need attention. |
| **Below 0.60** | Significant breakdown. Redesign the tool interface. |

PCS is a behavioral proxy for what Anthropic measures with attribution graphs. They look inside the model. We compare what it says with what it did.

## Lineage

- **NN Group**: user interview methodology, three-level experience model (extended to six for agents)
- **Grice**: cooperative principle and four maxims, conversational implicature
- **Anthropic**: "Writing Tools for Agents" (engineering), "Tracing Thoughts in Language Models" (interpretability)
- **Rappa et al.**: Gricean analysis of human-LLM interaction (pragmatic coherence requires both parties)

## Part of the AX series

This skill accompanies [The AX Interview](https://peleke.me/writing/ax-07-the-ax-interview) article on the portfolio site. The article provides the theory; this skill provides the protocol.

---

*Security-scanned by [brunnr](https://github.com/Peleke/brunnr). Seven threat classes. Zero LLM in the gate.*
