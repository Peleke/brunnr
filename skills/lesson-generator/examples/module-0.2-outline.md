# Module 0.2: Probability & Counting — Narrative Outline

> **Status**: Exemplar outline demonstrating the level of detail needed before notebook generation.
>
> **What makes this ready**: War stories linked, jargon-earning order established, section-by-section thought process documented, continuity threads explicit.

---

## Module Metadata

**Arc**: 0 — Probabilistic Foundations
**Position**: Module 2 of 8
**Prerequisites**: Module 0.1 (SalienceScorer)
**Estimated time**: ~90-120 minutes

**Falsifiable claim**: "I can compute P(hypothesis | data) from first principles and explain why 3/5 vs 2/5 isn't enough evidence to ship."

**Implementation target**: `probability.py` module with `n_choose_k`, `binomial_pmf`, `bayes_update`

---

## War Story Integration

**Origin story** (before Story A): Introduce buildlog — why it exists (the `/workspace` vs `/runpod-volume` problem from 0.1), what it does (tracks rules, learns which help), and the loop (task → rules → agent → outcome → update).

**Story A**: SalienceScorer in production. The loop is working. Rules that help get selected more. Celebration.

**Story B**: The A/B test disaster. Treatment (scorer-picked rules) vs Control (random). 5 trials each. 3/5 vs 2/5. "Treatment wins!" Ship it. One month later: metrics tanked. The 3/5 was noise.

**The Turn**: "How surprised should I be by 3/5 vs 2/5?" — this is the question that would have saved us.

**Threading**: Story A uses the SalienceScorer from 0.1. Story B exposes that we don't know how to evaluate evidence. The bridge is "we need probability foundations."

---

## Conceptual Scope

| Concept | Why We Need It | Narrative Hook |
|---------|----------------|----------------|
| Sample spaces | Know what could happen | "Before asking 'how likely', list all possibilities" |
| Combinatorics (n choose k) | Count without listing | "2^100 outcomes? We need a shortcut" |
| Probability as ratio | Turn counts into likelihood | "10 ways out of 32 = 31.25%" |
| Binomial distribution | Generalize to any p | "What if success rate isn't 50%?" |
| Conditional probability | Reason given evidence | "P(A given B) — the denominator changes" |
| Bayes' theorem | Flip the conditional | "We want P(hypothesis | data), not P(data | hypothesis)" |
| Prior → Posterior | The update loop | "Today's posterior is tomorrow's prior" |

**What we DON'T cover** (deferred):
- Beta distributions (teased → Module 0.3)
- Thompson Sampling (teased → Module 0.7)
- Confidence intervals (Module 0.6)
- Hypothesis testing formalism (Module 0.5)

---

## Part-by-Part Narrative Sketch

### PART 0: The Origin Story

**Scene**: You're building AI agents. They keep making stupid mistakes. You realize: agents need rules, and you need to learn which rules help.

**The problem**: 50 rules, can't use all at once. Need to pick.

**The naive approach**: Pick randomly. Sometimes lucky.

**The insight**: Learn which rules help. Track successes. This is like gambling on slot machines — the formal name is "multi-armed bandit" (teased, not explained).

**What you build**: buildlog — stores rules, records outcomes, picks promising rules.

**The loop**:
```
Task → buildlog picks rules → Agent runs → Outcome → Update beliefs → Repeat
```

**The missing piece**: Task succeeded, but did the agent follow the rules? Need to measure compliance.

**→ That's Module 0.1**: SalienceScorer. Three signals, weighted combination, validated at ρ > 0.8.

---

### PART 1: Story A — The Scorer in the Loop

**The updated loop**: Now includes SalienceScorer evaluating compliance before updating beliefs.

**Illustration table**: Show how different compliance scores change what buildlog learns.

**The celebration**: It's working! Agent improving. Rules that help get selected.

**Then**: You get ambitious. Want to prove it works.

---

### PART 2: Story B — The Experiment That Went Wrong

**The question**: How do we KNOW the scorer helps? Need a comparison.

**The experiment**:
- Group A (treatment): Rules picked by buildlog
- Group B (control): Rules picked randomly

> *Earn the jargon*: Explain "treatment" and "control" before using them.

**Results after 5 trials each**:
- Treatment: 3/5 (60%)
- Control: 2/5 (40%)

"Treatment wins!" Ship it.

**One month later**: Treatment at 44%, Control at 46%. Treatment is WORSE.

**What happened**: 3/5 vs 2/5 was noise.

---

### PART 3: The Turn — What Does "Surprising" Mean?

**The realization**: Should have asked "how surprised should I be?"

**The thought process** (slow, step by step):
1. What if there's no real difference? (null hypothesis — don't name it yet)
2. If both are 50%, what would we expect?
3. How often would 3/5 happen by chance?

**The skill we're building**: Turn "how surprised?" into a number.

**The promise**: By end of module, you can say "P(3/5 by chance) = X" and make decisions.

---

### SECTION A: What Could Happen? (Sample Spaces)

**Thought process**: Before "how likely is 3/5?", need to know what else could happen.

**Scenario**: 5 trials, each S or F. List all outcomes.

**Concept**: Sample space = set of all possible outcomes. 2^5 = 32.

**Interactive cell**: Generate and display all 32, grouped by number of successes.

**Insight**: 1 way to get 5/5, 5 ways to get 4/5, 10 ways to get 3/5. The counts matter!

---

### SECTION B: Counting Smarter (Combinatorics)

**Thought process**: 32 is fine. 2^100 is impossible. Need a shortcut.

**Scenario**: How many ways to get exactly 3 successes in 5 trials?

**Insight**: Choosing which 3 positions are successes. Order doesn't matter.

**Concept**: "n choose k" = C(n,k) = n! / (k! × (n-k)!)

**Implementation**: Build `n_choose_k(n, k)`.

**Interactive cell**: Pascal's triangle visualization.

**Interlude**: "Why does the formula work?" — walk through the logic of dividing out redundancies.

---

### SECTION C: Probability as Counting (The Ratio)

**Thought process**: 32 outcomes, 10 have 3 successes. If equally likely, P(3) = 10/32.

**Concept**: P(event) = favorable / total

**Assumption**: Each outcome equally likely (true if p = 0.5 — the "no difference" assumption).

**Build the full table**: P(k) for k = 0 to 5.

**Interactive cell**: Bar chart. Name it: "binomial distribution."

**The answer**: P(≥3) = 50%. Getting 3/5 by chance happens HALF the time.

**Punchline**: You shipped on an outcome that happens by chance 50% of the time.

---

### SECTION D: But What If It's Not 50/50?

**Thought process**: We assumed 50%. What if treatment is actually 60%?

**Scenario**: Generalize to any success rate p.

**Concept**: P(k successes) = C(n,k) × p^k × (1-p)^(n-k)

**Implementation**: Build `binomial_pmf(k, n, p)`.

**Interactive cell**: Plot binomial for p = 0.5, 0.6, 0.7. Watch peak shift.

**Insight**: Even at p = 0.6, P(3/5) = 34.6%. Still common!

---

### SECTION E: Flipping the Question (Conditional Probability)

**Thought process**: We computed P(data | hypothesis). But we want P(hypothesis | data).

**Concept**: Conditional probability P(A|B) = P(A and B) / P(B)

**Intuition**: Of all worlds where B is true, what fraction have A?

**Example**: P(heart | red) = 13/26 = 0.5 (not 13/52)

**Interactive cell**: Conditional probability calculator with Venn diagram.

**Key insight**: We need to flip the conditional.

---

### SECTION F: Bayes' Theorem (The Flip)

**Thought process**: We can compute P(3/5 | 60%). We want P(60% | 3/5).

**Concept**: Bayes' theorem:
```
P(hypothesis | data) = P(data | hypothesis) × P(hypothesis) / P(data)
```

**Name the pieces**: Likelihood, Prior, Evidence, Posterior.

**Worked example**: H1 (60%) vs H2 (50%), prior 50/50, see 3/5.
- Posteriors: 52.6% vs 47.4%
- Barely moved!

**Implementation**: Build `bayes_update(prior, likelihood, evidence)`.

**Interactive cell**: Try different priors. See how posterior changes.

**Punchline**: 5 trials isn't enough to move beliefs much.

---

### SECTION G: The Update Loop

**Thought process**: One update barely moved us. What about more data?

**Concept**: Bayesian updating is iterative. Posterior becomes new prior.

**Interactive cell**: Simulate 5, 10, 20, 50, 100 trials. Watch convergence.

**Insight**: With enough data, truth wins. But "enough" > 5.

**Teaser for 0.3**: Discrete hypotheses (50% vs 60%) are limiting. Want continuous. That's distributions. Beta distribution. Module 0.3.

---

### PART 5: Back to the A/B Test

**Full circle**: Redo the analysis properly.

**Exercise**: Compute P(treatment better | 3/5 vs 2/5). Set threshold. How many trials needed?

**Answer**: Posterior barely above 50%. Needed 50+ more trials.

**Constitutional rule**: Never ship on vibes. Compute P(hypothesis | data). Set threshold. Wait.

---

### PART 6: Exercises & Wrap-Up

**Exercise 1**: Build `probability.py` with all functions.

**Exercise 2**: Monty Hall — compute with Bayes.

**Exercise 3**: Simpson's Paradox — conditional probability + imbalanced groups.

**Exercise 4 [PUBLISH]**: "Why We Stopped Trusting 5-Trial A/B Tests" — the story for practitioners.

---

### OUTRO

**What you built**: `probability.py`, intuition for surprise, P(hypothesis | data).

**What you know**: 3/5 not surprising, Bayes flips conditionals, small samples lie.

**What's missing**: Discrete hypotheses are limiting. Need continuous distributions.

**Next**: Module 0.3 — Beta distribution, the bandit's secret weapon.

---

## Continuity Checklist

| From → To | Thread |
|-----------|--------|
| Module 0.1 → Part 0 | RunPod incident → buildlog → SalienceScorer |
| Part 0 → Part 1 | Scorer validated → deployed in loop |
| Part 1 → Part 2 | Loop working → A/B test to prove it |
| Part 2 → Part 3 | A/B "worked" → crashed → what went wrong? |
| Part 3 → Section A | "How surprised?" → list possibilities |
| Section A → B | Listed → count faster |
| Section B → C | Counts → probability |
| Section C → D | P(data \| hypothesis) → vary hypothesis |
| Section D → E | Conditional probability → want the flip |
| Section E → F | Flip = Bayes' theorem |
| Section F → G | One update → keep updating |
| Part 5 → Exercises | Apply everything |
| Outro → 0.3 | Discrete → continuous distributions |

---

## Jargon-Earning Order

| Term | Introduced | Earned By |
|------|------------|-----------|
| buildlog | Part 0 | Explaining what it does first |
| multi-armed bandit | Part 0 | Slot machine analogy, explicitly deferred |
| treatment/control | Part 2 | "Group A/B" first, then named |
| sample space | Section A | Listing outcomes first |
| n choose k | Section B | "Choosing positions" intuition |
| binomial distribution | Section C | Building the table first, then naming |
| conditional probability | Section E | Card example first |
| Bayes' theorem | Section F | "The flip" intuition first |
| prior/posterior/likelihood | Section F | After formula, as labels |
