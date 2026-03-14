# Scoring Rubric

Detailed calibration guide for scoring harvested pain quotes. Every quote gets scored on 4 dimensions. This rubric ensures scores are consistent, justified, and actionable.

---

## Dimension 1: Specificity (Weight: 2x)

**What it measures:** How precisely does the quote identify a pain point? Vague pain is useless for content. Specific pain maps directly to a repo.

| Score | Calibration | Example |
|-------|-------------|---------|
| 1-2 | Completely vague, could apply to anything | "DevOps is hard" |
| 3-4 | Names a general area but nothing specific | "Kubernetes has a steep learning curve" |
| 5-6 | Names a specific tool/concept but not a specific problem | "I'm struggling with Terraform modules" |
| 7-8 | Names a specific problem with a specific tool in a specific context | "I can't figure out how to share Terraform state between my CI pipeline and local development without one overwriting the other" |
| 9-10 | Names exact scenario, exact failure mode, exact gap | "Every GitHub Actions tutorial shows a single-stage pipeline. None of them show how to handle: matrix builds for multiple Python versions, caching dependencies across jobs, deploying to staging first with approval gates, then auto-deploying to production. I need the FULL thing, not another 'hello world' pipeline." |

**Scoring test:** Can you build a specific repo feature directly from this quote? If yes, score 7+. If you'd need to guess what they actually mean, score lower.

---

## Dimension 2: Intensity (Weight: 2x)

**What it measures:** How much does this person actually hurt? Measured by emotional language, effort described, and desperation signals.

| Score | Calibration | Indicators |
|-------|-------------|------------|
| 1-2 | Mild curiosity or passing mention | "I wonder if there's a better way" |
| 3-4 | Noticeable friction, some frustration | "This is kind of annoying" |
| 5-6 | Real frustration, time wasted, seeking help | "I've been stuck on this for hours" |
| 7-8 | Significant suffering, emotional language, considering giving up | "I'm pulling my hair out", "I've wasted the entire weekend", "I'm about to just give up and use ClickOps" |
| 9-10 | Existential frustration, career impact, abandoning the path | "I'm starting to think DevOps isn't for me", "3 months in and I still can't deploy anything to production", "I've spent $2000 on courses and I still feel like I know nothing" |

**Intensity indicators (language patterns):**
- **Low (1-4):** "wondering", "curious", "kind of", "a bit"
- **Medium (5-6):** "frustrated", "stuck", "confused", "hours"
- **High (7-8):** "nightmare", "insane", "pulling my hair out", "losing my mind", "wasted days"
- **Extreme (9-10):** "giving up", "not for me", "career mistake", "wasted months", "thousands of dollars"

**Scoring test:** Would you feel bad for this person if they said this to you in person? If yes, score 6+. If you'd feel the urge to immediately help, score 8+.

---

## Dimension 3: Solvability (Weight: 2x)

**What it measures:** Can we actually demolish this pain point with an instructional repo? This is the most important dimension for content potential.

| Score | Calibration | Example |
|-------|-------------|---------|
| 1-2 | Organizational, cultural, or economic — can't solve with code | "My company won't adopt DevOps", "Nobody's hiring DevOps juniors" |
| 3-4 | Partially solvable but requires experience/mentorship, not just a repo | "I don't know what I don't know about DevOps", "How do I think like an SRE?" |
| 5-6 | Solvable but requires a large, complex repo or course | "I need to learn the entire AWS ecosystem", "How do I architect a microservices platform?" |
| 7-8 | Directly solvable with a focused repo + walkthrough | "I need a working CI/CD pipeline with tests, linting, and deploy", "Show me secrets management that actually works" |
| 9-10 | Perfectly solvable — the repo IS the answer | "I just need a production-ready Dockerfile for a Python app with multi-stage builds", "Give me a GitHub Actions workflow for a monorepo with path-based triggers" |

**Solvability test:** Can you write the repo's README title right now? If yes, score 8+. If you'd need to scope a whole curriculum, score 5 or below.

### Solvability Killers (auto-cap at 3)

These patterns cap solvability regardless of other factors:
- "My team/company won't..." (organizational)
- "The job market..." (economic)
- "Imposter syndrome" (psychological, not educational)
- "I don't have time to..." (scheduling, not content)
- "The technology keeps changing" (existential, not actionable)

### Solvability Boosters (add +1-2)

These patterns boost solvability:
- Person names a specific template/config they wish existed (+2)
- Person describes exactly what the solution would look like (+2)
- Person has tried multiple resources and lists what's missing (+1)
- Person says "I would pay for..." (+1)

---

## Dimension 4: Engagement (Weight: 1x)

**What it measures:** Social proof that this pain is shared, not just one person's problem.

| Score | Calibration | Metrics |
|-------|-------------|---------|
| 1-2 | No engagement, buried comment | 0-5 upvotes, 0 replies |
| 3-4 | Some engagement, a few agree | 5-20 upvotes, 1-3 replies |
| 5-6 | Moderate engagement, clear agreement | 20-75 upvotes, 5-10 replies, some "same here" |
| 7-8 | High engagement, many people share the pain | 75-200 upvotes, 10-25 replies, multiple "same here" |
| 9-10 | Viral-level engagement, massive validation | 200+ upvotes, 25+ replies, cross-posted, "this is the post I've been looking for" |

### Platform-Specific Engagement Calibration

Engagement metrics mean different things on different platforms:

| Platform | Low (1-3) | Medium (4-6) | High (7-8) | Extreme (9-10) |
|----------|-----------|--------------|------------|-----------------|
| Reddit (comment) | 0-10 upvotes | 10-50 upvotes | 50-200 upvotes | 200+ upvotes |
| Reddit (post) | 0-20 upvotes | 20-100 upvotes | 100-500 upvotes | 500+ upvotes |
| HN | 0-5 points | 5-30 points | 30-100 points | 100+ points |
| Stack Overflow | 0-5K views | 5-20K views | 20-100K views | 100K+ views |
| Twitter/X | 0-20 likes | 20-100 likes | 100-500 likes | 500+ likes |
| Dev.to | 0-10 reactions | 10-50 reactions | 50-200 reactions | 200+ reactions |

**Engagement edge cases:**
- A quote in a niche subreddit (r/terraform, 50K members) with 30 upvotes may be more significant than one in r/programming (6M members) with 100 upvotes. Adjust for community size.
- Recent quotes with moderate engagement may still be growing. Note if the quote is < 48 hours old.

---

## Overall Score Calculation

```
overall = (specificity * 2 + intensity * 2 + solvability * 2 + engagement * 1) / 7
```

### Score Interpretation

| Overall Score | Meaning | Action |
|---------------|---------|--------|
| 1-3 | Low potential | Skip — not worth a "From the Wild" post |
| 4-5 | Moderate potential | Archive — might be useful combined with other quotes |
| 6-7 | Good potential | Generate content brief — this is a solid "From the Wild" candidate |
| 8-9 | Excellent potential | Priority content brief — build the repo ASAP |
| 10 | Unicorn | Drop everything — this is the perfect "From the Wild" post |

### Score Justification Format

Every score MUST include a one-sentence justification:

```
Quote: "I've been through 5 Terraform courses and not a single one shows how to
manage state in a team environment. They all use local state. WHO USES LOCAL STATE
IN PRODUCTION?" — u/tf_frustrated, r/devops, 312 upvotes

Scoring:
  specificity: 9 — "Pinpoints exact gap: team state management. Names what's wrong
    with existing courses (all use local state). Crystal clear what a solution looks like."
  intensity: 8 — "ALL CAPS frustration, '5 courses' = significant time/money invested,
    rhetorical question dripping with exasperation."
  solvability: 9 — "A repo showing Terraform with remote state (S3 + DynamoDB), state
    locking, workspaces, and team workflow would directly answer this."
  engagement: 9 — "312 upvotes on r/devops = massive validated pain."
  overall: 8.7
```
