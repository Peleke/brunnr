# Bragi Review: recursive-dogfood
# Date: 2026-03-09
# Source: article-draft skill (28-rule Bragi Prose Gate)

Here is the Bragi review of "Recursive Dogfood."

---

## Bragi Review: "Recursive Dogfood"

### R1 [bragi:c33015a1] Em-dash overuse

No em dashes visible in the provided text. **Pass.**

---

### R7 [bragi:d720e228] Punchy fragment marketing copy

Multiple violations, concentrated in the closing sections:

1. **"The vault is real. The files are there. The links resolve."** -- Three staccato fragments in sequence. This is tagline energy, not technical writing. The claim is already made by the preceding sentence; these fragments just thump the podium.

2. **"That sentence sounds like a party trick. The vault artifacts prove it happened."** -- Two-sentence mic drop. The first sentence preempts criticism by naming it; the second answers with a fragment-length assertion. This is ad copy structure: objection, then slogan.

3. **"The pipeline worked."** (end of second section) -- Standalone sentence-as-paragraph. Fine once. But the article uses this pattern at least four times, and by the closing it reads as a tic.

4. **"The recursion bottoms out at the vault."** -- Another standalone declarative doing rhetorical work that the surrounding evidence should be doing instead.

**Fix direction:** Merge these fragments into their preceding paragraphs. Let the evidence table at the end carry the weight instead of hammering standalone declarations after it.

---

### R8 [bragi:e30cf4d5] Rhythmic parallel construction closers

**"Three layers of recursion"** section:

> The pipeline generated the data. The deck pitched the pipeline. The narrative-pass rewrote the deck. The persona came from the pipeline's own persona-extract run.

This is a chain of parallel subject-verb-object sentences building to a crescendo. It reads like a sermon closer. The structure is doing the persuading, not the content.

Also the final line of "What This Proves":

> "...validated itself as a business idea, then generated its own pitch deck, then wrote its own performance script using a persona it extracted from its own signal scan."

Three parallel "then" clauses. Same pattern.

**Fix direction:** Break the parallelism. Vary sentence length and structure. One compound sentence with a subordinate clause will do more than four rhythmically identical declarations.

---

### R19 [bragi:463490f1] / R12 [bragi:02959dda] Self-congratulatory tone / Promotional puffery

This is the structural risk of the entire article. The premise is "I pointed my tool at itself and it said I should sell it." The article needs to work harder to earn the reader's trust, because the default reading is: "man builds validation machine; machine validates man; man writes article about how validated he is."

Specific hotspots:

1. **"54 out of 60. Thirteen points above the next alternative."** -- Presented without interrogation. The reader's first question is "who calibrated the scoring?" and the article never answers it.

2. **"The pipeline scored its own productization higher than anything else it had ever evaluated."** -- This is the most self-congratulatory sentence in the piece. It needs immediate, aggressive qualification. The one-line bias check mention ("Moderate excitement bias detected") is not enough; it reads as a fig leaf.

3. **"Each layer consumed the output of the layer below it"** -- Framed as profound. It is just... how pipelines work. The recursion is interesting; calling it profound is puffery.

4. **"That sentence sounds like a party trick."** -- Pre-emptive self-awareness does not neutralize the problem. It signals the author knows the tone is off but chose to keep it anyway.

**Fix direction:** Lead with the bias check, not the score. Dedicate a full paragraph to why self-evaluation is structurally suspect. Then present the score as "despite that caveat, here's what the numbers said." The article currently buries the caveat and leads with the brag.

---

### R22 -- Wall paragraphs

Two sections contain dense multi-sentence paragraphs with no visual breaks:

1. **"The Prior Runs"** -- The March 5 run paragraph packs signal count, subreddit names, persona count, SDP score, landing page line count, SVG count, email sequence count, and kill criteria into one block. That is at least five distinct data points crammed into prose. Use a table or a short bulleted list.

2. **"The Evidence"** -- The paragraph about Playwright scraping mixes sourcing methodology, attribution claims, and tool names. Split the "every quote came from a real person" claim from the technical details of how scraping worked.

3. **"The Ejection"** -- "68 commits. 21 skills across 5 categories. A JSON Schema..." is data masquerading as prose. Table it.

**Fix direction:** Any time you have three or more numeric facts in a paragraph, pull them into a list or table. The article already uses tables and SVGs elsewhere; be consistent.

---

### R26 [bragi:e4d6eee0] Thesis restated too many times

The core claim -- "the pipeline validated itself" -- appears in at least five distinct phrasings:

1. "The pipeline scored its own productization higher than anything else it had ever evaluated."
2. "a well-structured skill pipeline can turn its own output into its own input and produce something worth shipping"
3. "It validated itself by applying the same rigor it applies to everything else"
4. "The pipeline that validates business ideas validated itself as a business idea, then generated its own pitch deck..."
5. "The vault artifacts prove it happened."

Each rephrasing adds nothing the previous one did not say. By the fifth, the reader is being lectured.

**Fix direction:** State the thesis once in "What This Proves." Cut or subordinate the other four instances. Trust the evidence sections to carry the argument. The recursive run data is genuinely interesting; the repetition makes it feel like the author doesn't trust the data to land.

---

### R17 [bragi:92b40f51] Hedging with 'not' lists

> "Not that AI agents can replace product thinking. They cannot."

Classic R17. This is defining your thesis by what it is not, then using a staccato negation for emphasis. The reader doesn't yet know what the thesis IS, so the negation is evasive.

**Fix direction:** Lead with the positive claim. "The recursive run proves something narrower and more useful: [claim]." Delete the "Not that..." opener entirely. If the distinction from AGI hype matters, put it in a parenthetical or footnote, not as the section's opening gambit.

---

### Staleness Check

The article is pinned to specific dates and relative time references that will rot:

- "Four weeks ago" (lede, first sentence)
- "February 8", "February 12", "March 5", "March 6, 2:00 PM"
- "37 signals" (appears twice), "42/60", "50/60", "54 out of 60", "1,493-line", "68 commits", "21 skills", "18-slide"

The dates are fine in a "Field Notes" category if the publication date is visible. But "Four weeks ago" in the lede will be wrong within days of publication. Replace with a concrete anchor: "In early February" or just drop the temporal framing and start with the monorepo fact.

The numeric counts (37 signals, 1,493 lines, 68 commits) are evidence and should stay, but consider whether the reader needs all of them or whether they blur together into "lots of numbers that prove I did work."

---

### Pelekification Opportunities

1. **The lede buries the hook.** "Four weeks ago I had 29 AI agent skills in a monorepo" is inventory, not tension. The actual hook is the agent's observation: "You built an entire product discovery pipeline and forgot to use it on yourself." Consider opening with that quote, then backing into the setup.

2. **The series cross-references are dutiful, not useful.** "Article 1... Article 2... Article 3... This article covers..." reads like a table of contents, not prose. Either cut this to a single sentence with links or move it to a callout box. It interrupts the narrative momentum.

3. **"The Narrative Layer" section is the most interesting part and it's buried.** The fact that you built a new skill (narrative-pass) during the session to fix lifeless speaker notes is a genuinely compelling detail. It demonstrates builder instinct in real time. Promote this higher or give it more space.

4. **The Receipts table is strong.** It does what the repeated thesis statements try to do, but with actual evidence. Let it be the closing argument. Cut the prose after it to one sentence maximum.

5. **Voice inconsistency.** The technical sections (Prior Runs, Ejection) read like buildlog entries. The closing sections (What This Proves, Receipts) read like conference talk scripts. Pick one register. Given the "Field Notes" category, the buildlog voice is the right one -- which means the closers need to come down in temperature.

---

### Summary Scorecard

| Rule | Severity | Count | Verdict |
|------|----------|-------|---------|
| R1 (em dashes) | -- | 0 | Pass |
| R7 (punchy fragments) | High | 4+ | Fail -- concentrated in closing sections |
| R8 (parallel closers) | Medium | 2 | Fail -- "three layers" section + final sentence |
| R17 (hedging with not) | Medium | 1 | Fail -- "What This Proves" opener |
| R19 (self-congratulatory) | High | 4 | Fail -- structural risk across article |
| R22 (wall paragraphs) | Medium | 3 | Fail -- Prior Runs, Evidence, Ejection |
| R26 (thesis repetition) | High | 5 | Fail -- same claim stated 5 times |

**Overall:** The evidence is real and the recursive premise is genuinely interesting. The article's main problem is not trusting the evidence to speak. It keeps restating the thesis in increasingly sermonic registers, which undermines the very rigor it claims to demonstrate. Fix the tone and the structure is sound.