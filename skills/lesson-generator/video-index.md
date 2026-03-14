# Video Index — Arc 0: Probabilistic Foundations

YouTube video mappings for embedding in Arc 0 notebooks. Referenced by `engagement-patterns.md` and `engagement-pass/SKILL.md`.

**Format**: Each entry has video ID, title, creator, target module/section, and timing rationale.

**Usage**: Use `embed_video()` from `interactive-templates.md` with these IDs.

---

## Module 0.1: Taste Demo — Salience Scoring

| Video ID | Title | Creator | Target Section | Rationale |
|----------|-------|---------|----------------|-----------|
| `zwAD6dRSVyI` | Spearman's Rank Correlation Clearly Explained | StatQuest (Josh Starmer) | After Spearman interlude (cell 34) | Reinforces rank correlation concept right after the reader has computed ρ by hand. Different visual angle from our code-first approach. |
| `1X4WDmbFptI` | Is Most Published Research Wrong? | Veritasium | After "The Turn" (cell 16) | Motivates why measurement matters — the reader just saw their scorer fail, this video deepens the "why" of rigorous evaluation. |

### Notes
- Module 0.1 is light on videos (max 1-2) since it's the taste demo — code is the star
- The Spearman video is the highest-priority embed for this module

---

## Module 0.2: Probability & Counting

| Video ID | Title | Creator | Target Section | Rationale |
|----------|-------|---------|----------------|-----------|
| `HZGCoVF3YvM` | But what is a probability? | 3Blue1Brown | After sample space listing (Part 1) | Geometric/visual intuition for probability spaces — complements our code-first counting approach. |
| `8idr1WZ1A7Q` | The Binomial Distribution | 3Blue1Brown | After binomial PMF implementation | Visual intuition for why the formula works — the reader already built it in code. |

### Notes
- Module 0.2 focuses on counting and basic probability — keep videos focused on these foundations
- Save Bayes theorem video for Module 0.4 where it's the main event

---

## Module 0.3: Distributions & Beta Priors

| Video ID | Title | Creator | Target Section | Rationale |
|----------|-------|---------|----------------|-----------|
| `IYdiKeQ8Ppg` | Binomial Distribution Clearly Explained | StatQuest | After distribution gallery exercise | Clear walkthrough of binomial — reader has built it, now sees it explained differently. |
| `juF3r12nM5A` | Beta Distribution Clearly Explained | StatQuest | After Beta prior elicitation tool | Connects Beta shape to real intuition — why α, β control the shape the way they do. |

### Notes
- This module has the distribution gallery — videos reinforce specific distributions after the reader has plotted them
- McElreath Lecture 1 (Statistical Rethinking) is also relevant here but is long-form — reference in companion text callout, don't embed

---

## Module 0.4: Bayesian Updating

| Video ID | Title | Creator | Target Section | Rationale |
|----------|-------|---------|----------------|-----------|
| `lG4VkPoG3ko` | Bayes theorem, the geometry of changing beliefs | 3Blue1Brown | After first posterior computation | THE Bayes video. Reader has just computed a posterior by hand — this gives the geometric intuition they'll never forget. |
| `R13BD8qKeTg` | Bayes' Theorem — The Simplest Case | StatQuest | Before the interlude on conjugacy | Simpler treatment that bridges the reader's code to the formal theorem. |

### Notes
- The 3B1B Bayes video (`lG4VkPoG3ko`) is the highest-priority embed in the entire arc
- Place it AFTER the reader has done the work — it's a reward, not a prerequisite

---

## Module 0.5: Hypothesis Testing & Fisher Exact

| Video ID | Title | Creator | Target Section | Rationale |
|----------|-------|---------|----------------|-----------|
| `vemZtEM63GY` | p-values, Clearly Explained | StatQuest | After computing first p-value | Reader just got a p-value from their data — now understand what it actually means (and doesn't mean). |
| `0oc49DyA3hU` | Hypothesis Testing and The Null Hypothesis | StatQuest | After null hypothesis introduction | Reinforces the "assume no difference" framework they just used in code. |

### Notes
- p-values are widely misunderstood — the StatQuest video is essential here
- Consider also linking Cassie Kozyrkov's "Statistics for the Terrified" talks in companion text callouts

---

## Module 0.6: Bootstrap CIs & Experimental Design

| Video ID | Title | Creator | Target Section | Rationale |
|----------|-------|---------|----------------|-----------|
| `Xz0x-8-cgaQ` | Bootstrapping Main Ideas | StatQuest | After bootstrap implementation | Reader built bootstrap from scratch — video reinforces the "why it works" intuition. |
| `TqOeMYtOcLw` | Confidence Intervals Clearly Explained | StatQuest | After CI computation | Bridges from "I computed a CI" to "I understand what it means." |

### Notes
- Bootstrap is surprisingly intuitive once you've coded it — the video seals the deal

---

## Module 0.7: Thompson Sampling & Bandits

| Video ID | Title | Creator | Target Section | Rationale |
|----------|-------|---------|----------------|-----------|
| `e3L1PIY0CNA` | Multi-Armed Bandit — Computerphile | Computerphile | After bandit problem introduction | Accessible explainer before diving into the math. |

### Notes
- Module 0.7 is more specialized — fewer mainstream videos available
- The Russo et al. tutorial paper is the primary "video-like" resource (it's very readable)
- Consider embedding bandit playground animations instead of external videos

---

## Module 0.8: Ship statistics.py + trials.py

No video embeds — this is a shipping module. All energy goes into code quality and integration.

---

## Maintenance Guide

### Adding a new video

1. Find the video on YouTube, copy the 11-character ID from the URL (after `v=`)
2. Add an entry to the appropriate module table above
3. Include: target section (be specific — "after cell N" or "after [concept] introduction"), timing rationale
4. Verify the video is still available (YouTube videos get deleted)
5. Test the embed: `from IPython.display import YouTubeVideo; YouTubeVideo("VIDEO_ID")`

### Quality criteria for video selection

- **Trusted creators**: 3Blue1Brown, StatQuest, McElreath, Veritasium, Numberphile, Computerphile, Cassie Kozyrkov
- **Specific over general**: "Spearman Correlation Explained" > "Statistics 101"
- **Short over long**: < 20 minutes preferred. If longer, specify a `start` timestamp
- **Visual over talking-head**: Videos that show diagrams, animations, or worked examples
- **Complements, never replaces**: The video adds a different angle; the notebook's code-first approach is primary

### Video ID verification

Video IDs in this file should be periodically verified. If a video is unavailable:
1. Check if the creator re-uploaded (search their channel)
2. Find an alternative from the same creator or a trusted alternative
3. Update the ID and note the change date
