# Bragi Review: agents-dont-learn (v2)
# Date: 2026-03-09
# Source: Manual 28-rule Bragi Prose Gate + Pelekification + staleness check
# File: /Users/peleke/Documents/Projects/portfolio/src/content/writing/agents-dont-learn.mdx

---

## Article Overview

**Prose lines:** 9-24, 87 (the rest is HTML series card layout)
**Word count:** ~350 words of prose
**Function:** Series index page. Establishes thesis, then links to three series articles + four receipts.

---

## Pass 1: Bragi Scan (28 Rules)

### Violations Found

**R7 — Punchy fragment marketing copy**

- **Line 9:** `"Every agent on the market wakes up blank."`
  Standalone fragment functioning as a tagline. Identical phrasing appears in the frontmatter description (line 3), doubling the slogan effect.
  **Fix direction:** This is the opening line, so some punch is earned. The problem is the exact repetition in the description. Either differentiate the description from the opener, or expand line 9 into a complete sentence that grounds the claim: "Every agent on the market wakes up blank, and your workflow absorbs the cost."

- **Line 87:** `"Your agent wakes up blank tomorrow. The question is whether it remembers anything from today."`
  Two-sentence rhythmic closer. Better than the prior version ("It doesn't have to.") but still reads as landing-page copy. The shift from "every agent" (line 9) to "your agent" (line 87) is a good move, but "The question is whether..." is a soft, open-ended formulation that deflects rather than resolves.
  **Fix direction:** End with forward motion or a concrete image. Options:
  1. "Your agent wakes up blank tomorrow. The series below is a record of making that expensive."
  2. "Your agent wakes up blank tomorrow. These articles are the engineering log for making it stop."
  3. Cut entirely. Line 24 ("what we tried, what broke, and what survived") is a stronger natural ending for the prose section.

- **Severity:** Medium. The opener is forgivable; the closer needs work.

---

**R8 — Tricolon/pentad enumerations for rhythm**

- **Line 11:** `"your codebase, your preferences, your conventions, your past mistakes"`
  Four-item enumeration. Apply the escalation test:
  - codebase (what you built) -> preferences (how you work) -> conventions (team norms) -> past mistakes (failure history)
  Each adds a new dimension (artifact -> style -> norms -> history). **PASSES the escalation test.**

- **Line 11:** `"Every time. From scratch. Forever."`
  Tricolon. Frequency -> mechanism -> time horizon. **PASSES the escalation test.** (Noted in prior review as well.)

- **Line 21:** `"makes the same wrong tool selection, hits the same context ceiling, burns the same tokens on the same dead ends"`
  Tricolon with "the same" anaphora. Apply escalation test:
  - wrong tool selection (decision error) -> context ceiling (resource limit) -> burns tokens on dead ends (waste from repeated failure)
  Each sharpens: bad choice -> hard limit -> compounding waste. **PASSES**, though the anaphora ("the same... the same... the same...") is doing rhythmic work that borders on marketing cadence. The repetition of "the same" is the structural gimmick, not the content. Borderline.
  **Fix direction (if tightening):** Drop one "the same" to break the rhythm: "The agent makes the same wrong tool selection, hits the context ceiling again, burns tokens on dead ends it already explored."

- **Severity:** Low. All three pass the escalation test. The line 21 anaphora is the only borderline case.

---

**R14 — Vague attribution**

- **Line 13:** `"the industry is treating it like a feature gap instead of an architecture failure"`
  "The industry" is vague. Which companies? Which products? This is a claim about what other people are doing, attributed to a collective noun.
  **Fix direction:** Either name names ("Anthropic ships memory as a feature; OpenAI ships memory as a feature. Neither ships a feedback loop.") or weaken to something defensible without attribution: "The default is still stateless. Most memory features are retrieval bolted on after the fact, not feedback loops that change behavior."
  **Severity:** Medium. This is the thesis-level claim and it's unsourced.

---

**R17 — Hedging with "not" lists / leading with negative**

- **Line 15:** `"A filing cabinet doesn't learn. You don't get smarter by buying a bigger filing cabinet."`
  Two consecutive negation sentences. The point is what learning IS (behavior change from feedback), but the argument is made entirely through what it ISN'T.
  **Fix direction:** Lead with the positive claim, then use the filing cabinet as contrast:
  1. "Learning means changing what you do based on what happened last time. RAG doesn't do that. It's a filing cabinet: bigger storage, same behavior."
  2. "You get smarter by changing what you do based on what happened last time. A bigger filing cabinet doesn't get you there."
  **Severity:** Medium. Two consecutive negative sentences in a 350-word piece is a high density.

---

**R18 — Colon-into-bold-statement**

- **Line 17:** `"**Does the system make better decisions after 100 sessions than after 1?**"`
  Bold question on its own line. This is the "colon-into-bold" pattern without a literal colon: the preceding paragraph sets up a framing argument, then this line drops the bold hammer. The bold formatting is doing the work that the argument should be doing.
  **Fix direction:** Integrate into the paragraph flow. Options:
  1. Make it a non-bold sentence that follows the filing cabinet argument: "The litmus test is simple: does the system make better decisions after 100 sessions than after 1?"
  2. Keep the standalone line but drop the bold: let the content carry the weight.
  **Severity:** Medium. This is one of the article's strongest sentences, but the formatting is doing rhetorical work the words could handle alone.

---

**R22 — Wall-of-text paragraphs (multiple beats)**

- **Lines 11 (single line in source, renders as one paragraph):**
  `"Your $200/month Claude subscription. Your custom GPT. Your Cursor workspace with 47 rules files you hand-wrote because the machine can't remember what you told it yesterday. Every single one of these systems starts each session at zero. You are the memory. You are the learning loop. You re-explain your codebase, your preferences, your conventions, your past mistakes. Every time. From scratch. Forever."`

  This is one paragraph with at least **four independent beats**:
  1. The enumeration of products (Claude, GPT, Cursor) — situation
  2. "Every single one starts at zero" — the generalization
  3. "You are the memory. You are the learning loop." — the flip
  4. "You re-explain..." + "Every time. From scratch. Forever." — the cost

  Beat 3 ("You are the memory") is the strongest moment in the article and it's buried mid-paragraph.
  **Fix direction:** Break after "yesterday." and again after "learning loop." so the three beats breathe:

  > Your $200/month Claude subscription. Your custom GPT. Your Cursor workspace with 47 rules files you hand-wrote because the machine can't remember what you told it yesterday.
  >
  > Every single one of these systems starts each session at zero. You are the memory. You are the learning loop.
  >
  > You re-explain your codebase, your preferences, your conventions, your past mistakes. Every time. From scratch. Forever.

  **Severity:** High. This is the article's most important paragraph and its best line ("You are the memory") gets no visual weight.

---

**R25 — "Not just X, but also Y" / "It's not X, it's Y" (false dichotomy)**

- **Line 13:** `"treating it like a feature gap instead of an architecture failure"`
  This is the "not X but Y" variant: "instead of" performs the same rhetorical move as "not just... but also." The reader gets a binary that hasn't been earned. Why is it an architecture failure and not a feature gap? The article asserts the distinction but doesn't prove it.
  **Fix direction:** Either argue for why it's architectural (statelessness is baked into the session model, not a missing checkbox), or drop the binary and just state the claim: "The default is still stateless. The problem is architectural: the session model has no feedback path."
  **Severity:** Low-medium. The binary framing is defensible given the article's argument, but "feature gap vs. architecture failure" is doing heavy lifting without support.

---

**R26 — Restating the obvious**

- **Line 3 (description) vs. Line 9 (opener):**
  Description: `"Every agent on the market wakes up blank."`
  Line 9: `"Every agent on the market wakes up blank."`
  Verbatim repetition. The reader who sees the description and then reads the first line gets the exact same sentence twice.
  **Fix direction:** Differentiate the description. Make it a summary rather than the opening line: "Your AI tools start every session at zero. You are the memory, the learning loop, the feedback mechanism they don't have."

- **Lines 21-22:**
  `"The cost is compound: every session that starts at zero re-introduces mistakes..."` (line 21)
  `"You absorb the cost in review time. Your team absorbs it in velocity."` (line 22)
  "The cost" appears in both sentences. Line 22 restates the cost claim from line 21 using different nouns (review time, velocity). This is mild: line 22 adds specificity (individual cost vs. team cost), so it's more "sharpening" than "restating." Borderline pass.

  **Severity:** The description/opener repetition is a clear violation. The lines 21-22 pair is borderline.

---

### Rules with CLEAN PASSES

| Rule | Status |
|------|--------|
| R1 — Em dashes | PASS. Zero em dashes. |
| R2 — AI blocklist words | PASS. No "crucial," "delve," "landscape," "showcase," "enhance," "pivotal," etc. |
| R3 — Performative honesty | PASS. |
| R4 — Self-referential pivots | PASS. |
| R5 — Inflated significance framing | PASS. The prior version had "unsolved problem...almost nobody." The current version ("architecture failure") is a claim, not an inflation. |
| R6 — Hedging then inflating | PASS. Prior version fixed. |
| R9 — Rhythmic parallel closers | PASS. Line 87 is close but reads as a question rather than a participial chain. |
| R10 — Challenges-and-future-prospects | PASS. |
| R11 — Elegant variation | PASS. "Agent" is used consistently. |
| R12 — Copula avoidance | PASS. |
| R13 — Dismissive 'with' framing | PASS. |
| R15 — False ranges | PASS. "After 100 sessions than after 1" is a real range. |
| R16 — Superficial participle analysis | PASS. |
| R19 — Promotional puffery | PASS. No "groundbreaking," "renowned," etc. |
| R20 — Notability assertion | PASS. |
| R21 — Blunt fragment negation | PASS. No "Not X." standalone fragments. |
| R23 — Full-clause linking | PASS. Series card links use short descriptive text. |
| R24 — Mirrored affirmation pairs | PASS. "You are the memory. You are the learning loop." is parallel but not a mirrored affirmation ("X is real. So is Y."). These are parallel identity claims, not equipoise. |
| R27 — Bare conjunction paragraphs | PASS. |
| R28 — Emotional cliche templates | PASS. |

---

## Pass 2: Pelekification Check

### Line breaks as breath marks
- **VIOLATION (high priority).** Line 11 needs decomposition (see R22 above). "You are the memory. You are the learning loop." deserves its own visual line. Currently buried.
- Line 19 ("The answer, everywhere, is no.") is correctly isolated. Good.

### Colon extension for earned continuation
- **Line 21:** `"The cost is compound: every session that starts at zero re-introduces mistakes..."` — Good use. The colon says "here's the proof." This is correct Pelekification.
- **Line 24:** `"...the record: what we tried, what broke, and what survived."` — Good. Colon earns the enumeration.

### Ellipsis for trailing thought
- Not used. No clear opportunities in this 350-word piece. PASS (no violation, no missed opportunity).

### Semantic punctuation
- Line 22 uses period between "review time" and "Your team absorbs it in velocity." These are parallel actions; a semicolon would be more precise: "You absorb the cost in review time; your team absorbs it in velocity."
  **Fix direction:** Replace period with semicolon on line 22.

### Bold for argumentative weight, not decoration
- **VIOLATION.** Line 17: `"**Does the system make better decisions after 100 sessions than after 1?**"` — The entire question is bolded. Bold should highlight the load-bearing words, not the entire sentence. If bolding: `"Does the system make **better decisions** after 100 sessions than after 1?"` Or better: drop bold entirely and let the standalone line carry the weight.

### Semicolons for parallel actions
- Line 22 (see semantic punctuation above). "You absorb the cost in review time. Your team absorbs it in velocity." — Parallel structure with "absorb." Semicolon is the correct connector.

---

## Pass 3: Staleness Check

### Time-relative phrases
- **None found.** No "recently," "last week," "just shipped," "this month." Clean.

### Price/number references
- **Line 11:** `"$200/month"` — Claude Max pricing as of early 2026. Will go stale when pricing changes. The specific number does rhetorical work (grounds the frustration in a real dollar amount). **Recommendation: keep, flag for periodic review.** Add a comment in the MDX source: `{/* STALE CHECK: Claude Max pricing — verify quarterly */}`
- **Line 11:** `"47 rules files"` — Evergreen. Specific enough to feel real, generic enough to not date.
- **Line 17:** `"100 sessions... 1"` — Evergreen framing.

### Thesis staleness
- **Line 13:** `"the industry is treating it like a feature gap instead of an architecture failure"` — Medium risk. Anthropic, OpenAI, and Google are all shipping memory features. By mid-2026, "the industry is treating it like a feature gap" may be outdated because the industry may have shipped features that partially address the claim. The defensible version is about *architecture* (stateless session model), not about *industry neglect*.
  **Fix direction:** Tighten to: "The default is still stateless. Memory features are shipping, but retrieval isn't learning: the session model has no feedback path."

---

## Summary

| Category | Count |
|----------|-------|
| Bragi violations | 7 (R7 x2, R14, R17, R18, R22, R25, R26) |
| Pelekification gaps | 3 (breath marks, semantic punctuation, bold misuse) |
| Staleness risks | 2 ($200 pricing, industry-neglect thesis claim) |

---

## Prioritized Fix List

### Critical (fix before publish)

1. **R22 — Break the wall at line 11.** This is the article's most important paragraph and its best line ("You are the memory") is buried. Break into three paragraphs at the thought boundaries. This is the single highest-impact change. (Also addresses Pelekification: breath marks.)

2. **R18 + Pelekification (bold) — De-bold line 17.** Either integrate the question into prose flow ("The litmus test is simple: does the system make better decisions after 100 sessions than after 1?") or keep standalone but drop the full-sentence bold. Bold the operative phrase if anything: "**better decisions**."

3. **R17 — Flip the negation at line 15.** Lead with what learning IS ("changing behavior based on outcomes"), then use the filing cabinet as contrast. Two consecutive negative sentences in 350 words is too dense.

### Major (fix for quality)

4. **R14 — Ground "the industry" at line 13.** Either name specific products/companies or rephrase to avoid vague attribution. "The default is still stateless" is already strong; "the industry is treating it like..." is the weak half.

5. **R25 — Earn the binary at line 13.** "Feature gap instead of architecture failure" is a strong claim that needs one sentence of support. Why is statelessness architectural? Because the session model has no feedback path. Say that.

6. **R26 — Differentiate description from opener.** The frontmatter description (line 3) is verbatim line 9. The reader sees the same sentence twice. Rewrite the description to be a summary, not the opening line.

7. **Pelekification (semicolon) — Line 22.** Change the period to a semicolon: "You absorb the cost in review time; your team absorbs it in velocity." Parallel actions deserve parallel punctuation.

### Minor (nice to have)

8. **R7 — Rework the closer at line 87.** "The question is whether it remembers anything from today" is softer than the prior version but still reads as copy. Consider cutting it entirely (line 24 is a stronger natural ending) or replacing with a concrete forward-pointing image.

9. **R8 (borderline) — Break the anaphora at line 21.** "the same... the same... the same..." is borderline rhythmic gimmick. Consider varying one instance to break the pattern while keeping the escalation.

10. **Staleness — Tighten the thesis claim.** Reframe line 13 to be about the session model's lack of a feedback path, not about industry neglect. This makes the claim architectural (durable) rather than observational (perishable).

---

## Strongest Assets (preserve these)

- **"You are the memory. You are the learning loop."** — Best line in the piece. Give it visual weight via line break.
- **"RAG stapled to a chatbot"** — Sharp, specific, memorable.
- **"Every time. From scratch. Forever."** — Passes escalation test. Earned tricolon.
- **"47 rules files you hand-wrote"** — Specific detail that proves the author lives this.
- **"what we tried, what broke, and what survived"** (line 24) — Strong natural ending with escalation.
- **The series card layout** — Clean navigation. HTML is well-structured.
