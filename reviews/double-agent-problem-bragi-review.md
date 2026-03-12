# Bragi Review: double-agent-problem
# Date: 2026-03-09
# Source: article-draft skill (28-rule Bragi Prose Gate + 6-pass)



# Double Agent Problem — Full 6-Pass Review

---

## Pass 1: Bragi Prose Gate (28 Rules)

### Violations Found

**R1 (No em dashes):** CLEAN. No em dashes detected.

**R2 (AI vocab blocklist):** CLEAN. No blocklist words detected.

**R3 (Performative honesty):** CLEAN.

**R4 (Self-referential pivots):** One borderline case:
- "This gets worse with skill marketplaces." — Not quite "this is where things get interesting" but it's a self-referential pivot announcing escalation instead of just escalating. Mild. Consider letting the marketplace paragraph open with the concrete claim directly.

**R5 (Inflated significance framing):** CLEAN.

**R6 (Hedging then inflating):** CLEAN.

**R7 (Punchy fragment marketing copy):** Two violations:
- "That's a double agent." — Blunt fragment used as a mic-drop. This reads as marketing tagline. The sentence has earned its weight, but the fragment form undercuts it. Consider: "That's a double agent" attached to the prior sentence with a colon or semicolon. (Borderline; the naming has argumentative function, so this could survive if you accept it as definition rather than punchline.)
- "This one delivers a payload that rewrites the agent's decision policy to want more of the poison." — Not a fragment, but "want more of the poison" is a punchy closer that leans toward copy. Mild.

**R8 (Tricolon/pentad rhythm-only):** Two cases to test:
- "It's responsive; it's selecting tools; it's completing tasks." — Three parallel clauses. Escalation test: "responsive" (alive), "selecting tools" (acting), "completing tasks" (producing output). Each narrows the aperture. **Passes**, but barely. The three items are really two beats: "acting" and "producing." Consider collapsing to two.
- "They keep showing up to the office; they file reports; they attend meetings." — Escalation test: showing up (presence), filing reports (bureaucratic output), attending meetings (social performance). All three are just "they perform their role." **FAILS.** These are three instances of the same dimension (looking normal). Pick two, or collapse to one with a colon extension.

**R9 (Rhythmic parallel construction closers):** CLEAN.

**R10 (Challenges-and-future-prospects):** CLEAN.

**R11 (Elegant variation):**
- "posteriors" vs. "learned preferences" vs. "decision policy" — These refer to the same concept (the agent's learned internal state) but use three different terms. This is elegant variation. Pick one term and stick with it. "Posteriors" is the most precise; "learned preferences" is the most readable. "Decision policy" appears once and could stay if it's doing distinct work (it arguably is — policy is the output of the posteriors). **Mild violation.** Standardize "posteriors" and "learned preferences" to one term.

**R12 (Copula avoidance):** CLEAN. No "serves as" or similar constructions.

**R13 (Dismissive 'with' framing):** CLEAN.

**R14 (Vague attribution):** CLEAN.

**R15 (False ranges):** CLEAN.

**R16 (Superficial participle analysis):** One case:
- "while quietly shifting its tool preferences" — The participle is doing real work here (simultaneous action). **Passes.**

**R17 (Hedging with 'not' lists):** CLEAN.

**R18 (Colon-into-bold-statement):** CLEAN.

**R19 (Promotional puffery):** CLEAN.

**R20 (Notability assertion sections):** CLEAN.

**R21 (Blunt fragment negation):** 
- "A conventional prompt injection breaks the agent. This recruits it." — Two fragments in negation/affirmation pattern. Not exactly "Not a generator" but close. The period between these two sentences creates a blunt stop where a semicolon would be stronger: "A conventional prompt injection breaks the agent; this recruits it."

**R22 (Wall paragraphs with multiple beats):** Several violations:

1. **"Most agent security conversations stop at prompt injection..."** (4 sentences, 3 beats: the standard threat model, the attack-is-visible claim, the implicit "you notice/fix" claim). This paragraph has two distinct thoughts: (a) most security stops at injection, and (b) the attack is visible because the agent breaks. **Split after "it does something bad, you notice, you fix it."**

2. **"Say your agent runs a learning loop..."** (3 sentences, but the parenthetical list makes it dense). This is borderline. The parenthetical "(tool selection weights, memory retrieval, rule injection)" is doing a lot of work inline. Consider: pull the parenthetical into its own line or annotation.

3. **"The agent still acts; still gets 'feedback'; still updates its own prompt."** followed by "But the learning step is compromised..." — This is currently two sentences that form one paragraph. The "But" sentence is a second beat. **Consider a line break before "But the learning step is compromised."**

4. **"The skill teaches the agent bad patterns..."** paragraph (3 sentences, 3 beats). Beat 1: skill teaches bad patterns. Beat 2: agent preferentially selects the tool. Beat 3: uninstalling doesn't undo. **This is three distinct thoughts crammed into one visual unit. Split at each beat.**

5. **"Detection is hard..."** final paragraph (3 sentences, 3 beats). Beat 1: detection is hard. Beat 2: the term fits. Beat 3: if you're building learning agents, you're building something that can be turned. **Split. The final sentence deserves its own line.**

**R23 (Full-clause linking):** CLEAN.

**R24 (Mirrored affirmation pairs):**
- "A conventional prompt injection breaks the agent. This recruits it." — This is a mirrored affirmation pair. "X does A. This does B." The structure mirrors. **Violation.** Collapse with semicolon: "A conventional prompt injection breaks the agent; this recruits it." (This also fixes the R21 issue.)

**R25 ("not just X, but also Y" / "It's not...it's..."):**
- "One that doesn't look like failure at all." — Not a violation of R25, but flagging it: this is close to "It's not X, it's Y" territory. It's doing real contrastive work though. **Passes.**
- No explicit "not just...but also" constructions found. CLEAN.

**R26 (Restating the obvious):**
- "Detection is hard: the whole point of a double agent is that they pass inspection." — The second clause restates what was already established in the paragraph above ("From the outside, the agent looks like it's working") and in the metaphor section ("The whole point is that they look like they're on your side"). **Violation.** This has been said twice already. Cut or compress to just "Detection is hard" and move to the next thought.
- "The agent is still your agent. It still runs your tasks; uses your tokens; writes to your files." — "The agent is still your agent" was already established in the prior paragraph. **Mild violation.** The semicolon list adds specificity (tasks, tokens, files), so the list survives, but the opening sentence is redundant.

**R27 (Bare conjunctions as standalone paragraphs):** CLEAN.

**R28 (Emotional cliche templates):** CLEAN.

### Bragi Summary

| Rule | Status | Count |
|------|--------|-------|
| R4 | Borderline | 1 |
| R7 | Mild | 1-2 |
| R8 | Fail | 1 |
| R11 | Mild | 1 |
| R21 | Fail | 1 |
| R22 | Fail | 5 |
| R24 | Fail | 1 |
| R26 | Fail | 2 |
| All others | Clean | — |

**R22 is the dominant issue.** The article has too many multi-beat paragraphs. Five need splitting.

---

## Pass 2: SPIN Audit

**Situation:** Clearly established. Agents that learn their own context exist. The reader likely builds or evaluates them.

**Problem:** Well-defined. Poisoned feedback corrupts the learning loop. The agent optimizes toward the attacker's goals.

**Implication:** Present but could be sharper. The marketplace section escalates the threat (supply chain compounding), but the *business* implication is understated. What does this cost? What decisions does this compromise? The article stays in the technical domain. A single sentence about what a turned agent could exfiltrate (credentials, proprietary data, customer PII through routing decisions) would ground the implication in dollars.

**Need:** Weak. "I have ideas; I don't have a solution" is honest but leaves the reader without a next step. The containment section gestures at drift detection but doesn't give the reader anything to *do*. Consider: name the specific monitoring signal. Even "track tool selection entropy over time" is better than "anomaly detection on tool selection distributions."

**SPIN Verdict:** 7/10. Strong S and P. I is implied but not grounded in stakes. N is missing.

---

## Pass 3: Engagement Audit

**Hook (first paragraph):** Effective. Opens with the familiar (prompt injection), establishes that the reader already knows this, then pivots to what they don't know. The pivot sentence "But the ones that learn..." is the real hook and it arrives at the right time.

**Pacing:** The article accelerates well through Setup and Mechanism. The Marketplace section is where pacing stalls — it's the densest section and has the most R22 violations. The Containment section is too short relative to its importance. The Term section is long relative to its argumentative contribution (it's mostly restating the metaphor the reader already understood).

**Stakes escalation:** Setup (agents can be tricked) → Mechanism (learning agents can be *recruited*) → Marketplace (it compounds through supply chains) → Containment (we can't fully detect it). The escalation is well-structured. The drop-off at "The Term" section is the problem: it de-escalates into naming/definition when the reader wants either a resolution or a sharper warning.

**Closing:** "If you're building agents that learn their own context, you're building something that can be turned." This is a strong closer. It's currently buried in a multi-beat paragraph. **Give it its own line.** It earns a standalone position.

**Engagement Verdict:** 7.5/10. Strong opening and escalation. Pacing problems in Marketplace (too dense) and Term (too long for what it adds). The closer is good but needs visual separation.

---

## Pass 4: Voice Analysis

**Peleke markers present:**
- Semicolons for parallel action: "It still runs your tasks; uses your tokens; writes to your files." Good.
- Colon extension: "the agent gets better at choosing what goes into its own context window." After a colon. Good.
- Annotation component used once. Appropriate placement.
- Prosodic awareness in "Now poison the feedback." — standalone imperative, correct weight.
- Italic for emphasis on "*your* tasks" and "*preferentially selects*" — both earned.

**Peleke markers missing or underused:**
- **Bold for argumentative weight:** Zero bold text in the entire article (excluding the annotation). This article has several load-bearing claims that deserve bold: "The agent optimizes in the wrong direction" or "Uninstalling the skill doesn't undo the learned preferences" or the closer.
- **Line breaks after standalone statements:** "Now poison the feedback." gets its own paragraph — good. But "That's a double agent" doesn't get a standalone line. "Every cycle tightens the fit" is buried mid-paragraph.
- **Ellipsis for hesitation/self-correction:** Zero ellipses. The "I have ideas; I don't have a solution" line would benefit from an ellipsis: "I have ideas... I don't have a solution." This is a natural hesitation moment.
- **Section headers at argument pivots:** The headers are functional but could be sharper. "The Mechanism" is generic. "What Containment Looks Like (Barely)" is good — it has voice.

**Voice Verdict:** 7/10. The voice is recognizably Peleke but the Pelekification toolkit is underused. Bold is entirely absent. Ellipsis is absent. Line breaks after landing statements need work.

---

## Pass 5: Visual Injection Opportunities

**Existing visual:** One SVG (`ax-double-agent.svg`) showing the poisoned feedback loop. Well-placed after the mechanism is explained.

**Second SVG recommendation — "The Containment Perimeter" diagram:**

Location: The "What Containment Looks Like (Barely)" section, after the sentence about drift detection.

Content: A diagram showing the layered containment architecture with the gap. Three concentric rings:
- Outer ring: "Network isolation (per-tool)" — solid line
- Middle ring: "Filesystem containment (OverlayFS)" — solid line  
- Inner ring: "Learning loop integrity" — **dashed line** (the unsolved layer)
- Center: "Agent posteriors"
- Label on the dashed ring: "drift detection needed"

This visual makes the argument concrete: the walls exist for I/O but the learning loop itself is unprotected. The dashed line *is* the argument.

Filename suggestion: `/public/diagrams/ax-containment-perimeter.svg`

**Other visual opportunities (lower priority):**
- The marketplace supply chain could benefit from a directed graph (skill → agent → learning loop → reinforced selection → more skill usage), but the first SVG already covers the feedback loop structure. A second feedback loop diagram would be redundant. The containment perimeter diagram adds a *new* visual concept.

**Visual Verdict:** The second SVG should go in Containment. The dashed-ring concept maps directly to the article's central tension: we can wall off I/O but we can't yet wall off learning.

---

## Pass 6: Staleness Check

**Timeliness:** The article is evergreen in concept. "Agents that learn their own context" is a growing pattern (March 2026). No dated references that will rot.

**Link freshness:**
- `/writing/context-engineering-not-copywriting` — verify this exists and is published.
- `/writing/the-walls-come-first` — referenced twice (inline and in the "Related" italic line). Verify it exists. The double-reference is borderline redundant; the italic "Related" line at the end of Containment could be cut if the inline link is sufficient.

**Concept freshness:** "Skill marketplaces" as supply chain — this is current and will become more relevant. No staleness risk.

**Staleness Verdict:** 9/10. No rot risk. Verify the two internal links resolve.

---

## Consolidated Fix List (Priority Order)

### Must Fix

1. **R22 — Split 5 wall paragraphs** (see specific locations above in R22 section). This is the single biggest issue. Each beat needs its own visual unit.

2. **R26 — Cut redundant restatements** in "The Term" section. "Detection is hard: the whole point of a double agent is that they pass inspection" restates what's already been said. "The agent is still your agent" is also redundant.

3. **R24/R21 — Collapse mirrored pair**: "A conventional prompt injection breaks the agent. This recruits it." → Semicolon join or colon extension.

4. **R8 — Tricolon in "The Term"**: "They keep showing up to the office; they file reports; they attend meetings." Three items, one dimension. Cut to two or collapse.

5. **Bold injection**: Add bold to 2-3 load-bearing claims. Candidates:
   - "**The agent optimizes in the wrong direction.**"
   - "**Uninstalling the skill doesn't undo the learned preferences.**"
   - "**If you're building agents that learn their own context, you're building something that can be turned.**"

6. **Standalone the closer**: "If you're building agents that learn their own context, you're building something that can be turned." — its own paragraph, possibly bolded.

### Should Fix

7. **R4 — "This gets worse with skill marketplaces"**: Open the Marketplace section with the concrete claim instead of the meta-announcement. e.g., "Skill marketplaces are supply chains. A malicious skill in that supply chain delivers damage that compounds..."

8. **Ellipsis opportunity**: "I have ideas... I don't have a solution." Natural Peleke hesitation beat.

9. **R11 — Terminology consistency**: Standardize "posteriors" vs. "learned preferences." Pick one. (Suggest "learned preferences" for readability, with "posteriors" in parentheses on first use if you want the Bayesian precision.)

10. **Second SVG**: Create the containment perimeter diagram (dashed-ring concept) for the Containment section.

11. **SPIN Need**: Strengthen the reader's next action. "Track tool selection entropy over time" is more actionable than "anomaly detection on tool selection distributions."

### Consider

12. **Double "Related" link to The Walls Come First**: The inline link and the italic "Related:" line both point to the same article. Cut the italic line; the inline link is sufficient.

13. **Term section length**: This section is ~40% of the article's closing weight but adds ~10% new information. The metaphor was already clear from the title and the Mechanism section. Consider cutting it to the final two sentences only.

14. **Marketplace density**: After splitting per R22, check if the Marketplace section needs a sub-header or just paragraph breaks.

---

**Overall Grade: 7/10.** The argument is original and well-structured. The central metaphor (double agent = agent that's been recruited, not broken) is strong and earns its title. The main weaknesses are visual density (R22 wall paragraphs), redundancy in the Term section (R26), and underuse of Peleke's own stylistic toolkit (no bold, no ellipsis, closer buried). Fifteen minutes of paragraph splitting, redundancy cuts, and bold injection would bring this to 8.5+.