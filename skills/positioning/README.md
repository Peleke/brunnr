# Positioning

[![pipeline: hunter](https://img.shields.io/badge/pipeline-hunter-blue)]() [![framework: Dunford](https://img.shields.io/badge/framework-Dunford-purple)]() [![context: fork](https://img.shields.io/badge/context-fork-orange)]()

Strategic positioning engine implementing April Dunford's "Obviously Awesome" framework. Sits between `offer-scope` and `pitch` in the hunter pipeline. Produces a complete positioning canvas, messaging hierarchy, ICP profile, and competitive landscape — all grounded in web research and upstream pipeline data.

## Pipeline Position

```
offer-scope → positioning → pitch
```

**Feeds FROM**: `offer-scope` (product context, draft positioning), `persona-extract` (Four Forces, pain stories), `swot-analysis` (validated strengths, moat assessment)

**Feeds INTO**: `pitch` (headline from messaging hierarchy, problem section from competitive alternatives, copy avoids anti-messaging terms)

**Kanban**: Does NOT advance the card (enrichment step). Card stays in "Offer Scoped."

## The 8 Phases

| Phase | What It Does | Web Search? |
|-------|-------------|-------------|
| 1. Competitive Alternatives | Maps what customers do today without you (min 4, max 8) | Yes |
| 2. Unique Attributes | Identifies what you do that alternatives can't — classifies as truly_unique, best_in_class, table_stakes, or irrelevant | Yes |
| 3. Value Articulation | Extracts functional, emotional, and social value from each unique attribute | No |
| 4. Target Customer (ICP) | Builds ultra-specific ICP + anti-ICP, specific enough to find 10 in 30 min | No |
| 5. Market Category | Generates 3-5 candidates, web-validates, selects using Dunford criteria | Yes |
| 6. Emotional Hooks | Discovers relief vs. aspiration framing + anti-messaging words to NEVER use | No |
| 7. Expansion Sequence | Maps now/next/after messaging discipline per lifecycle stage | No |
| 8. Competitive Moats | Identifies technical/market/data/brand moats with messaging order | No |

## I/O

### Input

| Source | Required? | What It Provides |
|--------|-----------|-----------------|
| `offer-scope` | Yes | Product name, format, price, value equation, positioning draft, build spec |
| `persona-extract` | Yes | Pain stories, Four Forces, decision triggers, objections, WTP, channels |
| `swot-analysis` | Recommended | Validated strengths → attributes, moat assessment → Phase 8 |
| `decision-log` | Yes | Decision record for the opportunity |
| `signal-scan` | Yes | PAIN, SPEND, COMPETITIVE, AUDIENCE signals |
| Seed document | Optional | Existing positioning exercise to validate and deepen |

### Output

| Artifact | Type | Vault Path |
|----------|------|-----------|
| Positioning Canvas | `positioning-canvas` | `Admin/Product-Discovery/Positioning/{slug}-positioning-canvas-{date}.md` |
| Messaging Hierarchy | `messaging-hierarchy` | `Admin/Product-Discovery/Positioning/{slug}-messaging-hierarchy-{date}.md` |
| ICP Profile | `icp-profile` | `Admin/Product-Discovery/Positioning/{slug}-icp-profile-{date}.md` |
| Competitive Landscape | `competitive-landscape` | `Admin/Product-Discovery/Positioning/{slug}-competitive-landscape-{date}.md` |
| JSON Spec | structured | `Admin/Product-Discovery/Positioning/{slug}-positioning-{date}.json` |

## Workflow

```
1. Load _conventions.md
2. Read upstream artifacts (offer-scope, persona, swot, decision, signal-scan)
3. Phase 1: Web search for competitive alternatives
4. Phase 2: Map unique attributes against alternatives
5. Phase 3: Articulate value per advancing attribute (functional/emotional/social)
6. Phase 4: Build ICP + anti-ICP from persona data + Phase 3 value
7. Phase 5: Generate category candidates, web-validate, select
8. Phase 6: Discover emotional hooks + anti-messaging → Bragi review gate
9. Phase 7: Map expansion sequence (now/next/after)
10. Phase 8: Identify competitive moats with messaging order
11. Produce all 5 output artifacts
12. Write to vault
```

## Seed Mode

Provide an existing positioning exercise as input and the skill will validate, structure, and deepen it rather than starting from scratch. Useful when:

- A prior brainstorm produced positioning ideas that need structure
- A competitor analysis exists that should feed alternatives
- An existing product has positioning that needs refreshing

## Quality Gate

Phase 6 (emotional hooks) and the messaging hierarchy are human-facing prose. Both MUST pass the Bragi review gate (`buildlog_gauntlet` with Bragi persona) before finalization — per the prose quality convention in `_conventions.md`.

## References

| File | Purpose |
|------|---------|
| `references/output-schema.json` | JSON Schema for structured output validation |
| `references/dunford-framework.md` | Dunford's "Obviously Awesome" framework reference |
| `references/positioning-canvas-template.md` | Blank canvas scaffold for Phases 1-8 |
| `references/category-selection-guide.md` | Category evaluation criteria for Phase 5 |

## Intellectual Lineage

- **April Dunford** — "Obviously Awesome" (core framework)
- **Al Ries & Jack Trout** — "Positioning: The Battle for Your Mind" (anti-messaging, mental real estate)
- **Geoffrey Moore** — "Crossing the Chasm" (beachhead market, ICP specificity)
- **Clayton Christensen** — "Competing Against Luck" (Jobs To Be Done → value dimensions)
- **W. Chan Kim & Renée Mauborgne** — "Blue Ocean Strategy" (category creation, non-competition)
- **Hamilton Helmer** — "7 Powers" (moat identification framework)
- **Alex Hormozi** — "$100M Offers" (value equation cross-reference)
