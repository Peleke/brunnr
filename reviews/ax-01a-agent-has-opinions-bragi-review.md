# Bragi Review: ax-01a-agent-has-opinions
# Date: 2026-03-09
# Source: article-draft skill (28-rule Bragi Prose Gate + 6-pass)

No external reference files. I'll work from the 28 rules as stated and the article text provided. Here is the review.

---

## Bragi Review: "The Agent Has Opinions"

### R1 -- Em dashes (NO em dashes allowed)

| # | Location | Violation | Fix |
|---|----------|-----------|-----|
| 1 | Para 2: "seven major issues — zero hallucinated" | em dash | Rewrite: "seven major issues. Zero hallucinated citations out of nineteen." |
| 2 | "What AX isn't" section: "though Maren uses the word 'annoying'..." | Not an em dash but worth flagging: no violation here. | -- |

**Count: 1 violation.** Severity: LOW (easy mechanical fix).

---

### R2 -- Blocklist words

| # | Word | Location | Fix |
|---|------|----------|-----|
| 1 | **"key"** (adj) | "She wants the thing that makes her next session 30% less wasteful, not the architecturally **elegant** thing" -- "elegant" is not on the list. But check: no "key adj" found. | -- |
| 2 | **"showcase"** | Not found. | -- |
| 3 | **"landscape"** | Not found. | -- |
| 4 | **"valuable"** | Not found. | -- |
| 5 | **"enhance"** | Not found. | -- |

**Count: 0 violations.** The article is clean on blocklist. Well done.

---

### R7 -- Punchy fragment marketing copy

| # | Location | Fragment | Verdict | Fix |
|---|----------|----------|---------|-----|
| 1 | "She was." | Two-word closer after "Be frank and brutal" | **Violation.** This is a punchy dramatic fragment used for effect, exactly the pattern R7 targets. | Fold into prior sentence: "She'd just finished the Scrivly review. 'Be frank and brutal,' I said. 'It's heavily WIP.' She took me at my word." or integrate the payoff into the next line. |
| 2 | "Loop closes." | Maren's dialogue | Acceptable -- this is the character speaking, not the author performing. | -- |
| 3 | "We're collecting it now. Stay tuned." | Closing line | **Borderline.** "Stay tuned" is a punchy CTA fragment. | Cut "Stay tuned." It's newsletter voice. End on "We're collecting it now." |

**Count: 1 clear, 1 borderline.** Severity: MEDIUM.

---

### R8 -- Tricolon/escalation test

| # | Location | Pattern | Verdict |
|---|----------|---------|---------|
| 1 | "real bugs, real architectural contradictions, caught before they become implementation surprises" | Tricolon. Does each element add a new dimension? "real bugs" -> "real architectural contradictions" (escalates from bug to design flaw) -> "caught before they become implementation surprises" (adds temporal dimension). | **Pass.** Escalation is genuine. |
| 2 | "Slim the payload...Close the learning loop...Let the agent pre-filter" | Bullet list of three actions. | **Pass.** These are three distinct engineering changes, not rhetorical rhythm. |
| 3 | "three concrete design improvements, a metric taxonomy, and a measurement framework" | Tricolon. "improvements" -> "taxonomy" -> "framework." Each is genuinely different. | **Pass.** |
| 4 | "she does operate under real constraints..., she does make real decisions..., and those decisions are influenced by the tool's design" | Triple "she does" anaphora. | **Borderline.** The repetition of "she does" is rhythmic parallel construction more than escalation. The third clause shifts from describing to explaining causality, so it arguably passes. | 

**Count: 0 clear violations, 1 borderline.** Severity: LOW.

---

### R17 -- Hedging with "not" lists

| # | Location | Pattern | Fix |
|---|----------|---------|-----|
| 1 | "AX is not 'UX for bots.' It's not anthropomorphizing the agent or pretending it has preferences... The agent doesn't care about visual design, brand consistency, or emotional resonance. It doesn't get frustrated..." | **Clear violation.** Four consecutive negations define AX by what it isn't. This is a textbook "not" list hedge. | State what AX IS first, then use one negation at most for contrast. The article does eventually define AX positively ("Agent Experience: the design of systems where...") but buries it after four negations. Lead with the positive definition. |
| 2 | "Not 'did the agent complete one tool call' but 'did the agent complete a multi-step review...'" | **Borderline.** Single "not X but Y" contrast used for clarification, not hedging. | Could be tightened but not a serious violation. |

**Count: 1 clear violation.** Severity: HIGH. The "What AX isn't" section is the weakest section in the article. Restructure to lead with the definition.

---

### R19 -- Promotional puffery

| # | Location | Pattern | Fix |
|---|----------|---------|-----|
| 1 | "enables experimental designs that human UX research can only dream of" | **Violation.** "can only dream of" is puffery/hype framing. | Replace with a concrete claim: "enables controlled A/B experiments on identical inputs, which human UX research cannot replicate." |
| 2 | "a distinction without a design-relevant difference" | Not puffery. This is a precise philosophical move. | -- |

**Count: 1 violation.** Severity: MEDIUM.

---

### R22 -- Wall-of-text paragraphs (1 thought per visual unit)

| # | Location | Line count | Thoughts | Fix |
|---|----------|------------|----------|-----|
| 1 | "The epistemological status is genuinely weird..." paragraph | 7 sentences | At least 3 distinct thoughts: (a) the epistemic weirdness, (b) the real constraints and decisions, (c) the closed loop argument. | Split after "...the tool's design." New paragraph at "The feedback she gave changed..." |
| 2 | "CX's Customer Effort Score becomes..." paragraph | 4 sentences | 2 thoughts: (a) what transfers, (b) what's novel. | Split at "But some things are genuinely novel." (Already starts with "But" which signals a turn -- give it its own paragraph.) |
| 3 | Opening paragraph | 3 sentences but dense | Packs tool description + architecture + sampling + gauntlet flow into one block. | Split after "applied against whatever the agent is working on." New paragraph at "The agent runs the gauntlet..." |
| 4 | "I'd been thinking about cost in seconds..." paragraph | Ends with a bold declaration that deserves its own line. | The bold sentence "Maren's cost function is measured in tokens." is buried. | Pull the bold sentence into its own paragraph. Let it land. |

**Count: 4 violations.** Severity: HIGH. This is the most impactful fix category -- splitting these will dramatically improve readability.

---

### R25 -- "Not just X, but also Y"

| # | Location | Pattern | Fix |
|---|----------|---------|-----|
| 1 | "Not 'did the agent complete one tool call' but 'did the agent complete a multi-step review...'" | **Violation.** Classic "not X but Y" construction. | Rewrite: "The unit of measurement becomes the full workflow: did the agent complete a multi-step review without burning 40% of its context on overhead?" |

**Count: 1 violation.** Severity: LOW.

---

### R26 -- Restating the obvious

| # | Location | Pattern | Fix |
|---|----------|---------|-----|
| 1 | "Every token spent on overhead is a token unavailable for the actual work." | **Violation.** This is a zero-sum tautology. The reader already knows this from the context window discussion. | Cut entirely. The preceding concrete numbers (10%, 67KB) already make the point. |
| 2 | "The conclusions from this conversation became a concrete plan:" followed by the same three bullets already stated earlier | **Violation.** The bullet list at the end repeats the three changes almost verbatim from the body. | Cut the repeated bullets. Reference them: "The three changes from that conversation ship this week." |
| 3 | "The tool I built is unusable by the majority of agents in the wild before a single review rule fires." | This restates what was just demonstrated with the context window numbers. | **Borderline.** It's a summary punch line. Could stay if the preceding numbers are trimmed, but as-is it's redundant with the SVG data. |

**Count: 2 clear, 1 borderline.** Severity: MEDIUM.

---

### Other rule violations caught in pass

**R5 (Inflated significance framing):**
- "That's a closed loop." -- Acceptable. It's a factual claim, not inflated.
- "That's what makes this a failure mode unto itself." -- **Borderline.** "Failure mode unto itself" is slightly grandiose. Consider: "That's a separate failure mode."

**R9 (Rhythmic parallel construction closers):**
- "between catching the flaw in a contract and missing it, between dodging the punch and getting knocked out" -- **Violation.** This is a mirrored parallel pair used as a closer. The boxing metaphor also flirts with R28 (emotional cliche). Fix: pick one analogy or make both concrete to the domain.

**R11 (Elegant variation):**
- "context-window-bounded agent" then "context consumption" then "context-window budgeting" -- Three different ways of saying "context window is limited." Not a violation per se (these are genuinely different facets), but worth noting.

**R28 (Emotional cliche templates):**
- "dodging the punch and getting knocked out" -- **Borderline.** Boxing metaphor is cliche-adjacent. The contract example before it is better.

---

### Pelekification Opportunities

Pelekification = making the prose sound like Peleke specifically, not generic "smart tech writer." Based on the voice in existing articles and the CLAUDE.md context:

| # | Location | Current | Pelekification |
|---|----------|---------|----------------|
| 1 | Opening | "I built buildlog. It's a review system..." | The opening is functional but flat. Peleke's voice tends to start with a specific moment or observation, not a product description. Consider opening with the 67KB number or the moment Maren pushed back, then backfill what buildlog is. |
| 2 | "The epistemological status is genuinely weird" | Reads like philosophy seminar. | Peleke's voice handles epistemics with more wry self-awareness. Something like: "I'm aware this paragraph is going to sound like I'm claiming my chatbot has feelings. I'm not. But..." |
| 3 | "Customer Experience (CX) research has spent decades..." | This paragraph reads like a literature review. | Peleke doesn't do lit reviews. He makes the point and drops the reference. Compress to: "CX already has the vocabulary for this. Customer Effort Score becomes Developer Effort Score. Journey mapping becomes workflow mapping." Cut the Nielsen Norman name-drop unless it's doing specific work. |
| 4 | "The design discipline for that customer doesn't exist yet." | Good line, but it's buried mid-paragraph. | Pull it out. Give it air. This is the thesis of the article. |
| 5 | "So what IS it?" | The all-caps "IS" feels like a blog post for a SaaS landing page. | Peleke doesn't do that. Cut the question entirely -- just drop the definition. |
| 6 | The Maren dialogue formatting | Block quotes for Maren, bold for Peleke | This works but could be more distinctive. Consider whether Maren's voice has a consistent register that differentiates from Peleke's authorial voice. Right now they sound similar. |
| 7 | "Stay tuned." | Newsletter/podcast sign-off. | Cut. Peleke doesn't do CTAs. |
| 8 | "Chicken-and-egg, and currently the chicken is skeptical." | Good line. Sounds like Peleke. Keep. | -- |
| 9 | Ending | The article ends with a whimper: "We're collecting it now. Stay tuned." + "Series links at bottom." | End on the concrete plan or on the uncomfortable question. The current ending deflates the piece. |

---

### Severity Summary

| Severity | Rules | Count |
|----------|-------|-------|
| **HIGH** | R17 (not-list hedge in "What AX isn't"), R22 (wall paragraphs x4) | 5 |
| **MEDIUM** | R7 (punchy fragments x2), R19 (puffery x1), R26 (restating obvious x2), R9 (parallel closer x1) | 6 |
| **LOW** | R1 (em dash x1), R25 (not-just x1), R8 (borderline tricolon x1) | 3 |

### Top 3 Actions (highest impact)

1. **Restructure "What AX isn't"** (R17): Lead with the positive definition. Kill the four-negation preamble. This is the conceptual heart of the article and it currently starts by telling you what it's not for four sentences.

2. **Split wall paragraphs** (R22): Four paragraphs need splitting. The opening, the epistemology paragraph, the CX transfer paragraph, and the "cost in seconds" paragraph. Each contains 2-3 distinct ideas compressed into one block.

3. **Cut the redundant ending** (R26): The three-bullet recap at the end repeats the body verbatim. The article should end on "These changes ship this week" or circle back to the opening observation. "Stay tuned" and "Series links at bottom" are anti-climactic.