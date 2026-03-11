# Bragi Review: ax-series
# Date: 2026-03-09
# Source: article-draft skill (28-rule Bragi Prose Gate + 6-pass)



## Bragi Review: AX Series Index Page

### R1: Em Dashes (—)

**No violations found.** The text uses no em dashes. Clean.

---

### R2: Blocklist Words

**1 violation:**

- **"Not because they lack capability"** — "capability" is not on the blocklist, so this is fine.

Actually, scanning more carefully against the full blocklist:

**No violations found.** None of the 23 blocklist words appear.

---

### R7: Punchy Fragment Marketing Copy

**2 violations:**

1. **"Not UX for bots. Not prompt engineering."** — Two punchy negation fragments in sequence, functioning as marketing copy to position the concept. This also overlaps with **R21 (blunt fragment negation)**.
   - *Fix:* Fold into the surrounding sentence. E.g., "...an autonomous agent operating under hard resource constraints, which means something different from UX for bots or prompt engineering. It's the systematic study of..."

2. **"Not hallucination. Not reasoning failure. A framing failure."** — Triple punchy fragment, dramatic reveal structure. Also triggers **R21** and borders on **R8 (tricolon)**.
   - *Fix:* "The failure wasn't hallucination or reasoning. It was framing." (One sentence, keeps the punch without the copywriter cadence.)

**Severity: Medium.** These are the most AI-patterned lines in the piece.

---

### R8: Tricolon / Pentad

**2 violations:**

1. **"...how tool design, API responses, feedback loops, and system affordances shape what an agent can and will do."** — Four-item list (quadcolon). Passes the escalation test loosely (each item is more abstract), but four nouns in a row reads as catalog padding. "System affordances" is vague enough to cut.
   - *Fix:* "...how tool design, API responses, and feedback loops shape what an agent can and will do."

2. **"Not hallucination. Not reasoning failure. A framing failure."** — Tricolon (flagged above under R7). The third element is the payoff. Classic escalation-to-reveal.
   - *Fix:* See R7 fix above.

**Severity: Low-Medium.** The quadcolon is mild. The tricolon is the real offender.

---

### R19: Puffery

**1 borderline case:**

- **"The conversation that defined AX as a design discipline."** — Declaring that a single conversation "defined" a discipline is a significance claim. It's your own discipline and your own conversation, so it's less puffery than self-mythologizing, but it reads as inflated framing (**R5** overlap).
   - *Fix:* "The conversation that turned AX from an observation into a design problem." (Scopes the claim to your own thinking, not a field.)

**Severity: Low.** The rest of the page is refreshingly concrete.

---

### R22: Wall Paragraphs

**1 violation:**

- **Paragraph 2** ("The other twenty-eight aren't broken...") is 4 sentences but reads dense because of conceptual stacking. Acceptable for a lede, but the final two sentences ("The agent didn't decide against them. It never considered them. The frame never opened.") could breathe as a separate beat.
   - *Fix:* Line break before "The agent didn't decide against them."

**Severity: Low.** This is borderline. The paragraph isn't truly a wall, but splitting sharpens it.

---

### R25: "Not just X, but Y"

**No violations found.** The "not X, not Y" constructions are negation patterns (R21), not the "not just X but also Y" formula.

---

### R26: Restating the Obvious

**1 violation:**

- **"The agent didn't decide against them. It never considered them."** — These say the same thing. "Never considered" is the stronger version of "didn't decide against." Pick one.
   - *Fix:* Cut "The agent didn't decide against them." Keep "It never considered them. The frame never opened."

**Severity: Low.** But cutting tightens the lede's best moment.

---

### R21: Blunt Fragment Negation (bonus, triggered by R7 findings)

**2 violations** (same lines as R7):
- "Not UX for bots. Not prompt engineering."
- "Not hallucination. Not reasoning failure."

Fixes covered above.

---

### R5: Inflated Significance Framing (bonus)

**1 violation:**

- **"The conversation that defined AX as a design discipline."** — Covered under R19. Same fix.

---

### Pelekification Opportunities

Pelekification = making the language more concrete, more Peleke-voiced (direct, dry, technically precise, no borrowed authority).

1. **"the design of systems where the primary consumer is an autonomous agent operating under hard resource constraints"** — This is a definition sentence doing too much work. It's correct but reads like an abstract. Peleke's voice would ground it in something specific first, then generalize.
   - *Opportunity:* Lead with the constraint ("An agent has 128K tokens and no memory between sessions") then name the discipline.

2. **"Its trust isn't built over years of software keeping promises; it's evaluated per-session, from scratch, based on whether the tool demonstrated value last time."** — The semicolon construction is structurally fine, but "software keeping promises" is a metaphor doing no work. Peleke's voice prefers the mechanical explanation.
   - *Opportunity:* "Trust resets every session. The agent checks whether the tool returned useful output last time. That's the entire trust model."

3. **"A 67KB config payload that consumed 10% of her context window."** — This is already peak Peleke. Leave it. This is the standard the rest of the page should match.

4. **Description meta tag** — "From tool descriptions to feedback loops, from token budgets to channel vision." This is a parallel construction ("from X to Y, from A to B") that reads as tagline copy. For SEO/meta it's fine, but if it renders on-page, it should be flattened.

---

### Severity Summary

| Rule | Count | Severity |
|------|-------|----------|
| R7 (punchy fragments) + R21 | 2 | **Medium** |
| R8 (tricolon/quadcolon) | 2 | Low-Medium |
| R26 (restating obvious) | 1 | Low |
| R19/R5 (puffery/inflation) | 1 | Low |
| R22 (wall paragraph) | 1 | Low |

**Overall: Clean page.** The main issue is two clusters of punchy negation fragments that pattern-match to AI marketing copy. Fix those and this reads like Peleke throughout. The "67KB config payload" line and the Channel Vision summary are the voice targets for the rest of the page.