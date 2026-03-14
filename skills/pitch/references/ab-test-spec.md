# A/B Test Spec

> Phase 6 of the pitch skill. Contains the A/B testing framework for solo operators,
> including headline variants, price variants, channel priority, metrics, and decision thresholds.

## Phase 6: A/B Test Spec

Define what to test once distribution is flowing. This is NOT enterprise CRO. This is what a solo operator can actually test with 100-500 visitors.

### 6.1 Headline Variants

Generate 2-3 headline alternatives with rationale:
- **Variant A**: [headline] -- Rationale: [why this might work]
- **Variant B**: [headline] -- Rationale: [why this might work]
- **Variant C**: [headline] -- Rationale: [why this might work]

Each variant should take a different angle: pain-focused, outcome-focused, curiosity-focused, specificity-focused.

### 6.2 Price Point Variants

Generate 2-3 price alternatives:
- **Variant A**: $[price] -- Rationale: [positioning at this price, what it signals]
- **Variant B**: $[price] -- Rationale: [positioning at this price, what it signals]
- **Variant C**: $[price] -- Rationale: [positioning at this price, what it signals]

Cross-reference with offer-scope SPEND data and format ceiling.

### 6.3 Channel Priority Order

Rank channels by expected ROI:
- **Channel 1**: [channel] -- Rationale: [why test first] -- Test budget: [time/money]
- **Channel 2**: [channel] -- Rationale: [why second] -- Test budget: [time/money]
- **Channel 3**: [channel] -- Rationale: [why third] -- Test budget: [time/money]

### 6.4 Metrics to Track

For each metric:
- **Metric**: What to measure
- **Target**: What "good" looks like
- **Measurement method**: Specific tool or method (Gumroad analytics, Google Analytics, UTM parameters, manual tracking)

Minimum metrics:
- Landing page visitors (by source)
- Landing page conversion rate (visitors -> purchase)
- Email signup rate (visitors -> email)
- Launch post engagement (upvotes, comments, shares by platform)
- Revenue (total, by channel)

### 6.5 Decision Thresholds

For each test:
- **Metric**: What you are measuring
- **Threshold**: At what point do you declare a winner
- **Action**: What you do when the threshold is hit

Example: "If Headline B gets 2x the click-through rate of Headline A over 200+ visitors, switch to Headline B permanently."

### A/B Test Rules

- Solo operators cannot run statistically significant A/B tests with 50 visitors. Use sequential testing: try one version for a week, measure, try another, compare. Not perfect, but actionable.
- Test one variable at a time. Do not change the headline AND the price AND the CTA simultaneously.
- Define the decision threshold BEFORE running the test. Otherwise you will rationalize any result.
