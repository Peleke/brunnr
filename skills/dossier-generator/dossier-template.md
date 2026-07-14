# {{OFFERING_TITLE}} — Partner Dossier

*Partner-confidential. A dual-format handoff: **Part A** is a human executive summary to skim and decide from; **Part B** is an agent-facing implementation spec to execute. They snap together on the I/O contract in between.*

*Confidentiality: the source system is a production engine built for a real client, referred to here only by codename **{{CLIENT_CODENAME}}** ({{CLIENT_DOMAIN}}). All identifying detail is scrubbed. The architecture is a generalized {{CLOUD}}-native, {{LANGUAGE}}-laid-out analog that stays structurally executable without fingerprinting the client.*

---

# PART A — Executive Summary (human-facing)

## Intent
{{ONE_PARAGRAPH: what this is, what is proposed, why now. A decision brief, not a pitch.}}

## The ROI argument (read this first)
**We do not sell {{TECH}}. We sell {{VALUE_IN_BUSINESS_TERMS}}.**

The cost we remove:
- **{{COST_1}}** ({{how it accrues, ideally a K x H x C style formula}})
- **{{COST_2}}**
- **{{COST_3, e.g. the error/liability tail}}**
- **{{COST_4, e.g. audit}}**

Price against the value removed, not features or tokens. The buyer is {{BUYER_MOTIVATION}}; lead with {{THE_FEAR}} and {{THE_SAVINGS}}, and the technology is a footnote.

## Estimated cost (loose, tighten later)
| Rung | Model | Rough anchor |
|------|-------|--------------|
| {{RUNG_1}} | Fixed fee | {{ANCHOR_1}} |
| {{RUNG_2}} | Fixed scope | {{ANCHOR_2}} |
| {{RUNG_3}} | Scoped project | {{ANCHOR_3}} |
| {{RUNG_4}} | Retainer | {{ANCHOR_4}} |

Margin lives in the reusable core; the bespoke part is {{BESPOKE_SURFACE}}.

## The opportunity, in a paragraph
{{ONE_PARAGRAPH: the pain, why off-the-shelf fails, what we have built.}}

## Principal sources
- {{SOURCE_1}}
- {{SOURCE_2}}

## Assumptions
- {{ASSUMPTION_1}}
- {{ASSUMPTION_2}}

## Confidence boundaries
- **High confidence (grounded in code that runs):** {{...}}
- **Medium confidence (reasoned, not tested):** {{...}}
- **Low confidence (open research questions):** {{...}}. The first things to test, not to assume.

## The decision this asks for → Decisions Block
```yaml
decisions:
  go_no_go: <go | no-go | explore>
  first_vertical: <...>
  target_accounts: [<named, or "agent sources">]
  entry_motion: <paid-discovery | free-qualifier>
  offer_tier_to_lead_with: <...>
  owner_split_confirmed: <yes | adjust: ...>
  open_questions_to_close: [<...>]
```

---

# I/O CONTRACT

Part A produces `decisions`. Part B **consumes `decisions`** as execution parameters:

| Part A decision | Drives in Part B |
|-----------------|------------------|
| `first_vertical` | the comparable-client research sub-pipeline scope |
| `target_accounts` | the account-research and outreach-draft tasks |
| `entry_motion` | which offer rung is scoped and priced first |
| `offer_tier_to_lead_with` | the deliverable an agent scopes first |
| `open_questions_to_close` | the research tasks queued before commitment |

If a decision field is empty, Part B halts on that branch and flags it rather than guessing.

---

# PART B — Implementation Spec (agent-facing)

## Operational instructions
Execute this partner-confidential go-to-market and delivery spec. Consume the `decisions` block. For each task, produce the named artifact. Codename the client ({{CLIENT_CODENAME}}); never output the real name. Mark unknown facts `TODO(verify)` and continue. Keep every claim confidentiality-safe.

## Opportunity, structured
- **ICP:** {{...}}
- **Deal flow (stages):** {{...}}
- **Timelines:** {{...}}

## Task 1 — Comparable-client research sub-pipeline
Scope to `first_vertical`. Define concrete ICP filters, generate 15-30 real candidate accounts (web research, cited), and for each give the likely buyer persona, plausible pain, and reachability. Rank by fit and ease-to-close. Output a table.

## Task 2 — Account research (for `target_accounts`)
For each named account: the corpus and QA function, the likely buyer, a specific observable pain, a one-line wedge. One brief each.

## Task 3 — Offer sketch (scope `offer_tier_to_lead_with` first)
The ladder, each rung with its ROI hook attached. Reusable-vs-bespoke split.

## Task 4 — Codebase architecture (generalized analog)
The system as a confidentiality-safe spec, grounded in the real codebase. State the invariant, the layers, and the "why not the simpler thing" defenses.

## Task 5 — Deliverables to emit
The comparable-client table, the per-account briefs, the entry offer sheet, a sanitized architecture one-pager, and a prioritized next-actions list keyed to `open_questions_to_close`.

---

*Next: the human fills the Decisions Block, an agent runs Part B against it, and the deck is generated per `deck-spec.md`.*
