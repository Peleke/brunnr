# Module 0.3: Distributions & Beta Priors — Narrative Outline

> **Status**: Ready-to-generate outline.
>
> **What makes this ready**: War stories linked, jargon-earning order established, section-by-section thought process documented, continuity threads explicit, engagement elements planned per skill sections 13-18.

---

## Module Metadata

**Arc**: 0 — Probabilistic Foundations
**Position**: Module 3 of 8
**Prerequisites**: Module 0.2 (Probability & Counting — binomial PMF, Bayes' theorem basics)
**Estimated time**: ~90-120 minutes

**Falsifiable claim**: "I can derive Beta(α,β) parameters from a plain-English belief statement and explain why Beta(1,1) is uniform, Beta(3,1) is optimistic, and why my specific prior is justified."

**Implementation target**: Extend buildlog's `BetaParams` class with distribution visualization and prior elicitation helper.

---

## Starting State (What the Reader Has from 0.2)

The reader walks into Module 0.3 with:

1. **`binomial_pmf(k, n, p)`** — they built this. They can compute P(k successes in n trials | p).
2. **`bayes_update(prior, likelihood, evidence)`** — they built this. They can flip P(data|H) → P(H|data) for *discrete* hypotheses.
3. **The A/B test disaster** — they shipped on 3/5 vs 2/5, got burned. They know small samples lie.
4. **The gap they felt**: In 0.2's Bayes section, they compared "Is p = 50% or 60%?" and got posteriors 47.4% vs 52.6%. The module ended by saying: "Discrete hypotheses are limiting. What if p could be *anything*? That's distributions. Module 0.3."

**The opening move**: Pick up the binomial PMF from 0.2 directly. "You can compute P(k|n,p). But you assumed p was known. What if p *is* the unknown?" That's the entire module in one sentence.

---

## War Story Integration

**No generic recap**. Open with the binomial PMF they built, show the gap (p was always given), and *immediately* connect to the bandit: "In buildlog, p is the unknown success rate of each rule. You need a way to represent your uncertainty about p."

**Story A — The Hardcoded Priors**: When you first built the bandit for buildlog, you needed starting beliefs for each rule's success rate (their unknown p). You Googled "beta distribution bandit" and found a blog post that said:
- `Beta(1,1)` = "no opinion" (uniform)
- `Beta(3,1)` = "probably good"
- `Beta(1,3)` = "probably bad"

You hardcoded `Beta(3,1)` for every new rule because "rules are usually good, right?" It worked. The bandit converged, good rules rose, bad rules faded.

**Story B — The Wrong Prior Disaster**: Then you added a batch of experimental rules — aggressive rewrites that changed agent behavior dramatically. These rules had maybe a 20% success rate. But your prior said "probably 75% good." The bandit started by selecting these experimental rules heavily (the prior said they were good), collected a string of failures, and took *200 trials* to overcome the bad prior and learn these rules were actually harmful. Meanwhile, a proven rule with Beta(50,15) was waiting — but the bandit kept picking the experimental rule because its prior was high.

**The Turn**: "Why did we use Beta(3,1) for everything? Because a blog post said so. We didn't ask: *What do we actually believe about this rule?* We need a way to translate beliefs into priors."

**Threading**:
- Story A uses the buildlog bandit from Modules 0.1-0.2 (and teased in 0.2's "multi-armed bandit" mention).
- Story B exposes that we can't just pick priors from a menu — we need to *derive* them from beliefs.
- The bridge: "We need to understand distributions — especially the Beta distribution — well enough to justify every prior we set."

---

## Conceptual Scope

| Concept | Why We Need It | Narrative Hook |
|---------|----------------|----------------|
| Distribution as shape | Move from "P(k) for one k" to "the full picture" | "A distribution is a shape that tells a story" |
| Bernoulli/Binomial (already built) | Foundation for Beta derivation | "You have binomial_pmf. Now meet the rest of the family" |
| Continuous vs discrete | Why we need distributions on [0,1] | "p isn't 50% or 60% — it's somewhere on a continuum" |
| PDF vs PMF | The continuous version of "probability of k" | "PMF counts, PDF smears" |
| Beta distribution | The distribution for unknown probabilities | "It lives on [0,1] and can be any shape you need" |
| α and β as pseudo-counts | Why Beta(3,1) means "3 successes, 1 failure observed" | "Prior is fake data you bring to the table" |
| Prior elicitation | Translate beliefs → Beta parameters | "I think 70%, ±15% → Beta(α,β)" |
| Credible intervals | What "±15%" means rigorously | "The middle 90% of my belief" |
| Conjugacy (teased) | Why Beta + Binomial = Beta (mechanics deferred to 0.4) | "The posterior is the same shape as the prior — that's not an accident" |

**What we DON'T cover** (deferred):
- Bayesian updating mechanics / conjugacy proof → Module 0.4
- Normal, Gamma, Poisson in depth → mentioned in gallery, deep-dive later
- Hypothesis testing with continuous priors → Module 0.5
- Credible intervals vs confidence intervals → Module 0.6

---

## Engagement Plan (Skill Sections 13-18)

| Type | Count | Where | What |
|------|-------|-------|------|
| Concept map | 1 | Cell 3 (after imports) | `arc_progress_map(0, 8, 3)` — modules 1-2 green, 3 blue |
| Video embed | 2 | After distribution gallery; After Beta elicitation | StatQuest Binomial (`IYdiKeQ8Ppg`); StatQuest Beta (`juF3r12nM5A`) |
| Plotly | 3 | Distribution gallery; Beta shape explorer; Prior comparison | Interactive distribution switcher; 3D α-β surface; side-by-side prior plot |
| Widget | 2 | Beta shape explorer; Prior elicitation | α/β sliders → live PDF; "I think X%, ±Y%" → Beta params |
| Animation | 1 | After Beta introduction | Beta shape morphing as α,β change (FuncAnimation) |
| Build-a-toy | 1 | Exercises | Prior Elicitation Tool: belief → Beta params → plot → credible interval |
| Manim stub | 1 | After Beta shape section | `# TODO: Manim — probability simplex, Beta as distribution on [0,1]` |

---

## Part-by-Part Narrative Sketch

### PART 0: The Opening — From Binomial PMF to "p Is Unknown"

**No recap. Start with what they built.**

Open with their `binomial_pmf(k, n, p)` from Module 0.2. Run it: `binomial_pmf(3, 5, 0.5) = 0.3125`. "You can compute P(3 successes in 5 trials | p=0.5). You did this."

Then: `binomial_pmf(3, 5, 0.6) = 0.3456`. Different p, different answer.

Then: `binomial_pmf(3, 5, ???)`. "But here's what you've been avoiding. In the real world — in buildlog, in your A/B tests, in every experiment — p is the thing you don't know. You computed P(data|p). But p was always given. What if p itself is the question?"

**The gap**: "You need a way to represent *uncertainty about p*. Not 'p is 50% or 60%' — you tried that in 0.2 and it was limiting. You need 'p is probably between 55% and 75%, and here's exactly how confident I am.'"

**The word**: "That's a **distribution**. A shape that encodes your belief about where p lives."

**Visual**: Concept map (arc progress, module 3 highlighted). Then: a teaser plot — three different "shapes of belief" about p on the same axes, unlabeled. "By the end of this notebook, you'll know what each of these shapes means and how to build the right one."

---

### PART 1: Story A — The Hardcoded Priors

**The context**: buildlog's bandit needs a starting belief for every rule. When you set it up, you hardcoded:
- New rules: `Beta(3,1)` — "probably good"
- Untested: `Beta(1,1)` — "no opinion"

**The code**: Show the actual BetaParams dataclass. Show how the bandit uses `np.random.beta(α, β)` to sample and decide.

**The celebration**: It works! Rules converge. Good rules get selected. You ship it.

**Visual**: Plot showing 4 rules converging over 100 trials — good rules rise, bad rules fall. (matplotlib — simple line chart, clean)

---

### PART 2: Story B — The Wrong Prior

**The incident**: New batch of experimental rules. Aggressive rewrites. True success rate: ~20%. But `Beta(3,1)` says "probably 75% good."

**The disaster**: Bandit heavily selects experimental rules (prior says they're great). Racking up failures. A proven rule (`Beta(50,15)`) is sitting there, neglected, because the experimental rule's prior started higher.

**The damage**: Show the simulation — 200 trials wasted before the bandit recovers.

**Visual**: Plotly line chart showing selection probability of the experimental rule vs. the proven rule over 200 trials. Hover shows trial number, rule name, selection probability, cumulative success rate. The "crossover point" where the bandit finally learns is the visual punchline.

**The post-mortem**: "We used Beta(3,1) because a blog post said to. We didn't ask: what do we *actually believe* about this rule?"

---

### PART 3: The Turn — Distributions as Shapes of Belief

**The question**: "What does Beta(3,1) even *mean*? Why not Beta(5,2) or Beta(10,3)? How do you choose?"

**The realization**: A distribution isn't just a formula. It's a *shape*. The shape encodes what you believe — where the most likely values are, how spread out your uncertainty is, and where the boundaries lie.

**The promise**: "By the end of this notebook, you'll be able to translate any plain-English belief into a Beta distribution and *justify* it."

---

### SECTION A: The Distribution Gallery — Where Beta Fits

**Thought process**: "I know Bernoulli and Binomial — I built binomial_pmf. Where does Beta fit in the family tree?"

**Scenario**: Start from `binomial_pmf(k, n, p)`. "You have this function. It answers 'how many successes?' But there's a whole family of distribution shapes, each answering a different question. Let's meet them — so you know which tool to reach for."

**Content**:
- **Bernoulli**: The coin flip. P(success) = p. The atom. "You built on top of this in 0.2."
- **Binomial**: n coin flips. "How many successes?" "This is *your* `binomial_pmf`. You own this."
- **Poisson**: "How many events in a time window?" (Slack messages per hour, errors per deploy). Mentioned, not deep-dived.
- **Normal/Gaussian**: The bell curve. "Appears when you add enough of anything." Mentioned, teased for Arc 1.
- **Beta**: "What's the probability of the probability?" The distribution for unknown p.

**Interactive cell (Plotly)**: Distribution gallery. Plotly figure with dropdown/buttons to switch between distributions. Each shows the PMF/PDF with hover data. The Beta option has α/β sliders via Plotly animation frames.

**Insight**: "Beta is special because it lives on [0,1] — perfect for modeling unknown probabilities."

**Video**: StatQuest Binomial (`IYdiKeQ8Ppg`) after the gallery — reinforces the binomial they built in 0.2, bridges to "but what if p is unknown?"

> **Go deeper**: Blitzstein & Hwang Ch. 3 (distributions), McElreath Ch. 2 (generative models), ThinkBayes Ch. 2 (distributions as beliefs).

---

### SECTION B: Meet the Beta Distribution

**Thought process**: "OK, Beta lives on [0,1]. What does it look like? How do α and β control the shape?"

**Scenario**: Start with Beta(1,1). Plot it. "It's flat. Uniform. Every value of p is equally likely."

**Build up**:
1. Beta(1,1) — flat. "I have no idea."
2. Beta(2,1) — tilts right. "Probably good, but not sure."
3. Beta(3,1) — more tilted. "Probably good."
4. Beta(10,3) — peaked. "Pretty confident it's around 75%."
5. Beta(1,3) — tilts left. "Probably bad."
6. Beta(50,50) — sharp peak at 0.5. "Very confident it's 50/50."

**Implementation**: `from scipy.stats import beta as beta_dist`. Plot each with `beta_dist.pdf(x, α, β)`.

**Widget (ipywidgets)**: Two sliders (α and β, range 0.5 to 50). Live plot updates showing the PDF. Display mean, mode, variance, and 90% credible interval below the plot. Include special cases highlighted: "You're at Beta(1,1) — uniform!" or "Mean = 0.75, you think this works 3/4 of the time."

**Insight**: "α and β aren't arbitrary. They're like *fake observations*. α = prior successes, β = prior failures. Beta(3,1) means 'I've seen 3 successes and 1 failure' — even though you haven't seen any real data yet."

**The "pseudo-counts" revelation**: This is the big aha. α−1 successes, β−1 failures. Beta(1,1) = 0 fake observations = uniform. Beta(3,1) = 2 fake successes, 0 fake failures. The numbers *mean something*.

---

### SECTION C: The Math Behind the Shape (PDF)

**Thought process**: "We've been plotting Beta. What's the actual formula?"

**Concept-first**: "You know the shape. You know α and β control it. The formula just writes down what the plot already shows."

**The PDF**:
```
f(p; α, β) = p^(α-1) × (1-p)^(β-1) / B(α, β)
```

Where B(α, β) is the normalization constant (Beta function — makes the area = 1).

**Walk through each piece**:
- `p^(α-1)`: Pulls density toward 1 as α grows (more "successes")
- `(1-p)^(β-1)`: Pulls density toward 0 as β grows (more "failures")
- `B(α, β)`: Makes the total area 1 (so it's a valid probability distribution)

**Verification cell**: Compute the PDF by hand for Beta(3,1) at p=0.5, verify against `beta_dist.pdf(0.5, 3, 1)`.

**Key formulas** (after building intuition):
- Mean: α / (α + β) — "fraction of fake successes"
- Mode: (α-1) / (α+β-2) for α,β > 1 — "most likely value"
- Variance: αβ / [(α+β)² (α+β+1)] — "how spread out"

**Interactive cell**: Table showing α, β, mean, mode, variance for our example Betas. The reader should feel "oh, the mean is just the fraction of successes, that makes sense."

---

### SECTION D: Beta Shape Morphing — Watching Belief Crystallize

**Thought process**: "How does the shape change as we get more 'observations'?"

**Static version first**: Grid of 6 plots showing Beta(1,1) → Beta(2,1) → Beta(5,2) → Beta(10,3) → Beta(30,10) → Beta(100,33). Each has the same x-axis. Watch the peak sharpen and center around 0.75.

**Animation (FuncAnimation)**: Smooth morphing from Beta(1,1) to Beta(100,33), incrementing α by 1 and β by ~0.33 each frame. The peak sharpens, narrows, centers. Frame counter shows "α=X, β=Y, mean=Z".

**Insight**: "More data (even fake data) → sharper belief. That's what 'confidence' looks like mathematically."

**Manim stub**: `# TODO: Manim animation — probability simplex, showing Beta as a curve sliding along the [0,1] interval, morphing shape like a living thing`

---

### Interlude: Why Beta? The Conjugacy Teaser

**Hook question**: "Why Beta specifically? Why not put any distribution on [0,1]?"

**The short answer**: Because when you observe Binomial data and your prior is Beta, the posterior is also Beta. The math stays clean. You just update α and β.

**Show it** (mechanically, without proving):
- Prior: Beta(3, 1)
- Observe: 7 successes, 3 failures in 10 trials
- Posterior: Beta(3+7, 1+3) = Beta(10, 4)

"That's it. Add successes to α, failures to β. We'll prove why this works in Module 0.4. For now, just see that it works."

**Verification cell**: Plot prior Beta(3,1) and posterior Beta(10,4) on the same axes. The posterior is shifted and sharper.

**Video**: StatQuest Beta Distribution (`juF3r12nM5A`) — after the reader has built intuition for α, β, and seen the conjugacy teaser. The video gives a different visual angle on *why* the shape does what it does.

**Conjugacy preview**: "Module 0.4 is entirely about Bayesian updating. We'll derive why this works, prove it, animate the posterior evolving trial by trial. For now, the takeaway: Beta is the *right* prior for binary outcomes because the math stays in the family."

> **Go deeper**: McElreath Ch. 2 (grid approximation vs conjugate updating), ThinkBayes Ch. 3 (the Beta-Binomial model), Jaynes Ch. 3 (why conjugate priors emerge from symmetry).

---

### SECTION E: Prior Elicitation — Translating Beliefs to Numbers

**Thought process**: "OK, I get Beta. But how do I choose α and β for a *real* situation?"

**The problem**: Your domain expert says "I think this rule works about 70% of the time, give or take 15%." You need to turn that into Beta(α, β).

**Method 1 — Mean + variance matching**:
- "Works 70%" → mean = 0.7 → α/(α+β) = 0.7
- "Give or take 15%" → interpret as standard deviation ≈ 0.15 → variance ≈ 0.0225
- Solve the system of equations → get α and β

**Implementation**: Build `elicit_prior(mean, std)` → returns (α, β).

**Verification**: Plot Beta(α, β), check that 90% credible interval covers roughly [0.55, 0.85].

**Method 2 — Pseudo-count intuition**:
- "I'd believe this like I'd believe 7 successes and 3 failures" → Beta(7, 3)
- Even simpler: "How many trials would I need to see before I trust this?" → α + β ≈ that many

**Comparison table**: Show 3 belief statements → both methods → resulting Betas side-by-side.

**Widget (ipywidgets)**:
- Slider: "I think it works X% of the time" (0-100)
- Slider: "My uncertainty: ±Y%" (1-40)
- Output: α, β values, plot of Beta PDF, 90% credible interval, equivalent pseudo-count interpretation
- Compare against: Beta(1,1), Beta(3,1), and the elicited prior — all on one plot

---

### SECTION F: The Buildlog Fix — Justified Priors

**Thought process**: "Let's go back to the disaster from Story B and fix it."

**The fix**: Instead of `Beta(3,1)` for everything, elicit priors per rule *type*:

| Rule Type | Belief | Elicited Prior | Justification |
|-----------|--------|---------------|---------------|
| Proven patterns | "Works ~80%, confident" | Beta(16, 4) | 20 pseudo-observations |
| New features | "Maybe 50%, very uncertain" | Beta(2, 2) | Only 4 pseudo-observations |
| Experimental rewrites | "Probably ~30%, uncertain" | Beta(3, 7) | Pessimistic, wide |
| Meta-rules | "Works ~60%, moderate confidence" | Beta(6, 4) | 10 pseudo-observations |

**Plotly comparison**: Four Beta PDFs on one plot, different colors, hover shows α, β, mean, credible interval. The visual difference between "everything is Beta(3,1)" and "tailored priors" is striking.

**Simulation**: Rerun the Story B disaster with tailored priors. Experimental rule starts with Beta(3,7) instead of Beta(3,1). Now the bandit explores it cautiously, doesn't over-invest, and the proven rule keeps getting selected.

**The punchline**: "Same data. Different priors. Wildly different outcomes. Priors matter."

---

### PART 4: Back to the A/B Test (Continuity Thread)

**Quick connection**: "Remember our A/B disaster from Module 0.2? We observed 3/5 vs 2/5 and shipped. Now we can say *more* — we can express our *uncertainty* about the true rates as Beta distributions."

**Quick exercise**:
- Treatment: 3 successes, 2 failures → Beta(1+3, 1+2) = Beta(4, 3) (starting from uniform)
- Control: 2 successes, 3 failures → Beta(1+2, 1+3) = Beta(3, 4)

**Plot**: Both posteriors on the same axes. They overlap massively. "You can literally *see* that you can't tell them apart."

**Bridge to 0.5**: "In Module 0.5, we'll compute exactly how much they overlap and formalize 'can't tell them apart' as a hypothesis test."

---

### PART 5: Exercises

**Exercise 1**: Distribution Gallery Implementation
Build `distribution_gallery()` — a function that takes a distribution name and parameters, returns a dictionary with PMF/PDF values, mean, variance, and a plot. Test with Bernoulli, Binomial, Poisson, Normal, Beta.

**Exercise 2**: Prior Elicitation Challenge
Given 5 plain-English belief statements, derive Beta priors using both methods (mean+variance matching AND pseudo-count intuition). Plot all 5, verify credible intervals match the stated uncertainty.

**Exercise 3 [BUILD-A-TOY]**: Prior Elicitation Tool
Build an interactive prior elicitation tool with:
- Text input: "I think [rule] works about X% of the time, give or take Y%"
- Sliders for X (0-100) and Y (1-40)
- Output: Beta(α,β) parameters, PDF plot, 90% credible interval
- Comparison mode: overlay your elicited prior against Beta(1,1) and Beta(3,1) defaults
- "Pseudo-count equivalent" display: "This is like having seen N trials with M successes"

Success criteria:
- Changing X shifts the peak of the PDF
- Changing Y widens/narrows the distribution
- Credible interval updates in real-time
- Comparison plot clearly shows how your prior differs from defaults

Extensions:
- Add a "Feed data" button: observe K successes in N trials, update the prior to posterior
- Add preset beliefs: "Optimistic", "Pessimistic", "No opinion", "Strong conviction"
- Export: print the Python code for `beta_dist(α, β)` that the reader can copy into their project

**Exercise 4 [PUBLISH]**: "Choosing Priors for AI Agent Rules"
Write a visual guide using the distribution gallery. Show:
1. Why uniform priors waste learning time
2. How to elicit priors from domain knowledge
3. The "wrong prior disaster" and how tailored priors fix it
4. A decision tree: "What should my prior be?"

Format: Markdown + plots, ready for a blog post or buildlog docs.

---

### OUTRO

**What just happened**: You took "Beta(3,1) because a blog post said so" and replaced it with principled prior elicitation. Along the way, you:
- Met the distribution family (Bernoulli, Binomial, Poisson, Normal, Beta)
- Understood what α and β *mean* (pseudo-counts)
- Built tools to translate beliefs into priors
- Fixed the buildlog disaster with justified priors

**Falsifiable claim check**: Can you derive Beta parameters from "I think X works Y%, ±Z%"? Can you explain why Beta(1,1) is uniform? Why Beta(3,1) is optimistic? Yes? Claim met.

**Publication note**: Exercise 4 is a draft for "Choosing Priors for AI Agent Rules" — run an edit pass and it's ready for buildlog docs.

**What's next**: You've set priors. But what happens when data comes in? Module 0.4 is about **Bayesian updating** — watching the posterior evolve as evidence accumulates, proving *why* Beta + Binomial stays Beta, and building a dynamics tracker that shows belief crystallization in real time.

→ [Module 0.4: Bayesian Updating](../module-0.4-bayesian-updating/0.4-bayesian-updating-core.ipynb)

---

## Continuity Checklist

| From → To | Thread |
|-----------|--------|
| Module 0.2 outro → Part 0 | binomial_pmf(k,n,p) assumed p known → "What if p is the unknown?" |
| Part 0 → Part 1 (Story A) | p is unknown in buildlog → bandit needs starting beliefs → hardcoded Beta(3,1) |
| Part 1 → Part 2 (Story B) | Hardcoded works → until it doesn't (experimental rules) |
| Part 2 → Part 3 (The Turn) | Wrong prior disaster → "How do we choose priors?" |
| Part 3 → Section A | Need to understand distributions → the gallery |
| Section A → B | Gallery overview → deep dive on Beta |
| Section B → C | Intuition for shape → the actual formula |
| Section C → D | Static shapes → animated morphing |
| Section D → Interlude | Shape understood → why Beta specifically? (conjugacy teaser) |
| Interlude → Section E | Conjugacy = Beta is the right choice → now choose well |
| Section E → F | Elicitation method → apply to buildlog |
| Section F → Part 4 | Fixed buildlog → revisit A/B test from 0.2 |
| Part 4 → Part 5 | Analysis → exercises |
| Outro → Module 0.4 | Priors set → what happens when data arrives? |

---

## Jargon-Earning Order

| Term | Introduced | Earned By |
|------|------------|-----------|
| distribution | Part 0 | "Shape of belief" intuition from recap |
| PDF vs PMF | Section A | "PMF counts, PDF smears" — after seeing both |
| Beta distribution | Section A gallery | Seeing it in context of the family |
| α and β (parameters) | Section B | Playing with slider and seeing shape change |
| pseudo-counts | Section B | "α−1 successes, β−1 failures" revelation |
| Beta function B(α,β) | Section C | After the formula, as normalization |
| conjugacy | Interlude | Mechanically — add successes to α, failures to β |
| prior elicitation | Section E | After understanding what priors mean |
| credible interval | Section E | "The middle 90% of my belief" |
| mode | Section C | After mean — "most likely value" |
