# Bragi Review: qortex-integration-benchmarks
# Date: 2026-03-09
# Source: article-draft skill (28-rule Bragi Prose Gate + Pelekification + Staleness)
# Article: "Plugging a Knowledge Graph into 7 Agent Frameworks"
# Location: /Users/peleke/Documents/Projects/portfolio/src/content/writing/qortex-integration-benchmarks.mdx

---

## Summary

- Bragi violations: 14 (5 clear, 6 borderline, 3 structural)
- Priority rules hit: R1 (0), R7 (2), R8 (2), R19 (1), R22 (3), R26 (3), R17 (0), R25 (2)
- Staleness risks: 5 flagged
- Pelekification gaps: 6 identified

---

## R1 -- Em dashes (NO em dashes allowed)

**Count: 0 violations.** The article uses no em dashes. Clean.

---

## R7 -- Punchy fragment marketing copy

| # | Line | Quote | Verdict | Fix |
|---|------|-------|---------|-----|
| 1 | L39 | "Same codebase, one transport layer." | **Violation.** Two-phrase fragment used as a punchy tagline. This is ad copy rhythm. | Integrate: "The TypeScript adapters talk to the same Python engine over MCP stdio through a single transport layer." |
| 2 | L34 | "Zero skips allowed." | **Borderline.** Three-word fragment after a factual statement. The brevity is punchy but the claim is literal (CI enforces zero skips). | Acceptable as-is because it describes an actual CI constraint, but consider folding: "100 adapter tests run in CI on every push with zero skips allowed." |

**Count: 1 clear, 1 borderline.** Severity: LOW.

---

## R8 -- Tricolon/escalation test

| # | Line | Pattern | Verdict | Fix |
|---|------|---------|---------|-----|
| 1 | L69 | "adding a knowledge graph, typed relationships, and a feedback loop" | Tricolon. Does each item add a new dimension? Knowledge graph (structure) -> typed relationships (semantics of structure) -> feedback loop (learning from structure). | **Pass.** Each item adds a genuinely different capability layer. |
| 2 | L91 | "Multiple frameworks, multiple domains, real users generating real feedback." | Tricolon with anaphoric "multiple." frameworks -> domains -> users. | **Borderline.** The first two items ("multiple frameworks, multiple domains") are parallel synonyms for "breadth." The third shifts to a different category (users + feedback). Consider: "Real users across multiple frameworks and domains, generating real feedback." |
| 3 | L153 | "We need more data, domains, feedback, and time." | Tetrad. data -> domains -> feedback -> time. | **Pass.** Four genuinely distinct requirements. Not rhythmic padding. |
| 4 | L11 | "CrewAI has `KnowledgeStorage`. LangChain has `VectorStore`. Agno has `KnowledgeProtocol`. AutoGen has `Memory`." | Tetrad of parallel "X has Y" statements. | **Pass.** These are four distinct factual statements. Not rhetorical rhythm; it's a survey. |

**Count: 0 clear violations, 1 borderline.** Severity: LOW.

---

## R17 -- Hedging with "not" lists (lead with positive)

| # | Line | Pattern | Verdict | Fix |
|---|------|---------|---------|-----|
| 1 | L151 | "Framework authors don't change anything. Users don't learn a new API" | Two consecutive negations. | **Not a violation.** These are two distinct factual claims (zero framework changes, zero API learning curve), not a hedging "not-list" that avoids saying what the thing IS. The positive statement follows immediately: "you swap the import, and things work." |

**Count: 0 violations.** Clean.

---

## R19 -- Promotional puffery

| # | Line | Quote | Verdict | Fix |
|---|------|-------|---------|-----|
| 1 | L157 | "the floodgates are already poised to open" | **Violation.** "Floodgates" is hype metaphor. The article has been admirably restrained about qortex's maturity throughout, then undercuts itself in the final sentence with a flood metaphor that implies massive scale impact. | Rewrite: "And once a thesis is proven, the distribution infrastructure is already in place." Or cut entirely; L155 ("the integrations work, and CI guarantees they remain in sync") is a stronger ending. |
| 2 | L157 | "(we don't deal in 'ifs')" | **Borderline.** Parenthetical swagger that conflicts with the article's otherwise honest hedging (L57: "it's disingenuous to claim...", L83: "We're not sure yet."). | Cut the parenthetical. It undermines the credibility earned by the honest hedging throughout. |
| 3 | L85 | "Why This Matters Beyond Benchmarks" | Section header. "Why This Matters" is not puffery per se, but it's a notability assertion header (R20 adjacent). | **Borderline.** Consider renaming to something more concrete: "From Test Suites to Production" or "Three Production Consumers." |

**Count: 1 clear, 2 borderline.** Severity: MEDIUM.

---

## R22 -- Wall-of-text paragraphs (5+ sentences / multiple beats)

| # | Line | Sentence count | Beats | Fix |
|---|------|---------------|-------|-----|
| 1 | L33-35 | 3 bullet items, but the first bullet (L33) is a 2-sentence wall packing: (a) the 3 failures explanation, (b) the CrewAI DB replacement, (c) the interface vs. implementation distinction. | 3 beats in one bullet. | Split L33 after "local embedder." New sentence for the DB replacement context: "CrewAI recently replaced its DB layer. The adapter still passes because it targets the published `KnowledgeStorage` interface contract, not the internal storage implementation." |
| 2 | L41 | Single paragraph packing: (a) qortex now ships REST API, (b) it's a Starlette ASGI server, (c) it has 35+ endpoints, (d) API key and HMAC auth, (e) async client, (f) same protocol interface, (g) any language can use it, (h) adapter pattern carries over. | 8 distinct facts crammed into one sentence. | **Violation.** This is the worst wall in the article. Break after "local client." New paragraph: "Any application in any language can query qortex over the network. The adapter pattern and test scaffolding carry over directly." |
| 3 | L79 | Rule projection bullet item: packs (a) what rules are, (b) how they enter context, (c) that they're a specific case of the general system, (d) that they're a legacy monopartite projection, (e) that they exist to feed buildlog, (f) that buildlog was an earlier experiment, (g) that it's since deprecated and folded into qortex. | 7 beats in one list item. | Split aggressively. The parenthetical genealogy of buildlog belongs in a footnote or separate sentence. Core claim: "Explicit domain rules enter context when their linked concepts are activated." The buildlog history is a tangent. |

**Count: 3 violations.** Severity: HIGH. The L41 wall is the most impactful fix in the article.

---

## R25 -- "Not just X, but also Y" / "Not X but Y" / "It's not...it's..."

| # | Line | Pattern | Verdict | Fix |
|---|------|---------|---------|-----|
| 1 | L31 | "'Pass' means the framework's own test suite, not ours." | "X, not Y" contrast. | **Not a violation.** This is a factual clarification, not an LLM balancing construction. |
| 2 | L91 | "The real test isn't benchmarks; it's production." | "It's not X; it's Y." Classic R25 pattern. | **Violation.** Rewrite: "The real test is production." The reader already knows benchmarks are limited (the article just spent two sections saying so). |
| 3 | L35 | "(not pinned versions)" | Parenthetical "not X" clarification. | **Not a violation.** Factual disambiguation. |
| 4 | L59 | "the point is that swapping in a knowledge graph didn't degrade anything" | "that's not the point...the point is" structure across L57-59. | **Borderline.** The turn from "but it's disingenuous to claim" to "but that's not the point" is a double pivot. Consider collapsing: "The numbers suggest the graph layer helps on cross-cutting queries, but the sample size is too small to prove it. What matters: swapping in a knowledge graph didn't degrade anything." |

**Count: 1 clear, 1 borderline.** Severity: LOW-MEDIUM.

---

## R26 -- Restating the obvious / redundancy

| # | Line | Pattern | Verdict | Fix |
|---|------|---------|---------|-----|
| 1 | L149 | "The integration exercise proved one thing: qortex conforms to existing interfaces well enough to pass the tests that those frameworks wrote for their own backends." | This restates the article's description (L3), the table caption (L31), and the section header's implicit claim. By line 149, the reader has already absorbed this from the data. | **Violation.** The closing section opens by restating the thesis the reader already accepted 100 lines ago. Cut or compress to: "qortex passes their tests." Then move to the new information. |
| 2 | L155 | "Meanwhile, the integrations work, and CI guarantees they remain in sync." | Restates L34 ("100 adapter tests run in CI on every push") and L128 ("Adapter tests in CI guarantee we'll know ASAP when the integrations break"). Third time stating "CI keeps things working." | **Violation.** Cut. The reader knows CI runs. |
| 3 | L55 | "These are framework-provided test suites, not ours, so we cannot vouch for their rigor or reliability." | Restates L31 ("'Pass' means the framework's own test suite, not ours.") with nearly identical language. | **Violation.** Cut L55 entirely. The disclaimer at L31 already covers this. The retrieval quality section should just present the data. |

**Count: 3 violations.** Severity: HIGH. This is the article's biggest structural problem. The closing section (L147-157) is mostly restatement of claims already made. It adds only one new idea (L153: "We need more data") and one puffery line (L157: "floodgates"). The ending needs a complete rewrite.

---

## Other Rules -- Scan Results

### R2 -- Blocklist words

| Word | Found? | Location | Fix |
|------|--------|----------|-----|
| enhance | No | -- | -- |
| key (adj) | No | -- | -- |
| showcase | No | -- | -- |
| landscape | No | -- | -- |
| valuable | No | -- | -- |
| highlight (verb) | No | -- | -- |
| underscore | No | -- | -- |
| meticulous | No | -- | -- |
| load-bearing | No | -- | -- |
| pivotal | No | -- | -- |

**Count: 0 violations.** Clean.

### R3 -- Performative honesty

No instances of "Being honest:", "To be frank:", "The truth is:" found. Clean.

### R4 -- Self-referential pivots

No "This is where things get interesting" or similar. Clean.

### R5 -- Inflated significance framing

| # | Line | Quote | Verdict |
|---|------|-------|---------|
| 1 | L85 | "Why This Matters Beyond Benchmarks" | **Borderline.** "Why This Matters" is an inflated significance header. See R20 below. |

### R6 -- Hedging then inflating

No instances found. Clean.

### R9 -- Rhythmic parallel construction closers

| # | Line | Quote | Verdict |
|---|------|-------|---------|
| 1 | L81 | "When a result is accepted, the edges that led to it get a small boost. When it's rejected, they get penalized." | Mirrored parallel "When...When..." construction. | **Borderline.** This is describing a binary mechanism (accept/reject). The parallel is functional, not rhetorical. Pass. |

### R10 -- Challenges-and-future-prospects formula

No "Despite challenges..." patterns. Clean.

### R11 -- Elegant variation

| # | Pattern | Verdict |
|---|---------|---------|
| 1 | "adapters" / "adapter pattern" / "integrations" -- used in close proximity to mean the same thing. | **Borderline.** L87 says "adapter pattern," L128 says "integrations," L155 says "integrations." These are close enough to be the same concept. Pick one term and stick with it. |

### R12 -- Copula avoidance

No "serves as," "stands as," "represents a" found. Clean.

### R13 -- Dismissive 'with' framing

No violations found. Clean.

### R14 -- Vague attribution

No "experts argue" or "industry reports suggest." Clean.

### R15 -- False ranges

No "from X to Y" false ranges. Clean.

### R16 -- Superficial participle analysis

No trailing gerund clauses. Clean.

### R18 -- Colon-into-bold-statement

No violations. Clean.

### R20 -- Notability assertion sections

| # | Line | Pattern | Verdict |
|---|------|---------|---------|
| 1 | L85 | "Why This Matters Beyond Benchmarks" | **Borderline.** The section exists partly to argue that the work deserves attention. However, it also introduces the three production consumers (genuinely new information). The header is the problem, not the content. Rename the section. |

### R21 -- Blunt fragment negation

No "X. Not Y." standalone patterns found. Clean.

### R23 -- Full-clause linking

| # | Line | Quote | Verdict |
|---|------|-------|---------|
| 1 | L87 | `[This isn't something you just "get for free"](/writing/makes-it-look-easy)` | **Violation.** Full clause link. The operative concept is the article being linked to. | Rewrite: "The adapter pattern exists so that qortex can be swapped into any application already running one of these frameworks. Making that work is [its own engineering problem](/writing/makes-it-look-easy)." |

**Count: 1 violation.** Severity: LOW.

### R24 -- Mirrored affirmation pairs

No "X is real. So is Y." patterns. Clean.

### R27 -- Bare conjunction standalone paragraphs

No "But." or "And." standalone paragraphs. Clean.

### R28 -- Emotional cliche templates

| # | Line | Quote | Verdict |
|---|------|-------|---------|
| 1 | L157 | "the floodgates are already poised to open" | **Violation (also caught under R19).** "Floodgates" is an emotional cliche metaphor. | Already addressed under R19. |

**Count: 1 violation (overlap with R19).**

---

## Staleness Check

| # | Line | Claim | Risk | Verify |
|---|------|-------|------|--------|
| 1 | L23 | "46/49 pass" (CrewAI) | **HIGH.** Test counts change with framework releases. The article pins to "latest" versions in CI, so these numbers shift. | Run CI and update the table. |
| 2 | L24-29 | All test counts in the table (12/12, 26/26, 47, ~40, 31/31) | **HIGH.** Same issue. Any framework update changes these. | Either (a) pin to a date ("as of 2026-02-22") or (b) link to the live CI badge instead of hardcoding numbers. |
| 3 | L34 | "100 adapter tests" | **MEDIUM.** This total will change as adapters are added or tests grow. | Consider: "All adapter tests run in CI on every push." Drop the exact number. |
| 4 | L39 | "29 MCP tool calls over real stdio in 3.94 seconds, with a one-time ~400ms server spawn" | **MEDIUM.** These are specific benchmark numbers that will shift with code changes. | Pin to a commit or date. |
| 5 | L41 | "35+ endpoints" | **MEDIUM.** Endpoint count changes with API development. | Consider: "a Starlette ASGI server with dozens of endpoints" or pin to a version. |
| 6 | L33 | "CrewAI recently replaced its DB layer" | **HIGH (staleness language).** "Recently" is time-relative. When did this happen? In six months, "recently" will be wrong. | Replace with a specific version or date: "CrewAI replaced its DB layer in v0.X." |
| 7 | L71 | "benchmarks against the REST API are forthcoming" | **MEDIUM.** "Forthcoming" goes stale if they haven't shipped by publication. | Either publish them before the article goes live, or cut the promise. |

---

## Pelekification Check

### Line breaks as breath marks

The article is mostly well-structured but misses opportunities for breath marks:

| # | Line | Current | Suggestion |
|---|------|---------|------------|
| 1 | L59 | "the point is that swapping in a knowledge graph didn't degrade anything. The retrieval quality is at least as good, with room to improve as the graph matures." | The core claim ("didn't degrade anything") deserves its own line. Break after "degrade anything." Let it land. |
| 2 | L83 | "We're not sure yet. That's what we're testing." | These two sentences are doing the right thing (standalone landing). But they'd hit harder as a single visual unit separated from the paragraph above. Pull them out of the paragraph. |

### Colon extension

The article uses colons well in several places (L13, L59, L71, L149). No gaps.

### Ellipsis for trailing thought

**Missing.** The article has no ellipses. L83 ("We're not sure yet.") is a natural candidate for an ellipsis trail if hesitation is the intended register: "We're not sure yet...that's what we're testing." But the current period-period construction is also fine. Not a gap, just a missed texture opportunity.

### Semantic punctuation

| # | Line | Current | Issue |
|---|------|---------|-------|
| 1 | L91 | "The real test isn't benchmarks; it's production." | Semicolon used correctly for parallel contrast. Good. (Though the sentence itself is an R25 violation.) |
| 2 | L15 | Comma splice candidate: "It's early, but we decided to build adapters..." | Fine as-is. |

### Bold for weight not decoration

| # | Line | Current | Issue |
|---|------|---------|-------|
| 1 | L35 | "the **latest** versions" | **Good use.** "Latest" carries the argumentative weight (not pinned). |
| 2 | L77 | "**Vector similarity**", "**Graph traversal**", "**Rule projection**" | Bold on list item headers. This is structural labeling, not argumentative weight. | **Acceptable** for a numbered list, but note that these bolds serve as sub-headers, not emphasis. |
| 3 | Missing bold opportunities | L59: "didn't degrade anything" is the core claim of the Retrieval Quality section but has no typographic weight. L149: "proved one thing" could bold the one thing. | Consider bolding "didn't degrade anything" at L59. |

### Semicolons for parallel actions

Only one semicolon in the article (L91). The parallel constructions at L81 ("When a result is accepted...When it's rejected...") could use a semicolon to bind them: "When a result is accepted, the edges get a boost; when it's rejected, they get penalized."

---

## Severity Summary

| Severity | Rules | Violation Count |
|----------|-------|-----------------|
| **HIGH** | R22 (wall paragraphs x3), R26 (restatement x3) | 6 |
| **MEDIUM** | R19 (puffery x1 + 2 borderline), R25 ("not X it's Y" x1) | 2 clear + 3 borderline |
| **LOW** | R7 (punchy fragment x1), R8 (borderline tricolon x1), R23 (full-clause link x1), R28 (cliche x1, overlaps R19) | 3 clear + 1 borderline |

---

## Prioritized Fix List

### 1. Rewrite the closing section (L147-157) -- R26, R19, R28

**Impact: HIGH.** The "What This Shows" section is the weakest part of the article. It restates the thesis (L149), restates that CI works (L155), and ends with a puffery cliche (L157). The only new information is L153 ("We need more data, domains, feedback, and time").

**Direction:** Cut L149 entirely (or compress to 5 words). Cut L155 (third restatement of CI). Cut L157 (floodgates). Keep L151 and L153. End on L153 or on a forward-looking concrete claim (what specifically happens next). The article's best closing candidate is already at L83: "We're not sure yet. That's what we're testing." Consider whether the current closing section adds anything the article hasn't already said.

### 2. Break the L41 wall paragraph -- R22

**Impact: HIGH.** Line 41 is a single sentence packing 8 distinct facts about the REST API (server type, endpoint count, auth methods, client type, protocol compatibility, language agnosticism, adapter carry-over). No reader absorbs all of that in one pass.

**Direction:** Break after "local client." ("...an async `HttpQortexClient` that speaks the same protocol interface as the local client.") New paragraph: "Any application in any language can query qortex over the network. The adapter pattern and test scaffolding carry over directly."

### 3. Break the L79 rule projection wall -- R22

**Impact: MEDIUM.** The rule projection list item tries to explain what rules are, how they enter context, their relationship to the general system, their legacy status, their connection to buildlog, buildlog's history, and buildlog's deprecation. Seven beats in one list item.

**Direction:** Core claim: "Explicit domain rules enter context when their linked concepts are activated." Everything about buildlog genealogy goes in a parenthetical footnote or a separate sentence after the list.

### 4. Cut the L55 restatement -- R26

**Impact: MEDIUM.** "These are framework-provided test suites, not ours, so we cannot vouch for their rigor or reliability" restates L31 ("'Pass' means the framework's own test suite, not ours"). The disclaimer was already made. The retrieval quality section should present data without re-disclaiming.

**Direction:** Delete L55. The data table and the hedging at L57 ("it's disingenuous to claim...") already provide the necessary epistemic humility.

### 5. Fix "not X; it's Y" at L91 -- R25

**Impact: LOW-MEDIUM.** "The real test isn't benchmarks; it's production." is an LLM balancing construction. The reader already knows benchmarks are limited.

**Direction:** "The real test is production." Five words. Done.

### 6. Fix full-clause link at L87 -- R23

**Impact: LOW.** `[This isn't something you just "get for free"](/writing/makes-it-look-easy)` links a full clause instead of the operative concept.

**Direction:** "Making that work is [its own engineering problem](/writing/makes-it-look-easy)." or "The adapter pattern isn't free; building it was [its own project](/writing/makes-it-look-easy)."

### 7. Pin or remove staleness-prone numbers -- Staleness

**Impact: MEDIUM (over time).** Six specific numbers in the article (test counts, endpoint counts, MCP timing) will go stale as the project evolves. "Recently" at L33 is already a time bomb.

**Direction:** Either (a) add "as of 2026-02-22" to the benchmark table, (b) link to live CI badges instead of hardcoding test counts, or (c) remove exact numbers in favor of "all tests pass" language. Replace "recently" with a version number or date.

### 8. Kill "floodgates" and "(we don't deal in 'ifs')" at L157 -- R19, R28

**Impact: LOW but important for credibility.** The article earns trust through honest hedging ("We're not sure yet," "it's disingenuous to claim"). The final sentence undercuts all of that with swagger and a cliche metaphor.

**Direction:** Delete L157 entirely. End on L155 or L153. Or, if you want a forward-looking close: "The distribution infrastructure is in place. Now we need the data to prove the thesis."

---

## Notes

The article is remarkably clean for a Claude first draft. Zero blocklist words, zero em dashes, zero performative honesty, zero self-referential pivots. The honest hedging throughout (L57, L59, L83) is the article's greatest strength and the reason the closing puffery (L157) is so jarring -- it violates the contract the article spent 150 lines building.

The structural issues (R22 walls, R26 restatement) are the highest-priority fixes. The content is solid; the packaging needs tightening.
