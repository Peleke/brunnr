# Decision Log

## A Ground-Up Masterclass in Structured Product Decision-Making

**What this is:** An exhaustive guide to the discipline of deciding what to build, when to build it, and why -- written for elite engineers who can ship anything but have never made a rigorous product decision.

**Who this is for:** You are technically brilliant. You can architect distributed systems, ship production ML pipelines, write compilers for fun. But when someone asks "why are you building *this* and not *that*?" you don't have a good answer. You build what seems cool. You build what someone asked for. You build what's technically interesting. And sometimes that works out. But you've never once sat down with a structured framework and said: "Given everything I know about the market, my strengths, the competitive landscape, and the available signal data -- THIS is the highest-expected-value thing I can build right now, and here's exactly why."

This document teaches you that discipline. All of it. The names, the frameworks, the vocabulary, the process, and the specific synthesis this skill implements.

---

## Part 1: The Discipline

### What IS Structured Product Decision-Making?

Structured product decision-making is the practice of systematically evaluating what to build next using explicit criteria, frameworks, and evidence -- then recording that decision so you can learn from it later.

It sits at the intersection of three related disciplines:

**Product Prioritization** is the tactical question: given a backlog of 47 things we *could* build, what order do we build them in? Prioritization frameworks like RICE and ICE live here. This is a necessary but insufficient piece of the puzzle. Most engineers who have heard of "product thinking" stop here -- they learn RICE scoring and think they're done. They are not.

**Strategy** is the structural question: what game are we playing, and how do we win? Strategy asks whether you should even be in this market at all. It asks about competitive moats, market positioning, and long-term defensibility. Hamilton Helmer's *7 Powers*, Michael Porter's *Five Forces*, and Roger Martin's *Playing to Win* live here. Strategy tells you which battles are worth fighting. Prioritization tells you which weapons to bring.

**Portfolio Management** is the meta question: how do we allocate our finite time and attention across multiple bets? This is where Daniel Vassallo's *Small Bets*, Rob Walling's *Stair Step Method*, and Nassim Taleb's *Barbell Strategy* live. Portfolio thinking says: you are not making one decision. You are making a series of decisions over time, and the sequence and diversity of those decisions matters as much as any individual choice.

Structured product decision-making is ALL THREE of these, woven together with cognitive bias awareness (Kahneman, Duke) and decision logging (so you actually learn from your choices).

### Why Do Most Builders Skip This?

Because building is fun and deciding is not. Engineers get dopamine from shipping code. They do not get dopamine from staring at a spreadsheet wondering whether "pain intensity" should be weighted 3x or 4x relative to "competition gap."

There is also a cultural myth in tech that great products come from visionary founders who just *know* what to build. Steve Jobs didn't use RICE scoring, right? This is survivorship bias at its finest. You see the one Steve Jobs. You do not see the ten thousand founders who also trusted their gut and built something nobody wanted. Jobs himself was fired from Apple for making bad product decisions (the Lisa, the NeXT Cube's price point). He learned. The gut feeling that worked in 2007 was informed by decades of structured learning about what customers actually want.

The cost of skipping this step is not dramatic. It is quiet. It is the slow accumulation of months spent building things that were technically impressive but strategically irrelevant. It is the opportunity cost -- the thing you *didn't* build because you were busy building the wrong thing. And because opportunity cost is invisible, you never feel the pain directly. You just wonder, years later, why you're not further along.

### The Canon: Key Thinkers and Texts

Here are the people and works that define this field. For each, the key insight and how it applies to the question "I have signal data, now what do I build?"

**Marty Cagan -- *Inspired* and *Empowered***
Key insight: The best product teams discover solutions to real customer problems, rather than building features stakeholders request. Cagan distinguishes "feature teams" (teams that take orders) from "empowered product teams" (teams that own outcomes). His concept of "product discovery" -- continuous, rapid experimentation to reduce risk before committing to build -- is foundational.
Application: Your signal data IS a form of product discovery. But signal data alone is not enough. You need to validate that the signals point to real, painful, frequent problems before you commit engineering time.

**Rich Mironov -- *The Art of Product Management***
Key insight: Product management is fundamentally about saying no. The hardest part is not generating ideas -- it is killing good ideas that are not good *enough* relative to alternatives. Mironov's framing of product management as "the economics of software" is powerful: every feature has a cost (not just to build, but to maintain, support, document, and sunset).
Application: When you score opportunities, you must account for the *ongoing* cost, not just the build cost. A feature that takes 2 days to build but creates a permanent support burden is more expensive than it looks.

**Intercom -- RICE Scoring**
Key insight: Prioritization needs to account for *how many people* a feature helps (Reach), *how much* it helps them (Impact), *how sure you are* about those estimates (Confidence), and *how much work it takes* (Effort). RICE was created by Sean McBride at Intercom to move prioritization beyond gut feeling.
Application: RICE is the default framework for scoring signal-derived opportunities. It forces you to separate "this sounds exciting" from "this affects a lot of people with high confidence and low effort."

**Teresa Torres -- *Continuous Discovery Habits* and Opportunity Solution Trees**
Key insight: Product decisions should flow from a clear tree structure: desired outcome at the top, opportunities (customer needs/pain points) in the middle, and solutions at the bottom. This prevents "solution-first thinking" -- jumping to "let's build X" before understanding the opportunity space.
Application: Before scoring anything, map your signal data into an opportunity solution tree. What customer outcomes does each opportunity serve? Are there multiple signals pointing to the same underlying opportunity?

**Daniel Kahneman -- *Thinking, Fast and Slow***
Key insight: Human judgment is riddled with systematic cognitive biases. System 1 (fast, intuitive) thinking dominates most decisions, but it is prone to anchoring, availability bias, confirmation bias, and dozens of other failure modes. System 2 (slow, analytical) thinking is more reliable but requires deliberate effort.
Application: Every step of this decision process is designed to force System 2 engagement. Scoring frameworks, written rationales, and pre-mortems are all System 2 tools. Without them, you will default to building whatever your System 1 finds exciting.

**Annie Duke -- *Thinking in Bets***
Key insight: Decision quality and outcome quality are different things. A great decision can lead to a bad outcome (bad luck). A terrible decision can lead to a great outcome (good luck). If you judge decisions by outcomes alone, you learn nothing. Duke calls this "resulting" and it is the most common failure mode in retrospective analysis.
Application: This is why we log decisions with their rationale and confidence level. When we revisit a decision six months later, we evaluate whether the *process* was sound, not just whether the *outcome* was good.

**Jeff Bezos -- One-Way Doors, Two-Way Doors, Regret Minimization**
Key insight: Decisions should be categorized by their reversibility. A "one-way door" (Type 1 decision) is irreversible or nearly so -- signing a 10-year lease, choosing a programming language for your core platform, taking VC money. A "two-way door" (Type 2 decision) is easily reversible -- launching a feature you can sunset, testing a price point you can change, trying a marketing channel you can abandon. Most decisions are Type 2, but most organizations treat them like Type 1, leading to paralysis. Bezos also popularized the "regret minimization framework": project yourself to age 80 and ask whether you'd regret *not* trying this.
Application: For a solo creator shipping small bets, almost everything is a two-way door. This means you should bias heavily toward action. Spend 80% less time analyzing and 80% more time shipping and measuring. The decision-log process exists not to slow you down but to ensure you are learning from each bet.

**Keith Rabois -- Barrels vs. Ammunition**
Key insight: In any organization, there are "barrels" (people who can take an idea from zero to shipped) and "ammunition" (people who can contribute to execution but cannot drive it independently). The constraint on output is always the number of barrels, not the amount of ammunition.
Application: As a solo creator, you are the only barrel. Every decision you make about what to build is also a decision about what you are NOT building. Your barrel-time is the scarcest resource. This makes prioritization existentially important -- not an academic exercise.

**Hamilton Helmer -- *7 Powers***
Key insight: Long-term business value comes from having at least one of seven "powers" (durable competitive advantages): Scale Economies, Network Economies, Counter-Positioning, Switching Costs, Branding, Cornered Resource, or Process Power. Without a power, even a great product will eventually be competed away.
Application: When evaluating opportunities, ask: "If this succeeds, does it create or strengthen a power?" If the answer is no, you might still build it (for revenue, for learning), but you should know that its value will erode over time.

**Michael Porter -- *Competitive Strategy* and Five Forces**
Key insight: An industry's profitability (and therefore a product's potential) is determined by five structural forces: threat of new entrants, bargaining power of suppliers, bargaining power of buyers, threat of substitutes, and rivalry among existing competitors. Porter's key contribution is making "competition" a structural analysis rather than a vibes check.
Application: Before building in a market, assess the five forces. A market with low barriers to entry, powerful buyers, and many substitutes is a terrible place to build -- even if the signal data looks strong. The signals might be real, but the economics are unfavorable.

---

## Part 2: Decision Frameworks

### Scoring Frameworks

These are the quantitative tools for comparing opportunities against each other.

#### RICE (Reach x Impact x Confidence / Effort)

Developed at Intercom by Sean McBride. Each opportunity is scored across four dimensions:

- **Reach**: How many people will this affect in a given time period? (e.g., "500 users per quarter")
- **Impact**: How much will each affected person benefit? Scored on a scale (3 = massive, 2 = high, 1 = medium, 0.5 = low, 0.25 = minimal)
- **Confidence**: How sure are you about the Reach and Impact estimates? (100% = high confidence backed by data, 80% = reasonable estimate, 50% = guess)
- **Effort**: How many person-months of work? (lower is better -- it's the denominator)

**Formula**: `(Reach x Impact x Confidence) / Effort`

**When it works**: When you have reasonably good data on reach and effort. When you are comparing features within an existing product with existing users. When your team is large enough that effort estimation matters.

**When it fails**: When you are a solo creator and all your "reach" numbers are speculative. When the opportunities being compared are so different in nature that scoring them on the same axes feels forced. When it gives you a numerically precise answer to a fundamentally uncertain question, creating false confidence.

#### ICE (Impact x Confidence x Ease)

A simpler variant popular with growth teams. Each dimension is scored 1-10.

- **Impact**: How much will this move the needle?
- **Confidence**: How sure are you?
- **Ease**: How easy is it to implement? (inverse of effort)

**Formula**: `Impact x Confidence x Ease` (all 1-10)

**When it works**: Quick-and-dirty prioritization for growth experiments. When you need speed over precision. When the team has enough shared context that calibrating "7 out of 10" means something consistent.

**When it fails**: When different people's calibrations diverge wildly (your "8 impact" is my "4 impact"). When you need to compare across very different types of work.

#### Weighted Scoring

Custom criteria with custom weights. You define what matters (revenue potential, strategic fit, technical risk, learning value, excitement, etc.), assign weights to each criterion, score each opportunity on each criterion, and compute a weighted sum.

**When it works**: When RICE/ICE don't capture the dimensions that actually matter for your context. When you want to make your priorities explicit and debatable.

**When it fails**: When you over-engineer the weights to justify the decision you already want to make. When you have so many criteria that the model becomes opaque.

#### Opportunity Scoring (Anthony Ulwick -- *Jobs to Be Done*)

Ulwick's insight: customers hire products to do jobs. The best opportunities are jobs that are both *important* and *underserved*.

**Formula**: `Opportunity = Importance + max(Importance - Satisfaction, 0)`

This means: highly important, highly unsatisfied needs score highest. Important needs that are already well-served score lower.

**When it works**: When you have customer research data on importance and satisfaction. When you are trying to find unmet needs in an existing market.

**When it fails**: When you are creating a new market where customers can't articulate their needs. When the "jobs" are novel enough that importance ratings don't exist.

#### When to Use Which?

| Situation | Framework |
|-----------|-----------|
| Existing product, comparing features | RICE |
| Growth experiments, fast iteration | ICE |
| Custom context, many dimensions | Weighted Scoring |
| Market analysis, finding unmet needs | Opportunity Scoring |
| Solo creator, signal-based decisions | Hybrid (see Part 7) |

### Strategic Frameworks

These are the qualitative lenses for evaluating whether an opportunity is worth pursuing at all.

#### One-Way Door vs. Two-Way Door (Bezos)

Before analyzing an opportunity in depth, ask: "Is this reversible?" If yes, stop analyzing and start doing. The cost of analysis often exceeds the cost of trying and reverting. Most product decisions for solo creators are two-way doors: you can ship a feature and remove it, launch a product and sunset it, try a positioning and change it.

**The test**: If this goes wrong, can I undo it within 2 weeks with no lasting damage? If yes, it is a two-way door.

Reserve deep analysis for one-way doors: choosing your platform, picking a co-founder, signing binding agreements, choosing markets that require years of investment before payoff.

#### 7 Powers (Helmer)

After identifying an attractive opportunity, ask: "If I win here, am I defensible?" Helmer's seven powers are:

1. **Scale Economies** -- unit costs decline with volume (unlikely for solo creators)
2. **Network Economies** -- product gets better as more people use it (possible: marketplaces, platforms, communities)
3. **Counter-Positioning** -- incumbents can't copy you without damaging their existing business (very relevant: your small bet can be structured to exploit incumbent incentive misalignment)
4. **Switching Costs** -- users face costs to move to a competitor (data lock-in, workflow integration, learning curve)
5. **Branding** -- customers pay a premium for the brand (earned over time through trust and consistency)
6. **Cornered Resource** -- exclusive access to a valuable resource (your unique expertise, proprietary data, relationships)
7. **Process Power** -- organizational capabilities that are hard to replicate (less relevant for solo creators)

**Application**: You do not need all seven. You need one. For solo creators, the most accessible powers are Counter-Positioning, Switching Costs, and Cornered Resource (your unique expertise and perspective IS a cornered resource).

#### Blue Ocean Strategy (Kim and Mauborgne)

Are you competing in an existing market ("red ocean" -- bloody with competition) or creating a new market space ("blue ocean" -- wide open)? The strategic canvas tool maps your offering against competitors on key value dimensions. The goal is to find dimensions where you can simultaneously *eliminate* costs competitors bear and *create* value competitors don't offer.

**Application**: When signal data shows high demand in a crowded market, ask: is there a way to reframe this that creates a blue ocean? Can you serve a different segment, deliver value through a different mechanism, or combine features in a novel way?

#### Ansoff Matrix

A 2x2 matrix crossing product (existing vs. new) with market (existing vs. new):

| | Existing Market | New Market |
|---|---|---|
| **Existing Product** | Market Penetration (lowest risk) | Market Development (medium risk) |
| **New Product** | Product Development (medium risk) | Diversification (highest risk) |

**Application**: Know which quadrant you are operating in. If this is your first product, you are in the highest-risk quadrant (new product, new market). Mitigate by choosing a market you know well (even if the product is new) or by adapting an existing product type for a new market.

### Portfolio Frameworks

These address the meta-question: how do I manage a series of decisions over time?

#### Small Bets (Daniel Vassallo)

Vassallo's core thesis: do not put all your eggs in one basket. Instead, launch a portfolio of small, independent bets. Each bet should be cheap to try (days to weeks, not months), quick to validate, and capable of generating revenue independently. The portfolio approach means any single failure is affordable, and you benefit from optionality -- the chance that one bet overperforms.

**Key idea**: You are not looking for "the one idea." You are building a portfolio of options. Some will fail, some will be modest, and if your process is good, some will surprise you.

**Application**: After scoring opportunities, you do not pick the single highest-scoring one and go all-in. You pick the 2-3 best, ship them quickly, and let market feedback determine which one to double down on.

#### Stair Step Method (Rob Walling)

Walling's approach is sequential rather than parallel. He advocates building progressively:

- **Step 1**: One-time purchase products (WordPress plugins, templates, small tools) -- learn to market and sell
- **Step 2**: Subscription products with small monthly revenue targets -- learn recurring revenue dynamics
- **Step 3**: SaaS or products with network effects -- leverage everything you learned

Each step builds skills and confidence for the next. You do not start with the ambitious SaaS vision. You earn your way there.

**Application**: When evaluating opportunities, consider where you are on the staircase. If you have never sold anything, pick the smallest, most shippable opportunity first, regardless of its RICE score. The learning value of shipping and selling something -- anything -- dominates all other factors early in your journey.

#### Barbell Strategy (Taleb, Applied to Products)

Taleb's barbell strategy from finance: avoid the middle. Instead, allocate to two extremes: very safe bets (predictable, low-downside) and very aggressive bets (low probability, massive upside). Avoid the mediocre middle (moderate risk, moderate return).

**Application**: In your portfolio, have "cashflow bets" (boring products that reliably generate revenue) and "moonshot bets" (ambitious products that probably fail but would be transformative if they succeed). Do not have a portfolio of all medium-risk, medium-return products.

### Speed Frameworks

These address the question: how do I avoid analysis paralysis?

#### OODA Loop (John Boyd)

Observe, Orient, Decide, Act. Developed by fighter pilot and military strategist John Boyd. The key insight: the side that cycles through this loop faster wins. In business, this means the speed of your decision-making is itself a competitive advantage. A good decision made quickly beats a perfect decision made slowly.

**Application**: Time-box your decision process. If you have been analyzing for more than a day on a two-way door decision, you are overthinking it. Ship. Measure. Iterate.

#### Minimum Viable Decision

What is the smallest commitment you can make to move forward? You do not need to decide "we are building this product for the next two years." You need to decide "I am spending this week building an MVP to test this hypothesis." Scope the decision to match the reversibility.

#### Disagree and Commit (Bezos)

Sometimes the team (or the voices in your head, if you are a solo creator) will not reach consensus. That is fine. The framework says: voice your disagreement clearly, then commit fully to the decision once it is made. Half-hearted execution poisons everything. This also applies to your own internal debate: once you have run the process and made the call, stop second-guessing and execute with conviction. You can revisit at the predetermined date, not before.

---

## Part 3: The Lingo

A conversational glossary of terms you will encounter (and use) in product decision-making.

**Opportunity cost**: The value of what you *didn't* do. If you spend 3 months building Feature A, the opportunity cost is whatever Feature B would have generated in those 3 months. This is the single most important concept in product decision-making because it is invisible. You never see the path not taken. Frameworks make opportunity cost visible by forcing you to compare alternatives explicitly.

**Sunk cost fallacy**: "I've already spent 3 months on this, I can't stop now." Yes you can. The 3 months are gone regardless. The only question is: given what you know NOW, is continuing the best use of your FUTURE time? Engineers are especially susceptible to this because they form emotional attachments to code they have written. Killing a project feels like killing a child. It is not. It is pruning a garden.

**Confirmation bias**: The tendency to seek and interpret information that confirms what you already believe. If you have already decided you want to build a particular product, you will subconsciously weight positive signals more heavily and dismiss negative ones. The antidote is a pre-mortem (see below) and an explicit search for disconfirming evidence.

**Survivorship bias**: You read about the founders who succeeded. You do not read about the 1,000 who did the same thing and failed. When someone says "Dropbox succeeded by building a simple product in a crowded market, so you should too," they are exhibiting survivorship bias. The relevant question is: of all the startups that built simple products in crowded markets, what percentage succeeded?

**Local maximum vs. global maximum**: You can be at the top of a small hill (local maximum) while a much taller mountain exists elsewhere. In product terms: you can optimize your current product to be the best version of itself, but you might be in the wrong market entirely. Scoring frameworks help you see the global landscape, not just the local terrain.

**Type 1 vs. Type 2 decisions**: Bezos's framing. Type 1 (one-way doors) are irreversible and deserve deep analysis. Type 2 (two-way doors) are reversible and should be made quickly. Most decisions are Type 2. Treat them accordingly.

**"Strong opinions, loosely held"**: Originally from Paul Saffo at the Institute for the Future. It means: form a clear hypothesis (strong opinion) based on available evidence, but be willing to change it when new evidence arrives (loosely held). It is often misused to justify stubbornness ("I have a strong opinion!") without the critical second half (loosely held means actually updating when you're wrong).

**Conviction vs. evidence**: Sometimes the data is ambiguous and you have to make a call based on intuition. This is legitimate -- but only if you have earned the right to have intuition through experience. Jeff Bezos can trust his gut about e-commerce because he has 30 years of pattern recognition. You probably cannot trust your gut about a market you entered last month. Know which mode you are in.

**"Default alive vs. default dead" (Paul Graham)**: If you stopped actively working on growth, would your company survive on its current trajectory? Default alive means you have enough revenue and low enough costs to sustain indefinitely. Default dead means you are burning runway. This affects decision-making: default-dead companies must prioritize revenue immediately; default-alive companies can afford to invest in longer-term strategic bets.

**Escape velocity**: The minimum traction needed for a product to become self-sustaining (through organic growth, word-of-mouth, or recurring revenue). Before escape velocity, every day without growth is a day closer to death. After escape velocity, the product grows on its own momentum.

**Market timing vs. execution**: There is an eternal debate about whether timing or execution matters more. The honest answer: timing is more important for *which* products succeed in a given era, but execution determines *which company* captures the opportunity. You cannot control timing. You can control execution. But you should be aware of timing -- launching a product for a need that will not be acute for 5 more years is a timing mistake no amount of execution can fix.

**First mover advantage (and why it is usually wrong)**: The naive view is that being first to market gives you a permanent advantage. The reality: first movers often bear the cost of educating the market, making mistakes, and establishing the category -- only to be overtaken by fast followers who learn from those mistakes. Google was not the first search engine. Facebook was not the first social network. The iPhone was not the first smartphone.

**Fast follower advantage**: Letting someone else prove the market exists, then entering with a better product, better positioning, or better execution. This is often a more rational strategy than being first, especially for solo creators with limited resources.

**Build vs. buy vs. partner**: For every feature or capability, you have three options: build it yourself, buy an existing solution (SaaS tool, library, API), or partner with someone who has it. Engineers default to "build" because building is their superpower. This is a bias. The correct answer is often "buy" or "partner," preserving your scarce barrel-time for the things that are truly differentiating.

**"Will this still matter in 10 years?" (Bezos)**: Bezos focuses Amazon's investments on things he is confident will matter in a decade. Customers will still want low prices, fast delivery, and wide selection in 2035. This filter eliminates trendy but ephemeral opportunities.

**"What would have to be true?" (Roger Martin)**: Instead of asking "Is this a good idea?", Martin reframes: "What would have to be true for this to be a great idea?" This is powerful because it transforms a debate into a set of testable hypotheses. If you can enumerate the conditions required for success, you can evaluate each one independently.

**Pre-mortem (Gary Klein)**: Before starting a project, imagine it has failed catastrophically. Now work backwards: why did it fail? This surfaces risks and assumptions that optimism bias would otherwise hide. It is far more effective than a post-mortem because you can still change course.

**Decision journal**: A written log of decisions, including the date, the options considered, the criteria used, the decision made, the confidence level, and the rationale. Reviewed periodically to identify patterns in your decision-making. Annie Duke and Daniel Kahneman both advocate this as the single most effective tool for improving judgment over time.

---

## Part 4: The Process

How an experienced product leader goes from "I have signal data" to "I'm building THIS."

### Step 1: Frame the Decision

**What exactly are we deciding?**

This sounds obvious but it is the most commonly skipped step. "What should I build next?" is too vague. Good framings are:

- "Given my signal scan showing 12 opportunities, which 2-3 should I prototype this month?"
- "Should I build an API product for developers or a no-code tool for marketers?"
- "Of these three validated ideas, which one ships fastest to paying customers?"

**What beginners get wrong**: They skip framing entirely and jump to scoring. Without a clear frame, you end up comparing apples to oranges -- a Chrome extension versus a SaaS platform versus a consulting productization.

**What experts do**: They spend significant time on framing because a well-framed decision is half-solved. They define the time horizon, the success metric, and the constraints before looking at any options.

### Step 2: List the Options

**What are ALL the things we could build?**

This is the divergent phase. Be comprehensive. Include the obvious options and the weird ones. Include "do nothing" as an explicit option (it often wins and that is fine). Include variations and combinations.

**What beginners get wrong**: They list 2-3 options and compare them. This is too few. You get anchored on your initial ideas and miss creative alternatives.

**What experts do**: They generate 10+ options, including deliberately provocative ones. "What if we built the opposite of what the signal data suggests?" Sometimes the contrarian bet is the right one.

### Step 3: Define Criteria

**What matters for THIS decision?**

Not all criteria matter equally for all decisions. For your first product ever, "speed to ship" and "learning value" might dominate. For your fourth product, "revenue potential" and "strategic moat" might dominate.

Common criteria for solo creators:
- **Pain intensity**: How badly does the target customer need this?
- **Spend evidence**: Are people already paying for inferior solutions?
- **Edge match**: Does this play to my unique skills and expertise?
- **Time to ship**: How quickly can I get a testable version out?
- **Competition gap**: Is there a meaningful opening in the competitive landscape?
- **Audience fit**: Do I already have access to the target customers?

**What beginners get wrong**: They use someone else's criteria without adapting to their context. RICE was designed for a 200-person product org at Intercom. Your criteria should reflect YOUR situation.

**What experts do**: They define criteria fresh for each major decision, drawing from established frameworks but customizing ruthlessly.

### Step 4: Score and Rank

**Apply a framework.**

Take your criteria, score each option on each criterion (1-5 or 1-10 scale), apply weights if you are using weighted scoring, and compute a ranked list.

**What beginners get wrong**: They treat the scores as gospel. "The spreadsheet says Option B scored 78 and Option A scored 76, therefore we must build Option B." The scores are tools for structured thinking, not oracles. A 2-point difference is noise.

**What experts do**: They use scores to identify clusters. "Options A, B, and C are all in the 70-80 range and clearly better than Options D through G in the 30-50 range. Now let's do deeper qualitative analysis on the top cluster."

### Step 5: Apply Strategic Filters

**Does this opportunity create a moat? Is this a one-way or two-way door?**

The scoring tells you what is tactically attractive. The strategic filters tell you what is strategically sound. An opportunity might score well on RICE but fail the 7 Powers test (no defensibility) or the Ansoff Matrix test (it puts you in the highest-risk quadrant with no experience to justify it).

**What beginners get wrong**: They skip this step entirely. They pick the highest-scoring option and start building.

**What experts do**: They use strategic filters as a veto or a promotion mechanism. A strategically strong opportunity gets promoted even if it scored slightly lower. A strategically weak opportunity gets flagged even if it scored highest.

### Step 6: Check for Bias

**Am I choosing this because I WANT to build it, or because the data says to?**

This is the hardest step. Run a pre-mortem: "It's 6 months from now and this product failed. Why?" If you can easily generate failure scenarios, your confidence should decrease. Ask: "If my best friend proposed this idea, would I tell them to go for it?" Often we are more objective about other people's decisions than our own.

**What beginners get wrong**: They do not check for bias at all. Or they perform a perfunctory check that does not actually change anything.

**What experts do**: They have a specific anti-bias ritual. Some use a "red team" (someone whose job is to argue against the decision). Solo creators can use a decision journal entry where they explicitly list reasons NOT to pursue the chosen option.

### Step 7: Make the Call

**Decide. Record. Set a revisit date.**

Write down: "I am building X. I chose it over Y and Z for these reasons. My confidence is [high/medium/low]. I will revisit this decision on [date]."

The revisit date is crucial. It prevents both premature abandonment (quitting too early because of a rough week) and the sunk cost trap (continuing too long because you have already invested).

**What beginners get wrong**: They make the decision but do not record it. Three months later they cannot remember why they chose this path, which makes it impossible to learn from the decision.

**What experts do**: They treat the decision record as a sacred artifact. It is the raw material for future learning.

### Step 8: Log Everything

**The decision, the alternatives, the reasoning, the confidence level.**

A decision log entry should include:
- **Date**: When the decision was made
- **Decision**: What you decided
- **Alternatives considered**: What you did not choose (and why)
- **Key criteria**: What mattered most in this decision
- **Confidence**: How sure you are (percentage or high/medium/low)
- **Rationale**: 2-3 sentences on WHY this option won
- **Risks**: What could go wrong
- **Revisit date**: When you will re-evaluate

### Step 9: Set a Kill Criterion

**What would make us abandon this? Define it BEFORE you start.**

This is the most sophisticated step and the one most people skip. Before you write a single line of code, define the conditions under which you will stop. Examples:

- "If I have not acquired 10 paying customers within 6 weeks of launch, I will sunset this."
- "If the prototype takes more than 2 weeks to build, I will reduce scope or abandon."
- "If user retention at day-7 is below 20%, this is not working."

**What beginners get wrong**: They do not set kill criteria, so they never kill anything. Every project becomes a zombie -- not dead but not alive, consuming time and energy indefinitely.

**What experts do**: They set kill criteria before they start and they actually enforce them. They know that the ability to kill projects quickly is what makes a portfolio strategy work. A portfolio of small bets only works if you actually kill the losers.

---

## Part 5: Why Logging Decisions Matters

### Decision Journals

Annie Duke and Daniel Kahneman both advocate decision journaling as the single highest-leverage practice for improving your judgment. The concept is simple: before you learn the outcome, write down what you decided, why, and how confident you are.

The reason this works is that memory is unreliable. After an outcome is known, your brain retroactively edits your memory of the decision to be more consistent with the outcome. If the project succeeded, you remember being confident. If it failed, you remember having doubts. This is called *hindsight bias* and it makes learning impossible unless you have a written record.

### Separating Decision Quality from Outcome Quality

This is the most important conceptual shift in the entire document. There are four possible combinations:

| | Good Outcome | Bad Outcome |
|---|---|---|
| **Good Decision** | Deserved success -- repeat this process | Bad luck -- do not change the process |
| **Bad Decision** | Good luck -- do not get cocky | Deserved failure -- learn and change |

Most people only look at outcomes. They double down after success (even if the decision was bad) and retreat after failure (even if the decision was sound). A decision journal lets you evaluate the *diagonal*: was this a good process that got unlucky, or a bad process that got lucky?

### "Resulting"

Annie Duke's term for judging a decision by its outcome. Example: "I went all-in with pocket aces and lost to a runner-runner flush. Therefore going all-in with pocket aces was a bad decision." No. It was a great decision that got unlucky. If you change your strategy because of this one outcome, you are "resulting" and your future decisions will be worse.

In product terms: "I launched a well-researched product with strong signal data and it failed because a pandemic hit / a competitor got acquired by Google / the market shifted unexpectedly. Therefore my research process was wrong." No. The process was fine. The outcome was bad luck. Learn what you can, but do not overhaul a sound process because of one bad outcome.

### How to Review Past Decisions

Set a monthly or quarterly ritual:
1. Re-read your decision log entries from 3-6 months ago
2. For each: what happened? Was the outcome good or bad?
3. Separate the decision quality from the outcome quality
4. Look for patterns: Am I consistently overconfident? Do I underweight competition? Do I overweight my own excitement?
5. Adjust your process (not your gut) based on patterns

### The Difference Between a Bad Decision and Bad Luck

A bad decision is one where the process was flawed *given what you knew at the time*. You ignored available evidence. You skipped the bias check. You did not consider alternatives. You let excitement override analysis.

Bad luck is when the process was sound but unforeseeable events changed the outcome. The market shifted. A competitor launched first. A key platform changed its API.

The distinction matters because only bad decisions are learnable. You can fix your process. You cannot fix your luck. But if you do not have a decision log, you cannot tell which one it was.

---

## Part 6: Case Studies

### How Bezos Decided to Start Amazon

In 1994, Jeff Bezos was a VP at D.E. Shaw, a quantitative hedge fund, earning a very comfortable salary. He noticed that web usage was growing at 2,300% per year. He made a list of 20 products that could be sold online and ranked them. Books won: they were a commodity product (no quality variation), the existing catalog was enormous (too large for any physical store), and the existing distribution infrastructure (book wholesalers) was already in place.

But the decision to *leave his job* and actually do it? That came from his "regret minimization framework." He projected himself to age 80 and asked: "Will I regret not trying this?" The answer was obviously yes. He would not regret trying and failing. He would regret not trying. This is a strategic filter applied to a personal decision -- and it worked because the key variable was not "will this succeed?" but "is the downside tolerable?"

**Lesson**: The best decision frameworks match the actual question being asked. Bezos did not need RICE scoring. He needed a framework for irreversible life decisions.

### How Basecamp Decides What to Build

Basecamp (formerly 37signals) uses the "Shape Up" methodology developed by Ryan Singer. The core concept is "appetite": instead of estimating how long something will take and then deciding whether to build it, they start by deciding how much time they are *willing to spend* (the appetite) and then shape the project to fit within that constraint.

A 6-week cycle gets a shaped pitch. The pitch includes the problem, the appetite, the solution (at the right level of abstraction), rabbit holes to avoid, and no-gos (explicitly out-of-scope elements). A betting table of senior leaders decides which pitches to bet on for the next cycle. Crucially, any project that is not completed within its 6-week cycle is not automatically extended -- it goes back to the pitch pile and must re-earn its slot.

**Lesson**: Constraining the investment (time-boxing) is a more effective discipline than estimating the cost. "Is this worth 2 weeks of effort?" is a better question than "How long will this take?"

### How Indie Hackers Decide: Vassallo vs. Walling

Daniel Vassallo left a $500K/year job at Amazon to pursue indie products. His approach: launch many small bets quickly, see what the market responds to, and double down on winners. His portfolio has included an AWS book, a Twitter course, a no-code course, and multiple SaaS experiments. Some succeeded, some failed, and the portfolio as a whole generates sustainable income.

Rob Walling (founder of MicroConf, Drip) advocates a sequential approach: start with small, simple products (WordPress plugins, info products) to learn marketing and sales, then graduate to more ambitious products once you have the skills and the audience. His stair step method has you earning your way to SaaS, not jumping straight to it.

These are not contradictory but rather different philosophies suited to different temperaments and stages. Vassallo's approach works when you have savings and can tolerate variance. Walling's approach works when you need reliable income at each step.

**Lesson**: There is no single correct portfolio strategy. The correct strategy is the one that matches your financial situation, risk tolerance, and skills. But HAVING a portfolio strategy is non-negotiable -- the alternative is random wandering.

### A Bad Decision Made with Good Data

In 2013, a well-funded startup (let's call them "Beacon") had extensive user research showing that small business owners wanted an all-in-one financial management tool. The signal data was strong: surveys, interviews, willingness-to-pay studies. They spent 18 months building a comprehensive platform. By the time they launched, QuickBooks had launched a nearly identical feature set as an add-on to their existing product. Beacon's tool was arguably better, but QuickBooks had distribution, switching costs, and brand trust. Beacon never achieved escape velocity and shut down after burning through $12M.

The data was right: small business owners DID want this. The decision process was flawed: they never ran a competitive dynamics analysis (Porter's Five Forces would have flagged the threat of incumbent response), they never asked "What would have to be true for an incumbent NOT to copy this?" (Roger Martin's framing), and they never set a kill criterion tied to market timing.

**Lesson**: Good signal data is necessary but not sufficient. Strategic analysis -- particularly competitive analysis and timing assessment -- is equally important. The process matters more than any single input.

---

## Part 7: The Framework This Skill Implements

### The Signal-to-Decision Pipeline (SDP)

This decision-log skill implements a named framework called the **Signal-to-Decision Pipeline** (SDP). It is a hybrid synthesis of established frameworks, adapted specifically for solo creators working from signal scan data.

Here is the lineage:

| Component | Source | Adaptation |
|-----------|--------|------------|
| Signal data as input | Teresa Torres (Opportunity Solution Trees) | Signals from automated scans replace manual customer interviews as the discovery layer |
| Scoring dimensions | Intercom (RICE), adapted | Six custom dimensions replace RICE's four: `pain_intensity`, `spend_evidence`, `edge_match`, `time_to_ship`, `competition_gap`, `audience_fit` |
| Reversibility filter | Jeff Bezos (Type 1/Type 2) | For solo creators shipping small bets, nearly everything is a two-way door -- so we bias toward action and speed |
| Portfolio framing | Daniel Vassallo (Small Bets) | We are not picking THE thing. We are picking the FIRST bet in a portfolio. This reduces the stakes of any single decision and eliminates perfectionism |
| Decision logging | Annie Duke (Thinking in Bets) | Every decision is recorded with confidence, rationale, alternatives, and a revisit date -- creating the raw material for learning |
| Kill criteria | Basecamp (Shape Up appetite model) | Every bet gets a time-box and explicit failure conditions defined before work begins |
| Strategic check | Hamilton Helmer (7 Powers) | After scoring, a lightweight strategic filter asks: "Does this create or strengthen a power?" |
| Bias check | Daniel Kahneman (pre-mortem via Gary Klein) | Before finalizing, a structured pre-mortem surfaces hidden assumptions and biases |

### How It Works in Practice

**Input**: Signal scan output -- a set of opportunities with quantitative and qualitative data (market signals, pain indicators, competitive landscape observations, audience sentiment).

**Step 1 -- Frame**: Define the decision scope. "Which 1-3 opportunities from this signal scan should I prototype this sprint?" The frame is always time-bounded and action-oriented.

**Step 2 -- Score**: Each opportunity is scored on six dimensions (1-5 scale):

- **Pain Intensity** (1-5): How acute is the problem? Is this a vitamin (nice-to-have, score 1-2) or a painkiller (must-have, score 4-5)?
- **Spend Evidence** (1-5): Are people already paying for solutions? Paying for bad solutions is the strongest signal (score 5). Free alternatives with no willingness-to-pay is the weakest (score 1).
- **Edge Match** (1-5): Does this play to your unique technical skills, domain expertise, or audience access? A perfect match (score 5) means you can build something others cannot. No edge (score 1) means you are competing on execution alone.
- **Time to Ship** (1-5): How quickly can you get a testable version to market? Under a week (score 5). Over a month (score 1). Speed is overweighted because fast iteration is the solo creator's primary advantage.
- **Competition Gap** (1-5): Is there a meaningful opening? No competitors (score 5, but verify demand exists). Crowded market with differentiation opportunity (score 3). Crowded market with entrenched incumbents (score 1).
- **Audience Fit** (1-5): Do you already have access to the target customers? Existing audience that's asking for this (score 5). No audience and no clear acquisition channel (score 1).

**Step 3 -- Rank**: Compute a weighted score. Default weights reflect solo creator priorities:

```
Score = (pain_intensity x 3) + (spend_evidence x 3) + (edge_match x 2)
      + (time_to_ship x 2) + (competition_gap x 1) + (audience_fit x 1)
```

Pain and spend are weighted highest (demand validation). Edge and speed are weighted next (execution advantage). Competition and audience are weighted lowest (important but not dominant).

Maximum possible score: 60. Minimum: 12.

**Step 4 -- Filter**: Apply the Bezos reversibility filter. Any opportunity scoring above 35 that can ship in under 2 weeks is a two-way door: bias toward action. Any opportunity requiring more than a month of work or irreversible commitments gets the full strategic analysis (7 Powers, Ansoff Matrix, pre-mortem).

**Step 5 -- Decide and Log**: Select 1-3 opportunities. For each, record:

```
## Decision Log Entry

**Date**: YYYY-MM-DD
**Decision**: Build [X]
**Score**: [N]/60
**Confidence**: [High/Medium/Low]
**Rationale**: [2-3 sentences on why this won]
**Alternatives considered**: [List with brief reasons for rejection]
**Kill criterion**: [Specific condition under which you will stop]
**Revisit date**: [When you will re-evaluate]
**Pre-mortem notes**: [Top 3 reasons this could fail]
**Strategic power**: [Which of the 7 Powers does this create, if any?]
```

**Step 6 -- Execute with commitment**: Once logged, execute with full commitment until the revisit date or until the kill criterion is met. No second-guessing in between. Disagree and commit -- even with yourself.

### Why This Synthesis Works

The SDP is designed for a specific persona: a technically elite solo creator who has signal data and needs to make fast, defensible, logged decisions about what to build. It combines:

1. **The rigor of scoring frameworks** (RICE/ICE lineage) -- so decisions are not purely intuitive
2. **The speed of reversibility-based analysis** (Bezos) -- so you do not over-analyze two-way doors
3. **The resilience of portfolio thinking** (Vassallo) -- so no single decision is existential
4. **The learning system of decision logging** (Duke/Kahneman) -- so every decision, whether it leads to a good or bad outcome, makes you smarter
5. **The strategic grounding of competitive analysis** (Helmer/Porter) -- so you are not just building what is popular but what is defensible

This is not a new invention. It is a named assembly of proven components. Every piece has been validated by practitioners, researchers, or both. The contribution is the specific assembly -- choosing which frameworks to combine, how to weight them, and how to sequence them for the solo creator context.

---

## Appendix: Recommended Reading (Prioritized)

If you read nothing else, read these three:

1. **Annie Duke -- *Thinking in Bets*** (2018). Teaches you to separate decision quality from outcome quality. Changes how you think about every decision you make.
2. **Teresa Torres -- *Continuous Discovery Habits*** (2021). Teaches you to structure the space between "signal" and "solution." The opportunity solution tree is the missing link.
3. **Daniel Vassallo -- *The Small Bets Approach*** (available as a course and essays). Teaches portfolio thinking for solo creators.

Then, as you go deeper:

4. **Marty Cagan -- *Empowered*** (2020). How the best product organizations make decisions.
5. **Hamilton Helmer -- *7 Powers*** (2016). What makes a business defensible long-term.
6. **Daniel Kahneman -- *Thinking, Fast and Slow*** (2011). The cognitive science underneath all of this.
7. **Ryan Singer -- *Shape Up*** (2019, free online). How Basecamp time-boxes and bets.
8. **Rob Walling -- *The SaaS Playbook*** (2023). Practical sequencing for bootstrapped founders.
9. **Michael Porter -- *Competitive Strategy*** (1980). The foundational text on industry analysis.
10. **Jeff Bezos -- Annual Shareholder Letters** (1997-2020, free online). Primary source on reversible decisions, disagree-and-commit, and long-term thinking.

---

*This skill takes signal scan output and runs it through the Signal-to-Decision Pipeline, producing scored, ranked, strategically filtered, and fully logged decision records. It is the bridge between "here is what the market is telling us" and "here is what we are building and why."*
