# Output Template

> Full markdown output template for the pitch skill. Defines the complete structure
> of the pitch vault document including all sections and deployment outputs.

## Pitch Markdown Output Structure

```markdown
---
type: pitch
date: YYYY-MM-DD
status: draft
tags:
  - hunter/pitch
  - hunter/domain/{domain-slug}
  - hunter/opportunity/{opportunity-slug}
offer_ref: "{offer-slug}"
persona_ref: "{persona-slug}"
swot_ref: "{swot-slug}"
decision_ref: "{decision-slug}"
signal_scan_ref: "{signal-scan-slug}"
---

# Pitch: [Product Name]

**Date**: [date]
**Domain**: [domain]
**Opportunity**: [opportunity]
**Product**: [product name]
**Format**: [format]
**Price**: [price]

---

## Landing Page Copy

### Headline
[headline]

### Subheadline
[subheadline]

### Above the Fold
[hook copy]

### The Problem
[full problem section copy]

### The Solution
[full solution section copy]

### What's Inside
[section-by-section breakdown]

### Social Proof
[social proof strategy copy]

### Pricing
[full pricing section copy]

### FAQ
[all FAQs]

### Call to Action
**Primary**: [CTA copy]
**Secondary**: [CTA copy]

---

## Launch Posts

### [Platform 1]: [Title]
[full post]

### [Platform 2]: [Title]
[full post]

### Twitter/X Thread
[full thread]

---

## GitHub README

### Product Structure (if technical domain)
[directory layout, file manifest, learning path, prerequisites]

### README.md Content
[full README content]

---

## Landing Page HTML

**File**: `index.html` (on `{product-slug}` branch)
**Preview URL**: [{vercel-preview-url}]({vercel-preview-url})
**Sections rendered**: [list of sections from Phase 1 that were converted to HTML]
**Hero image in OG tags**: Yes/No
**File size**: {N} bytes

---

## Email Sequence

### Email 1: [Subject Line] (Day 0)
[full email]

### Email 2: [Subject Line] (Day 2)
[full email]

### Email 3: [Subject Line] (Day 4)
[full email]

### Email 4: [Subject Line] (Day 6)
[full email]

### Email 5: [Subject Line] (Day 7)
[full email]

---

## Launch Checklist

### Pre-Launch (Days -7 to -1)
[task list with tools and times]

### Launch Day
[hour-by-hour plan]

### Week 1
[daily action plan]

### Ongoing Cadence
[weekly/monthly plan]

### Month 2-3 Growth
[growth actions]

---

## A/B Test Spec

### Headline Variants
[variants with rationale]

### Price Variants
[variants with rationale]

### Channel Priority
[ranked channels]

### Metrics
[metrics with targets]

### Decision Thresholds
[thresholds with actions]

---

## Kill Criteria

### Week 1
[threshold + action]

### Month 1
[threshold + action]

### Month 3
[threshold + action]

### Qualitative Signals
[signal interpretations]

### Pivot Triggers
[triggers + directions]

---

## References

- **Offer Spec**: [[Admin/Product-Discovery/Offers/{offer-slug}]]
- **Persona**: [[Admin/Product-Discovery/Personas/{persona-slug}]]
- **SWOT Analysis**: [[Admin/Product-Discovery/SWOT/{swot-slug}]]
- **Decision Log**: [[Admin/Product-Discovery/Decisions/{decision-slug}]]
- **Signal Scan**: [[Admin/Product-Discovery/Signal-Scans/{signal-scan-slug}]]
```

## Deployment Outputs

### Launchpad Product Branch: `github.com/Peleke/launchpad` branch `{product-slug}`
- Full product directory structure from Phase 3a
- Product README from Phase 3b
- Hero image from Phase 3c (or HTML comment with image intent)
- `emails/` directory with individual email files from Phase 4.6
- PR opened against `main` for operator review (Phase 3d)

### Landing Page HTML: `index.html` on launchpad branch root
- Single-file HTML landing page generated from Phase 1 copy (Phase 3e)
- Dark theme, mobile responsive, zero dependencies
- Open Graph meta tags for social sharing
- Immediately deployable via Vercel branch preview
- Preview URL: `https://launchpad-git-{product-slug}-kwayet-fs-projects.vercel.app`

### Content Seeds: `{vault}/Writing/Content-Briefs/{product-slug}-{platform}-seed-{YYYY-MM-DD}.md`
- One file per launch post (Phase 2.4)
- Frontmatter: `type: content-brief`, `status: backlog`, platform tag
- Picked up by content-planner for full brief generation after operator review

### Launch Checklist Kanban: `{vault}/Admin/Product-Discovery/Pitches/{product-slug}-launch-checklist.kanban.md`
- Obsidian Kanban board with Pre-Launch, Launch Day, Week 1, Ongoing columns (Phase 5.6)
- Tasks have dates, checkable on mobile via iCloud sync

### Review Reminders: Appended to pitch markdown in vault
- Obsidian Tasks format with dates and `#hunter/review` tags (Phase 7.6)
- Week 1, Month 1, Month 3 review dates
- Queryable by Obsidian Tasks and Dataview plugins

### Pipeline Tracker: `{vault}/Admin/Product-Discovery/Pipeline.md`
- Table of all products with branch links, preview URLs, status
- Updated by pitch skill when creating a new product
- Format:

```markdown
| Product | Branch | Preview URL | Price | Status | Pitch Date |
|---------|--------|-------------|-------|--------|------------|
| {name} | [{slug}](https://github.com/Peleke/launchpad/tree/{slug}) | [Preview]({vercel-url}) | ${price} | spec | {date} |
```
