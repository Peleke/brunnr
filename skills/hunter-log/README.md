# hunter-log

## A Masterclass in Structured Decision Logging for Product Discovery

*Why the best product thinkers treat every decision like a trade in their portfolio — and how you can start today.*

---

## Table of Contents

1. [The Discipline: Decision Intelligence and Knowledge Management](#the-discipline)
2. [Why Logging Matters (Convince the Skeptical Engineer)](#why-logging-matters)
3. [Frameworks for Decision Logging](#frameworks-for-decision-logging)
4. [The Lingo](#the-lingo)
5. [The Process: How hunter-log Works](#the-process)
6. [Obsidian as the Tool](#obsidian-as-the-tool)
7. [The Anti-Patterns](#the-anti-patterns)
8. [Case Studies](#case-studies)
9. [The Provenance Chain Framework](#the-provenance-chain-framework)
10. [Further Reading](#further-reading)

---

## The Discipline

You are an excellent engineer. You can build anything. But here is a question that should make you uncomfortable: **can you explain, right now, why you chose to build the last three things you built?** Not a hand-wavy "it seemed like a good idea." The actual inputs. The alternatives you rejected. The confidence level you had. The information you wished you had but did not.

If you cannot, you are flying blind on the most consequential decisions in your business — and you are not alone. Most technical founders treat product decisions like throwaway code: make them, move on, never review.

This is a mistake, and it is the mistake this entire system exists to fix.

### What Is Decision Intelligence?

Decision intelligence is an emerging discipline at the intersection of data science, social science, and managerial science. It is not about making perfect decisions. It is about building a **systematic process** for making decisions, recording them, reviewing them, and improving over time. The same way you would never ship code without version control, you should never ship a product decision without a decision log.

The field draws from multiple traditions, each of which contributes something essential.

**Annie Duke — Thinking in Bets (2018).** Duke is a former professional poker player turned decision strategist. Her central insight: **every decision is a bet on an uncertain future, and the quality of the decision is independent of the outcome**. A good decision with a bad outcome is still a good decision. A bad decision with a good outcome is still a bad decision. She calls the mistake of judging decisions by their outcomes "resulting," and it is the single most common error in product thinking. Her framework: record your decisions with confidence levels *before* you know the outcome. Then review whether your confidence was calibrated, not whether the outcome was good. This is the intellectual backbone of everything hunter-log does.

**Daniel Kahneman — Thinking, Fast and Slow (2011).** Kahneman won the Nobel Prize for demonstrating that human judgment is riddled with systematic biases. Two are especially relevant here. First, **hindsight bias**: after you know an outcome, your brain rewrites history to make it seem inevitable. ("I always knew that product would fail.") Second, **noise**: inconsistency in judgments that should be identical. On different days, in different moods, with different framing, you will make different decisions about the same problem. Logs are the antidote to both. They freeze your reasoning at the moment of decision, before hindsight can corrupt it.

**Gary Klein — Sources of Power (1998).** Klein is the father of recognition-primed decision making (RPD), the study of how experts actually make decisions in high-stakes, time-pressured environments. His research on firefighters, ICU nurses, and military commanders found that experts do not weigh options in a spreadsheet — they pattern-match from experience and simulate forward. His critical contribution to logging: **the pre-mortem**. Before committing to a decision, imagine it is six months from now and it failed spectacularly. Then write down why. This forces you to articulate risks while you are still emotionally detached enough to see them. Log the pre-mortem alongside the decision.

**Tiago Forte — Building a Second Brain (2022).** Forte's PARA method (Projects, Areas, Resources, Archive) is the organizational backbone of personal knowledge management. His key insight: your brain is for having ideas, not storing them. **Offload storage to an external system so your brain can focus on connections and creativity.** His concept of "progressive summarization" — highlight on first pass, bold on second pass, extract on third — is how you turn raw notes into usable knowledge without spending all your time organizing.

**Sonke Ahrens — How to Take Smart Notes (2017).** Ahrens popularized the Zettelkasten method outside of German academia. The method's power comes from **atomic notes** (one idea per note) that are **heavily interlinked**. The value is not in any single note but in the connections between notes. Applied to product discovery: each signal, each decision, each persona, each offer is an atomic note. Over time, the links between them reveal patterns you would never see in a flat list. This is why we use Obsidian.

**Ray Dalio — Principles (2017).** Dalio built Bridgewater Associates into the world's largest hedge fund by systematizing decision-making with radical transparency. His framework: **write down your principles (if-then rules) and update them when reality contradicts them.** Applied to solo product work: you are both the decision-maker and the reviewer. Your log IS your set of principles, evolving in real time. His concept of "believability-weighted decision making" — weighting opinions by demonstrated competence — maps to tracking your own calibration across different domains. You might discover you are 80% accurate on technical feasibility estimates but only 40% accurate on pricing.

**Jeff Bezos — Shareholder Letters on Decision-Making.** Bezos introduced the distinction between **Type 1 decisions** (irreversible, high-stakes — walk through a one-way door) and **Type 2 decisions** (reversible, lower-stakes — walk through a two-way door). Most product decisions are Type 2 but get treated as Type 1, causing analysis paralysis. Bezos argues that Type 2 decisions should be made quickly by individuals, not slowly by committees. The log lets you move fast on Type 2 decisions (ship a $29 PDF tomorrow) while being rigorous on Type 1 decisions (choosing your entire brand direction).

**Ben Horowitz — The Hard Thing About Hard Things (2014).** Horowitz's contribution is honesty about uncertainty. There is no formula. There is no algorithm. You are making decisions with incomplete information under time pressure, and that is never going to change. The discipline is not eliminating uncertainty but **making the best decision you can with what you know, recording it, and learning from the result.** His framework: when there is no good answer, pick the least bad one and execute decisively. Then log why.

**Shane Parrish — Farnam Street / The Great Mental Models.** Parrish curates mental models — reusable thinking frameworks drawn from physics, biology, economics, psychology, and other fields. Relevant models for product decisions: **inversion** (instead of "how do I succeed?" ask "how would I guarantee failure?"), **second-order thinking** (if this works, what happens next?), **map vs. territory** (your model of the market is not the market). Logs are where you practice applying these models until they become instinctive.

**Philip Tetlock — Superforecasting (2015).** Tetlock ran a massive study of prediction accuracy and found that the best forecasters share a trait: they **track their predictions quantitatively and update their confidence based on results**. They assign probabilities, not vibes. They say "I am 70% confident this will work" and then check whether things they said were 70% likely actually happened 70% of the time. This is confidence calibration, and it is one of the most powerful things a decision log enables.

**Richard Feynman.** "The first principle is that you must not fool yourself, and you are the easiest person to fool." Feynman's razor applies directly. Without a log, you WILL fool yourself. You will remember your successful decisions as more deliberate than they were and your failed decisions as more unlucky than they were. The log is your defense against self-deception.

---

## Why Logging Matters

You are skeptical. You build things for a living, and you are good at it. Why would you add process overhead to something that is fundamentally about shipping fast?

Here are the concrete, engineering-brained reasons.

### Resulting Will Destroy Your Judgment

Annie Duke's concept of "resulting" is this: you judge a decision by its outcome rather than by the process that produced it. A startup ships a feature on gut feel, it works, and the founder concludes their gut is reliable. Another startup does rigorous research, ships a well-reasoned product, and it flops because of bad timing. The first founder "learns" to trust their gut. The second "learns" that research is a waste of time. Both lessons are wrong. The outcome was largely determined by factors outside the decision itself. But without a log of the actual reasoning, you cannot distinguish a good decision with a bad outcome from a bad decision with a good outcome. Over dozens of product decisions, resulting will systematically corrupt your judgment. You will double down on lucky guesses and abandon sound processes that happened to fail once.

### Hindsight Bias Will Rewrite Your Memory

After you know an outcome, your brain *literally rewrites your memory* of what you believed before the outcome. This is not a metaphor. It is a well-documented cognitive phenomenon Kahneman calls "creeping determinism." You will look at a failed product and think "I always had a bad feeling about that." You probably did not. You will look at a successful product and think "I knew that was going to work." You might not have. Without a written record captured at the moment of decision, you have no way to know what you actually thought. Your memory is not a recording device — it is a story generator, and it optimizes for narrative coherence over accuracy.

### Pattern Recognition Requires Data

After you log 20 product decisions with rationale, confidence levels, and outcomes, something remarkable happens: you start seeing YOUR patterns. Not generic human biases — YOUR specific tendencies. Maybe you consistently overestimate how fast you can ship. Maybe you underestimate your audience's willingness to pay. Maybe you are great at identifying pain points but terrible at picking distribution channels. These patterns are invisible without data. With data, they become your most valuable asset — the meta-knowledge that makes every future decision better.

### Knowledge Compounds

Each logged decision makes future decisions faster and better. When you face a new product decision and can pull up three previous decisions in similar domains — with your original reasoning, the outcome, and what you learned — you are not starting from zero. You are starting from experience that has been captured, structured, and made searchable. This is the difference between 10 years of experience and 1 year of experience repeated 10 times. The log is what converts lived experience into compounding knowledge.

### Accountability Without Blame

Solo founders have a unique problem: nobody reviews their decisions. There is no board, no co-founder, no product review. This can feel liberating, but it is actually dangerous. The log serves as your accountability partner. Not to judge or blame, but to force you to articulate your reasoning BEFORE you act. The act of writing down "I am doing X because of Y, and I am Z% confident" makes you think harder than you would otherwise. It is the same principle as rubber duck debugging: explaining your reasoning to an external system (even a text file) improves the reasoning itself.

### The Trader's Journal Analogy

Professional traders are REQUIRED to keep a trading journal. Every trade. Entry price, exit price, thesis, emotional state, market conditions, whether the trade followed their rules or was impulsive. Why? Because without a journal, traders fall prey to the same biases that kill product decisions — resulting, hindsight bias, overconfidence, sunk cost fallacy. The trading journal is not optional in professional trading. It is considered a survival skill.

Product decisions are trades. You are betting time, money, and energy on an uncertain outcome. You have a thesis (this product will solve this pain for this audience at this price), entry criteria (signals that justify the bet), exit criteria (what would make you kill it), and an emotional state that influences everything. Every argument for a trading journal applies to a product decision journal. The only reason product people do not keep them is that nobody taught them to.

---

## Frameworks for Decision Logging

### Annie Duke's Decision Journal

The simplest and most powerful framework. For every significant decision, record:

| Field | What to Write | Example |
|-------|--------------|---------|
| **Date** | When you made the decision | 2026-02-08 |
| **Decision** | What you decided to do | Ship "DevOps Decision Guide" as first product |
| **Options considered** | What alternatives you evaluated | Cybersecurity roadmap, tutorial hell guide, Notion templates |
| **Confidence level** | Your honest probability of success (%) | 65% — strong signals but first time selling |
| **Rationale** | Why this option over the others | Richest signal density, highest price tolerance, strongest edge |
| **Information you had** | What data informed the decision | Signal scan with real Reddit quotes, Udemy pricing data, competitive gap analysis |
| **Information you wished you had** | What would have made you more confident | Actual conversion data, direct customer conversations, competitor revenue numbers |
| **Pre-mortem** | "If this fails in 6 months, why?" | Distribution channel unclear, might not reach target audience, PDF format might be wrong for this persona |
| **Kill criteria** | What would make you abandon this | Zero sales after 2 weeks of distribution effort, negative feedback on framing |
| **Review date** | When to revisit this decision | 2026-03-08 |

**The monthly review.** At the end of each month, go back and compare your predicted outcomes with actual outcomes. Were you as confident as you should have been? Did the risks you pre-mortem'd actually materialize? Were there risks you missed? Update your calibration.

The key question in review is NOT "did it work?" It is: **"Given what I knew at the time, was this a good decision?"** These are different questions, and conflating them is the source of most learning failures.

### Gary Klein's Pre-Mortem

The pre-mortem is so important it deserves its own section. Here is the exercise:

1. You have made a decision. You are about to commit resources.
2. BEFORE you commit, stop. Close your eyes. Imagine it is six months from now.
3. Imagine the decision **failed spectacularly**. Not a quiet failure — a disaster.
4. Now: write down **why it failed**. Be specific. Name the failure mode.
5. Log this alongside the decision.

Why this works: once you have committed to a decision emotionally, your brain actively suppresses risk signals. You want to believe it will work, so you discount evidence that it will not. The pre-mortem hacks this by asking you to imagine the failure as already having happened. This gives your brain "permission" to generate risks, because you are not arguing against your own decision — you are explaining a fait accompli.

Klein's research shows that pre-mortems increase the ability to identify reasons for future outcomes by 30%. Thirty percent more risks identified, just by changing the framing from "what could go wrong?" to "it went wrong — why?"

### Ray Dalio's Believability-Weighted Decision Making

Dalio's system at Bridgewater weighs every opinion by the speaker's track record. In a meeting, the opinion of someone who has been right 9 out of 10 times on this type of question counts more than the opinion of someone who has been right 3 out of 10 times.

Applied to solo founder work, this becomes **self-calibration by domain**. After 20+ logged decisions, you can calculate your track record across different types of judgments:

- **Technical feasibility estimates**: "I said I could build it in 1 day. I actually built it in 1 day 14 out of 15 times. I am well-calibrated here."
- **Pricing estimates**: "I predicted willingness to pay at $49. Actual successful price was $29 three out of four times. I consistently overestimate."
- **Market timing**: "I said 'now is the right time' for 6 products. Two succeeded. I am not reliable on timing."
- **Distribution predictions**: "I said I would get traction on Reddit for 4 products. I got traction for 1. My distribution intuition is weak."

This data is gold. It tells you where to trust yourself and where to seek outside input. You cannot generate it without a log.

### Tiago Forte's PARA Method (Applied to Product Discovery)

PARA is an organizational framework. It answers "where does this note go?" with four categories:

**Projects** are active product bets with a defined outcome and deadline. In the hunter pipeline, these are the offers you are building right now. "Ship DevOps Decision Guide by Friday" is a project.

**Areas** are ongoing domains of responsibility with no end date. In your case: DevOps education, programming education, cybersecurity education. You continuously scan these areas for signals. They do not "finish."

**Resources** are reference material you might need someday. Signal scans, persona research, competitive analyses, pricing benchmarks. Not tied to a current project, but valuable to store and search.

**Archive** is completed or killed projects, moved out of active view but preserved with lessons learned. This is where failed products go — and it is the most valuable folder, because failures teach more than successes.

The mapping to hunter-log's vault structure:

| PARA Category | Vault Folder | Contents |
|---------------|-------------|----------|
| Projects | Offers/ | Active offer specs being built |
| Areas | Signal Scans/ | Ongoing domain scans |
| Resources | Personas/, Decisions/ | Reference material and recorded decisions |
| Archive | (status: archived in frontmatter) | Killed products, completed ships with retros |

### Zettelkasten / Atomic Notes (Applied to Signals)

The Zettelkasten ("slip box") was invented by German sociologist Niklas Luhmann, who used it to write 70+ books and nearly 400 academic articles. The method is simple in principle, profound in practice:

1. **One idea per note.** Each note is "atomic" — it captures one insight, one signal, one observation.
2. **Every note has a unique identifier.** In our system, this is the frontmatter `type` + `date` + slug.
3. **Notes link to each other.** A pain signal links to the persona who feels it. The persona links to the offer designed for them. The offer links back to the decision that selected it. These links are bidirectional (Obsidian wikilinks with backlinks).
4. **The value is in the connections, not the notes.** A single signal scan is useful. Twenty signal scans with interlinked personas, decisions, and offers form a knowledge graph that reveals cross-domain patterns you would never see otherwise.

Applied to product discovery: each signal is an atomic note. "DevOps engineers spend 6-15 hours per week on tool sprawl" is one note. "Mid-level DevOps engineer, 2-4 years experience, overwhelmed by tool complexity" is another. The link between them — pain to persona — is where the insight lives. Over time, you might discover that the same persona archetype appears across cybersecurity, DevOps, AND programming education. That cross-domain insight creates a brand opportunity that no single scan would reveal.

This is exactly what happened in the initial hunter scan. The meta-signal — "education over-indexes on tool tutorials and under-indexes on systems thinking" — emerged from cross-signal connections, not from any single data point.

---

## The Lingo

A vocabulary for precise thinking about product decisions. Use these terms in your logs to be specific about what you mean.

**Decision quality vs. outcome quality.** (Annie Duke) A good decision can produce a bad outcome. A bad decision can produce a good outcome. Quality of decision and quality of outcome are correlated but NOT the same. The log helps you evaluate decision quality independently of outcome.

**Resulting.** (Annie Duke) Judging decisions by their outcomes. "We shipped the feature and revenue went up, so the decision was good." This is a fallacy. Revenue might have gone up for unrelated reasons. The log protects you by freezing your reasoning at the moment of decision.

**Hindsight bias / creeping determinism.** (Kahneman) After knowing the outcome, your brain makes it seem inevitable. Logs capture what you ACTUALLY thought before you knew.

**Confidence calibration.** (Tetlock) Are you as right as often as you think? If you say you are 80% confident about 10 things, approximately 8 of them should turn out to be right. If only 4 do, your confidence is miscalibrated. Track this over time.

**Pre-mortem.** (Klein) "Imagine this already failed. Why?" Done BEFORE committing. Identifies risks your optimism is hiding.

**Post-mortem.** (Standard practice) "What happened and why?" Done AFTER an outcome. Less powerful than a pre-mortem because hindsight bias is already active, but still valuable — especially when paired with the pre-decision log.

**Kill criteria.** Define failure conditions BEFORE you start. "If I have zero sales after two weeks of active distribution, I will kill this product and do a retro." Without kill criteria, the sunk cost trap takes over.

**Sunk cost trap.** Continuing because you have already invested time and money, not because it is working. "I already spent a week on this, I cannot stop now." Yes you can. Kill criteria prevent this.

**Opportunity cost.** What you are NOT building because you are building this. Every "yes" is a "no" to something else. Log the alternatives you rejected — you may come back to them.

**Reversible vs. irreversible decisions.** (Bezos Type 1 / Type 2) Type 1 decisions are one-way doors — hard to reverse, high stakes, deserve thorough analysis. Type 2 decisions are two-way doors — easy to reverse, lower stakes, should be made quickly. Most product decisions are Type 2. Shipping a $29 PDF is Type 2. Choosing your entire brand direction is closer to Type 1. Log both, but allocate analysis time accordingly.

**Signal vs. noise.** Is this data meaningful or random? One Reddit post is noise. Fifty Reddit posts with the same complaint are signal. The log accumulates data points so you can distinguish between them over time.

**Base rate.** What is the background success rate for this type of bet? If the base rate for first-time info products is 10% profitability, your 65% confidence needs serious justification.

**Second-order effects.** If this works, what happens next? If DevOps Decision Guide sells, you have validated the "post-tutorial gap" thesis across domains. That is more valuable than the revenue. If it fails, what do you learn? You learn about distribution, pricing, and audience — which makes the next bet better.

**Provenance.** Where did this data come from? How trustworthy is it? A Reddit post with 500 upvotes is stronger provenance than a blog post by someone selling a competing product. Log your sources.

**Progressive summarization.** (Forte) Layer your highlights over multiple passes. First pass: highlight key sentences. Second pass: bold the highlights that matter most. Third pass: extract the bolded content into a summary. This prevents both over-processing (spending hours organizing a note you read once) and under-processing (never extracting value from raw notes).

**Atomic notes.** (Zettelkasten) One idea per note. Heavily linked. Small notes are more reusable and more linkable than long documents.

**Graph thinking.** The connections between notes are as valuable as the notes themselves. A pain signal connected to three personas and two offers tells you more than any of those five notes in isolation.

**Backlinks.** The reverse link. In Obsidian, if Note A links to Note B, Note B automatically shows a backlink to Note A. This means you can navigate forward (scan to decision to persona to offer) AND backward (offer back to its originating pain signals). This bidirectional navigation is what makes provenance chains work.

**Knowledge compounding.** Each note makes future notes more valuable because there are more nodes to link to. The 50th signal scan connects to 49 previous scans. Patterns that were invisible at scan 5 become obvious at scan 50.

**Spaced repetition.** Reviewing old decisions at intervals (1 week, 1 month, 3 months) to extract patterns and update your calibration. The `revisit_by` field in decision frontmatter is a spaced repetition trigger.

---

## The Process

hunter-log is the **persistence layer** for the hunter product discovery pipeline. It does not do analysis. It does not make decisions. It formats structured output and saves it to Obsidian with proper frontmatter, cross-links, and tags.

### Pipeline Architecture

```
signal-scan --> decision-log --> persona-extract --> offer-scope
                                                        |
                              hunter-log (saves everything to Obsidian)
```

Each skill in the pipeline produces a JSON output wrapped in a `PipelineEnvelope`:

```typescript
interface PipelineEnvelope {
  skill: "signal-scan" | "decision-log" | "persona-extract" | "offer-scope"
  version: "1.0"
  session_id: string      // Ties this pipeline run together
  timestamp: string       // ISO 8601
  input_refs: string[]    // What artifacts fed into this output
  output: SkillOutput     // The skill-specific payload
}
```

hunter-log receives an envelope and:

1. **Determines document type** from `envelope.skill` (maps to a vault folder and frontmatter schema)
2. **Generates Obsidian-compatible markdown** with proper YAML frontmatter, wikilinks, and hierarchical tags
3. **Saves to the correct directory** in the vault (`Signal Scans/`, `Decisions/`, `Personas/`, `Offers/`)
4. **Updates the kanban board** (`Pipeline.kanban.md`) with the new artifact's status
5. **Updates the session log** (`Sessions/session-{id}.md`) to tie this pipeline run together chronologically
6. **Creates cross-links** between documents using wikilinks, enabling Obsidian's graph view and backlink navigation

### Vault Structure

```
ClawTheCurious/
  Product Discovery/
    Pipeline.kanban.md          # Master kanban board (visual pipeline tracking)
    Plan.md                     # Index page with live Dataview queries
    Signal Scans/               # One file per domain scan
    Decisions/                  # One file per decision (with pre-mortem + kill criteria)
    Personas/                   # One file per persona deep-dive
    Offers/                     # One file per offer spec
    Sessions/                   # Session logs tying pipeline runs together
```

### Frontmatter Schemas

Every document hunter-log writes has YAML frontmatter. This is what makes Dataview queries work — you can filter, sort, and aggregate across all documents using SQL-like syntax.

**Signal Scan:**
```yaml
type: signal-scan
domain: "DevOps Education"
date: 2026-02-08
session: "session-2026-02-08-001"
top_opportunity: "Production Design Patterns"
top_score: 9.0
status: complete
tags: [hunter/scan, hunter/domain/devops-education]
```

**Decision:**
```yaml
type: decision
date: 2026-02-08
session: "session-2026-02-08-001"
chosen_opportunity: "Production Design Patterns"
alternatives_considered: ["Career Roadmaps", "Tutorial Escape", "Notion Templates"]
confidence: 65
revisit_by: 2026-03-08
status: active
signal_scan: "[[Signal Scans/2026-02-08-devops-education]]"
tags: [hunter/decision, hunter/domain/devops-education]
```

**Persona:**
```yaml
type: persona
date: 2026-02-08
session: "session-2026-02-08-001"
persona_name: "Mid-Level DevOps Engineer"
pain_intensity: 8
willingness_to_pay: high
decision_ref: "[[Decisions/2026-02-08-domain-selection]]"
tags: [hunter/persona, hunter/domain/devops-education]
```

**Offer Spec:**
```yaml
type: offer-spec
date: 2026-02-08
product_name: "The DevOps Decision Guide"
format: PDF
price_point: "$29-49"
ship_time: "1 day"
status: spec
persona_ref: "[[Personas/mid-level-devops-engineer]]"
tags: [hunter/offer, hunter/domain/devops-education]
```

### Cross-Linking (The Provenance Chain)

Every artifact links backward to its inputs using Obsidian wikilinks:

```
Offer Spec
  -> links to Persona ("designed for [[Personas/mid-level-devops-engineer]]")
    -> links to Decision ("selected via [[Decisions/2026-02-08-domain-selection]]")
      -> links to Signal Scan ("based on [[Signal Scans/2026-02-08-devops-education]]")
```

Because Obsidian renders backlinks automatically, you can also navigate in reverse. Click on any signal scan and see every decision, persona, and offer that references it. This is provenance — the full chain of reasoning from raw market signal to shippable product.

---

## Obsidian as the Tool

Why Obsidian specifically, and not Notion, Roam, Google Docs, or a database?

**Local-first.** Your data lives on your filesystem as plain markdown files. No vendor lock-in. No API dependency. No "what happens if the company shuts down?" anxiety. You can read these files with `cat`. You can search them with `grep`. You can version-control them with `git`. This matters for a system you are building your business intelligence on.

**Graph view.** Obsidian's graph visualization shows every note as a node and every wikilink as an edge. With hunter-log's cross-linking, this means you can literally SEE the connections between scans, decisions, personas, and offers. After a few pipeline runs, the graph reveals clusters — domains where you have deep coverage, isolated notes that need more connections, and cross-domain links that suggest brand opportunities.

**Backlinks.** Click any offer and see its full provenance chain in the backlinks pane. "What signals led to this offer?" is answered instantly. "What other offers came from the same persona?" is one click away. This is the Zettelkasten in action — bidirectional navigation through your knowledge graph.

**Dataview.** The Dataview plugin lets you write SQL-like queries over your notes' frontmatter. Live dashboards that update automatically:

```dataview
TABLE domain, top_score, status
FROM "Product Discovery/Signal Scans"
WHERE status = "complete"
SORT top_score DESC
```

```dataview
TABLE chosen_opportunity, confidence, status
FROM "Product Discovery/Decisions"
WHERE status = "active"
SORT date DESC
```

```dataview
TABLE product_name, format, price_point, ship_time
FROM "Product Discovery/Offers"
WHERE status != "killed"
SORT date DESC
```

These are not static reports. They are live queries that update every time you add a new note. Your index page (`Plan.md`) becomes a real-time dashboard of your entire product discovery pipeline.

**Kanban.** The Kanban plugin renders a markdown file as a visual board. `Pipeline.kanban.md` tracks every opportunity through stages: Scan Complete, Decision Made, Persona Done, Offer Scoped, Shipped, Reviewing.

**Hierarchical tags.** Tags like `hunter/domain/devops-education` and `hunter/scan` enable both broad filtering ("show me everything tagged `hunter`") and narrow filtering ("show me only DevOps signal scans"). The tag pane gives you a tree view of your entire taxonomy.

**Full-text search.** Search across every note instantly. When you remember a specific Reddit quote from three months ago but cannot remember which scan it was in, full-text search finds it in seconds.

---

## The Anti-Patterns

These are the failure modes that kill knowledge management systems. If you recognize yourself in any of these, adjust immediately.

### Log Everything Syndrome

You start logging religiously. Every thought, every observation, every micro-decision. Within two weeks you have 200 notes and zero insights. The problem: you are generating so much volume that you never review anything. The log becomes a write-only database.

**The fix:** Log decisions, not observations. A decision is something where you chose one option over at least one other. "I chose to target DevOps over cybersecurity" is a decision worth logging. "I noticed a Reddit post about Kubernetes" is an observation worth capturing only if it changes a signal score.

### Forgetting to Review

A log you never read is a diary, not a tool. The value of decision logging comes from the REVIEW — comparing predictions to outcomes, updating calibration, extracting patterns. If you write a log entry and never look at it again, you have done the hardest part (capturing the reasoning) and skipped the most valuable part (learning from it).

**The fix:** Set a `revisit_by` date on every decision. Put it in the frontmatter. Use a Dataview query to surface decisions that are due for review:

```dataview
TABLE chosen_opportunity, confidence, revisit_by
FROM "Product Discovery/Decisions"
WHERE revisit_by <= date(today)
SORT revisit_by ASC
```

Schedule 30 minutes on the last Friday of every month for decision review. Non-negotiable. This is where the compounding happens.

### Perfecting the System

You spend three days redesigning your frontmatter schema. You rebuild your tag taxonomy from scratch. You write custom CSS for your Obsidian theme. You read four articles about Zettelkasten best practices. You have not made a single product decision in a week.

**The fix:** The system should be invisible. If you spend more than 5% of your product time on the logging system itself, the system is too complex. hunter-log exists specifically to solve this — it handles the formatting, the frontmatter, the cross-links, and the kanban updates. You focus on the decisions.

### Not Logging Failures

Successful products feel good to review. Failed products feel bad. So you log the successes in detail and skip over the failures, or you log them with a terse "didn't work, moving on."

**The fix:** Failed products and killed decisions are MORE valuable than successes. Success has many fathers — it is hard to know which factor was decisive. Failure is often traceable to a specific miscalculation. "I was wrong about pricing" or "I was wrong about distribution channel" or "the pain was real but the audience would not pay" — these are precise, actionable lessons. Log them with the same rigor as successes. Include what you would do differently.

### Narrative Bias

You write your log entries like blog posts — clean, coherent narratives with a beginning, middle, and end. The problem: narratives smooth out the uncertainty and messiness that is the actual experience of making decisions. Your log says "after careful analysis, I chose DevOps because..." when the reality was "I went back and forth for 45 minutes, changed my mind twice, and eventually went with DevOps partly because the signal scan said 9/10 and partly because I had more energy for it."

**The fix:** Raw notes are more valuable than polished narratives for learning. Record the mess. Record the uncertainty. Record the emotional state. "I am 65% confident but honestly I am picking this partly because I am excited about it and excitement matters for sustained effort" is a more useful log entry than "selected based on signal strength and edge analysis."

---

## Case Studies

### Bridgewater Associates: Decision Logs at Organizational Scale

Ray Dalio's Bridgewater Associates runs on what they call "radical transparency." Every meeting is recorded. Every decision is logged with the reasoning of every participant. Every participant has a "baseball card" — a quantified track record of their predictions across different domains.

When a trade fails, Bridgewater does not ask "who screwed up?" They ask "what was the decision process, and where did it break down?" If the process was sound but the outcome was bad, they do not change the process. If the process was flawed, they update their principles.

The result: Bridgewater has produced higher risk-adjusted returns than almost any fund in history, not because they are smarter, but because they learn faster. Their decision logs create a feedback loop that compounds over decades.

**Lesson for solo founders:** You do not need a team to implement radical transparency. You need radical transparency with yourself. The decision log is your baseball card. After 50 logged decisions, you will know your strengths and weaknesses with quantitative precision.

### Professional Poker: Hand Histories as Decision Logs

Professional poker is the closest analog to product decisions. Every hand is a bet under uncertainty with incomplete information. The outcome is heavily influenced by luck. The only sustainable edge is process quality.

Every serious poker player reviews their "hand histories" — a complete log of every hand played, including the cards, the betting action, the pot odds, and crucially, the reasoning at each decision point. Software tools (PokerTracker, Hold'em Manager) aggregate these histories into statistics: VPIP (voluntarily put money in pot), PFR (pre-flop raise), 3-bet percentage, c-bet percentage.

Over thousands of hands, these statistics reveal leaks — systematic errors in judgment. A player might discover they are calling too often on the river (sunk cost trap), or not raising enough with strong hands pre-flop (leaving money on the table), or tilting after bad beats (emotional decision-making).

**Lesson for solo founders:** Your product decisions ARE poker hands. The market is the opponent. The outcome is partially random. The only edge is in the decision process. Log every "hand" — what you decided, why, what happened, and what you learned. After 20+ logged decisions, your leaks will become visible.

### Tiago Forte's BASB and Creator Product Pipelines

Tiago Forte did not just write about Building a Second Brain — he used the method to build a multimillion-dollar education business. His process: capture everything interesting, organize by actionability (PARA), progressively summarize to extract insights, and express — turn captured knowledge into shipped products.

His course progression illustrates compounding knowledge: he started with a single cohort-based course, used student feedback (logged) to iterate, expanded into self-paced formats, then a book, then a certification program. Each product was informed by logs from the previous products — what students struggled with, what resonated, what pricing worked, what marketing messages converted.

**Lesson for solo founders:** The pipeline is the product. Each stage generates knowledge that feeds the next stage. But only if you capture it. Forte's system works because every piece of feedback, every student email, every cohort retro goes into the second brain. Your signal scans, decisions, personas, and offers are the same thing — a structured knowledge base that gets more valuable with each run.

### Niklas Luhmann's Zettelkasten: 70+ Books from Linked Notes

Niklas Luhmann was a German sociologist who published 70 books and nearly 400 academic articles in roughly 30 years. His secret was not superhuman productivity — it was a system. His Zettelkasten (slip box) contained roughly 90,000 handwritten index cards, each with a single idea, each linked to related cards through a numbering system.

Luhmann described his Zettelkasten as a "communication partner" — he would consult it when starting a new paper, and the connections between cards would suggest lines of argument he had not consciously planned. The system surfaced insights that no individual card contained. The value was emergent — a property of the network, not of any node.

**Lesson for solo founders:** This is exactly what Obsidian's graph view does for your product discovery pipeline. After enough signal scans, decisions, and persona extractions, the connections between notes will suggest product opportunities that no single analysis would reveal. The meta-signal from the initial hunter scan — "education over-indexes on tutorials and under-indexes on systems thinking" — is a Zettelkasten-style emergent insight. It was not in any individual signal. It emerged from the connections between signals across four domains.

---

## The Provenance Chain Framework

hunter-log implements what we call the **Provenance Chain** pattern. It is a synthesis of the frameworks described above, adapted for solo product discovery.

### Principles

1. **Every artifact links backward to its inputs.** An offer spec links to a persona, which links to a decision, which links to a signal scan. You can trace any product idea back to the raw market evidence that motivated it. (Zettelkasten: atomic, linked notes.)

2. **Every artifact is tagged for queryability.** Hierarchical tags (`hunter/scan`, `hunter/domain/devops-education`, `hunter/offer`) enable Dataview queries, filtered searches, and tag-pane navigation. (PARA: organizational structure for retrieval.)

3. **Sessions tie pipeline runs together chronologically.** A session log captures "on this date, we ran a signal scan, made a decision, extracted personas, and scoped an offer." This is the timeline view. (Annie Duke: decision journal with dates and sequence.)

4. **The kanban provides at-a-glance pipeline status.** Which opportunities are at which stage? What is stalled? What shipped? (Agile: visual workflow management.)

5. **Dataview queries create live dashboards.** Your index page is not a static document — it is a set of queries that always reflect the current state of your pipeline. (Forte: progressive summarization applied to an entire knowledge base.)

6. **The graph reveals cross-domain patterns over time.** After multiple pipeline runs across multiple domains, the graph view shows clusters, bridges, and isolated nodes. Clusters are well-explored territories. Bridges are cross-domain insights. Isolated nodes are opportunities for further connection. (Zettelkasten: emergent insight from network structure.)

### Credits

This framework synthesizes:

- **Annie Duke** (decision journals, confidence calibration, resulting)
- **Gary Klein** (pre-mortems, recognition-primed decision making)
- **Daniel Kahneman** (cognitive bias awareness, noise reduction)
- **Ray Dalio** (principles-based decision making, believability weighting)
- **Tiago Forte** (PARA method, progressive summarization)
- **Sonke Ahrens / Niklas Luhmann** (Zettelkasten, atomic linked notes, graph thinking)
- **Jeff Bezos** (Type 1 / Type 2 decision classification)
- **Philip Tetlock** (confidence calibration, superforecasting)
- **CI/CD engineering** (immutable artifacts with provenance, pipeline architecture)

The pipeline structure itself borrows from CI/CD thinking: each skill produces an immutable artifact (JSON envelope) that feeds the next stage. hunter-log is the deployment step — it takes the artifact and persists it to the production knowledge base (Obsidian). Just as you would never deploy code without knowing what commit it came from, you should never ship a product without knowing what signals, decisions, and personas it came from.

---

## Further Reading

### Essential (Start Here)

| Book | Author | Key Concept |
|------|--------|-------------|
| *Thinking in Bets* | Annie Duke | Decision quality vs. outcome quality, resulting |
| *Thinking, Fast and Slow* | Daniel Kahneman | Cognitive biases, System 1 / System 2 |
| *How to Take Smart Notes* | Sonke Ahrens | Zettelkasten method, atomic notes, graph thinking |
| *Building a Second Brain* | Tiago Forte | PARA method, progressive summarization |

### Deep Dives

| Book | Author | Key Concept |
|------|--------|-------------|
| *Sources of Power* | Gary Klein | Recognition-primed decision making, pre-mortems |
| *Principles* | Ray Dalio | Systematic decision-making, radical transparency |
| *Superforecasting* | Philip Tetlock | Confidence calibration, quantified prediction |
| *The Hard Thing About Hard Things* | Ben Horowitz | Decisions under genuine uncertainty |
| *The Great Mental Models (Vol. 1-4)* | Shane Parrish | Inversion, second-order thinking, map vs. territory |

### Shareholder Letters and Essays

- **Jeff Bezos** — Amazon shareholder letters (especially 1997 and 2015 on decision-making speed and Type 1 / Type 2 decisions)
- **Richard Feynman** — "Cargo Cult Science" (Caltech commencement, 1974) on the discipline of not fooling yourself

### Tools

- [Obsidian](https://obsidian.md) — Local-first, linked knowledge base
- [Obsidian Dataview](https://github.com/blacksmithgu/obsidian-dataview) — SQL-like queries over your notes
- [Obsidian Kanban](https://github.com/mgmeyers/obsidian-kanban) — Visual pipeline tracking

---

*hunter-log does not think for you. It remembers for you. The thinking is still yours — but now it compounds.*
