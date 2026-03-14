# Clustering Guide

Reference for quote-to-persona Phase 2 (Clustering). Use this to analyze behavioral dimensions and map fields across the pipeline.

---

## Behavioral Dimensions

Cluster on these four dimensions. Pain categories (tutorial-gap, debugging-hell, etc.) describe WHAT hurts. These dimensions describe WHO is hurting.

### 1. Journey Stage

Where is this person in their learning/career arc?

| Stage | Signals in Quote | Example Phrases |
|-------|-----------------|-----------------|
| **Pre-entry** | Hasn't started yet, researching | "thinking about", "should I", "is it worth" |
| **Early learner** | Just started courses/tutorials | "just started", "beginner", "first project" |
| **Tutorial loop** | Years of consuming, not building | "been doing this for X years", "another course", "tutorial hell" |
| **Practitioner** | Doing the work daily, hitting walls | "in production", "at my job", "every day I" |
| **Experienced** | 5+ years, seeing the industry from above | "I've been doing this for", "I interviewed", "back in my day" |
| **Burned out** | Past caring, considering exit | "I want out", "don't care anymore", "not sustainable" |

### 2. Frustration Type

HOW do they express their pain? The voice matters as much as the content.

| Type | Signals | What It Tells You |
|------|---------|-------------------|
| **Desperate plea** | "Please help", "I need", ALL CAPS demands | High urgency, ready to act. Most likely to convert. |
| **Bitter humor** | Sarcasm, memes, dark jokes | Universal pain, good for content. Pain is real but coping mechanism is active. |
| **Resigned acceptance** | "That's just how it is", "you get used to it" | Deep pain, low urgency. Needs push factor to convert. |
| **Angry critique** | Calling out industry, blaming tools/people | Pain channeled outward. May not see themselves as the buyer. |
| **Constructive analysis** | Diagnosing the problem, suggesting solutions | Often the hiring manager perspective. Good for social proof, not the primary buyer. |

### 3. Attempted Solutions

What have they already tried? This reveals what they'll compare your product to.

| Solution | What It Means |
|----------|--------------|
| **Udemy/YouTube/MOOCs** | Price-anchored low ($10-30). Expects structured content. |
| **Certifications** | Willing to invest ($200-400). Credential-motivated. |
| **Homelabs/side projects** | Self-directed. Will value a structured project path. |
| **Job-hopping** | Career-motivated. Looking for portfolio/skill differentiation. |
| **Nothing (apathy)** | Hardest to convert. Needs strong push factor. |
| **Books/docs** | Self-learner. Prefers written/reference format. |
| **Bootcamps** | Willing to invest big ($5K-15K). Expects transformation. |

### 4. Career Context

What's their professional situation? Determines WTP and urgency.

| Context | WTP Signal | Urgency Signal |
|---------|-----------|----------------|
| **Student/job seeker** | Low personal ($0-50/mo), but desperate | HIGH — career at stake |
| **Junior employed** | Moderate ($20-100/mo) | MEDIUM — wants to level up |
| **Mid-level transitioning** | Moderate-high ($50-200) | HIGH — identity shift happening |
| **Senior/lead frustrated** | High ($100-500) | LOW — venting, not buying for themselves |
| **Solo practitioner** | Moderate ($30-100/mo) | HIGH — no team to learn from |
| **Hiring manager** | Not the buyer, but the recommender | MEDIUM — will share resources with team |

---

## Example Archetype Patterns

These are examples from previous DevOps scans. Do NOT hardcode them — let the data create its own clusters.

| Archetype | Journey Stage | Frustration Type | Attempted Solutions | Career Context |
|-----------|--------------|-----------------|-------------------|---------------|
| The Eternal Student | Tutorial loop | Desperate plea | Udemy, YouTube, books, courses | Job seeker or junior |
| The Pipeline Arsonist | Practitioner | Bitter humor / angry critique | Trial and error, Stack Overflow | Mid-level employed |
| The Fundamentals Ghost | Experienced (observer) / Practitioner (subject) | Constructive analysis / Angry critique | AWS console clicking, copy-paste configs | Hiring manager observing juniors/mids |
| The Invisible Operator | Burned out | Resigned acceptance | Carrying the org, no learning time | Mid-to-senior solo practitioner |

---

## Field Mapping: wild-scan → quote-to-persona → offer-scope

| wild-scan field | quote-to-persona usage | offer-scope field |
|----------------|----------------------|-------------------|
| `quote` | → `pain_stories[].pain` + `pain_stories[].evidence` | `persona.pain_stories[].pain` + `.evidence` |
| `author` | → attribution in evidence string | (embedded in evidence) |
| `platform` + `community` | → `channels[].platform` | `persona.channels[].platform` |
| `url` | → evidence attribution, evidence_map reference | (embedded in evidence) |
| `engagement.value` | → evidence attribution, WTP signal | (embedded in evidence) |
| `engagement.replies` | → same_here signal, cluster weight | (not directly mapped) |
| `engagement.same_here_count` | → cluster validation, pain universality | (not directly mapped) |
| `context` | → `pain_stories[].situation` | `persona.pain_stories[].situation` |
| `pain_category` | → clustering input (secondary to behavioral dims) | (not directly mapped) |
| `scores.specificity` | → pain_story richness indicator | (not directly mapped) |
| `scores.intensity` | → `pain_stories[].emotional_state` | `persona.pain_stories[].emotional_state` |
| `scores.solvability` | → decision_triggers, offer mapping | (informs offer-scope Phase 1) |
| `scores.engagement` | → cluster anchoring, WTP signal | (informs offer-scope Phase 7) |
| `overall_score` | → cluster anchor weighting | (not directly mapped) |

---

## Cluster Quality Criteria

### Good Cluster

- 3+ quotes that share at least 2 behavioral dimensions
- Archetype name that a stranger could understand without reading the quotes
- Clear distinction from every other cluster
- At least 1 high-scoring quote (overall_score >= 7) as the anchor
- The quotes SOUND like they could be from the same type of person

### Bad Cluster

- Fewer than 3 quotes (merge it)
- Named after the pain_category instead of the behavior ("The Tutorial-Gap People" = bad)
- Overlaps significantly with another cluster on 3+ dimensions (merge them)
- Contains only low-scoring quotes (overall_score < 6) — may be noise, not a real archetype
- Quotes sound like they come from very different types of people forced together

### When to Merge

Merge two clusters if:
- Same journey stage AND same career context
- One cluster has fewer than 3 quotes and the nearest cluster shares 2+ dimensions
- You can't articulate the behavioral difference in one sentence

### When to Split

Split a cluster if:
- It contains 8+ quotes with clearly different frustration types
- The "archetype name" requires an "or" to describe it ("The Student or the Practitioner" = split)
- Pain stories within the cluster describe fundamentally different scenarios
