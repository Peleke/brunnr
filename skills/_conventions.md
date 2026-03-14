---
name: hunter-conventions
description: "Shared conventions for the hunter product-discovery pipeline: canonical paths, frontmatter contracts, folder-to-type mapping, statuses, tags, cross-references, and the PipelineEnvelope schema."
---

# Hunter Pipeline Conventions
## Preamble — loaded by every skill in the hunter pipeline

All skills in the hunter product discovery pipeline MUST follow these conventions.

---

## Path Variables

These variables are used throughout all pipeline skills. The current values for this installation are listed below. When the pipeline is ejected to a standalone repo, these are set via `.hunter-config.yaml`.

| Variable | Current Value |
|---|---|
| `${VAULT}` | `/Users/peleke/Library/Mobile Documents/iCloud~md~obsidian/Documents/ClawTheCurious` |
| `${SKILLS_DIR}` | `/Users/peleke/Documents/Projects/skills/skills/custom` |
| `${HUNTER_DIR}` | `/Users/peleke/Documents/Projects/hunter` |

---

## Canonical Paths

### Obsidian Vault (PRIMARY output target)
```
${VAULT}
```

**IMPORTANT**: This is the iCloud-synced vault. Do NOT write to `/Users/peleke/Documents/Vaults/ClawTheCurious/` — that path is stale.

### Skills Directory
```
${SKILLS_DIR}/
```

### Hunter Project (repo-relative docs, NOT primary output)
```
${HUNTER_DIR}/
```

Use `${HUNTER_DIR}/docs/` for internal working documents only. All publishable/queryable output goes to the vault.

---

## Vault Folder Contract (Type → Folder Mapping)

Every document type maps to exactly one folder. This is the "table" in our vault-as-database.

| Document Type | Folder | Source Skill |
|---|---|---|
| Signal Scan | `Admin/Product-Discovery/Signal-Scans/` | `signal-scan` |
| Decision | `Admin/Product-Discovery/Decisions/` | `decision-log` |
| Persona | `Admin/Product-Discovery/Personas/` | `persona-extract` |
| SWOT Analysis | `Admin/Product-Discovery/SWOT/` | `swot-analysis` |
| Offer Spec | `Admin/Product-Discovery/Offers/` | `offer-scope` |
| Positioning Canvas | `Admin/Product-Discovery/Positioning/` | `positioning` |
| Messaging Hierarchy | `Admin/Product-Discovery/Positioning/` | `positioning` |
| ICP Profile | `Admin/Product-Discovery/Positioning/` | `positioning` |
| Competitive Landscape | `Admin/Product-Discovery/Positioning/` | `positioning` |
| Pitch | `Admin/Product-Discovery/Pitches/` | `pitch` |
| Community Pitch | `Admin/Product-Discovery/Offers/` | `community-pitch` |
| Skool Pitch | `Admin/Product-Discovery/Offers/` | `skool-pitch` |
| Session Log | `Admin/Product-Discovery/Sessions/` | `hunter-log` |
| Pipeline Board | `Admin/Product-Discovery/Pipeline.kanban.md` | `hunter-log` |
| Pipeline Index | `Admin/Product-Discovery/_index.md` | `hunter-log` |
| Lead | `Admin/Outreach/Leads/` | `hunter-log` |
| Conversation | `Admin/Outreach/Conversations/` | `hunter-log` |
| Outreach Board | `Admin/Outreach/Hunter-Log.kanban.md` | `hunter-log` |
| Content Brief | `Writing/Content-Briefs/` | `content-planner` |
| Content Board | `Writing/Content-Plan.kanban.md` | `content-planner` |
| Draft | `Writing/Drafts/` | `content-planner` / manual |
| Wild Index | `Writing/From-The-Wild/` | `wild-scan` |
| One-Pager | `Admin/Product-Discovery/One-Pagers/` | `one-pager` |
| Research Note | `Writing/Research/` | manual |

**Rules:**
- One file per artifact (scan, decision, persona, offer, etc.)
- Filename format: `{descriptive-slug}-{YYYY-MM-DD}.md`
- If a file already exists at the target path: APPEND under `## Update: {ISO timestamp}`, do NOT overwrite

---

## Frontmatter Contract

Every document MUST have YAML frontmatter with AT MINIMUM these fields:

### Required (all types)
```yaml
type: string        # one of: signal-scan | decision | persona | swot-analysis |
                    # offer-spec | positioning-canvas | messaging-hierarchy |
                    # icp-profile | competitive-landscape |
                    # pitch | community-pitch | skool-pitch |
                    # session | content-brief | wild-index | lead |
                    # conversation | draft | research-note
date: YYYY-MM-DD    # creation date
status: string      # see valid statuses below
tags: string[]      # MUST include hunter/{type} or content/{type} at minimum
```

### Valid Statuses by Type

| Type | Valid Statuses |
|---|---|
| signal-scan | `complete`, `partial` |
| decision | `active`, `superseded`, `abandoned` |
| persona | `complete`, `partial` |
| swot-analysis | `complete`, `partial` |
| offer-spec | `spec`, `building`, `shipped`, `killed` |
| positioning-canvas | `complete`, `partial` |
| messaging-hierarchy | `complete`, `partial` |
| icp-profile | `complete`, `partial` |
| competitive-landscape | `complete`, `partial` |
| pitch | `draft`, `review`, `final`, `shipped` |
| community-pitch | `spec`, `building`, `launched`, `killed` |
| skool-pitch | `spec`, `building`, `launched`, `killed` |
| session | `in-progress`, `complete` |
| content-brief | `backlog`, `drafting`, `review`, `published` |
| lead | `cold`, `warm`, `hot`, `converted`, `lost` |
| conversation | `active`, `stale`, `closed` |
| draft | `wip`, `review`, `final` |
| wild-index | `active`, `archived` |
| research-note | `active`, `archived` |

### Tag Hierarchy

All tags use the `hunter/` prefix to avoid collisions with the rest of the vault.

```
hunter/
├── scan              # all signal scans
├── decision          # all decisions
├── persona           # all persona research
├── swot              # all SWOT analyses
├── offer             # all offer specs
├── positioning        # all positioning artifacts
├── pitch             # all pitches (go-to-market packages)
├── community         # all community pitches
├── skool             # all Skool-specific pitches
├── session           # all session logs
├── domain/
│   ├── devops-education
│   ├── programming-education
│   ├── cybersecurity-education
│   └── {slug}
├── opportunity/
│   └── {slug}
├── format/
│   ├── pdf
│   ├── video
│   ├── community
│   └── {type}
├── price/
│   └── {range}       # e.g., 29-49
└── status/
    ├── active
    ├── shipped
    └── killed

content/
├── brief             # all content briefs
├── from-the-wild     # wild-scan quote indices
├── series/
│   └── {slug}        # e.g., memory-gap, building-in-public, from-the-wild
├── channel/
│   ├── linkedin
│   ├── blog
│   └── substack
└── draft

outreach/
├── lead
├── conversation
└── status/
    └── {status}
```

---

## Cross-Reference Syntax

### Internal vault links (between documents in the vault)
Use Obsidian wikilinks:
```
[[Admin/Product-Discovery/Decisions/devops-first-2026-02-08]]
[[Admin/Product-Discovery/Personas/frustrated-mid-level-2026-02-08]]
[[Writing/Content-Briefs/every-framework-has-memory]]
```

### Buildlog references
```
buildlog://{repo-name}/{entry-slug}
```
Example: `buildlog://buildlog-template/workflow-enforcement-tiers-1-2`

### GitHub references
```
gh://{owner}/{repo}/pull/{number}
gh://{owner}/{repo}/issues/{number}
```
Example: `gh://Peleke/qortex/pull/62`

Or full URLs for PRs/issues:
```
[PR #62](https://github.com/Peleke/qortex/pull/62)
```

### Pipeline references (between skills)
Use the artifact ID (filename slug without extension):
```
signal_scan_ref: "devops-education-2026-02-08"
decision_ref: "devops-first-2026-02-08"
persona_ref: "mid-level-devops-engineer-2026-02-08"
```

---

## Discovery Protocol

To find documents across the vault, skills use:

1. **Glob** by folder: `Admin/Product-Discovery/Decisions/*.md` → all decisions
2. **Frontmatter filter**: read YAML, check `type`, `status`, `domain`, etc.
3. **Dataview queries** (in _index.md): `FROM "Admin/Product-Discovery/Decisions" WHERE status = "active"`

This is the vault-as-database pattern:
- Frontmatter = schema
- Folders = tables
- Cross-refs (wikilinks, refs) = foreign keys
- Dataview = SQL
- When we need a real backend, it's a mechanical migration

---

## Pipeline Data Flow

```
signal-scan ──→ decision-log ──→ persona-extract ──→ swot-analysis ──→ offer-scope ──→ positioning ──→ pitch ──→ one-pager ──→ hunter-log
                                        │                                    │
                                        │                              community-pitch ──→ hunter-log
                                        │                              skool-pitch ──→ hunter-log
                                        │
                                        └──→ content-planner
                                                    │
                                              (reads both pipelines
                                               + GitHub + buildlog
                                               + wild-scan indices)

wild-scan ──→ Writing/From-The-Wild/ (quote indices)
         └──→ Writing/Content-Briefs/ (series: "From the Wild")
              └──→ content-planner picks these up
```

Every skill:
1. Reads _conventions.md before doing anything
2. Produces JSON output (PipelineEnvelope)
3. Calls hunter-log to persist to the vault (OR writes directly following these conventions)
4. Links backward to upstream artifacts via `*_ref` fields in frontmatter
5. Updates Pipeline.kanban.md (see Pipeline Kanban Contract below)

---

## Context Metadata

Skills that perform extensive web search or analysis SHOULD declare `context: fork` in their YAML frontmatter:

| Skill | context: fork? | Reason |
|---|---|---|
| signal-scan | Yes | Extensive web search |
| decision-log | Yes | Multi-phase scoring |
| persona-extract | Yes | Web search + raw stories |
| swot-analysis | Yes | 4-quadrant research |
| reddit-harvest | Yes | Playwright session |
| offer-scope | No | Reads upstream, no search |
| positioning | Yes | Competitive alternatives + category validation |
| pitch | No | Generates from data |
| hunter-log | No | Pure I/O |

---

## Skill Description Guidelines

- `description` in YAML frontmatter MUST be under 100 tokens (~75 words)
- First sentence: what the skill does (verb phrase)
- Second sentence: when to use it
- No framework names or output format details in descriptions

---

## Pipeline Kanban Contract

**Path:** `{vault}/Admin/Product-Discovery/Pipeline.kanban.md`

The Pipeline kanban tracks every product idea from scan to shipped/killed. Skills that advance the pipeline stage MUST move the card as part of their output step.

### Columns and Owning Skills

| Column | Moved here by | Card format |
|--------|---------------|-------------|
| Signal Scanned | `signal-scan` | `- [ ] {product-or-domain-name}` |
| Decision Made | `decision-log` | `- [ ] {opportunity-name} — [[decision-ref]]` |
| Persona Researched | `persona-extract` | `- [ ] {opportunity-name} — [[persona-ref]]` |
| Offer Scoped | `offer-scope` | `- [ ] [[offer-ref\|Product Name ($price)]]` |
| Building | operator (manual) | `- [ ] [[pitch-ref\|Product Name ($price)]] — launch date: YYYY-MM-DD` |
| Shipped | operator (manual) | `- [ ] [[pitch-ref\|Product Name]] — shipped YYYY-MM-DD` |
| Killed | operator or kill criteria | `- [ ] ~~Product Name~~ — killed YYYY-MM-DD: {reason}` |

### How to Move a Card

1. Read `Pipeline.kanban.md`
2. Find the card by product/opportunity name (substring match is fine)
3. Remove the `- [ ]` line from the current column
4. Add the updated `- [ ]` line under the new column header
5. If the card does not exist yet (first time in pipeline), add it to the appropriate column

### Skills That Do NOT Move the Card

- `swot-analysis`: runs between persona and offer, does not advance the pipeline stage (card stays in "Persona Researched")
- `positioning`: runs between offer-scope and pitch, does not advance the pipeline stage (card stays in "Offer Scoped")
- `pitch`: the pitch generates launch materials but does not mean the operator has committed to launching. Card stays in "Offer Scoped" until the operator sets a launch date and moves it to "Building" manually.
- `content-planner`: operates on a separate content pipeline, does not touch the product discovery kanban

### Card Lifecycle Example

```
Monday:    signal-scan adds    "- [ ] DevOps education gap"                      → Signal Scanned
Monday:    decision-log moves  "- [ ] DevOps Decision Kit — [[decision-ref]]"    → Decision Made
Tuesday:   persona-extract moves "- [ ] DevOps Decision Kit — [[persona-ref]]"   → Persona Researched
Wednesday: offer-scope moves   "- [ ] [[offer-ref|DevOps Decision Kit ($29)]]"   → Offer Scoped
Thursday:  pitch runs, card stays in Offer Scoped (PR open, launch date TBD)
Friday:    operator moves      "- [ ] [[pitch-ref|DevOps Decision Kit ($29)]] — launch date: 2026-02-17" → Building
```

---

## PipelineEnvelope (Skill I/O Contract)

Every skill output wraps in:
```json
{
  "skill": "signal-scan | decision-log | persona-extract | swot-analysis | offer-scope | positioning | pitch | one-pager | community-pitch | skool-pitch | content-planner",
  "version": "1.0",
  "session_id": "session-YYYY-MM-DD-NNN",
  "timestamp": "ISO 8601",
  "input_refs": ["upstream-artifact-id", ...],
  "output": { ... }
}
```

---

## Prose Quality Gate

**MANDATORY**: Any skill that produces prose content (landing page copy, launch posts, README copy, email sequences, content briefs, pitch summaries) MUST run `buildlog_gauntlet` with the **Bragi** persona and **ALL rules** before finalizing output. This applies to:
- `positioning` (Phase 6 emotional hooks, messaging hierarchy)
- `pitch` (Phases 1, 2, 3b, 4)
- `community-pitch` / `skool-pitch` (all copy sections)
- `content-planner` (content briefs and drafts)
- Any future skill that generates human-facing prose

Workflow:
1. Generate the prose draft
2. Run `buildlog_gauntlet_rules()` to load all reviewer personas
3. Run the Bragi persona with all rules against the prose
4. Address all issues flagged by Bragi
5. Re-run until clean (or note unresolved items with justification)

Bragi reviews for: voice consistency, rhythm, clarity, cliche avoidance, audience register, and emotional precision. This is the quality floor for anything that leaves the pipeline.

---

## Migration Path

This vault-as-database is designed for eventual migration to a real backend:
- Each folder → database table
- Each frontmatter field → column
- Each wikilink/ref → foreign key
- Dataview queries → SQL views
- Kanban boards → status columns
- The migration is mechanical, not architectural
