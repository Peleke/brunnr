# Bragi Review: two-ships-qortex-distributed ("Wind on the Wire")
# Date: 2026-03-09
# Source: article-draft skill (28-rule Bragi Prose Gate + Pelekification + Staleness)

---

## Pass 1: Bragi Prose Gate (28 Rules)

### R1 — No em dashes

**VIOLATIONS FOUND: 0**

Full scan: zero em dash characters (`—`) in the article. The article uses colons, semicolons, periods, and ellipsis consistently. **PASS.**

---

### R2 — No AI vocab blocklist

**VIOLATIONS FOUND: 1**

1. L83: `"the right one can be an accelerant"` — "accelerant" is not on the standard blocklist but reads like elevated AI-register diction. **BORDERLINE.** The metaphor is deliberate (paired with "fatal" in the same sentence), and the sentence earns it. **FLAG but don't block.**

No instances of: landscape, crucial, pivotal, meticulous, enhance, highlight, showcase, underscore, valuable, key (adj), delve, tapestry. **PASS on blocklist proper.**

---

### R3 — No performative honesty

No instances of "honestly," "to be frank," "the truth is," "I'll be real." **PASS.**

---

### R4 — No self-referential pivots

No instances of "This is where things get interesting" or equivalent. **PASS.**

---

### R5 — No inflated significance framing

**VIOLATIONS FOUND: 0**

No "this changes everything," "the implications are staggering," or equivalent. The article stays grounded in technical specifics. **PASS.**

---

### R6 — No hedging then inflating

No instances found. **PASS.**

---

### R7 — No punchy fragment marketing copy

**VIOLATIONS FOUND: 3**

1. **L103**: `"Something had to give."` — Standalone punchy fragment. Reads like a cliffhanger beat designed for drama. The preceding three-part construction (different language, different stack, different process) already makes the point. This fragment adds tension without information. **VIOLATION.**

2. **L67**: `"Dead in the water so fast even the sharks be suspicious."` — Punchy colloquial fragment with comedic intent. This one is borderline because it's clearly a deliberate voice choice (humorous register), but the joke is doing marketing work: exaggerating failure for effect. **BORDERLINE — author's call.** If it stays, it earns its place through humor, not through selling.

3. **L194**: `"Now? We've got options."` — Two punchy fragments closing the entire article. "We've got options" is a marketing tagline. The article earned a real closing thought and instead delivers a bumper sticker. **VIOLATION.**

---

### R8 — Tricolon/pentad escalation test

**VIOLATIONS FOUND: 2**

1. **L101**: `"from a different language, on a different stack, in a different process."` — Tricolon. Each item adds a new dimension: language (semantic), stack (technical), process (runtime). Genuine escalation from abstract to concrete. **PASS — barely.** The repetition of "different" weakens it. Consider varying the structure.

2. **L61–63** (the three bullet points under "Over the Wire"):
   - "Pipes Don't Survive Container Boundaries"
   - "No Load Balancing"
   - "No Auth"

   Three items, escalating from infrastructure to security. Each adds a new dimension. **PASS** as an enumeration. But the bullet descriptions themselves contain punchy fragment cadence (see R7 and R22 notes below).

3. **L158**: `"Henceforth, time evolution takes place in three spaces:"` followed by three styled cards (Vindler, Interlinear, MindMirror). This is structural tricolon as page design. Each card is a distinct project with distinct status. **PASS.** This is enumeration, not rhetorical escalation.

---

### R9 — No rhythmic parallel construction closers

**VIOLATIONS FOUND: 1**

1. **L194**: `"Now? We've got options."` — This is the article's final line. It's a two-beat rhythmic closer (question fragment, then assertion fragment). It tries to end on a drum hit instead of an insight. **VIOLATION.** The article opens with a specific technical claim ("qortex was a library: Now it's a service") and should close with something that mirrors that specificity, not a vague confidence statement.

---

### R10 — No challenges-and-future-prospects formula

**VIOLATIONS FOUND: 1**

1. **L189–194** ("Roadmap" section): "Next steps are plugging into the systems above to prove efficacy. That's really it." followed by a deployment suggestion and "Now? We've got options." This is a light version of the challenges-and-future-prospects formula: the article ends by looking forward instead of landing. **VIOLATION.** The Roadmap section adds almost no information. The Downstream section already shows what's next. Consider cutting Roadmap entirely or folding the one useful detail (Supabase/Railway deployment) into Downstream.

---

### R11 — No elegant variation

**VIOLATIONS FOUND: 0**

The article consistently uses "qortex" for the system, "Vindler" for the agent, "Interlinear" for the app. No unnecessary synonymic variation. "Library" vs "service" is the deliberate contrast, not elegant variation. **PASS.**

---

### R12 — No copula avoidance

**VIOLATIONS FOUND: 0**

Uses "is" directly: "qortex was a library: Now it's a service" (L14), "It was not fine for production" (L54), "REST is more than enough" (L76). No "serves as," "functions as," "acts as." **PASS.**

---

### R13 — No dismissive 'with' framing

**VIOLATIONS FOUND: 0**

No instances of "A demo with persistence" or similar minimizing constructions. **PASS.**

---

### R14 — No vague attribution

**VIOLATIONS FOUND: 0**

All claims are first-person or attributed to specific systems. No "experts say," "many believe," "it's widely known." **PASS.**

---

### R15 — No false ranges

**VIOLATIONS FOUND: 0**

No "from X to Y" range claims. **PASS.**

---

### R16 — No superficial participle analysis

**VIOLATIONS FOUND: 0**

No "leveraging," "utilizing," "harnessing" constructions. **PASS.**

---

### R17 — No hedging with 'not' lists (lead with positive)

**VIOLATIONS FOUND: 2 (PRIORITY FOCUS)**

1. **L22**: `"This is _not_ what we set out to do."` — Opens a section by defining the work by what it isn't. The next four paragraphs explain what they were actually doing (building Interlinear, forking the dictionary). The negation lead delays the positive assertion. **VIOLATION.** Rewrite: Lead with what they set out to do ("We were building a language app..."), then note the detour.

2. **L36**: `"Somehow, _still_, in 2026, duplicating database tables it had already created; using context from CLAUDE.md and SKILL.md only when it felt like it; suggesting the same fix it had already tried and abandoned ten minutes prior."` — This is a list of three negatives (things the agent does wrong). The positive assertion doesn't arrive until L40: "That's why we built qortex." The gap between problem (L36) and solution (L40–44) is bridged by the Annotation interlude. The negative list works here because the section is titled "The Problem," but the three-item negative construction is textbook R17. **BORDERLINE.** The negative list is earned by the section title. **FLAG but don't block.**

---

### R18 — No colon-into-bold-statement

**VIOLATIONS FOUND: 0**

Colons are used for extension, not for introducing bold-formatted punchlines. **PASS.**

---

### R19 — No promotional puffery

**VIOLATIONS FOUND: 3 (PRIORITY FOCUS)**

1. **L85**: `"This time, that's exactly how it burned: done, end-to-end, in a single afternoon."` — "End-to-end, in a single afternoon" is puffery cadence. It sells the speed without substantiation. How big was the change? How many files? How many tests? The claim is unanchored. **VIOLATION.** Either quantify (X files changed, Y tests passing) or trim to just "done in an afternoon."

2. **L121**: `"This doesn't happen on accident, by the way: agents don't just spit this out when you ask nicely."` — Self-congratulatory aside. The article already shows the architecture that made the swap possible. This sentence adds no information; it just asks the reader to be impressed. **VIOLATION.** Cut entirely. The architecture section already makes the point.

3. **L194**: `"Now? We've got options."` — Closes the article with a vague confidence assertion. "We've got options" is a sales line, not an insight. **VIOLATION (also flagged R7, R9).**

4. **L67**: `"Dead in the water so fast even the sharks be suspicious."` — Already flagged under R7. The exaggeration is comedic, but it's still selling failure for effect. **BORDERLINE.**

---

### R20 — No notability assertion sections

**VIOLATIONS FOUND: 0**

No "Why This Matters" section or equivalent. Section headers name topics, not significance. **PASS.**

---

### R21 — No blunt fragment negation

**VIOLATIONS FOUND: 1**

1. **L22**: `"This is _not_ what we set out to do."` — Standalone sentence leading with negation. Already flagged under R17. **VIOLATION.** Merge into the positive assertion that follows.

---

### R22 — No wall paragraphs (5+ sentences without visual break)

**VIOLATIONS FOUND: 3 (PRIORITY FOCUS)**

1. **L46–48** ("The Fix," paragraph starting "The graph tracks..."): This is technically one paragraph containing three distinct beats packed into a single dense block:
   - (a) The graph tracks paths (with two inline Annotations, each containing technical detail)
   - (b) Retrieval improves from usage, not curation
   - (c) The accept/reject feedback loop

   With the annotations expanded, this is a wall of cognitive load. The reader must process the prose, two tooltip-annotations, AND a hyperlink all in one block. **VIOLATION.** Break after the first sentence (graph tracks paths / finds connections). Put the feedback loop explanation in its own paragraph.

2. **L56–58** ("Over the Wire," paragraph starting "MCP stdio works..."): Four sentences covering:
   - (a) When stdio works (general statement)
   - (b) Link to the standard transport spec
   - (c) Three example use cases (IDE, CLI, single-user agent)
   - (d) For that use case, stdio is the right call

   This is not severe, but the sentence starting with "An IDE connecting..." is a list pretending to be prose. **BORDERLINE.** Consider breaking the three examples into a list, or trimming to one example.

3. **L59–63**: The paragraph starting "The moment you need..." followed by three bold bullet points is well-structured. But each bullet point itself is a mini-paragraph. The **Load Balancing** bullet (L62) contains 3 sentences: "Every consumer gets its own subprocess. Scale to three... Scale to twelve..." These are fine as bullets but would be a wall if the bold labels were removed. **PASS — the bullets save it.**

---

### R23 — No full-clause linking

**VIOLATIONS FOUND: 0**

Hyperlinks use short, specific anchor text: "language app," "fork an Icelandic dictionary," "standard transport." No full-clause hyperlinks. **PASS.**

---

### R24 — No mirrored affirmation pairs

**VIOLATIONS FOUND: 0**

No "One does X. The other does Y." constructions. **PASS.**

---

### R25 — No "not just X, but also Y" (false dichotomy)

**VIOLATIONS FOUND: 1 (PRIORITY FOCUS)**

1. **L83**: `"Just as the wrong abstraction is fatal, the right one can be an accelerant."` — "Wrong abstraction is fatal / right one is an accelerant" is a false dichotomy that presents only two poles. Abstractions exist on a spectrum; most are neither fatal nor accelerants. The sentence is trying to sell the internal architecture as unusually good. **VIOLATION.** Rewrite to state what the abstraction actually enabled: "Because both transports implement the same `core` protocol, the migration was one import swap." (The article already says this in L109; this sentence in L83 is redundant puffery framing for it.)

---

### R26 — Restating the obvious (restatement/redundancy)

**VIOLATIONS FOUND: 4 (PRIORITY FOCUS)**

1. **L14 + L16**: The article opens with two sentences that say the same thing:
   - L14: `"qortex was a library: Now it's a service."`
   - L16: `"This is the story of how we moved the knowledge graph, learning store, and vector index off of localhost and onto the network"`

   The first sentence is the thesis. The second sentence restates it with more nouns. The reader got it. **VIOLATION.** Either cut L16 or merge it with L14 so the detail serves the thesis rather than restating it. E.g.: "qortex was a library: Now it's a service. Here's why we put the graph on the network, and what broke on the way."

2. **L105 + L109**: Two sentences that say the same thing about the import swap:
   - L105: `"We put core behind a REST API. Same graph, same learning store, same vector index. Different transport."`
   - L109: `"Switching from in-process to remote is one import swap. The code doesn't know or care where core lives."`

   Both explain the same point (transport change, same interface). The reader understands from the first. The second is earned because it's more concrete (the actual import swap), but the tricolon in L105 ("Same graph, same learning store, same vector index") is doing the same rhetorical work as L109's "one import swap." **MINOR VIOLATION.** Consider trimming L105 to just "We put `core` behind a REST API" and letting L109 do the explanatory work.

3. **L48 + L50**:
   - L48: `"It started as a Python library: you imported it, it ran in-process."`
   - This restates L14 ("qortex was a library"). The reader is 34 lines in and already knows this.

   **VIOLATION.** L48 adds the technical detail (Python, imported, in-process), which is new. But the framing ("It started as...") is a restatement. Rewrite to lead with the new detail: "The original client was an in-process Python import. If you wanted to use it from Next.js, you talked to it over MCP stdio."

4. **L99 + L101**:
   - L99: `"It was fine when the only consumer was Vindler itself."`
   - L101: `"It stopped being fine the moment Interlinear needed the same data from a different language, on a different stack, in a different process."`

   This is a mirrored restatement: "fine when X / not fine when Y." The construction is a common LLM pattern. The second sentence carries the information; the first is throat-clearing. **VIOLATION.** Cut L99. Start with: "The moment Interlinear needed the same data..."

---

### R27 — No bare conjunctions as standalone paragraphs

**VIOLATIONS FOUND: 1**

1. **L30**: `"But..."` — Standalone "But..." as its own paragraph. This is a deliberate pacing choice (creating a pause before the pivot to unforgivable errors). The ellipsis is a Peleke voice marker. **BORDERLINE — author's call.** The technique works here for breath, but the rule is the rule.

---

### R28 — No emotional cliche templates

**VIOLATIONS FOUND: 0**

No "imagine a world where," "picture this," or second-person hypothetical sales scenarios. **PASS.**

---

## Bragi Gate Summary

| Severity | Count |
|---|---|
| MAJOR violations (must fix) | 6 |
| Standard violations (should fix) | 7 |
| Borderline/flags (author's call) | 5 |
| Clean passes | 17 of 28 rules |

---

## Pass 2: Staleness Check

### Temporal Markers

1. **L95**: `"A year ago, the biggest AI question on anyone's mind was whether students were cheating with ChatGPT."` — **STALE.** Article date is 2026-02-23. "A year ago" places this in early 2025. By the time a reader encounters this article even a month later, "a year ago" becomes ambiguous. **Replace with "In early 2025" or "In January 2025."**

2. **L95**: `"MCP was a month old"` — This is relative to "a year ago," which is already stale. **Replace with "MCP was six weeks old" or give the actual launch date.**

3. **L93**: The Q1 2025 timeline diagram SVG is fine — the diagram itself is date-labeled and won't rot.

### Quantitative Claims to Verify

4. **L167**: `"v0.8.1"` — Verify this is still the current version at publish time. If qortex ships v0.9 before the article goes live, this is wrong.

5. **L125**: `"Python and TypeScript clients"` — Verify both SDKs still exist and are published.

### Link Rot Risk

6. **L95**: `https://www.pewresearch.org/short-reads/2025/01/15/...` — Pew links are generally stable. Low risk.
7. **L95**: `https://www.anthropic.com/news/constitutional-classifiers` — Anthropic may restructure URLs. Medium risk.
8. **L95**: `https://www.pento.ai/blog/a-year-of-mcp-2025-review` — Third-party blog. Higher rot risk.
9. **L135**: `https://peleke.github.io/qortex/getting-started/quickstart/` — Internal docs. Verify path is correct at publish.

---

## Pass 3: Pelekification Checks

### Line Breaks as Breath Marks

**VIOLATIONS FOUND: 3**

1. **L14**: `"qortex was a library: Now it's a service."` — This is the thesis statement. It lands. But it's immediately followed by L16 without a visual break (the architecture diagram on L18 provides one, but L16 sits between the thesis and the diagram as connective tissue). **Consider:** Let L14 breathe alone, then place the diagram, then begin the narrative. L16 is R26 redundancy anyway.

2. **L54**: `"It was not fine for production."` — This sentence lands. It gets its own paragraph (good), and the next paragraph begins immediately. The breath is there. **PASS.**

3. **L40**: `"That's why we built qortex: a knowledge graph with a learning layer that, as it were, does _not_ forget."` — The colon extension is good Peleke form. The "as it were" parenthetical adds voice. But this line deserves a beat after it. The next paragraph (L46, "The Fix") provides the section break. **PASS.**

### Colon Extension

**PRESENT AND WELL-USED:**

- L14: `"qortex was a library: Now it's a service."` — Thesis delivered via colon extension. Strong.
- L40: `"...a knowledge graph with a learning layer that, as it were, does _not_ forget."` — Colon introducing the defining clause.
- L85: `"done, end-to-end, in a single afternoon."` — Colon extending to the payoff.
- L131: `"Enabling it is one call: QortexService.async_from_env()."` — Colon extending to the proof.

**Grade: A.** The article uses colon extension frequently and correctly.

### Ellipsis for Trailing Thought

**PRESENT:**

- L30: `"But..."` — Ellipsis creating a pause before the pivot. Good Peleke usage.

**MISSING:**

- The article has zero other ellipsis instances. The voice is consistently assertive, which is fine for a technical article, but one more moment of self-interruption or trailing doubt would add texture. **FLAG — not required, but the article is 100% assertion.**

### Semantic Punctuation

**WELL-USED:**

- Semicolons: L36 uses semicolons for three parallel failures ("duplicating database tables...; using context...only when it felt like it; suggesting the same fix..."). This is strong Peleke punctuation.
- L125: `"One protocol, two languages, zero subprocess management."` — Commas in a compressed enumeration. Good.

**MISSING:**

- The "Over the Wire" bullets (L61–63) use bold headers and colons but could benefit from semicolons within the bullet descriptions to compress multi-beat explanations.

### Bold for Weight, Not Decoration

**VIOLATIONS FOUND: 1**

- L61–63: Bold is used for bullet headers (`**Pipes Don't Survive Container Boundaries**`, `**No Load Balancing**`, `**No Auth**`). This is structural, not argumentative. Fine for a list.
- **Missing:** The article has almost no bold in prose. Key claims like "one import swap" (L109), "same interface" (L109), and "one call" (L131) could carry bold for argumentative weight. **FLAG — consider adding 2-3 bold phrases for emphasis on the core technical claims.**

### Semicolons for Parallel Actions

**WELL-USED:**

- L36: Three parallel failures joined by semicolons. Strong.
- L105: `"Same graph, same learning store, same vector index."` — Uses commas instead of semicolons. This is fine because the items are noun phrases, not clauses. **PASS.**

**MISSING:**

- L101: `"from a different language, on a different stack, in a different process."` — Could use semicolons to give each dimension more weight, but commas work here for pace. **Author's call.**

---

## Consolidated Action Items (Priority Order)

### MUST FIX (blocks publish)

1. **R26 (L14+L16): Cut the thesis restatement.** L16 restates L14 with more nouns. Cut L16 or merge its detail into L14. Let the thesis land once.

2. **R26 (L99+L101): Cut the mirrored restatement.** "It was fine when... / It stopped being fine when..." is an LLM pattern. Cut L99. Start directly with "The moment Interlinear needed the same data..."

3. **R19 (L121): Cut the self-congratulatory aside.** "This doesn't happen on accident, by the way" adds no information. The architecture section already proves the point. Delete the sentence.

4. **R19 (L85): Quantify or trim the speed claim.** "Done, end-to-end, in a single afternoon" is puffery without evidence. Either add the proof (X files, Y tests) or trim to just "done in an afternoon."

5. **R7/R9/R19 (L194): Rewrite the closing.** "Now? We've got options." is a marketing tagline, not a closing thought. End on a specific technical insight or echo the opening thesis. E.g., "The library is a service. The service is live. The next question is whether the graph learns faster with more consumers feeding it."

6. **Staleness (L95): Replace "A year ago" and "a month old."** Use specific dates or date-independent framing. "In early 2025" or "In January 2025" for the former; "MCP had launched six weeks prior" or "MCP was barely two months old" with an anchor date for the latter.

### SHOULD FIX (significant quality improvement)

7. **R22 (L46–48): Break the wall paragraph in "The Fix."** Three beats (graph tracking, structural connections, feedback loop) packed into one dense block with two annotations. Split after the first sentence.

8. **R17 (L22): Lead with the positive.** "This is _not_ what we set out to do" delays the real story. Lead with: "We were building a language app to make it easier to study the sagas." Then note the detour.

9. **R25 (L83): Cut the false dichotomy.** "Wrong abstraction is fatal / right one is an accelerant" is a false binary that exists to sell the architecture. The next sentence already makes the real point. Cut L83 or rewrite as a factual statement about what the abstraction enabled.

10. **R10 (L189–194): Cut or absorb the Roadmap section.** The Downstream section already shows what's next (Vindler live, Interlinear WIP, MindMirror upcoming). The Roadmap section adds only the Supabase/Railway detail, which could be a single sentence in Downstream. The "Now? We've got options" closer is the worst line in the article.

11. **R26 (L105): Trim the tricolon restatement.** "Same graph, same learning store, same vector index. Different transport." is rhetorical flourish restating what L109 explains concretely. Trim L105 to: "We put `core` behind a REST API." Let L109 do the work.

12. **R7 (L103): Rework "Something had to give."** This is a punchy fragment that adds drama without information. The tricolon in L101 already makes the pressure clear. Either cut the fragment or make it do work: "Something had to give: the transport layer."

### NICE TO HAVE (polish)

13. **Pelekification: Add 2-3 bold phrases for argumentative weight.** Candidates: "one import swap" (L109), "one call" (L131), "same interface" (L109).

14. **Pelekification: Add one ellipsis or moment of doubt.** The article is 100% assertion. One trailing thought or self-correction would add texture. Candidate: after L85 ("done in a single afternoon"), add a beat of honest surprise or qualification.

15. **R26 (L48): Rewrite to avoid restating the thesis.** "It started as a Python library" echoes L14. Lead with the new technical detail: "The original client was an in-process Python import."

16. **R27 (L30): Author's call on "But..."** The standalone "But..." with ellipsis is a deliberate Peleke voice move. Keep or cut based on whether the breath mark earns its place in the final version.

17. **Staleness: Verify v0.8.1, SDK existence, and all doc links before publish.**

18. **Pelekification: Consider semicolons in the "Over the Wire" bullet descriptions** to compress multi-beat explanations within each bullet.

---

## Final Assessment

**Current grade: B+**

This article is structurally sound and technically specific. It does one thing well: explains why qortex moved from library to service, with enough architecture detail to be credible. The opening thesis ("qortex was a library: Now it's a service") is clean, and the colon extension throughout is strong Peleke voice.

The main problems are redundancy and puffery. The article restates its thesis at least four times (L14, L16, L48, L105) and contains three self-congratulatory asides that add no information (L85, L121, L194). Cutting these would tighten the article by ~15% and sharpen the voice.

The closing is the weakest section. "Now? We've got options" is a bumper sticker where the article needs a landing. The Roadmap section adds almost nothing that Downstream doesn't already cover. Cut Roadmap, end on Downstream, and give the article a real final thought.

The core fix is editorial, not structural: kill restatements, cut puffery, replace temporal markers, and let the architecture diagrams and code samples do the selling. The technical substance is already there. Stop overselling it.
