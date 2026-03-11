# Bragi Review: sixteen-thousand-lines-of-wrong
# Date: 2026-03-09
# Source: article-draft skill (28-rule Bragi Prose Gate + 6-pass)
# Focus: R1, R7, R8, R17, R19, R22, R25, R26 + staleness + Pelekification

---

# Full 6-Pass Review: "16,000 Lines of Wrong"

Source: `/Users/peleke/Documents/Projects/portfolio/src/content/writing/sixteen-thousand-lines-of-wrong.mdx`

---

## Pass 1: Bragi Scan (28 Rules)

### Hard Bans (1-5)

**Rule 1 — No em dashes:**
No em dashes found anywhere in the article. PASS.

**Rule 2 — No AI blocklist words:**
Scanning for: additionally, align with, bolstered, crucial, delve, emphasizing, enduring, enhance, fostering, garner, highlight (verb), interplay, intricate/intricacies, key (adj), landscape (abstract), load-bearing, meticulous/meticulously, pivotal, showcase, tapestry (abstract), testament, underscore (verb), valuable, vibrant.
None found. PASS.

**Rule 3 — No performative honesty:**
No "being honest," "to be frank," "the truth is" constructions. PASS.

**Rule 4 — No self-referential pivots:**
No "this is where things get interesting" or "but that's not what this article is about." PASS.

**Rule 5 — No inflated significance framing:**
No "marking a pivotal moment," "setting the stage for," "evolving landscape." PASS.

### Structural Bans (6-10)

**Rule 6 — No hedging then inflating:**
PASS. No "though limited, it contributes to the broader..." pattern.

**Rule 7 — No punchy fragment marketing copy:**
- Line 21: "The idea was right: I use it every day." — Not a fragment; this is a colon extension (Pelekification-positive). PASS.
- Line 35: "The gauntlet works because it's boring." — Standalone sentence used for punch. This reads as tagline copy. **VIOLATION.**
  - Fix: Integrate into the surrounding paragraph. "The gauntlet works because it's boring: rules are explicit and deterministic." merges the tagline into the explanation via colon extension.
- Line 64: "They fed *us*. Not the extraction pipeline." — Two-fragment punch. The second fragment is blunt negation (also flagged under R21). **VIOLATION.**
  - Fix: "They fed us, not the extraction pipeline." Single sentence, comma replaces the false emphasis.

**Rule 8 — No tricolon/pentad for rhythm (ESCALATION TEST):**
- Line 19: "capture every engineering decision you make, extract patterns from the record, and enforce the good ones automatically" — Three items. Escalation test: capture (input) → extract (processing) → enforce (output). Each adds a new pipeline stage. **PASS** — escalation test satisfied; this is a genuine three-stage pipeline, not rhythmic filler.
- Line 94: "Capture decisions, make them readable, let the writing emerge from the record." — Three clauses. Escalation test: capture (input) → make readable (transform) → let writing emerge (output). Same pipeline logic. However, this sentence closes the article and the tricolon cadence is doing rhythmic work, not just architectural description. The "let the writing emerge from the record" is lyrical, not precise. **BORDERLINE VIOLATION.**
  - Fix: Consider breaking the tricolon cadence. "Capture decisions. Make them readable. The writing follows." changes the rhythm from smooth tricolon to staccato-then-declaration — but that risks R7 (punchy fragments). Better: "Capture decisions and make them readable; the writing follows from the record." Semicolon parallels the two stages and earns the conclusion.

**Rule 9 — No rhythmic parallel construction closers:**
- Lines 98-99: "The idea was right. Most of the implementation was wrong. / Wrong code teaches you the right abstractions if you pay attention to where it breaks." — The closing is two sentences that mirror the opening (line 21-23). This is a circular close (engagement-positive), not a rhythmic parallel closer. The sentences carry different ideas (admission vs. principle). **PASS.**

**Rule 10 — No challenges-and-future-prospects formula:**
No "despite challenges, the future looks promising." PASS.

### Word-Level Bans (11-15)

**Rule 11 — No elegant variation:**
- "buildlog" is consistently "buildlog." "The gauntlet" stays "the gauntlet." "qortex" stays "qortex." No thesaurus cycling. PASS.

**Rule 12 — No copula avoidance:**
No "serves as," "functions as," "acts as." PASS.

**Rule 13 — No dismissive 'with' framing:**
PASS. No features reduced to prepositional afterthoughts.

**Rule 14 — No vague attribution:**
- Line 45: "no one is doing it" — This is a sweeping claim with no source. However, it's presented as the author's own assessment (first person, profanity-laden), not attributed to unnamed experts. The annotation adds a self-aware caveat ("At time of writing, anyway. We're trying."). **Borderline PASS** — the annotation rescues it, but "no one" is strong.

**Rule 15 — No false ranges:**
PASS. No "from X to Y" false spectrums.

### Analysis Bans (16-20)

**Rule 16 — No superficial participle analysis:**
PASS. No "leveraging X, enabling Y" gerund chains.

**Rule 17 — No hedging with 'not' lists (REQUESTED FOCUS):**
- Line 23: "But wrong code is only wasted if you don't learn from where it breaks." — This is a single negation in a conditional, not a staccato "not" list. PASS.
- Line 49: "Plausible and correct are different things." — States a positive distinction. PASS.
- Line 64: "They fed *us*. Not the extraction pipeline." — This is a blunt "Not X" fragment used as emphasis. Not a hedging list, but the negation IS the structure. **Flagged under R21 instead.**
- No "Not X. Not Y. Not Z." staccato negation patterns found. PASS for R17 specifically.

**Rule 18 — No colon-into-bold-statement:**
- Line 51: "Both features shared the same flaw: they used LLM calls where **structured data** would have been **cheaper and more reliable**." — Colon introduces a clause containing bold words. The bold is on the operative terms (structured data, cheaper and more reliable), not a standalone bold declaration. The colon is doing Pelekification-positive work (earned continuation). **PASS** — the bold serves argumentative weight, not formatting crutch.

**Rule 19 — No promotional puffery (REQUESTED FOCUS):**
- No "groundbreaking," "renowned," "boasts a," "showcasing" anywhere.
- Line 35: "The gauntlet works because it's boring." — "boring" is the opposite of puffery. PASS on R19 (flagged under R7 for being a punchy fragment).
- Line 38: "Turns out the simplest part was the only part that was right." — Evaluative but self-deprecating, not promotional. PASS.
- Line 45: "No sh*t: this is f*cking hard" — Profanity as emphasis, not puffery. The claim ("this is hard") is genuine and the annotation acknowledges uncertainty. PASS.
- No puffery violations. **PASS.**

**Rule 20 — No notability assertion sections:**
No "why this matters" section. The article doesn't argue for its own importance. PASS.

### Rhythm/Structure Bans (21-28)

**Rule 21 — No blunt fragment negation:**
- Line 64: "They fed *us*. Not the extraction pipeline." — **VIOLATION.** Period-then-"Not"-fragment is exactly the banned pattern. "A review tool. Not a generator." = "They fed us. Not the extraction pipeline."
  - Fix: "They fed us, not the extraction pipeline." Comma replaces the false emphasis.

**Rule 22 — No wall-of-text paragraphs (REQUESTED FOCUS):**
- Lines 33-34: "The **gauntlet** survived. A rule-based review system where custom rules gate PRs and commits. No LLM in the loop. You define rules. The rules check your code. The rules block or pass." — 6 sentences in one paragraph. Multiple independent beats: (1) the gauntlet survived, (2) what it is, (3) no LLM, (4) you define rules, (5) rules check code, (6) rules block or pass. **VIOLATION.** The staccato sentences compound the problem — six short declarations in a row create a wall even though each sentence is short.
  - Fix: Break after "No LLM in the loop." The first beat (what survived and what it is) separates from the second beat (how it works mechanically).

- Lines 42-44: "The hard part: automatically deriving rules from experience and injecting them into the agent's context. / Taking raw decision-outcome pairs, extracting patterns, then deciding which ones earn their token cost in the next session." — 2 sentences, but the second sentence (line 43-44) is a dense reformulation of the first. These could be a single sentence. Not a wall violation per se (only 2 sentences), but R26 may apply. **Borderline PASS for R22.**

- Lines 47: "The LLM-as-judge instrumentation was a distraction. Routing every commit through a language model to 'evaluate quality' sounded good in the design doc. In practice, it added latency to every commit and produced ratings too inconsistent to learn from." — 3 sentences but one continuous argument (claim → design rationale → practical failure). This is one beat with three sentences supporting it. **PASS.**

- Line 66: "Forty-two entries over four months. Dozens became published articles. The entries are what taught us to write about this work. This very article exists because buildlog made 'write down what you did and what you learned' a mechanical habit enforced by git hooks. Once the entries existed, the writing followed." — 5 sentences. Beats: (1) scale (42 entries / 4 months), (2) outputs (dozens became articles), (3) meta-claim (taught us to write), (4) self-reference (this article exists because...), (5) causal claim (entries → writing). **VIOLATION.** 5 sentences with 4+ independent beats.
  - Fix: Break after "Dozens became published articles." The first two sentences are the data. The remaining three are the reflection on what the data means.

- Line 90: "We didn't stop running it. The friction for logging build journals was low enough that it scaled: entries became blog posts, blog posts became fodder for LinWheel distribution. The capture pipeline feeds the content pipeline feeds the distribution pipeline. No step requires starting from scratch." — 4 sentences. Beats: (1) continued use, (2) scaling mechanism, (3) pipeline chain, (4) no-from-scratch claim. **BORDERLINE VIOLATION.** The pipeline chain sentence (3) restates what sentence (2) already said with different words (see R26 below).
  - Fix: Cut sentence (3) ("The capture pipeline feeds the content pipeline feeds the distribution pipeline.") — it restates line 90's colon extension.

**Rule 23 — No full-clause linking:**
- Line 13: `[building agents that learn](/writing/agents-dont-learn)` — Link text is a descriptive clause, not the operative noun. The operative concept is "agents that learn" or just the series. **BORDERLINE VIOLATION.** The link text functions as a description, not a standalone concept.
  - Fix: "part of a series on [agents that learn](/writing/agents-dont-learn)."
- Line 58: `[Make It Look Easy](/writing/makes-it-look-easy)` — Article title as link text. This is fine; titles are proper nouns. PASS.
- Line 38: `[template](https://github.com/Peleke/buildlog-template)` — Operative noun. PASS.
- Line 55: `[qortex](https://github.com/Peleke/qortex)` — Operative noun. PASS.

**Rule 24 — No mirrored affirmation pairs:**
No "X is real. So is Y." PASS.

**Rule 25 — No "not just X, but also Y" (REQUESTED FOCUS):**
- Line 23: "But wrong code is only wasted if you don't learn from where it breaks." — This is a conditional statement using "only...if," not the "not just X but Y" pattern. PASS.
- No "not only...but also" constructions found. **PASS.**

**Rule 26 — No restating the obvious (REQUESTED FOCUS):**
- Lines 42-44: "The hard part: automatically deriving rules from experience and injecting them into the agent's context. / Taking raw decision-outcome pairs, extracting patterns, then deciding which ones earn their token cost in the next session." — **VIOLATION.** Line 43-44 restates line 42 in more technical language. The reader understood "deriving rules from experience" the first time. The second sentence adds specificity (decision-outcome pairs, token cost) that could be folded into the first.
  - Fix: Merge into one sentence. "The hard part: taking raw decision-outcome pairs, extracting patterns, then deciding which ones earn their token cost in the next session." Cuts the abstract version, keeps the concrete one.

- Lines 90 (sentence 2) and 90 (sentence 3): "entries became blog posts, blog posts became fodder for LinWheel distribution. The capture pipeline feeds the content pipeline feeds the distribution pipeline." — **VIOLATION.** Sentence 3 restates sentence 2 in abstract pipeline language. The colon extension already showed the chain (entries → blog posts → LinWheel). The reader doesn't need it re-explained as "capture pipeline feeds content pipeline feeds distribution pipeline."
  - Fix: Delete "The capture pipeline feeds the content pipeline feeds the distribution pipeline."

- Lines 98-99: "The idea was right. Most of the implementation was wrong. / Wrong code teaches you the right abstractions if you pay attention to where it breaks." — Line 98 restates the article's thesis (already stated at lines 21-23). **BORDERLINE.** This is a circular close, which is engagement-positive, but it does restate. The second sentence (line 99) adds the "pay attention" principle, which is new. The first sentence (line 98) is pure restatement.
  - Verdict: The circular close earns the restatement. The "if you pay attention to where it breaks" is the new payoff that justifies returning to the opening frame. **PASS** — earned restatement via circular close.

**Rule 27 — No bare conjunctions as standalone paragraphs:**
- Line 23: "But wrong code is only wasted if you don't learn from where it breaks." — "But" opens a sentence, not a standalone paragraph. The sentence contains a full argument. PASS.

**Rule 28 — No emotional cliche templates:**
No "a mix of X and Y," "a sense of [noun] grew," "the weight of [abstract noun]." PASS.

---

### Bragi Scan Summary

| Rule | Status | Location | Severity |
|------|--------|----------|----------|
| 7 | VIOLATION | L35: "The gauntlet works because it's boring." — punchy fragment tagline | Minor |
| 7 | VIOLATION | L64: "They fed *us*. Not the extraction pipeline." — punchy fragment pair | Minor |
| 8 | BORDERLINE | L94: "Capture decisions, make them readable, let the writing emerge from the record." — tricolon closer | Minor |
| 21 | VIOLATION | L64: "Not the extraction pipeline." — blunt fragment negation | Minor |
| 22 | VIOLATION | L33-34: 6 sentences, 4+ beats in one paragraph (gauntlet description) | Major |
| 22 | VIOLATION | L66: 5 sentences, 4+ beats in one paragraph (entries reflection) | Major |
| 22 | BORDERLINE | L90: 4 sentences with restatement creating wall effect | Minor |
| 23 | BORDERLINE | L13: "building agents that learn" — full-clause link text | Minor |
| 26 | VIOLATION | L42-44: line 43-44 restates line 42 in more technical language | Major |
| 26 | VIOLATION | L90: "The capture pipeline feeds..." restates the preceding colon extension | Minor |

**Total: 7 clear violations across 5 rules (R7, R21, R22, R26), plus 3 borderline findings (R8, R22, R23).**

---

## Pass 2: Staleness Check (Requested)

### Time-Relative Phrases

No instances of "recently," "last week," "just shipped," "right now," or "currently" found in the article body.

- Line 45: "no one is doing it" with annotation "At time of writing, anyway." — The annotation itself is a time-relative hedge. **STALE RISK.** If someone ships adaptive context engineering before this article ages out of relevance, the claim becomes false.
  - Mitigation: The annotation handles this gracefully. Low urgency.

- Line 38: "The gauntlet still runs. The template is at v0.20.0 and still shipping updates." — **STALE RISK.** "v0.20.0" will become outdated as soon as a new version ships. "Still runs" and "still shipping updates" are time-relative.
  - Fix: Drop the version number. "The gauntlet still runs" is defensible as an evergreen claim if the template is actively maintained. Or: "The template has been shipping updates since [month]." gives a start date instead of a current state.

- Line 47: "sounded good in the design doc" — Past tense, no staleness risk.
- Line 55: "The qortex architecture exists because of what buildlog got wrong." — Present tense, evergreen. PASS.

### Staleness Summary

| Element | Risk | Fix |
|---------|------|-----|
| "v0.20.0" (L38) | **High** — goes stale on next release | Drop version number or use "20+ releases" |
| "no one is doing it" (L45) | **Medium** — annotation mitigates | Acceptable as-is; monitor |
| "still shipping updates" (L38) | **Low** — defensible while true | Acceptable |
| Internal article links | **Medium** — `/writing/makes-it-look-easy`, `/writing/vindler-learns-linkedin` must resolve | Verify these articles exist |

---

## Pass 3: Pelekification Audit (Requested)

### Line Breaks as Breath Marks

- Lines 17-23:
  ```
  [buildlog](url) was the exploration.

  16,000 lines of Python. The project started as a question...

  The idea was right: I use it every day.
  Most of the implementation was...Experimental.
  But wrong code is only wasted if you don't learn from where it breaks.
  ```
  Line 17: "was the exploration." gets its own line after the link. **GOOD.** The break is the emphasis.
  Lines 21-23: Three standalone lines, each carrying weight. "The idea was right" / "Most of the implementation was...Experimental" / "But wrong code is only wasted..." — **EXCELLENT.** Each line breathes. The ellipsis performs the hesitation. The capitalized "Experimental" after the ellipsis adds a visual beat. This is Pelekification at its best.

- Line 64: "They fed *us*. Not the extraction pipeline." — The line break before this gives it breath, but the blunt "Not" fragment (R21 violation) undermines the Pelekification. The italic on "us" is correct (bold for weight, italic for voice inflection). Fix the fragment; keep the breath mark.

### Colon Extension

- Line 21: "The idea was right: I use it every day." — **EXCELLENT.** The colon says "and here's the proof." Textbook colon extension.
- Line 42: "The hard part: automatically deriving rules..." — **GOOD.** Colon introduces the definition.
- Line 45: "No sh*t: this is f*cking hard" — **GOOD.** Colon extends the exclamation into the claim.
- Line 51: "Both features shared the same flaw: they used LLM calls where..." — **GOOD.** Colon delivers the verdict.
- Line 90: "...low enough that it scaled: entries became blog posts, blog posts became fodder..." — **GOOD.** Colon chains the scaling evidence.

Colon usage is strong throughout. No missed opportunities for colon extension detected.

### Ellipsis for Trailing Thought

- Line 22: "Most of the implementation was...Experimental." — **EXCELLENT.** The ellipsis performs the hesitation. The capitalized "Experimental" after the pause is a deliberate choice that reads as self-correction. This is the best single line in the article.

No other ellipsis usage. No missed opportunities — the article's tone is more direct than hesitant, so one ellipsis is the right density.

### Semantic Punctuation

- Colon usage: See above. Consistently used for explanation and proof delivery. GOOD.
- Semicolon usage: **ABSENT.** The article has zero semicolons. There are places where semicolons would serve parallel actions:
  - Line 19 could use a semicolon: "capture every engineering decision you make; extract patterns from the record; enforce the good ones automatically" — semicolons would emphasize the parallel pipeline stages better than commas.
  - Line 56: "Thompson Sampling replaced LLM-based evaluation. Instead of LLM-summarized patterns, we used structured decision-outcome pairs." — These are parallel corrections. A semicolon would bind them: "Thompson Sampling replaced LLM-based evaluation; structured decision-outcome pairs replaced LLM-summarized patterns."
  - **RECOMMENDATION:** Add 1-2 semicolons where parallel actions exist. The article currently relies exclusively on periods and colons.

- Period vs. colon: Generally correct. No places where a colon should replace a period.

### Bold for Weight, Not Decoration

- Line 33: "The **gauntlet** survived." — Bold on the subject noun. This is definitional bold (introducing a term), not argumentative weight. Acceptable but not Pelekification-positive. Could be italic instead (introducing a term the reader hasn't seen).
- Line 51: "**structured data** would have been **cheaper and more reliable**" — **EXCELLENT.** The bold words are exactly where the reader's eyes need to land. "Structured data" is the alternative. "Cheaper and more reliable" is the verdict. This is bold as argumentative weight.
- No instances of decorative bold (bolding headers-in-prose or every noun). PASS.

### Annotations as Cross-References

- Line 45: `<Annotation note="At time of writing, anyway. We're trying.">` with link to `/writing/context-engineering-not-copywriting` — **GOOD.** Cross-references across articles without interrupting flow.
- Line 47: `<Annotation note="...motivates qortex...">` — **GOOD.** Connects to the qortex project with rationale.
- Annotation density is appropriate (2 annotations in a ~100-line article).

### Missing Pelekification Opportunities

1. **No blockquote dialogue.** The article has no quoted speech or internal monologue. Line 19 could benefit from a blockquote framing the original question: "> What if you could capture every engineering decision you make?" — this would give the founding question visual weight.

2. **No typographical weight escalation at pivots.** The article transitions from "What Survived" to "The Shape of the Thing" (line 92) without any weight escalation. The pivot from "what worked / what didn't" to "what we learned" could use italic, blockquote, or a heavier visual marker.

---

## Consolidated Findings

### Summary

| Check | Result |
|-------|--------|
| Bragi violations | 7 violations, 3 borderline |
| Staleness risks | 2 (version number, time-relative "still") |
| Pelekification | Strong in lines 17-23 and 51; weak on semicolons and weight escalation |
| Em dashes (R1) | CLEAN |
| Punchy fragments (R7) | 2 violations |
| Tricolon (R8) | 1 borderline |
| Hedging 'not' lists (R17) | CLEAN |
| Puffery (R19) | CLEAN |
| Wall paragraphs (R22) | 2 violations, 1 borderline |
| "Not X but Y" (R25) | CLEAN |
| Restatement (R26) | 2 violations |

---

## Prioritized Fix List

### Priority 1: Fix Now (structural issues that weaken the piece)

**1. R22 — Break the gauntlet wall paragraph (lines 33-34)**
- Current: "The **gauntlet** survived. A rule-based review system where custom rules gate PRs and commits. No LLM in the loop. You define rules. The rules check your code. The rules block or pass."
- Fix: Break after "No LLM in the loop." First paragraph = what survived and what it is. Second paragraph = how it works mechanically.
- Why: 6 sentences in one block. The staccato creates a wall even though each sentence is short. The reader's eye needs a breath mark at the mechanism shift.

**2. R22 — Break the entries reflection paragraph (line 66)**
- Current: "Forty-two entries over four months. Dozens became published articles. The entries are what taught us to write about this work. This very article exists because buildlog made 'write down what you did and what you learned' a mechanical habit enforced by git hooks. Once the entries existed, the writing followed."
- Fix: Break after "Dozens became published articles." Data (first 2 sentences) separates from reflection (last 3 sentences).
- Why: 5 sentences, 4+ independent beats. The data and the reflection are different thoughts that need their own visual unit.

**3. R26 — Kill the restatement at lines 42-44**
- Current: "The hard part: automatically deriving rules from experience and injecting them into the agent's context. / Taking raw decision-outcome pairs, extracting patterns, then deciding which ones earn their token cost in the next session."
- Fix: Merge into one sentence: "The hard part: taking raw decision-outcome pairs, extracting patterns, then deciding which ones earn their token cost in the next session."
- Why: Line 43-44 says the same thing as line 42 with different words. Cut the abstract version, keep the concrete one.

### Priority 2: Fix for Quality

**4. R26 — Kill the pipeline restatement (line 90)**
- Current: "...entries became blog posts, blog posts became fodder for LinWheel distribution. The capture pipeline feeds the content pipeline feeds the distribution pipeline."
- Fix: Delete "The capture pipeline feeds the content pipeline feeds the distribution pipeline." The colon extension already showed the chain.
- Why: Restating the obvious. The reader followed the chain the first time.

**5. R7 + R21 — Fix the blunt fragment at line 64**
- Current: "They fed *us*. Not the extraction pipeline."
- Fix: "They fed *us*, not the extraction pipeline."
- Why: Period-then-"Not" fragment is a banned pattern (R21) and a punchy fragment pair (R7). Comma preserves the contrast without the fake emphasis.

**6. Staleness — Drop the version number (line 38)**
- Current: "The template is at v0.20.0 and still shipping updates."
- Fix: "The [template](url) is still maintained." Or drop the sentence entirely; the reader doesn't need a version number to trust the claim.
- Why: "v0.20.0" goes stale on the next release.

### Priority 3: Polish

**7. R7 — Consider softening the gauntlet tagline (line 35)**
- Current: "The gauntlet works because it's boring."
- Fix option: "The gauntlet works because it's boring: rules are explicit and deterministic." Colon extension merges the tagline into the explanation.
- Why: Standalone punchy fragment. The Pelekification-positive colon extension dissolves the R7 violation while keeping the claim.

**8. Pelekification — Add semicolons for parallel actions**
- Line 56: "Thompson Sampling replaced LLM-based evaluation. Instead of LLM-summarized patterns, we used structured decision-outcome pairs."
- Fix: "Thompson Sampling replaced LLM-based evaluation; structured decision-outcome pairs replaced LLM-summarized patterns."
- Why: Semicolons signal parallel corrections. The article currently has zero semicolons, which is a missed Pelekification opportunity.

**9. R8 Borderline — Consider breaking the closing tricolon (line 94)**
- Current: "Capture decisions, make them readable, let the writing emerge from the record."
- Fix option: "Capture decisions and make them readable; the writing follows from the record."
- Why: The tricolon cadence is doing rhythmic work at the close. Semicolon breaks the rhythm while keeping the meaning.

**10. R23 Borderline — Tighten the series link (line 13)**
- Current: "part of a series on [building agents that learn](/writing/agents-dont-learn)"
- Fix: "part of a series on [agents that learn](/writing/agents-dont-learn)"
- Why: Link text should highlight the operative concept, not the full clause.

---

## Violations by Rule Number (Quick Reference)

| Rule | Count | Lines | Quote |
|------|-------|-------|-------|
| R7 | 2 | 35, 64 | "The gauntlet works because it's boring." / "They fed *us*. Not the extraction pipeline." |
| R8 | 1 borderline | 94 | "Capture decisions, make them readable, let the writing emerge from the record." |
| R21 | 1 | 64 | "Not the extraction pipeline." (blunt fragment negation) |
| R22 | 2 + 1 borderline | 33-34, 66, 90 | Gauntlet paragraph (6 sentences), entries paragraph (5 sentences), pipeline paragraph (4 sentences with restatement) |
| R23 | 1 borderline | 13 | "building agents that learn" (full-clause link) |
| R26 | 2 | 42-44, 90 | Lines 43-44 restate line 42; "The capture pipeline feeds..." restates the colon extension |

**Rules with zero violations (from focus list):** R1, R17, R19, R25.

The article is clean on puffery (R19), hedging "not" lists (R17), em dashes (R1), and "not X but Y" (R25). Its main weaknesses are wall paragraphs (R22) and restatement (R26), which is a common co-occurrence: dense paragraphs often contain restatements because the author is unconsciously compensating for the wall by re-explaining.
