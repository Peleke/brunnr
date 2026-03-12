# Bragi Review: context-engineering-not-copywriting
# Date: 2026-03-09
# Source: article-draft skill (28-rule Bragi Prose Gate + 6-pass)

Now I have the full article. Let me run all 6 passes.

---

# Full 6-Pass Review: "Context Engineering Is Not Copywriting"

---

## Pass 1: Bragi Scan (28 Rules)

### Hard Bans (1-5)

| # | Rule | Status | Findings |
|---|------|--------|----------|
| 1 | No em dashes | **VIOLATION** | Line 27: "Each interaction is a pull." -- no literal em dash found on re-read. Let me verify carefully... No em dashes detected. **PASS** |
| 2 | No AI blocklist words | **VIOLATION** | Line 15: **"highlight"** not used as verb. Line 48: **"novel"** is not on the list. Scanning all lines... **"enhance"** not found, **"crucial"** not found, **"key"** -- Line 44: "which model to call, with what parameters, given what context" -- no "key as adjective" usage. Line 35: **"valuable"** not found. **PASS** |
| 3 | No performative honesty | **PASS** | No "to be honest," "frankly," "the truth is" constructions. |
| 4 | No self-referential pivots | **PASS** | No "but what I really want to talk about" or "let me step back" patterns. |
| 5 | No inflated significance framing | **BORDERLINE** | Line 46: "Both treat agents as what they are: partially observable Markov decision processes" -- this is a factual claim about a modeling choice, not inflated significance. **PASS** |

### Structural Bans (6-10)

| # | Rule | Status | Findings |
|---|------|--------|----------|
| 6 | No hedging then inflating | **PASS** | No "it might seem X, but actually it's ENORMOUS" patterns. |
| 7 | No punchy fragment marketing copy | **VIOLATION** | Line 15: "That's not engineering. That's copywriting." -- Two consecutive short declarative fragments used for rhetorical punch. This is marketing-copy cadence. Line 17: "That's the gap." -- same pattern. |
| 8 | No tricolon/pentad for rhythm | **NEEDS ESCALATION TEST** | Line 35: "**tools** (dozens of MCP tool schemas), **skills** (reusable prompt chunks with known token costs), and **context files** (workspace files the agent might need)" -- This is a list of three arm types. Each adds a genuinely new dimension (tool schemas vs. prompt chunks vs. workspace files). **PASS** -- escalation test satisfied. |
| 9 | No rhythmic parallel closers | **PASS** | The ending is not a rhythmic parallel. |
| 10 | No challenges-and-future-prospects formula | **PASS** | No "challenges remain but the future is bright" structure. |

### Word-Level Bans (11-15)

| # | Rule | Status | Findings |
|---|------|--------|----------|
| 11 | No elegant variation | **PASS** | "Bandit" stays "bandit." "Tools" stays "tools." No thesaurus cycling. |
| 12 | No copula avoidance | **PASS** | No "serves as," "functions as," "acts as" where "is" would do. |
| 13 | No dismissive 'with' framing | **PASS** | No "with X, Y becomes possible" that papers over difficulty. |
| 14 | No vague attribution | **PASS** | Line 48: "Garivier et al. formalized the theory in 2016" -- specific citation. |
| 15 | No false ranges | **PASS** | No "from X to Y" where both endpoints are basically the same thing. |

### Analysis Bans (16-20)

| # | Rule | Status | Findings |
|---|------|--------|----------|
| 16 | No superficial participle analysis | **PASS** | No "leveraging X, enabling Y, transforming Z" chains. |
| 17 | No hedging with 'not' lists | **PASS** | No "not X, not Y, not Z" lists used to avoid stating a position. |
| 18 | No colon-into-bold-statement | **VIOLATION** | Line 17: "treating the agent's prompt as a **policy**: a function from state to action" -- colon introduces bold term. Line 44: same pattern. Line 43-44 both use "**TensorZero**" and "**What I'm building**" after list markers into bold. These are list items with bold labels, which is a different pattern (descriptive list), but Line 17 is a straight colon-into-bold. |
| 19 | No promotional puffery | **PASS** | Claims are specific and backed by described implementation. |
| 20 | No notability assertion sections | **PASS** | No "why this matters" section. |

### Rhythm/Structure Bans (21-28)

| # | Rule | Status | Findings |
|---|------|--------|----------|
| 21 | No blunt fragment negation | **VIOLATION** | Section heading "## Not Just Tools" (line 33) plus the first sentence pattern. Not a standalone fragment per se, but the section title is the blunt negation pattern. |
| 22 | No wall-of-text paragraphs | **VIOLATION** | Line 29: The paragraph starting "The details matter..." has 4+ independent beats packed into one block: (1) not every interaction is a signal, (2) conversational turns discarded, (3) cold-start protection, (4) exploration rate, (5) token budget cap. This is a wall. Should be broken or converted to a list. |
| 23 | No full-clause linking | **PASS** | No "which is important because [full clause]" chains. |
| 24 | No mirrored affirmation pairs | **PASS** | No "X is real. So is Y." |
| 25 | No "not just X, but also Y" | **VIOLATION** | Line 33: Section title is literally "Not Just Tools." Line 35: "The bandit doesn't only select tools. It selects across three arm types" -- this is the "not just X, but also Y" structure. |
| 26 | No restating the obvious | **BORDERLINE** | Line 46: "Both treat agents as what they are: partially observable Markov decision processes where the observation function determines the quality of the action" -- the POMDP framing was already stated in line 17. This is a restatement, but it closes a comparison. Mild violation. |
| 27 | No bare conjunctions as standalone paragraphs | **PASS** | No standalone "And..." or "But..." paragraphs. |
| 28 | No emotional cliche templates | **PASS** | No "a mix of X and Y" emotion constructions. |

### Bragi Summary

**7 findings:**
- Rule 7 (punchy fragment marketing copy): Lines 15, 17 -- "That's not engineering. That's copywriting." / "That's the gap."
- Rule 18 (colon-into-bold): Line 17
- Rule 21 (blunt fragment negation): "Not Just Tools" heading
- Rule 22 (wall-of-text): Line 29 paragraph
- Rule 25 ("not just X, but also Y"): Section title + line 35
- Rule 26 (restating the obvious): Line 46 re-explains the POMDP framing from line 17

---

## Pass 2: SPIN Audit

**Situation:** The reader is building or managing AI agents that use system prompts, CLAUDE.md files, or similar context injection. They're probably hand-editing these files.

**Problem:** Hand-editing context is not engineering. There's no feedback loop. No optimization. The observation function (what goes into the context window) is being written by vibes, not by data.

**Implication:** Wasted tokens. Wasted context window. The agent uses tools it shouldn't. It ignores tools it should use. Performance degrades as tool/skill surface area grows. The human becomes the bottleneck, manually curating what the agent sees.

**Need-payoff:** The article demonstrates a working system (Vindler + multi-armed bandit) that automatically learns which tools, skills, and context files earn their token cost. The reader gets a concrete architecture to copy or build against.

### SPIN Assessment

| Element | Quality | Notes |
|---------|---------|-------|
| Situation | **Strong** | "Everyone's talking about it" -- grounded in a real trend. |
| Problem | **Strong** | "That's copywriting" is a sharp reframe. |
| Implication | **Weak** | The article never spells out the cost of NOT doing this. What happens when you have 50 tools and hand-edit? 200? The scaling pain is implied but never stated. There's no "and here's what breaks" moment. |
| Need-payoff | **Moderate** | The 30-day result (line 31) is the payoff, but it's one sentence. No numbers. "High-value tools have pulled ahead" is vague. How much context was saved? What was the token reduction? Did task completion improve? |

### SPIN Recommendations
1. Add one sentence of implication after the gap section: what breaks at scale without this?
2. Sharpen the 30-day payoff with at least one concrete number (token savings %, number of tools suppressed, or before/after context window utilization).

---

## Pass 3: Engagement Audit

### Protagonist

**Who is the protagonist?** The system (Vindler / the bandit) is the protagonist, not Peleke and not the reader. Peleke appears as "I" three times but only as the builder. The bandit is described doing things: observing, updating, selecting, suppressing.

**Assessment:** This works for a technical audience. The system-as-protagonist is fine for an architecture article. But the opening ("Everyone's talking about it. Almost nobody is actually engineering it.") addresses a crowd, not a person. Consider whether the ideal reader is an engineer who hand-edits CLAUDE.md and feels the pain, or a technical leader evaluating approaches. The article currently speaks to both and neither with full specificity.

### Circular Close

**Does the ending return to the opening?** The opening says "that's copywriting, not engineering." The ending says "treating 'what goes into the prompt' as an optimization problem instead of a text-editing problem." This is a clean circular close. The reframe at the end echoes the reframe at the top. **Strong.**

### Data Points

| Claim | Evidence | Strength |
|-------|----------|----------|
| Everyone's hand-editing | Implied (cultural observation) | Weak -- no example or link |
| Bandit learns tool selection | Described architecture | Moderate -- mechanism is clear but no repo link to bandit code |
| 30 days of real usage | "roughly 30 days" | Weak -- no metrics, no chart, no before/after |
| Garivier et al. 2016 | Named citation | Moderate -- no link |
| TensorZero comparison | Named company | Moderate -- but no link or specific reference |

**Data point density:** 5 claims, 0 hard numbers, 0 charts, 1 citation without link. For an article titled "engineering," the evidence is surprisingly narrative. The architecture description is detailed, but the results section is thin.

---

## Pass 4: Voice Analysis

### Register Detection

**Register A (Frustrated Engineer / Mickens):** Present in the opening. "That's not engineering. That's copywriting." has the Mickens energy of calling out an industry delusion. Lines 15-17 are solidly Register A. But it fades after the gap section. The implementation section (lines 23-31) is neutral technical prose -- no frustration, no edge. The article opens with a hot take and then switches to a conference paper.

**Register B (Self-Deprecating Narrator / Sedaris):** Absent. There's no self-deprecation, no "I tried the dumb thing first," no admission of failure or iteration. The 30-day result is presented as clean success. This makes the article feel like a press release for the bandit system rather than a build log.

**Register C (Tour Guide / Paul Ford):** Faint. Line 41: "If you squint, this is the bottom of a familiar stack" is Tour Guide voice -- inviting the reader to see a pattern. But it's one sentence. The rest of the stack section is declarative.

### Voice Assessment

The article has a **register mismatch**: it opens in Register A (frustrated engineer calling bullshit) and then switches to neutral technical exposition with no personality. The reader who was hooked by the frustration gets clinical prose for the payoff. Options:

1. **Commit to Register A throughout:** Add frustration-colored observations in the implementation section. "The first version penalized every tool on conversational turns. Turns out 'the user said hello' is not evidence that your code search tool is useless."
2. **Add Register B for the build section:** What went wrong? What did the bandits do that surprised you? Where did the cold-start problem bite?
3. **Add Register C for the stack section:** Guide the reader through the layers more slowly. "If you've ever used a router that picks which backend to call, you've seen this pattern."

---

## Pass 5: Visual Injection Opportunities

| Location | Opportunity | Type | Impact |
|----------|-------------|------|--------|
| After line 17 (The Gap) | Diagram: "Copywriting Loop" (human edits text, deploys, hopes) vs. "Engineering Loop" (agent acts, system observes, posteriors update, context adapts) | Side-by-side flow diagram | **High** -- makes the core argument visual |
| After line 31 (30-day result) | Chart: Posterior distributions for 5-6 representative tools after 30 days. Show the divergence. High-value tools with tight Beta distributions on the right, low-value tools suppressed on the left. | Bar chart or density plot | **High** -- this is the missing proof. The article claims the posteriors diverged but shows nothing. |
| After line 35 (arm types) | Table: Arm types (tools, skills, context files) with columns for count, avg token cost, selection mechanism | Simple table | **Medium** -- clarifies the three-arm architecture |
| After line 46 (stack comparison) | Stack diagram: Infrastructure layer (TensorZero: model selection) → Agent layer (Vindler: context selection) → Application layer (your app) | Vertical stack diagram | **Medium** -- makes the layering argument concrete |
| Line 48 (Garivier citation) | Inline link to the paper | Hyperlink | **Low effort, high credibility** |

### Priority

The posterior divergence chart (opportunity 2) is the single highest-impact addition. The article's credibility hinges on "it works after 30 days" and currently provides zero visual evidence.

---

## Pass 6: Staleness Check

**Publication date:** 2026-02-24 (approximately 2 weeks old as of today, 2026-03-09)

| Element | Current | Risk | Notes |
|---------|---------|------|-------|
| "Context engineering" as trending phrase | Still current | **Low** | The term is still active in discourse (Tobi Lutke tweet, Simon Willison posts, etc.) |
| TensorZero reference | Still active company | **Low** | They're shipping. Reference is safe. |
| CLAUDE.md / .cursorrules | Still the dominant pattern | **Low** | These are current tools. |
| "Everyone's talking about it. Almost nobody is actually engineering it." | May age quickly | **Medium** | If more people start building feedback loops (and they will), this claim becomes stale. Consider timestamping it: "As of early 2026..." or letting the claim stand and accepting it has a shelf life. |
| Garivier et al. 2016 | Evergreen | **None** | Math doesn't expire. |
| Vindler / OpenClaw link | Live repo | **Low** | As long as the repo exists. |
| "The memory layer is the extension I'm working on now" | Time-sensitive | **High** | This will become stale the moment memory ships. Update to past tense when it does, or remove the temporal marker ("I'm working on now" → describe the memory architecture directly). |

### Staleness Verdict

The article is fresh. Two time-bombs to watch:
1. Line 37: "the extension I'm working on now" -- will go stale when memory ships.
2. Line 15: "the phrase of the moment" -- will go stale when the discourse moves on (3-6 months).

---

## Consolidated Findings

### Must-Fix (Bragi violations that weaken the piece)

1. **Rule 22 (wall-of-text):** Line 29 paragraph needs breaking. Five independent beats in one block.
2. **Rule 25 + 21 ("Not Just Tools"):** Rename the section and restructure the opening sentence to avoid the banned "not just X, but also Y" pattern.
3. **Rule 7 (punchy fragments):** "That's not engineering. That's copywriting." and "That's the gap." -- these are effective but violate the rule. Consider combining into longer sentences that preserve the punch without the staccato marketing cadence.

### Should-Fix (SPIN / Engagement gaps)

4. **Missing implication:** What breaks when you don't do this? Add one sentence of scaling pain.
5. **Missing payoff numbers:** The 30-day claim needs at least one concrete metric. Token savings, tools suppressed, context utilization delta.
6. **Missing posterior chart:** The single highest-impact visual addition. Show the divergence.

### Consider (Voice / Polish)

7. **Register mismatch:** The opening is Register A (frustrated engineer), the body is neutral technical. Pick a lane or blend deliberately.
8. **Garivier citation needs a link.**
9. **TensorZero claim needs a link.**
10. **Line 37 time-bomb:** "I'm working on now" will go stale. Decide whether to timestamp it or describe the architecture without temporal markers.