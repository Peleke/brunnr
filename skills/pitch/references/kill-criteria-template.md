# Kill Criteria Template

> Phase 7 of the pitch skill. Contains kill criteria refinement framework with
> time-bounded thresholds, qualitative signals, pivot triggers, and Obsidian Task output.

## Phase 7: Kill Criteria Refinement

Inherit kill criteria from offer-scope and SWOT risk registry. Sharpen them with pitch-level specifics -- exact numbers, exact dates, exact actions.

### 7.1 Week 1 Threshold

- **Metric**: What to measure (e.g., units sold, launch post engagement, email signups)
- **Threshold**: Minimum acceptable number (e.g., "5 units sold" or "launch post reaches 50+ upvotes")
- **Action if below threshold**: What to do (iterate on positioning, try a different channel, or kill)

### 7.2 Month 1 Threshold

- **Metric**: Cumulative measure (e.g., total units, total revenue, email list size, repo stars)
- **Threshold**: Minimum acceptable number
- **Action if below threshold**: Specific pivot or kill action

### 7.3 Month 3 Threshold

- **Metric**: Growth trajectory measure (e.g., MRR if community launched, month-over-month growth rate, organic traffic trend)
- **Threshold**: Minimum acceptable trajectory
- **Action if below threshold**: Strategic decision -- pivot product, pivot audience, or full kill

### 7.4 Qualitative Signals

Signals that do not have clean numbers but indicate viability:
- What kind of feedback means "iterate" (e.g., "people engage with the free content but do not convert" = pricing or value perception issue)
- What kind of feedback means "pivot" (e.g., "people love the concept but want it in a different format" = format mismatch)
- What kind of feedback means "kill" (e.g., "zero engagement on free content across all channels" = positioning failure or wrong audience)

### 7.5 Pivot Triggers

Specific conditions that trigger a strategy change vs a full kill:
- **Trigger**: [specific condition]
- **Pivot direction**: [what changes -- audience, format, price, channel, or positioning]
- **Kill condition**: [when a pivot is not enough -- the hypothesis itself is wrong]

### Kill Criteria Rules

- Every threshold must be time-bounded and measurable. Not "get some traction" but "sell 10 units in the first 14 days."
- Kill criteria must be written BEFORE launch and agreed to BEFORE emotional investment builds.
- Distinguish between "iterate" (the mechanism needs tuning), "pivot" (the approach needs changing), and "kill" (the opportunity is not viable).

### 7.6 Obsidian Task Output

After generating kill criteria, write review reminder tasks to the pitch vault document using Obsidian Tasks plugin format. Append these to the pitch markdown under a `## Review Reminders` section:

```markdown
## Review Reminders

> [!warning] These are pre-committed review dates. Check the numbers. Do not rationalize.

- [ ] **Week 1 review**: Check units sold >= {week1_threshold}, launch post engagement, landing page visitors 📅 {launch_date + 7} #hunter/review
- [ ] **Month 1 review**: Check cumulative units >= {month1_threshold}, revenue >= ${month1_revenue}, email list >= {email_threshold}, GitHub stars >= {stars_threshold} 📅 {launch_date + 30} #hunter/review
- [ ] **Month 3 review**: Check growth trajectory (MoM positive?), cumulative units >= {month3_threshold}, community viability 📅 {launch_date + 90} #hunter/review
- [ ] **Time investment audit**: Total hours invested post-build. If > 40 hours and < 10 sales, trigger kill criteria review 📅 {launch_date + 30} #hunter/review
```

Replace all `{placeholder}` values with the actual numbers from Phase 7 thresholds. The `📅` date and `#hunter/review` tag make these queryable by Obsidian Tasks and Dataview.

If the operator has not specified a launch date, use `📅 TBD` and note that dates should be filled in when a launch date is set.
