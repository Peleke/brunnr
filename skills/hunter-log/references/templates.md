# Hunter Log -- Document Templates

Rendering templates for each document type produced by the hunter pipeline. Each template shows the complete markdown structure including frontmatter and body.

Use these templates when rendering PipelineEnvelope output to Obsidian-compatible markdown.

---

## Signal Scan Template

```markdown
---
type: signal-scan
domain: "{output.domain}"
date: {YYYY-MM-DD from timestamp}
session: "{envelope.session_id}"
operator_edge: "{output.operator_edge}"
top_opportunity: "{output.opportunities[0].name}"
top_score: {output.opportunities[0].overall_score}
opportunity_count: {output.opportunities.length}
status: complete
tags:
  - hunter/scan
  - hunter/domain/{domain-slug}
---

# Signal Scan: {output.domain}

**Date**: {date}
**Operator Edge**: {output.operator_edge}
**Session**: {envelope.session_id}

## Executive Summary

{output.meta_signal.summary}

## Signal Highlights

{For each of top 3-5 signals across all types:}
- **{signal.type}**: {signal.description} -- *{signal.evidence}* (Source: {signal.source})

## Opportunity Ranking

| Rank | Opportunity | Score | Pain | Spend | Edge | Speed | Gap | Audience |
|------|------------|-------|------|-------|------|-------|-----|----------|
{For each opportunity, sorted by overall_score desc:}
| {rank} | {name} | {overall_score}/10 | {pain_intensity} | {spend_evidence} | {edge_match} | {time_to_ship} | {competition_gap} | {audience_fit} |

## Top Opportunities

{For each opportunity scoring 6+:}

### {rank}. {opportunity.name} (Score: {overall_score}/10)

**Thesis**: {opportunity.thesis}

**Key signals**:
{For each signal linked to this opportunity:}
- {signal.type}: {signal.description} -- *{signal.evidence}*

**Ship candidates**:

| Product | Format | Price | Ship Time | Distribution |
|---------|--------|-------|-----------|-------------|
{For each ship_candidate:}
| {name} | {format} | {price_point} | {ship_time} | {distribution} |

## Recommended First Ship

**Product**: {output.recommended_first_ship.name}
**From opportunity**: {output.recommended_first_ship.opportunity}
**Rationale**: {output.recommended_first_ship.rationale}

## Signal Inventory

| Type | Count | Notes |
|------|-------|-------|
{For each of 7 signal types:}
| {type} | {count} | {gap_note if count < 3} |

## Based On

> [!info] Upstream Artifacts
{For each input_ref:}
> - [[{input_ref}]]

{If no input_refs:}
> First artifact in pipeline -- no upstream dependencies.
```

---

## Decision Template

```markdown
---
type: decision
date: {YYYY-MM-DD from timestamp}
session: "{envelope.session_id}"
domain: "{output.domain}"
chosen_opportunity: "{output.chosen_opportunity}"
alternatives_considered:
{For each alternative:}
  - "{alternative.name}"
confidence: {output.confidence}
revisit_by: {output.revisit_by}
status: active
signal_scan: "{input_refs[0]}"
tags:
  - hunter/decision
  - hunter/domain/{domain-slug}
---

# Decision: {output.chosen_opportunity}

**Date**: {date}
**Domain**: {output.domain}
**Confidence**: {output.confidence}
**Session**: {envelope.session_id}

## Decision

{output.rationale}

## Chosen Opportunity

**{output.chosen_opportunity}**

- **Score**: {output.chosen_score}/10
- **Key strength**: {output.chosen_key_strength}
- **Primary risk**: {output.chosen_primary_risk}

## Alternatives Considered

| Opportunity | Score | Why Not |
|------------|-------|---------|
{For each alternative:}
| {name} | {score}/10 | {rejection_reason} |

## Next Steps

{For each next_step:}
- [ ] {step.description} -- by {step.deadline}

## Revisit Criteria

> [!warning] Revisit by {output.revisit_by}
> {output.revisit_criteria}

## Based On

> [!info] Upstream Artifacts
{For each input_ref:}
> - [[Signal Scans/{input_ref}]]
```

---

## Persona Template

```markdown
---
type: persona
date: {YYYY-MM-DD from timestamp}
session: "{envelope.session_id}"
domain: "{output.domain}"
opportunity: "{output.opportunity}"
persona_name: "{output.persona_name}"
experience_range: "{output.experience_range}"
pain_intensity: {output.pain_intensity}
willingness_to_pay: {output.willingness_to_pay}
decision_ref: "{input_refs decision ref}"
status: complete
tags:
  - hunter/persona
  - hunter/domain/{domain-slug}
  - hunter/opportunity/{opportunity-slug}
---

# Persona: {output.persona_name}

**Date**: {date}
**Domain**: {output.domain}
**Opportunity**: {output.opportunity}
**Session**: {envelope.session_id}

## Overview

{output.persona_summary}

## Demographics

| Attribute | Value |
|-----------|-------|
| Experience range | {output.experience_range} |
| Role / title | {output.role} |
| Industry | {output.industry} |
| Company size | {output.company_size} |
| Location | {output.location} |

## Pain Points

{For each pain_point:}

### {pain_point.name}

- **Intensity**: {pain_point.intensity}/10
- **Frequency**: {pain_point.frequency}
- **Current workaround**: {pain_point.current_workaround}
- **Evidence**: *{pain_point.evidence}*

## Goals and Motivations

{For each goal:}
- **{goal.name}**: {goal.description}

## Willingness to Pay

**Level**: {output.willingness_to_pay}

{output.wtp_evidence}

| What They Buy | Price Range | Format | Where |
|--------------|-------------|--------|-------|
{For each existing_purchase:}
| {name} | {price} | {format} | {channel} |

## Objections and Barriers

{For each objection:}
- **{objection.name}**: {objection.description}
  - *Counter*: {objection.counter}

## Channels

Where this persona hangs out and discovers products:

{For each channel:}
- **{channel.name}**: {channel.description} (reach: {channel.reach})

## Based On

> [!info] Upstream Artifacts
{For each input_ref:}
> - [[Decisions/{input_ref}]]
```

---

## Offer Template

```markdown
---
type: offer-spec
date: {YYYY-MM-DD from timestamp}
session: "{envelope.session_id}"
domain: "{output.domain}"
opportunity: "{output.opportunity}"
product_name: "{output.product_name}"
format: "{output.format}"
price_point: "{output.price_point}"
ship_time: "{output.ship_time}"
persona_ref: "{input_refs persona ref}"
decision_ref: "{input_refs decision ref}"
status: spec
tags:
  - hunter/offer
  - hunter/domain/{domain-slug}
  - hunter/format/{format-slug}
  - hunter/price/{price-range-slug}
---

# Offer: {output.product_name}

**Date**: {date}
**Domain**: {output.domain}
**Format**: {output.format}
**Price**: {output.price_point}
**Ship Time**: {output.ship_time}
**Session**: {envelope.session_id}

## Product Spec

{output.product_description}

## Value Proposition

> [!tip] One-Liner
> {output.one_liner}

{output.value_proposition}

## Target Persona

**[[Personas/{persona_ref}]]**

- Pain addressed: {output.pain_addressed}
- Pain intensity: {output.pain_intensity}/10
- WTP match: {output.wtp_match}

## Scope

### Included

{For each included_item:}
- {item}

### Excluded (v1)

{For each excluded_item:}
- {item}

## Pricing Rationale

{output.pricing_rationale}

| Comparable | Price | Notes |
|-----------|-------|-------|
{For each comparable:}
| {name} | {price} | {notes} |

## Distribution Plan

| Channel | Strategy | Expected Reach |
|---------|----------|---------------|
{For each distribution_channel:}
| {name} | {strategy} | {reach} |

## Launch Checklist

{For each launch_step:}
- [ ] {step.description} -- {step.effort}

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
{For each risk:}
| {name} | {likelihood} | {impact} | {mitigation} |

## Based On

> [!info] Upstream Artifacts
{For each input_ref:}
> - [[{resolve_subdir(input_ref)}/{input_ref}]]
```

---

## Session Log Template

```markdown
---
type: session
date: {YYYY-MM-DD from session_id}
session_id: "{envelope.session_id}"
domain: "{output.domain or extracted from artifacts}"
pipeline_steps_completed:
  - {current_skill}
steps_remaining:
{For each remaining skill not yet completed:}
  - {skill_name}
artifacts:
  - "[[{subdir}/{filename}]]"
status: in-progress
tags:
  - hunter/session
---

# Session: {envelope.session_id}

**Date**: {date}
**Domain**: {domain}
**Status**: in-progress

## Pipeline Progress

| Step | Status | Artifact |
|------|--------|----------|
| signal-scan | {done or pending} | {wikilink or --} |
| decision-log | {done or pending} | {wikilink or --} |
| persona-extract | {done or pending} | {wikilink or --} |
| offer-scope | {done or pending} | {wikilink or --} |

## Activity Log

- {timestamp}: Created session -- saved {skill} output -> [[{subdir}/{filename}]]
```

---

## Kanban Board Template

This is the initial structure for `Pipeline.kanban.md`. Only create this file if it does not already exist.

```markdown
---
kanban-plugin: basic
---

## Signal Scanned

## Decision Made

## Persona Researched

## Offer Scoped

## Building

## Shipped

## Killed
```

### Kanban Card Format

When adding or moving cards:

```markdown
- [ ] **{Domain}** #hunter/domain/{domain-slug}
  Score: {top_score}/10 | Top: {top_opportunity}
  [[{subdir}/{filename}]]
```

---

## Plan.md Template

This is the initial structure for `Plan.md`. Only create this file if it does not already exist.

````markdown
---
type: plan
date: {YYYY-MM-DD}
tags:
  - hunter/plan
---

# Product Discovery Pipeline

Master index for hunter pipeline artifacts. Uses Dataview queries to stay up to date automatically.

## Active Decisions

```dataview
TABLE domain, chosen_opportunity, confidence, revisit_by
FROM "Product Discovery/Decisions"
WHERE status = "active"
SORT date DESC
```

## Pipeline Status

```dataview
TABLE domain, pipeline_steps_completed, status
FROM "Product Discovery/Sessions"
WHERE status = "in-progress"
SORT date DESC
```

## All Offers

```dataview
TABLE product_name, format, price_point, ship_time, status
FROM "Product Discovery/Offers"
SORT date DESC
```

## Recent Scans

```dataview
TABLE domain, top_opportunity, top_score, opportunity_count
FROM "Product Discovery/Signal Scans"
SORT date DESC
LIMIT 10
```

## All Personas

```dataview
TABLE persona_name, domain, opportunity, pain_intensity, willingness_to_pay
FROM "Product Discovery/Personas"
SORT date DESC
```
````

---

## Append Template

When appending to an existing file (collision detected), use this format:

```markdown

---

## Update: {ISO timestamp}

**Session**: {envelope.session_id}
**Reason**: Updated with new {skill} data

{Rendered body content for the new data, same structure as the original body sections}
```

Update the frontmatter `status` field if the new data changes it (e.g., `partial` to `complete`).
