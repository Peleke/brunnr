# Bragi Review: feedback-loop-retrieval-learns
# Date: 2026-03-09
# Source: Manual 28-rule Bragi Prose Gate + Pelekification + staleness check
# File: /Users/peleke/Documents/Projects/portfolio/src/content/writing/feedback-loop-retrieval-learns.mdx

---

## Article Overview

**Prose lines:** 13-15, 19-59, 186-190, 192-216, 242-279 (remaining lines are frontmatter, imports, HTML widget code, code blocks, images)
**Word count:** ~1,900 words of prose
**Function:** Technical walkthrough. Explains the qortex feedback loop: Thompson Sampling, edge weight adjustment, Personalized PageRank. Includes interactive Beta distribution widget, code example, competitive comparison, and convergence discussion.

---

## Pass 1: Bragi Scan (28 Rules)

### Violations Found

---

**R1 -- Em dashes**

- **Line 33:** `"— how edges estimate their own reliability"`
- **Line 34:** `"— how feedback reaches the graph"`
- **Line 35:** `"— how the graph decides what to surface"`
- **Line 213:** `"— cosine finds OpenID Connect (vocabulary match), but PPR also surfaces SAML"`

  Four em dashes total. Lines 33-35 use em dashes as list item separators in the table of contents. Line 213 uses an em dash to introduce a parenthetical explanation inside a blockquote.

  **Fix direction (lines 33-35):** Replace em dashes with colons. Each item already follows the pattern "Label -- explanation," and the colon is the natural Pelekification connector:
  - `[Thompson Sampling](#1-thompson-sampling): how edges estimate their own reliability`
  - `[Edge Weight Adjustment](#2-edge-weight-adjustment): how feedback reaches the graph`
  - `[Personalized PageRank](#3-personalized-pagerank): how the graph decides what to surface`

  **Fix direction (line 213):** Replace with a period and new sentence, or use a colon:
  1. `"How to implement enterprise SSO?" Cosine finds OpenID Connect (vocabulary match), but PPR also surfaces SAML...`
  2. `"How to implement enterprise SSO?": cosine finds OpenID Connect (vocabulary match), but PPR also surfaces SAML...`

  **Severity:** Low. The list em dashes are structural, not the LLM "dramatic pause" pattern. Still worth normalizing to colons for voice consistency.

---

**R7 -- Punchy fragment marketing copy**

- **Line 27:** `"Today? Same agent, same neighborhood, same question, but we're headed to Riverside Animal Clinic."`
  The question-then-answer cadence ("Today?") is a marketing rhythm. The anaphora "same... same... same..." is a sales punchline. However, this is inside a narrative vignette (the vet story), and the payoff ("Riverside Animal Clinic") is concrete. **Borderline.** The fragment serves the story; it doesn't read as a tagline in isolation.

- **Line 29:** `"No retraining. No re-embedding. Just good, old-fashioned, re-membering what's wrong, and not repeating it."`
  Three fragments: "No retraining. No re-embedding. Just..." This is textbook staccato negation sliding into a punchline. The hyphenation joke ("re-membering") adds charm, but the "No X. No Y. Just Z." template is a marketing formula.

  **Fix direction (line 29):** Flatten the negation into prose:
  1. "The embeddings didn't change. The index didn't change. The graph just remembered what went wrong, and stopped sending her there."
  2. "Nothing retrained. Nothing re-embedded. The graph adjusted two integers and stopped repeating the mistake."
  3. Keep the joke but break the staccato: "No retraining was involved, and no re-embedding. Just good, old-fashioned re-membering." (Loses energy; option 1 or 2 is better.)

  **Severity:** Medium. Line 29 is a clear pattern. Line 27 is borderline within narrative context.

---

**R8 -- Tricolon / rhythmic enumeration (apply ESCALATION TEST)**

- **Line 13:** `"You embed documents, build an index, and retrieval quality is fixed."`
  Three-item list. Escalation test: embed (data prep) -> build index (infrastructure) -> quality is fixed (consequence). Third item shifts from action to outcome. **PASSES** the escalation test. Each clause adds a different dimension.

- **Line 27:** `"Same agent, same neighborhood, same question"`
  Tricolon with "same" anaphora. Escalation test: agent (actor) -> neighborhood (place) -> question (intent). The three items establish "nothing changed except the graph." **PASSES** -- each anchors a different variable held constant.

- **Line 200:** `"Two integer increments per edge per feedback event, sub-microsecond, and it doesn't touch embeddings, the index, or the LLM."`
  This sentence contains a nested tricolon: "embeddings, the index, or the LLM." Escalation test: embeddings (data) -> index (structure) -> LLM (compute). Each is a progressively more expensive component. **PASSES** the escalation test.

- **Line 262:** `"The first 10 signals move edges from maximum uncertainty to reasonable confidence. By 50, the graph has a usable model of which paths matter. By 200, edge weights are well-separated."`
  Tricolon across three sentences: 10 -> 50 -> 200. Escalation test: uncertainty resolved -> usable model -> well-separated. Each is a genuine milestone on the convergence curve. **PASSES.**

- **Line 3 (description):** `"How Thompson Sampling, edge weight adjustment, and Personalized PageRank compose into a retrieval system..."`
  Tricolon matching the article's three sections. This is a structural enumeration, not a rhythmic one. **PASSES.**

  **Verdict:** All tricolons pass the escalation test. No violations.

  **Severity:** None. Clean.

---

**R17 -- Hedging with "not" lists / leading with negative**

- **Line 29:** `"No retraining. No re-embedding."`
  Two consecutive negation sentences. The point is positive (the graph learned from feedback), but the argument is made through what DIDN'T happen.

  This overlaps with the R7 flag above. The "No X. No Y." pattern is both staccato marketing copy AND a negation-first framing.

  **Fix direction:** Same as R7 fix: lead with what DID happen, then note what didn't:
  1. "The graph adjusted two integers and stopped repeating the mistake. No retraining. No re-embedding." (Positive first, negation as afterthought.)
  2. "Nothing was retrained or re-embedded. The graph re-membered, and stopped sending her there."

  **Severity:** Medium. Two negation fragments in sequence.

---

**R19 -- Promotional puffery**

- **Line 190:** `"The wild part: you never have to decide how adventurous to be."`
  "The wild part" is an evaluative frame. It tells the reader how to feel about the math instead of letting the math speak for itself. This is soft puffery: not "groundbreaking" or "remarkable," but it's the author editorially inflating the significance of a mathematical property.

  **Fix direction:**
  1. Drop the editorial frame entirely: "You never have to decide how adventurous to be. Flat curves naturally produce surprising rolls sometimes..."
  2. Replace with a concrete observation: "The useful side effect: you never have to decide how adventurous to be."
  3. "Here's what falls out of the math: you never have to decide how adventurous to be."

- **Line 264:** `"**Feedback history** forms a moat you can't reproduce by simply poaching users."`
  "Moat" is VC/business puffery vocabulary. In a technical walkthrough, this reads as a pitch to investors rather than an explanation to engineers. The bolding of "Feedback history" amplifies the promotional register.

  **Fix direction:**
  1. "Feedback history is not transferable. A competing deployment with the same data and embeddings doesn't have the edge weight history, and can't replicate the retrieval characteristics."
  2. "Feedback history is cumulative and deployment-specific. You can copy the data; you can't copy the learned paths."
  3. Cut the sentence entirely. The prior sentence ("A qortex graph running in production for months has retrieval characteristics that a fresh deployment can't replicate") already makes the point without business jargon.

  **Severity:** Medium. "The wild part" is minor. "Moat" is a register violation in a technical article.

---

**R22 -- Wall-of-text paragraphs (5+ sentences / 3+ independent beats)**

- **Line 15:** `"qortex adds a feedback loop. Every query can generate a signal. That signal adjusts edge weights in the knowledge graph. The next query for similar concepts benefits. Over time, retrieval shifts because the graph updated which paths it trusts, not because you re-embedded anything."`
  Five sentences, one paragraph. Four independent beats:
  1. qortex adds feedback (capability claim)
  2. Query generates signal (mechanism)
  3. Signal adjusts edges (how it propagates)
  4. Next query benefits (consequence)
  5. Over time, retrieval shifts (long-term effect)

  Beats 2-3 are tightly coupled (signal generation -> signal propagation), but beats 1, 2-3, 4, and 5 are four distinct ideas compressed into a single visual block. The reader's eye has no landing point.

  **Fix direction:** Break after the mechanism (sentence 3) and before the time-scale shift (sentence 5):

  > qortex adds a feedback loop. Every query can generate a signal. That signal adjusts edge weights in the knowledge graph.
  >
  > The next query for similar concepts benefits. Over time, retrieval shifts because the graph updated which paths it trusts, not because you re-embedded anything.

  **Severity:** High. This is the article's thesis paragraph and the reader's first encounter with the core mechanism. Five sentences without a breath mark buries the payoff.

- **Line 25:** `"She let the agent know, with words only humans know. The agent, to its credit, noticed, in the manner only machines understand: It adjusted two integers on the graph edges that led to its mistake result, weakening the path from 'Vet' to 'military retail' and strengthening the path to 'animal care.'"`
  One long compound sentence after a short opener. Two beats:
  1. Human gives feedback (colorfully)
  2. Machine processes it (technically, with two sub-operations)

  This is borderline. The colon usage is correct Pelekification (earned continuation). But the second sentence has three independent clauses joined by comma-conjunction: "adjusted two integers" + "weakening the path" + "strengthening the path." The sentence is 52 words long and carries two parallel participial phrases.

  **Fix direction:** Break after the colon's payoff, letting the weakening/strengthening pair stand as their own visual unit:

  > She let the agent know, with words only humans know. The agent, to its credit, noticed, in the manner only machines understand: it adjusted two integers on the graph edges that led to its mistake result.
  >
  > Weakening the path from "Vet" to "military retail." Strengthening the path to "animal care."

  Or keep as one paragraph but tighten: "It adjusted two integers on the relevant edges: weakened 'Vet' to 'military retail,' strengthened 'Vet' to 'animal care.'"

  **Severity:** Low-medium. Not a wall, but the sentence is load-bearing and would breathe better with a break.

- **Line 55:** `"The trick: instead of always picking the restaurant with the higher average (Chinese, forever), you *sample* from both distributions. The Chinese place reliably rolls a 6 or 7. The Indian place, because its curve is so wide, occasionally rolls a 9. On those nights, you try it. If it's great, its curve tightens around 'great.' If it's terrible, its curve tightens around 'terrible.' Either way, you learned something, and you didn't need a rule that says 'try something new 20% of the time.' The uncertainty itself was the exploration strategy."`
  **Eight sentences, one paragraph.** Five independent beats:
  1. The trick (sampling instead of argmax)
  2. Chinese place rolls predictably
  3. Indian place rolls wildly
  4. When you try it, the curve tightens either way
  5. You learned without an explicit exploration rule

  This is the article's best explanatory paragraph and it is a **wall**. The payoff sentence ("The uncertainty itself was the exploration strategy") is buried as sentence 8 of 8.

  **Fix direction:** Break into three paragraphs at the thought boundaries:

  > The trick: instead of always picking the restaurant with the higher average (Chinese, forever), you *sample* from both distributions.
  >
  > The Chinese place reliably rolls a 6 or 7. The Indian place, because its curve is so wide, occasionally rolls a 9. On those nights, you try it.
  >
  > If it's great, its curve tightens around "great." If it's terrible, its curve tightens around "terrible." Either way, you learned something, and you didn't need a rule that says "try something new 20% of the time." The uncertainty itself was the exploration strategy.

  **Severity:** High. This is the article's best teaching moment and the payoff line has zero visual weight.

- **Line 57:** `"Every connection in the graph works the same way. Each edge keeps a running tally: how many times has this path led somewhere useful, and how many times has it been a dead end? When the system needs to decide which paths to trust, it doesn't just pick the highest-scoring one. It rolls the dice, weighted by what it knows. Paths with a long track record get predictable rolls. Paths the system hasn't tried much get wild rolls, sometimes high, sometimes low, so they still get a chance to prove themselves."`
  Six sentences, one paragraph. Three beats:
  1. Each edge has a tally (mechanism)
  2. The system samples rather than takes the max (decision process)
  3. Well-known vs. untested paths behave differently (consequence)

  Another wall. The transition from restaurant analogy back to graph terminology happens mid-paragraph with no visual break.

  **Fix direction:** Break after the question (sentence 2) and before the consequence (sentence 5):

  > Every connection in the graph works the same way. Each edge keeps a running tally: how many times has this path led somewhere useful, and how many times has it been a dead end?
  >
  > When the system needs to decide which paths to trust, it doesn't just pick the highest-scoring one. It rolls the dice, weighted by what it knows.
  >
  > Paths with a long track record get predictable rolls. Paths the system hasn't tried much get wild rolls, sometimes high, sometimes low, so they still get a chance to prove themselves.

  **Severity:** High. Third consecutive dense paragraph in the Thompson Sampling section.

- **Line 270:** `"Two applications exercise this loop today. [Vindler](...) (the sandboxed agent runtime) queries qortex on every turn, uses the results, reports outcomes, and the graph updates accordingly. [Interlinear](/projects/interlinear) (adaptive language learning) will use the same mechanism to model concept mastery: morphosyntactic errors feed rejection signals, correct recall feeds acceptance signals, and the graph learns which pedagogical paths work for each learner."`
  Three sentences, but two of them are 30+ words with multiple clauses. Three beats:
  1. Two applications use this
  2. Vindler: query -> use -> report -> update
  3. Interlinear: errors -> rejections, recall -> acceptances, graph learns

  The Interlinear sentence alone contains three parallel actions joined by commas.

  **Fix direction:** Give each application its own paragraph:

  > Two applications exercise this loop today.
  >
  > [Vindler](...) (the sandboxed agent runtime) queries qortex on every turn, uses the results, reports outcomes, and the graph updates accordingly.
  >
  > [Interlinear](/projects/interlinear) (adaptive language learning) will use the same mechanism to model concept mastery: morphosyntactic errors feed rejection signals, correct recall feeds acceptance signals, and the graph learns which pedagogical paths work for each learner.

  **Severity:** Medium. Each product deserves its own breath.

  **R22 Total: 5 violations.** The Thompson Sampling section (lines 55-57) is the worst offender: three consecutive wall paragraphs.

---

**R25 -- "Not X but Y" / false dichotomy**

- **Line 15:** `"...retrieval shifts because the graph updated which paths it trusts, not because you re-embedded anything."`
  "Because X, not because Y" -- classic "not X but Y" in reverse order. The dichotomy is defensible (graph updates vs. re-embedding are genuinely different mechanisms), but the phrasing is the formulaic pattern.

  **Fix direction:**
  1. "...retrieval shifts. The graph updated which paths it trusts. The embeddings didn't change."
  2. "...retrieval shifts through edge weight updates, not re-embedding."
  3. Cut the "not because" entirely: "Over time, retrieval shifts because the graph updated which paths it trusts." The reader already knows from line 13 that static stores don't change.

  **Severity:** Low. The dichotomy is real, but the "not because" tag is redundant with the opening paragraph's premise.

- **Line 250:** `"Learning happens at the orchestration layer, not the retrieval layer."`
  Same pattern: "at X, not at Y." The distinction is real and load-bearing for the comparison section.

  **Fix direction:** This one earns its dichotomy. The article is making a precise technical distinction between where learning occurs. **Borderline pass.**

- **Line 252:** `"Designed for corpus summarization, not online agent retrieval."`
  Same pattern again: "for X, not Y."

  Three instances of "X, not Y" in the comparison section (lines 250, 252, 256 by implication) create a rhythmic repetition of the same structural template across consecutive paragraphs. Even if each individual instance is defensible, the cumulative effect reads as a formula.

  **Fix direction:** Vary the construction across the three comparisons. Keep one "X, not Y," rewrite the others:
  1. Line 250: "Learning happens at the orchestration layer. The archival search itself (vector similarity over pgvector) is static." (Already says this in the next sentence -- merge.)
  2. Line 252: "Designed for corpus summarization. There's no runtime feedback mechanism."

  **Severity:** Low individually. Medium collectively across the comparison section.

---

**R26 -- Restating the obvious / redundancy**

- **Line 242:** `"The embeddings are unchanged. The vector index is unchanged."`
  This restates what was already said on line 200 ("it doesn't touch embeddings, the index, or the LLM") and is the same point as line 15 ("not because you re-embedded anything"). By line 242, the reader has been told three times that the embeddings don't change.

  **Fix direction:**
  1. Cut entirely. The sentence after it ("But the next similar query will traverse different paths...") is the interesting claim. Let it stand alone.
  2. If keeping, compress: "Same embeddings, same index. Different traversal paths."

- **Line 256:** `"qortex targets the gap between all of these: runtime retrieval quality that changes from feedback, without re-embedding or LLM calls."`
  This restates the thesis from line 15, the mechanism from line 200, and the comparison-section setup. The description "runtime retrieval quality that changes from feedback" is a near-verbatim echo of "a retrieval system that updates itself from usage" (line 3, frontmatter description).

  **Fix direction:**
  1. Cut. The comparison section's individual entries already make the case by contrast.
  2. If keeping, sharpen to something the reader hasn't heard yet: "qortex is the only system in this list where retrieval quality changes after deployment without an LLM call." This adds the "only" specificity.

  **Severity:** Medium. The article tells the reader "embeddings don't change" at least four times (lines 15, 200, 242, 256 by implication). The repetition dilutes rather than reinforces.

---

### Rules with CLEAN PASSES

| Rule | Status |
|------|--------|
| R2 -- AI blocklist words | PASS. No "crucial," "delve," "landscape," "showcase," "enhance," "pivotal," "tapestry," etc. |
| R3 -- Performative honesty | PASS. No "to be honest," "frankly," etc. |
| R4 -- Self-referential pivots | PASS. No "but that's not what this article is about." |
| R5 -- Inflated significance framing | PASS. No "this changes everything" language. |
| R6 -- Hedging then inflating | PASS. |
| R9 -- Rhythmic parallel closers | PASS. The article ends with "Stay tuned." which is a soft closer but not a participial chain or rhythmic parallel. (Flagged separately as staleness concern below.) |
| R10 -- Challenges-and-future-prospects | PASS. "Open Questions" is honest and grounded, not the formulaic "challenges and exciting future prospects." |
| R11 -- Elegant variation | PASS. "qortex" used consistently. "The system," "the graph" refer to different scopes accurately. |
| R12 -- Copula avoidance | PASS. No "serves as," "functions as" constructions. |
| R13 -- Dismissive 'with' framing | PASS. |
| R14 -- Vague attribution | PASS. All claims are attributed to specific systems or linked. |
| R15 -- False ranges | PASS. "10 signals... 50... 200" is a real empirical range. |
| R16 -- Superficial participle analysis | PASS. The participial phrases on line 25 ("weakening..." / "strengthening...") describe concrete actions, not superficial analysis. |
| R18 -- Colon-into-bold-statement | PASS. Line 43 ("**Thompson Sampling** is one way to make it work") is bold-as-term-introduction, not bold-as-rhetorical-hammer. |
| R20 -- Notability assertion | PASS. No "why this matters" section. |
| R21 -- Blunt fragment negation | PASS. "No retraining. No re-embedding." is handled under R7/R17. |
| R23 -- Full-clause linking | PASS. No "which means that" connectors. |
| R24 -- Mirrored affirmation pairs | PASS. No "X is real. So is Y." constructions. |
| R27 -- Bare conjunction paragraphs | PASS. No standalone "And," "But," "So" paragraphs. |
| R28 -- Emotional cliche templates | PASS. No "a mix of X and Y" templates. |

---

### Bragi Scan Summary

| Rule | Status | Location |
|------|--------|----------|
| R1 | VIOLATION (x4) | Lines 33-35, 213: em dashes as separators and in blockquote |
| R7 | VIOLATION | Line 29: "No retraining. No re-embedding. Just..." staccato marketing |
| R17 | VIOLATION | Line 29: Two consecutive negation fragments (overlaps R7) |
| R19 | VIOLATION (x2) | Line 190: "The wild part" / Line 264: "moat" -- promotional register |
| R22 | VIOLATION (x5) | Lines 15, 25, 55, 57, 270: wall paragraphs with 3+ beats |
| R25 | VIOLATION (x2) | Lines 15, 252: "not because" / "not Y" false dichotomy pattern; cumulative in comparison section |
| R26 | VIOLATION (x2) | Lines 242, 256: "embeddings unchanged" repeated 3-4x across article |

**Total: 16 violations across 7 rules.**

---

## Pass 2: Pelekification Check

### Line breaks as breath marks

**VIOLATION (high priority).** Multiple locations need decomposition (detailed in R22 above):
- Line 15: thesis paragraph needs a breath after the mechanism description
- Line 55: best teaching moment is an 8-sentence wall; needs three breaks
- Line 57: another 6-sentence wall immediately following

The Thompson Sampling section (lines 45-59, post-widget lines 186-190) has the worst breath-mark density in the article. Three consecutive wall paragraphs with no visual relief.

**Good examples of breath marks already present:**
- Line 13 vs. line 15: opening paragraph is clean, one concept per paragraph
- Lines 21-29: the vet vignette uses short paragraphs effectively
- Line 186-188: post-widget walkthrough has good paragraph sizing

### Colon extension for earned continuation

**Strong usage throughout:**
- Line 25: `"...in the manner only machines understand: It adjusted two integers..."` -- Colon earns the mechanical explanation after the human/machine contrast. Excellent.
- Line 47: `"The other question: where's worth it to eat?"` -- Clean.
- Line 53: `"In Thompson Sampling terms: the Chinese place is Beta(14, 5)"` -- Sets up the concrete mapping.
- Line 55: `"The trick: instead of always picking..."` -- Earns the explanation.
- Line 186: `"both sliders at 1. That's the restaurant you've never been to."` -- Period instead of colon here; colon would be more precise since the second sentence explains the first. Minor.
- Line 270: `"...model concept mastery: morphosyntactic errors feed rejection signals..."` -- Colon earns the decomposition.

**No violations.** The article uses colons well and frequently. One minor opportunity on line 186.

### Ellipsis for trailing thought

- Line 49: `"Maybe?..."` -- Ellipsis used correctly for trailing uncertainty. Good.
- Line 23: `"...Nor amused at the circumstances."` -- Ellipsis used for dramatic pause in the vet story. Acceptable within narrative voice.
- Line 202: `"The updated weights feed into the next stage..."` -- Ellipsis used as a forward pointer to the next section. Good Pelekification: the trailing dot signals "keep reading."

**No violations.** Ellipsis usage is natural and purposeful.

### Semantic punctuation

- Line 39: `"An agent retrieves the wrong context and gives a bad answer; the user corrects it."` -- Semicolon correctly joins parallel actions (agent acts; user reacts). Good.
- Line 49: `"One hits the spot; the other's probably better."` -- Semicolon correctly connects parallel evaluations. Good.
- Line 53: `"You know what you're getting; a solid 7/10."` -- Semicolon introduces a clarification. Correct usage.

**MINOR OPPORTUNITY:**
- Line 242: `"The embeddings are unchanged. The vector index is unchanged."` -- These are parallel statements; if kept (rather than cut per R26), they should be joined with a semicolon: "The embeddings are unchanged; the vector index is unchanged."

### Bold for argumentative weight, not decoration

- Line 41: `"That's **learning**"` -- Bold on a single word carrying the definitional weight of the section. Correct usage.
- Line 43: `"**Thompson Sampling** is one way to make it work."` -- Bold as term introduction. Standard and appropriate.
- Line 207: `"**Personalized PageRank (PPR)**"` -- Term introduction. Fine.
- Line 264: `"**deployment duration matters**"` and `"**Feedback history**"` -- Two bold phrases in one paragraph. "Deployment duration matters" is an evaluative claim bolded for emphasis; the bolding is doing rhetorical work the sentence should handle. "Feedback history" is a term introduction.

  **Fix direction (line 264):** Drop the bold on "deployment duration matters." The sentence is already standalone and clear. If emphasis is needed, restructure: "A qortex graph running in production for months has retrieval characteristics that a fresh deployment can't replicate. Deployment duration is the variable, not data volume."

**Severity:** Low. One instance of decorative bolding on line 264.

### Semicolons for parallel actions

The article uses semicolons well in several places (lines 39, 49, 53). No violations. One opportunity on line 242 (see above).

---

## Pass 3: Staleness Check

### Time-relative phrases

- **Line 23:** `"Last month, the agent sent her to The Vet"` -- This is inside the vet narrative vignette, which is a fictional/illustrative scenario. "Last month" is part of the story's internal timeline, not a claim about real events. **Not a staleness risk.**

- **Line 278:** `"Stay tuned."` -- Soft time-relative phrase. It implies the distributed layer article is forthcoming. If the article is already published by the time this one goes live, "Stay tuned" is stale. If it never ships, "Stay tuned" is a broken promise.
  **Fix direction:** Replace with a definite forward reference or remove the temporal implication:
  1. "That data will come from the [distributed layer](/writing/two-ships-qortex-distributed)."
  2. "The distributed layer is designed to answer that question." (Removes the "stay tuned" without promising a timeline.)
  3. Cut "Stay tuned." entirely. The link already points forward.

  **Severity:** Medium. "Stay tuned" is the most common stale phrase in technical blogs.

### Test count references

- **Line 272:** `"2,041 tests pass across the qortex suite. 933 pass across Vindler."`
  These numbers will go stale as soon as either test suite changes. They're doing credibility work (proving the system runs in production), but the specific counts will be wrong within weeks.

  **Fix direction:**
  1. Round: "Over 2,000 tests pass across qortex. Over 900 across Vindler." (Still stales, but more slowly.)
  2. Link to CI badges or a live status page instead of hardcoding numbers.
  3. Remove the numbers and keep the claim: "The feedback loop runs in production on real interactions across both projects, not just benchmarks." The assertion is the interesting part; the exact count is noise.

  **Severity:** Medium. These will be wrong soon.

### Price / version references
- None found. Clean.

### Technology references
- ChromaDB, Pinecone, Qdrant, Weaviate, mem0, MemGPT/Letta, Microsoft GraphRAG, LangGraph/LangChain -- All active as of March 2026. The MemGPT-to-Letta rename is already reflected. No immediate staleness, but this comparison section is the highest-maintenance part of the article: any of these projects could ship a feedback feature and invalidate a claim.
  **Recommendation:** Add an MDX comment at the top of the comparison section: `{/* STALE CHECK: Verify comparison claims quarterly. Last verified: 2026-02-13 */}`

### Link rot risk
- `/writing/qortex-integration-benchmarks` (line 276): Internal link. Depends on this article existing.
- `/writing/two-ships-qortex-distributed` (line 278): Internal link. Depends on this article existing.
- `/projects/interlinear` (line 270): Internal link.
- `https://peleke.github.io/openclaw/` (line 270): External link to GitHub Pages. Medium risk if the repo moves.
- All comparison section links are to product homepages. Low risk.

### Thesis staleness
- The core thesis (feedback loops in retrieval are better than static indexes) is durable. The comparison section is the perishable part.

### Staleness Verdict
Two concrete risks: "Stay tuned" (line 278) and the hardcoded test counts (line 272). The comparison section needs periodic verification. The rest is architecturally durable.

---

## Pass 4: Voice Analysis (brief)

### Register A -- Frustrated Engineer / Mickens
Present in the vet vignette (lines 21-29). "She let the agent know, with words only humans know" is good sardonic voice. "Being new to Austin, she was neither suspicious of the incorrect address...Nor amused at the circumstances" -- good wry humor.

Absent from the technical sections (lines 37-59, 192-216). The Thompson Sampling explanation and the comparison section are precise but flat. No opinion, no frustration, no color.

### Register B -- Self-Deprecating Narrator / Sedaris
Present. The vet story has genuine voice. The mathematician joke (line 51: "even *mathematicians*, often observed going days eating nothing but chalk and abstractions") is excellent Register B. The restaurant analogy (lines 47-55) is the article's voice high point.

### Register C -- Tour Guide / Paul Ford
Dominant register for the technical sections. The widget walkthrough (lines 186-190) is good tour-guide voice: "both sliders at 1," "slide alpha to 11," "Now watch what happens."

### Voice Verdict
The article has two distinct voice zones: the vet vignette (strong Register A/B) and the technical walkthrough (clean Register C). The comparison section (lines 244-256) is the flattest: it reads like a product matrix, not prose. The convergence section (lines 258-266) would benefit from one sentence of opinion or one concrete anecdote.

---

## Consolidated Summary

| Category | Count | Key Issues |
|----------|-------|------------|
| R1 (em dashes) | 4 instances | Lines 33-35 (list separators), line 213 (blockquote) |
| R7 (punchy fragments) | 1 violation | Line 29: "No retraining. No re-embedding. Just..." |
| R17 (negation-first) | 1 violation | Line 29 (overlaps R7): consecutive negative fragments |
| R19 (puffery) | 2 violations | Line 190: "The wild part" / Line 264: "moat" |
| R22 (wall paragraphs) | 5 violations | Lines 15, 25, 55, 57, 270: the Thompson Sampling section is the worst offender |
| R25 (false dichotomy) | 2 violations | Lines 15, 252: cumulative "not X" pattern in comparison section |
| R26 (redundancy) | 2 violations | Lines 242, 256: "embeddings unchanged" said 3-4 times |
| Pelekification gaps | 2 | Breath marks (high), decorative bold (low) |
| Staleness risks | 3 | "Stay tuned" (L278), test counts (L272), comparison section shelf life |

**Total: 17 violations across 7 Bragi rules + 2 Pelekification gaps + 3 staleness risks.**

---

## Prioritized Fix List

### Critical (fix before publish)

1. **R22 -- Break the Thompson Sampling walls (lines 55, 57).** The 8-sentence paragraph at line 55 is the article's best teaching moment and its payoff sentence ("The uncertainty itself was the exploration strategy") has zero visual weight. The 6-sentence paragraph at line 57 immediately follows with no relief. Break both into 2-3 paragraphs at thought boundaries. This is the single highest-impact change.

2. **R22 -- Break the thesis paragraph (line 15).** Five sentences, four beats, no breath mark. The reader's first encounter with the core mechanism is a wall. Break after sentence 3 (mechanism described) so the consequence ("next query benefits") starts a new paragraph.

3. **R26 -- Kill the redundancy at line 242.** "The embeddings are unchanged. The vector index is unchanged." is the third or fourth time the article says this. Cut entirely or compress to "Same embeddings, same index" as a dependent clause: "Same embeddings, same index, but different traversal paths."

### Major (fix for quality)

4. **R7 + R17 -- Rework line 29.** "No retraining. No re-embedding. Just..." is staccato marketing + negation-first. Lead with what happened: "The graph adjusted two integers and stopped repeating the mistake. Nothing was retrained or re-embedded."

5. **R19 -- Cut "moat" from line 264.** Either cut the sentence (the prior sentence already makes the point) or replace with technical language: "Feedback history is cumulative and deployment-specific. You can copy the data; you can't copy the learned paths."

6. **R22 -- Break line 270 (The Production Loop).** Give Vindler and Interlinear their own paragraphs. Each product deserves its own breath.

7. **Staleness -- Replace "Stay tuned" on line 278.** Replace with a definite forward reference or cut entirely. "Stay tuned" is the most common stale phrase in technical blogs and dates the article immediately.

8. **Staleness -- Soften test counts on line 272.** Either round the numbers, link to a live status indicator, or remove the specific counts and keep the production-running claim.

### Minor (nice to have)

9. **R1 -- Replace em dashes on lines 33-35 with colons.** The list separators work fine with colons and match the article's existing colon-extension style.

10. **R19 -- Rephrase "The wild part" on line 190.** Drop the editorial frame or replace with a concrete observation: "The useful side effect:" or just start the sentence with "You never have to decide how adventurous to be."

11. **R25 -- Vary the "not X" constructions in the comparison section (lines 246-256).** Three consecutive paragraphs use the same "X, not Y" template. Keep one, rewrite the others to break the formula.

12. **R26 -- Evaluate whether line 256 is needed.** "qortex targets the gap between all of these" restates the thesis. The comparison section entries already make the case by contrast. Consider cutting or sharpening to something the reader hasn't heard: "qortex is the only system in this list where retrieval quality improves after deployment without an LLM call."

13. **Pelekification (bold) -- De-bold "deployment duration matters" on line 264.** The sentence is already standalone. Bold the operative term if anything: "Deployment **duration** is the variable."

14. **R1 -- Rewrite the em dash on line 213.** Replace with a period-new-sentence or colon inside the blockquote.

---

## Strongest Assets (preserve these)

- **The vet vignette (lines 21-29).** Best voice in the article. "She let the agent know, with words only humans know" is memorable and human. The story grounds abstract math in a concrete, funny scenario.
- **The restaurant analogy (lines 47-55).** Strong Register B/C blend. The mathematician joke lands. The analogy is genuinely useful for understanding Thompson Sampling.
- **The interactive Beta widget.** A working demonstration that lets the reader build intuition by manipulation. Rare in technical writing. High value.
- **"The uncertainty itself was the exploration strategy" (line 55).** Best sentence in the article. Give it visual weight.
- **The colon usage throughout.** The article uses colons consistently and well for earned continuation. This is strong Pelekification.
- **The comparison section's specificity.** Token counts for MemGPT (16,900), named products with links, precise descriptions of where each system does and doesn't learn. This earns the argument through evidence rather than assertion.
- **Line 266:** `"Whether this convergence property produces meaningfully better retrieval in practice, across diverse domains and at scale, is an open question. The empirical evidence is early."` Honest hedging. Earns credibility by admitting what isn't proven. Do not cut or weaken this.
