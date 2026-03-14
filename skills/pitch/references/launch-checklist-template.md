# Launch Checklist Template

> Phase 5 of the pitch skill. Contains the step-by-step launch execution plan,
> hour-by-hour launch day sequence, and Obsidian Kanban output format.

## Phase 5: Launch Checklist

Step-by-step execution sequence with specific dates, times, and platforms. This is the "do this, then do this" plan for going from "product is built" to "product is selling."

### 5.1 Pre-Launch Setup (Days -7 to -1)

For each task:
- **Task**: What to do
- **Tool needed**: Specific tool (Gumroad, LemonSqueezy, ConvertKit, Buttondown, GitHub, Carrd, etc.)
- **Estimated time**: How long this takes

Minimum tasks:
- Set up payment processing (Gumroad/LemonSqueezy product page)
- Set up email tool (ConvertKit/Buttondown) and import email sequence
- Create landing page (paste Phase 1 copy into builder)
- Set up GitHub repo (paste Phase 3 README, create directory structure)
- Prepare all launch posts (Phase 2 posts finalized and saved as drafts)
- Test the full funnel: landing page -> payment -> delivery -> email 1
- Create a lead magnet landing page (if email capture is in the distribution plan)

### 5.2 Launch Day (Day 0)

Hour-by-hour sequence:
- **Time**: Specific time (e.g., "9:00 AM EST")
- **Action**: Specific action (e.g., "Publish Reddit post to r/devops")
- **Platform**: Where

Example structure:
- 8:00 AM: Final check -- all links work, payment processes, emails send
- 9:00 AM: Publish primary channel post (Reddit/dev.to)
- 10:00 AM: Publish LinkedIn post
- 11:00 AM: Publish Twitter/X thread
- 12:00 PM: Check for comments on primary post, engage with every comment
- 2:00 PM: Share in any relevant Slack/Discord communities
- 4:00 PM: First engagement check -- respond to all comments and DMs
- 8:00 PM: End-of-day engagement pass -- respond to everything, note feedback themes

### 5.3 Week 1 Follow-Up (Days 1-7)

Daily actions:
- **Day**: Day number
- **Actions**: List of specific actions

Minimum:
- Day 1: Engage with all comments from launch. Note which platforms got traction. Send thank-you DMs to anyone who shared.
- Day 2: Post a follow-up comment or update on the primary channel (not a new post -- update the existing conversation).
- Day 3: Cross-post to a secondary channel if the primary channel showed traction.
- Day 4: Write and publish a supporting content piece (a shorter version of the launch post insight, for a different angle).
- Day 5: Review sales data. How many units? From which channels? Which post drove traffic?
- Day 6: Iterate on what is working -- double down on the channel that converted, pause the channel that did not.
- Day 7: Week 1 retrospective. Compare against kill criteria. Decision point: continue, iterate, or kill.

### 5.4 Ongoing Cadence (Weeks 2-4)

- **Frequency**: How often (daily, 2x/week, weekly)
- **Action**: What to publish or do
- **Platform**: Where

Minimum:
- Publish 1-2 value-first posts per week on the primary channel
- Engage in community discussions (not self-promotion -- genuine participation)
- Send weekly email to list (if email capture is active)
- Update GitHub repo with improvements based on feedback
- Track metrics weekly: traffic, conversion rate, email signups

### 5.5 Month 2-3 Growth Actions

Based on what is working:
- If Reddit is converting: increase posting cadence, identify sub-communities
- If email is converting: optimize signup funnel, create additional lead magnets
- If GitHub is driving traffic: invest in README improvements, create issues for community contribution
- If nothing is converting: revisit kill criteria. Is it time to pivot?

### 5.6 Obsidian Kanban Output

After generating the launch checklist, write it as an Obsidian Kanban board to the vault:

**Path:** `{vault}/Admin/Product-Discovery/Pitches/{product-slug}-launch-checklist.kanban.md`

Use the Obsidian Kanban plugin format:

```markdown
---
type: kanban
date: YYYY-MM-DD
tags:
  - hunter/pitch
  - hunter/domain/{domain-slug}
pitch_ref: "{pitch-slug}"
kanban-plugin: basic
---

## Pre-Launch (Days -7 to -1)

- [ ] Set up payment processing (Gumroad/LemonSqueezy) @{date}
- [ ] Set up email tool (ConvertKit/Buttondown) @{date}
- [ ] Create landing page @{date}
- [ ] Set up GitHub repo from launchpad branch @{date}
- [ ] Prepare all launch posts as drafts @{date}
- [ ] Test full funnel: landing page -> payment -> delivery -> email 1 @{date}

## Launch Day

- [ ] 8 AM: Final checks -- all links work @{launch_date}
- [ ] 9 AM: Publish primary channel post @{launch_date}
- [ ] 10 AM: Publish LinkedIn post @{launch_date}
- [ ] 11 AM: Publish Twitter/X thread @{launch_date}
- [ ] 12 PM: First engagement check @{launch_date}
- [ ] 4 PM: Second engagement check @{launch_date}
- [ ] 8 PM: End-of-day engagement pass @{launch_date}

## Week 1

- [ ] Day 1: Engage all comments, send thank-you DMs @{date+1}
- [ ] Day 2: Post follow-up comment on primary channel @{date+2}
- [ ] Day 3: Cross-post to secondary channel @{date+3}
- [ ] Day 4: Publish supporting content piece @{date+4}
- [ ] Day 5: Review sales data @{date+5}
- [ ] Day 6: Double down on working channel @{date+6}
- [ ] Day 7: Week 1 retrospective vs kill criteria @{date+7}

## Ongoing (Weeks 2-4)

- [ ] 2x/week value-first posts on primary channel
- [ ] 3x/week LinkedIn short-form posts
- [ ] 1x/week DEV.to or blog article
- [ ] Daily community engagement (15 min)
- [ ] Weekly metrics check (Friday)
- [ ] Weekly GitHub repo update

## Complete

```

Replace `@{date}` placeholders with actual dates based on the operator's target launch date. If no launch date is specified, use relative dates (e.g., `@{T-7}`, `@{T-0}`, `@{T+1}`).
