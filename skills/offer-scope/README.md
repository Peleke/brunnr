# Offer Scope: A Ground-Up Masterclass in Offer Design, Product Scoping, and Rapid MVPs

> **Who this is for:** You are an elite software engineer. You can build anything. You have never designed an *offer*. You have never priced a digital product. You have never thought about what format to ship in. This document teaches you the entire discipline -- the language, the frameworks, the names, and the sources -- so you can go from persona data to a shippable, sellable product spec in a single day.

> **Who wrote this (conceptually):** A synthesis of the best thinking from world-class marketing consultants and product strategists. Every framework is named. Every source is cited. Nothing is made up.

---

## Table of Contents

1. [The Discipline: Offer Design](#1-the-discipline-offer-design)
2. [The Hormozi Value Equation (The Core Framework)](#2-the-hormozi-value-equation)
3. [Product Formats and When to Use Each](#3-product-formats-and-when-to-use-each)
4. [Pricing Strategy from Zero](#4-pricing-strategy-from-zero)
5. [Scoping to One Day](#5-scoping-to-one-day)
6. [From Persona to Offer (The Bridge)](#6-from-persona-to-offer-the-bridge)
7. [The Lingo](#7-the-lingo)
8. [Distribution Channels](#8-distribution-channels-where-to-sell)
9. [Case Studies](#9-case-studies)
10. [The Framework: Signal-to-Ship Architecture](#10-the-framework-signal-to-ship-architecture)
11. [Canonical Reading List](#11-canonical-reading-list)

---

## 1. The Discipline: Offer Design

Here is the single most important distinction you will learn in this document:

**A product is what you build. An offer is what you sell.**

They are not the same thing. Not even close. And confusing the two is the number-one reason engineers build excellent software -- or write excellent content -- that nobody buys.

A product is a Terraform tutorial. An offer is: "The Terraform Decision Kit: Deploy production infrastructure in 2 hours, not 2 weeks. Includes the 4-environment template, the decision tree for choosing between ECS/EKS/Lambda, and a 30-minute video walkthrough. $49. Money back if it doesn't save you at least 8 hours on your next project."

See the difference? The product is the tutorial. The offer is the product *plus* the positioning, the price, the guarantee, the bonuses, the urgency, and the framing. The offer is the full package that makes a stranger hand you money.

This is why engineers build great things that don't sell. They ship products. They do not ship offers. They say "here is my Terraform tutorial" and wonder why nobody buys it. The answer is: nobody buys products. Everybody buys offers. An offer answers the question the product never does: *"Why should I buy this, specifically, right now, from you, at this price?"*

### The Thinkers You Need to Know

Offer design is not one person's idea. It is a discipline built over a century of direct-response marketing, distilled by a specific lineage of practitioners. Here are the people whose work matters most, and what each contributes to the practice of scoping a 1-day product from persona data:

**Alex Hormozi** -- *$100M Offers* (2021). The modern bible of offer design. Hormozi's key contribution is the **Value Equation** (covered in depth in Section 2). His insight: you do not need a better product; you need a better offer. He took gym owners from selling $500 memberships to $42,000 packages by redesigning the offer, not the gym. For our purposes, Hormozi teaches you to evaluate every decision point in your persona data through four lenses: dream outcome, perceived likelihood, time delay, and effort. The decision point that scores highest across all four is your product.

**Russell Brunson** -- *DotCom Secrets* (2015), *Expert Secrets* (2017). Brunson codified the **value ladder** and the **funnel**. His key insight: you never sell just one thing. You sell a sequence: free lead magnet, then a cheap tripwire, then a core offer, then a premium offer. Each step builds trust and qualifies the buyer. For 1-day scoping, Brunson tells you where your product sits on the ladder. Are you building the lead magnet (free, list-builder) or the core offer ($29-$297)? This changes everything about scope.

**Dan Kennedy** -- *No B.S. Direct Marketing* (multiple editions). The godfather of modern direct response. Kennedy's key insight: **all marketing is direct response or it is wasted money.** Every dollar you spend should produce a measurable result. For scoping, Kennedy teaches you to think in terms of specific, trackable actions: did they click, did they buy, did they use it? He also teaches the "message to market match" -- your offer must use the exact words your market uses to describe their problem.

**Gary Halbert** -- *The Boron Letters* (1984, published posthumously). Legendary copywriter. His most famous lesson: if you and a competitor both opened a hamburger stand, and you could choose one advantage, what would it be? A better location? Better burgers? Better prices? Halbert's answer: **a starving crowd.** The best offer in the world fails without demand. For our purposes: persona data is how you verify the starving crowd exists before you build anything.

**Claude Hopkins** -- *Scientific Advertising* (1923). The original measurement-obsessed marketer. Hopkins invented the coupon code (to track which ads worked), A/B testing, and the principle that advertising is salesmanship in print. His insight for scoping: **test everything, assume nothing.** The first version of your product is a hypothesis. You ship it, you measure, you iterate.

**Seth Godin** -- *Purple Cow* (2003), *This Is Marketing* (2018). Godin's key insight: **build for the smallest viable audience.** Do not try to make something everyone likes. Make something a small group of people *loves*. For scoping, this is liberating: you do not need 10,000 customers. You need 100 people who will pay $49 and tell their friends. Your persona data defines that smallest viable audience.

**Ramit Sethi** -- *I Will Teach You To Be Rich* (2009), and his portfolio of premium digital courses. Sethi's insight: **people will pay a premium for certainty.** His courses cost $2,000+ because they come with systems, scripts, and word-for-word templates that eliminate guesswork. For scoping: the more "done-for-you" your product feels, the more you can charge. Decision trees, templates, and scripts outvalue educational content.

**Patrick McKenzie (patio11)** -- Writing at kalzumeus.com and on Twitter. The patron saint of "charge more." His key insight for software developers: **you are dramatically underpricing your work.** Most indie devs charge $9 for something worth $900 because they anchor to their cost (near zero for digital), not to the value delivered. For scoping, patio11 teaches you to ask: "What is this worth to the buyer?" not "What did it cost me to build?"

**Rob Walling** -- *Start Small, Stay Small* (2010), the MicroConf community. Walling's key insight is the **Stair Step Method**: start with a one-time-purchase product (like a plugin or template), use the revenue to fund a SaaS, use the SaaS to fund something bigger. For scoping, this is crucial: your 1-day product is Step 1 of the staircase. It is not your life's work. It is the first rung.

**Amy Hoy** -- *Just F***ing Ship* (2014), Stacking the Bricks methodology. Hoy's key insight: **sell to people who have the problem RIGHT NOW.** Not people who might have the problem someday. Not people who are "interested in the space." People who are actively suffering and actively spending money to solve it. For scoping, this means: your persona data must show current pain and current spend, not hypothetical interest.

**Nathan Barry** -- *Authority* (2013), founder of ConvertKit. Barry's key insight: the **ladder of products.** Start with a blog post (free). Turn it into a guide ($29). Turn the guide into a course ($249). Turn the course into a workshop ($999). Each step is a repackaging of the same expertise at a higher level of done-for-you. For 1-day scoping: you are building the $29-$79 version. The course and workshop come later, informed by who buys and what they ask for.

---

## 2. The Hormozi Value Equation

This is THE framework for offer design. If you learn nothing else from this document, learn this equation:

```
Value = (Dream Outcome x Perceived Likelihood of Achievement) / (Time Delay x Effort & Sacrifice)
```

This is from Alex Hormozi's *$100M Offers*. It is the most actionable mental model for designing something people will pay for. Let's break down each variable.

### Dream Outcome (Numerator -- Maximize This)

The dream outcome is what the buyer actually wants. Not what they say they want. Not the feature. The *transformation*.

Nobody wants "a Terraform tutorial." They want to stop being the person on the team who can't deploy infrastructure. They want to get promoted. They want to stop feeling stupid in meetings with the DevOps team. They want to ship their side project to production without begging for help.

The dream outcome is always emotional, even when the buyer is technical. Engineers buy tools that make them feel competent, fast, and autonomous. The dream outcome is the *identity* they want to inhabit.

**How to extract this from persona data:** Look at the pain stories. What are they frustrated about? What are they embarrassed about? What would they brag about if they solved it? The dream outcome is the opposite of the pain, stated in the positive.

### Perceived Likelihood of Achievement (Numerator -- Maximize This)

Does the buyer believe *this specific product* will get them to the dream outcome? This is about credibility and specificity. A generic "learn Terraform" course has low perceived likelihood. "The exact Terraform config I used to deploy 14 production services at Scale Co" has high perceived likelihood.

Specificity creates believability. When you say "I will teach you Terraform," nobody believes you. When you say "I will give you the 4-file template that deploys a VPC, ECS cluster, RDS database, and CloudFront distribution in 11 minutes," people believe you because it is specific enough to be verifiable.

**How to increase perceived likelihood:**
- Use specific numbers ("save 8 hours," not "save time")
- Show credentials or experience ("I built this at a company doing $60MM ARR")
- Include testimonials or social proof (even 3 quotes from beta users)
- Offer a guarantee (money back if X -- this shifts risk from buyer to seller)

### Time Delay (Denominator -- Minimize This)

How fast will the buyer see results? A 40-hour course has enormous time delay. A template they can deploy in 15 minutes has almost none.

This is why templates outsell courses. This is why "done-for-you" outsells "learn-it-yourself." The buyer does not want to learn. They want the result. The faster they get the result, the more valuable the product.

**For 1-day products:** This is your biggest lever. If you can design something that delivers the transformation in minutes rather than hours, you have a dramatically more valuable offer. Decision trees, templates, scripts, checklists, and "just follow these steps" formats all minimize time delay.

### Effort and Sacrifice (Denominator -- Minimize This)

How much work does the buyer have to do? A course that requires 20 hours of focused study is high effort. A Notion template they duplicate and fill in is low effort. A decision tree they follow is even lower effort.

This variable also includes psychological sacrifice. Does the buyer have to change their identity? Learn a new paradigm? Admit they were wrong? The lower the effort and sacrifice, the higher the perceived value.

**The key insight:** Maximize the numerator (make the dream bigger, make achievement more believable) and minimize the denominator (make it faster, make it easier). Every offer design decision maps to one of these four variables.

### Worked Example

Suppose your persona data shows senior backend engineers struggling with the "should I learn Kubernetes or stick with ECS?" decision. Here is the value equation analysis:

| Variable | Low-Value Version | High-Value Version |
|---|---|---|
| Dream Outcome | "Learn about container orchestration" | "Make the right infrastructure decision and never second-guess it" |
| Perceived Likelihood | Generic comparison article | "Decision framework used at 6 YC companies, created by ex-AWS architect" |
| Time Delay | 12-hour video course | "15-minute decision tree + 2-page summary" |
| Effort & Sacrifice | Study for a week, build test environments | "Answer 7 questions, get a recommendation with rationale" |

Same topic. Radically different value. The high-value version is actually easier to build in one day AND more valuable to the buyer. This is not a paradox -- it is the core insight of offer design.

---

## 3. Product Formats and When to Use Each

Every digital product falls somewhere on a spectrum from "fastest to ship, lowest price ceiling" to "slowest to ship, highest price ceiling." Here is the full landscape:

### PDF / Guide ($9--$49)

**What it is:** A well-structured document -- could be a PDF, a beautifully formatted Notion page exported to PDF, or even a gated blog post.

**When to use it:** When you need to ship in under 8 hours. When the value is in the *decision* or the *framework*, not in hand-holding. When the buyer is sophisticated enough to implement on their own if they just had the right mental model.

**1-day version:** Write the core framework, include 2-3 worked examples, add a decision tree or checklist. 15-30 pages, no fluff.

**Price ceiling:** $49 for a standalone PDF is pushing it. Beyond that, you need to add another format.

**Best example:** Patio11's blog posts are essentially free guides that are worth thousands. If he packaged "Salary Negotiation for Engineers" as a $39 PDF with email scripts, it would sell like crazy. (He basically gives it away, which is a strategic choice.)

### Notion Template / Spreadsheet ($5--$79)

**What it is:** A pre-built workspace, database, tracker, or system that the buyer duplicates and fills in with their own data.

**When to use it:** When the value is in the *structure*, not the information. People pay for systems that remove the "blank page problem." A content calendar template. A hiring scorecard. An incident response runbook.

**1-day version:** Build the template, write brief instructions for each section, include one filled-in example.

**Price ceiling:** $79 for a single template. Template *bundles* (5-10 related templates) can go to $149.

**Best example:** Thomas Frank's Notion templates generate $1M+/year. The templates themselves are not complex. The value is in the system design and the "just fill this in" experience.

### Video Course ($97--$997)

**What it is:** Structured video lessons, usually with exercises, downloadable resources, and sometimes community access.

**When to use it:** When the skill requires *demonstration* (writing code, using a tool, navigating a UI). When the buyer needs to see someone do the thing before they can do it themselves.

**1-day version:** Record 4-6 screencasts of 10-15 minutes each. No editing beyond trimming the start and end. Ship it on Gumroad or Podia. You can legitimately record, upload, and publish a mini-course in one long day.

**Price ceiling:** $997 for a comprehensive course with community. $97-$297 is the common range for focused, topic-specific courses.

**Caution:** Completion rates for video courses are notoriously low. Udemy courses average under 15% completion. Higher-priced courses ($297+) see significantly better completion because the buyer has skin in the game.

### Workshop / Sprint ($197--$997)

**What it is:** A live, time-bounded event where participants work through a challenge together. Usually 2-8 hours spread over 1-3 days.

**When to use it:** When live interaction dramatically increases the perceived likelihood of achievement. When accountability matters. When you want higher conversion rates (live events convert at 2-5x the rate of static products).

**1-day version:** Announce a 3-hour live workshop for two weeks from today. Spend the day preparing slides and exercises. The product is the event itself.

**Price ceiling:** $997 for a multi-day sprint. $197-$497 is common for a single-session workshop.

**Key advantage:** Built-in urgency and scarcity. "This workshop is on March 15. There are 20 seats." No manufactured scarcity needed.

### Community / Membership ($29--$99/month)

**What it is:** Ongoing access to a group, typically with regular content drops, Q&A sessions, and peer interaction.

**When to use it:** When the value compounds over time. When the problems are ongoing (not one-time). When you want recurring revenue.

**1-day version:** You cannot build a real community in one day. But you can set up the infrastructure (Discord server, welcome sequence, first week of content) and pre-sell founding memberships.

**Price ceiling:** $99/month for niche professional communities. Beyond that, you are in mastermind territory ($500+/month) and need significant social proof.

**Caution:** Communities require constant maintenance. They are the highest-effort format to sustain. Do not start here.

### Consultation / Coaching ($97--$500/hour)

**What it is:** Direct, 1-on-1 access to your expertise.

**When to use it:** When you are learning what to build. Coaching is the best market research there is. You learn exactly what people struggle with, what language they use, and what they will pay for. Then you productize those sessions into a scalable product.

**1-day version:** Put up a Calendly link with Stripe payment. You are selling today.

**Price ceiling:** $500/hour for specialized technical consulting. If you can deliver $5,000+ in value per session (saving someone a week of engineering time), $500 is a bargain.

**Key insight from Ramit Sethi:** Coaching does not scale, but it teaches you what to build when you do scale.

### SaaS Tool ($29--$299/month)

**What it is:** Software-as-a-service. The holy grail of recurring, scalable revenue.

**When to use it:** After you have validated demand with simpler products. Never start here for a 1-day product.

**1-day version:** You can build a functional prototype of a simple SaaS tool in a day, but you cannot build the billing, onboarding, support, and maintenance infrastructure. A better 1-day play: build the workflow as a template or guide, validate demand, then build the tool.

**Price ceiling:** $299/month for B2B tools. Consumer SaaS rarely exceeds $29/month.

### Template + Video Bundle ($29--$149)

**What it is:** A template (Notion, spreadsheet, Figma, code repo) paired with a short video walkthrough showing how to use it.

**When to use it:** This is the single best format for a 1-day product. The template delivers the "done-for-you" value that minimizes effort and time delay. The video increases perceived likelihood by showing exactly how to use it. Together, they hit three of the four Hormozi variables.

**1-day version:** Build the template in the morning. Record a 15-30 minute walkthrough in the afternoon. Package and list on Gumroad by evening.

**Price ceiling:** $149 for a premium bundle. $49-$79 is the sweet spot.

---

## 4. Pricing Strategy from Zero

If you have never priced anything, this section takes you from zero to competent.

### The Wrong Way: Cost-Plus Pricing

Cost-plus means: figure out what it cost you to make, add a margin, charge that. This works for physical goods where materials and labor have real costs. It is completely wrong for digital products. Your marginal cost is zero. A PDF costs you nothing to duplicate. So cost-plus pricing gives you... zero plus margin on zero.

Ignore your costs. They are irrelevant to what you should charge.

### The Right Way: Value-Based Pricing

Value-based pricing means: figure out what this is worth to the buyer, then charge a fraction of that.

If your Terraform template saves a senior engineer 8 hours, and that engineer costs their company $100/hour, the template is worth $800 in saved time. Charging $49 is a 16x return on investment for the buyer. That is a no-brainer purchase.

The formula: **Price = Value to Buyer / 10** (at minimum). This is the "10x rule" -- your product should deliver at least 10x its price in value. Some practitioners (like Hormozi) argue for a 100x ratio. The point is: the buyer should feel stupid NOT buying it.

### Anchoring

Anchoring is the cognitive bias where people evaluate a price relative to the first number they see. If you show a "normally $299" price crossed out, then show $49, the buyer perceives $49 as cheap. Without the anchor, they might perceive $49 as expensive.

This is not manipulation if the anchor is real. If you do 1-on-1 consulting for $200/hour and the template captures 2 hours of your expertise, the anchor of "$400 in consulting value" is legitimate.

### Tiered Pricing (The Rule of Three)

Three tiers work because of the **decoy effect**: most people pick the middle option. Structure your tiers like this:

| Tier | What's Included | Price |
|---|---|---|
| Basic | The core template/guide | $29 |
| Standard | Template + video walkthrough + bonus resources | $49 |
| Premium | Everything + 30-min consultation call | $149 |

The Basic tier exists to make Standard look like a good deal. The Premium tier exists to make Standard look like a bargain. Most people buy Standard. This is by design.

### Charm Pricing

$29 instead of $30. $97 instead of $100. $197 instead of $200. This is not superstition. Decades of retail data show that prices ending in 7 or 9 convert measurably better than round numbers. Use charm pricing for products under $500. Above $500, round numbers signal premium quality.

### "Charge More" -- The patio11 Principle

Patrick McKenzie has repeated this message for over a decade: **you should charge more than you are comfortable with.** Most indie creators dramatically underprice because:

1. They anchor to their cost (near zero) instead of the buyer's value
2. They anchor to mass-market products (Udemy's $12.99 courses) instead of niche premium products
3. They are afraid of rejection ("nobody will pay $49 for a PDF")
4. They have imposter syndrome ("who am I to charge that much?")

The data is clear: raising prices almost always increases revenue, even when it decreases unit sales. A product at $49 with 100 buyers ($4,900) outperforms a product at $9 with 300 buyers ($2,700). And the $49 buyers are better customers -- they are more serious, more likely to use the product, more likely to leave testimonials.

### Price as Quality Signal

Here is a counterintuitive truth: **higher prices increase perceived quality AND completion rates.** Udemy courses at $12.99 have abysmal completion rates (under 15%). Courses priced at $497+ routinely see 61% or higher completion. Why? Because when people pay more, they value the product more. They show up. They do the work. They get results. They leave testimonials. The testimonials drive more sales.

Low prices attract tire-kickers. High prices attract serious buyers. Serious buyers get results. Results sell more product. This is a virtuous cycle, and it starts with pricing higher than your gut says is reasonable.

### The $29--$79 Sweet Spot for Digital Products

For a 1-day product -- a template, a guide, a mini-course -- the sweet spot is $29 to $79.

- **$29**: Low enough for an impulse buy. No committee approval needed. The buyer does not need to think hard. High enough to signal "this is not garbage."
- **$49**: The most common price point for quality digital products. Feels fair. Sits comfortably in the "I'll just buy it and expense it" range for professionals.
- **$79**: The upper end of impulse range. Works when the product has obvious, specific value (templates with proven results, decision trees for high-stakes choices).

Below $29, you are in "lead magnet territory" -- consider giving it away for free in exchange for an email address. Above $79, you need more social proof, more content, and a longer sales page.

### Launch Pricing

Your first launch should be discounted. Not because the product is worth less, but because you are buying testimonials. Offer the first 50 buyers a 40% discount ("founding member price"). Those 50 people buy at $29 instead of $49. They use the product. 10 of them give you testimonials. You raise the price to $49 with 10 testimonials on the sales page. Those testimonials are worth 10x the revenue you "lost."

### Lifetime vs. Subscription

For a 1-day product: sell it as a one-time purchase. Subscriptions require ongoing value delivery that you are not ready to commit to. One-time purchases let you move on to the next product.

Exception: if the product is inherently ongoing (a weekly newsletter, a resource library that grows), subscription makes sense from day one. But this is not a 1-day product -- it is a 1-day launch of an ongoing commitment.

---

## 5. Scoping to One Day

The art of the Minimum Viable Offer is not about cutting corners. It is about cutting *scope* without cutting *quality*. Here is how:

### The Napkin Test

Can you describe the entire product -- what it is, who it is for, and what it does for them -- on a napkin? If not, the scope is too big. A 1-day product solves ONE specific problem for ONE specific person in ONE specific way.

Bad: "A comprehensive guide to cloud infrastructure."
Good: "A decision tree that tells you whether to use ECS or Kubernetes, based on your team size, budget, and compliance requirements."

The napkin version is the good version. Always.

### Cut Scope, Not Quality

The instinct is to cover many topics at a surface level. Resist this completely. Cover fewer topics at a deep level. Three sections of real, actionable depth beat ten sections of overview every time.

A 1-day guide should have 3-5 sections. Each section should deliver one specific, actionable insight. That is it. The buyer came for the transformation, not the page count.

### The "Just the Decision Tree" Principle

Here is the most important scoping insight in this document: **people pay for decisions, not information.**

Information is free. It is abundant. Nobody needs another blog post explaining what Kubernetes is. What they need is someone to tell them: *given your specific situation, here is what you should do and here is why.*

The highest-value product is often literally a decision tree. "If X, do Y. If Z, do W." That is it. That is the product. It might be 3 pages long, and it might be worth more than a 300-page book, because it saves the buyer from the anxiety of choosing wrong.

### Identify the ONE Transformation

Your product delivers exactly one transformation. Before building anything, finish this sentence: "After using this product, the buyer will be able to _____ without _____."

Examples:
- "...choose the right database for their SaaS without spending a week researching options."
- "...write a technical blog post in 2 hours without staring at a blank page."
- "...set up CI/CD for their side project without reading DevOps documentation for a week."

One transformation. Clear. Specific. Measurable.

### Amy Hoy's "Just F***ing Ship" Methodology

Amy Hoy's framework is the operational companion to everything above. The principles:

1. **Start with the audience, not the idea.** You already have persona data. Use it.
2. **Find the pain they will pay to solve TODAY.** Not someday. Today.
3. **Build the smallest thing that solves that pain.** Not the most impressive thing. The smallest.
4. **Ship it before it is perfect.** Version 1.0 is a hypothesis. You will improve it based on feedback, not guesswork.
5. **Charge money from day one.** Free products attract people who do not value what you made. Paid products attract people who need what you made.

The "just ship" ethos is not about quality compromise. It is about recognizing that an imperfect product in the hands of a real buyer teaches you more than a perfect product still on your hard drive.

### The 1-Day Build Schedule

For a template + video bundle (the recommended 1-day format):

| Time Block | Activity |
|---|---|
| Morning (3 hrs) | Build the core template, decision tree, or guide |
| Midday (1 hr) | Write the Gumroad listing: title, description, pricing tiers |
| Afternoon (2 hrs) | Record the video walkthrough (1-2 takes, minimal editing) |
| Late afternoon (1 hr) | Set up payment, create a simple landing page, write 3 social posts |
| Evening (1 hr) | Publish, announce, send to 10 people who fit the persona |

Eight hours. One shippable product. First dollar by tomorrow.

---

## 6. From Persona to Offer (The Bridge)

This is the core of what the offer-scope skill does. It bridges the gap between persona research and a shippable product spec. Here is the process:

### Step 1: Surface Decision Points from Persona Data

Your persona data contains pain stories, frustrations, spending patterns, and decision points. Lay them all out. You are looking for moments where the persona is stuck, confused, or anxious about a choice.

Decision points look like: "Should I use X or Y?" or "How do I do Z without screwing up W?" or "I know I need to do X but I keep putting it off because I don't know where to start."

### Step 2: Score Each Decision Point

For each decision point, score it on three axes:

- **Pain intensity (1-10):** How much does this hurt? How often does it come up?
- **Urgency (1-10):** Do they need to solve this now, or can they defer it?
- **Willingness-to-pay (1-10):** Are they already spending money in this area? (Check SPEND data.)

The decision point with the highest combined score (pain x urgency x willingness-to-pay) is your product's target.

### Step 3: Design the Product That Intervenes at That Exact Moment

You are not building a comprehensive resource. You are building an intervention. The product arrives at the moment of maximum pain and says: "Here. I solved this for you. Follow these steps."

Match the format to the decision point:
- "Which tool should I choose?" -> Decision tree or comparison framework
- "How do I do this specific thing?" -> Template with walkthrough video
- "I don't know where to start." -> Step-by-step guide with the first 3 actions pre-defined

### Step 4: Write the Positioning Using the Persona's Exact Language

This is Dan Kennedy's "message to market match." Do not use your words. Use THEIR words. If the persona says "I'm drowning in YAML configs," your headline is "Stop Drowning in YAML Configs." If they say "I just want something that works," your subheadline is "A Terraform setup that just works -- deploy in 15 minutes."

Pull exact phrases from your persona research. The sales copy writes itself when you use the customer's language.

### Step 5: Set the Price Anchored to What They Already Pay

Look at the SPEND data from your persona research. What are they currently paying for tools, courses, books, and services in this area?

If they pay $29/month for a DevOps tool, a $49 one-time-purchase template is a no-brainer (less than 2 months of their tool spend, and it saves them time every month forever).

If they pay $2,000 for a bootcamp, a $79 guide that delivers 20% of the bootcamp's value is a steal.

Anchor your price to their existing spend, and make the math obviously favorable.

### Step 6: Define the 1-Day Build Spec

The build spec includes:
- **Product title and subtitle**
- **Format** (template, guide, video, bundle)
- **Sections/components** (no more than 5 for a 1-day build)
- **Time estimate per section** (aim for 1-2 hours each)
- **Tools needed** (Notion, Google Docs, Loom, Gumroad, Canva for cover)
- **One-sentence description of each section's value**
- **What is explicitly OUT of scope** (just as important as what is in)

### Step 7: Define the Distribution Plan

Where are these people? Your persona data includes CHANNEL data. Use it.

If they hang out on Reddit's r/devops, your launch plan includes a value-first Reddit post (NOT a sales pitch -- a genuinely useful post that happens to mention your product).

If they are on Twitter/X, your launch plan includes a thread that teaches the core framework and links to the product at the end.

If they read newsletters, your launch plan includes pitching 2-3 newsletter writers for a mention.

The distribution plan is as important as the product itself. A great product with no distribution plan is a tree falling in an empty forest.

---

## 7. The Lingo

This is a glossary of every term you will encounter in offer design, marketing, and product strategy. Know these and you can read any marketing book or course without getting lost.

**Offer vs. Product:** The product is what you build. The offer is the product + positioning + price + guarantee + bonuses + urgency + framing. You sell offers, not products.

**Value Ladder / Ascension Model:** A sequence of products at increasing price points. Free -> $29 -> $297 -> $2,000. Each step builds trust and qualifies the buyer for the next step. Coined by Russell Brunson.

**Lead Magnet:** A free resource given in exchange for an email address. Its only job is to start a relationship. Examples: checklists, cheat sheets, templates, short guides.

**Tripwire:** A cheap product ($7-$27) designed to convert a free subscriber into a paying customer. The goal is not profit; it is to get them to pull out their wallet once. After the first purchase, the second is much easier. Also called a "self-liquidating offer" (SLO).

**Core Offer:** Your main product. The thing that delivers the primary transformation. Typically $29-$497 for digital products.

**Profit Maximizer:** The premium upsell. After someone buys the core offer, you offer something more expensive: a course upgrade, a coaching call, a done-for-you service. This is where the real profit lives.

**Value Stacking:** Adding bonuses to your offer to increase perceived value without dramatically increasing your effort. "Buy the template and also get: the video walkthrough ($97 value), the cheat sheet ($29 value), and the resource list ($19 value)." Total value: $194. Your price: $49.

**Guarantee / Risk Reversal:** A promise that removes the buyer's risk. "30-day money back, no questions asked." Guarantees almost always increase conversion by more than they increase refunds. Hormozi's insight: the stronger the guarantee, the higher the conversion AND the lower the refund rate (because strong guarantees signal confidence).

**Urgency and Scarcity:** Reasons to buy now instead of later. Real urgency: "This workshop is on March 15 and won't be repeated." Real scarcity: "Only 20 seats because I personally review each participant's work." Manufactured urgency: "This price expires in 24 hours!" (works but erodes trust if used repeatedly).

**Social Proof:** Evidence that other people have bought and benefited. Testimonials, student counts, revenue numbers, logos of companies whose employees have used the product.

**Authority:** Credibility signals. Credentials, years of experience, notable employers, published work, conference talks, revenue figures.

**Direct Response vs. Brand Marketing:** Direct response asks for a measurable action (click, buy, sign up) right now. Brand marketing builds long-term awareness. For digital products, direct response is almost always the right approach. Dan Kennedy's entire career is built on this principle.

**Landing Page / Sales Page:** A single web page whose only purpose is to sell one product. No navigation. No distractions. One offer, one CTA.

**Above the Fold / Hero Section:** The portion of the page visible without scrolling. Must contain: the headline, the subheadline, a brief description or bullet points, and the primary CTA. If the above-the-fold content does not hook the reader, they never scroll.

**CTA (Call to Action):** The button or link that asks the buyer to act. "Buy Now." "Get Instant Access." "Join the Workshop." Every page needs exactly one primary CTA, repeated multiple times.

**Conversion Rate:** The percentage of visitors who take the desired action. A 2-5% conversion rate on a sales page is good. 5-10% is excellent. Below 1%, something is broken.

**AOV (Average Order Value):** The average amount a buyer spends per transaction. Upsells, bundles, and tiered pricing all increase AOV.

**Cart Abandonment:** When someone starts the purchase process but does not complete it. Typically 60-80% of carts are abandoned. Follow-up emails recover 5-15% of abandoned carts.

**Upsell / Downsell / Cross-sell:** Upsell: offering a more expensive version after the initial purchase. Downsell: offering a cheaper alternative if they decline the upsell. Cross-sell: offering a related but different product.

**OTO (One-Time Offer):** A special offer presented only once, typically right after a purchase. "You just bought the template -- add the video walkthrough for $19 (normally $49). This offer won't appear again."

**Funnel:** The journey from stranger to buyer. The classic model is AIDA: Awareness (they learn you exist) -> Interest (they engage with your content) -> Desire (they want what you offer) -> Action (they buy).

**Copy vs. Content:** Copy is the words that sell. Content is the words that teach. A blog post is content. A sales page is copy. Many engineers are good at content and terrible at copy because they have never studied the difference.

**Headline, Subheadline, Bullet Points, CTA:** The anatomy of a sales page. The headline grabs attention. The subheadline explains the value. The bullet points list specific benefits. The CTA tells them what to do. This structure has been proven for 100 years (Claude Hopkins was using it in the 1920s).

**"Features Tell, Benefits Sell."** A feature: "Includes 4 Terraform modules." A benefit: "Deploy production infrastructure in 15 minutes instead of 2 weeks." Features describe what the product HAS. Benefits describe what the product DOES FOR THE BUYER. Always lead with benefits.

**"People Buy on Emotion, Justify with Logic."** The decision to buy is emotional (relief, excitement, fear of missing out). The justification is logical ("it's tax deductible," "it'll save me 8 hours"). Your sales copy must do both: trigger the emotion, then provide the logic.

**"Sell the Transformation, Not the Information."** Nobody wants a 200-page PDF. They want the person they become after applying what is in the PDF. Sell that person. "Go from confused about infrastructure to confidently deploying production systems." That is a transformation. "200-page guide to Terraform" is information. One sells. One does not.

---

## 8. Distribution Channels (Where to Sell)

Building the product is half the work. Getting it in front of buyers is the other half. Here are the channels, with honest assessments:

**Gumroad** -- The easiest way to start selling digital products. 10% transaction fee (flat, no monthly cost). Built-in audience discovery (people browse Gumroad). Handles payment, delivery, and basic analytics. Downside: limited customization, the 10% fee adds up. Best for: your first product, validating demand.

**Lemon Squeezy** -- A modern Gumroad alternative with better UI, lower fees (5% + 50 cents), and good support for software licenses and SaaS billing. Best for: technical creators who want more flexibility than Gumroad.

**Teachable / Podia / Kajabi** -- Purpose-built for courses. Teachable is the biggest. Podia is the simplest. Kajabi is the most full-featured (and most expensive). Best for: video courses with multiple modules, especially if you want drip content (releasing modules on a schedule).

**Your Own Site + Stripe** -- Maximum control, maximum margin (Stripe charges 2.9% + 30 cents). Requires building your own checkout flow, delivery system, and sales page. Best for: after you have validated demand elsewhere and want to own the full experience.

**Product Hunt** -- Good for launch-day traffic if your product appeals to the PH audience (developers, designers, startup people). Best for: tools and templates, less effective for educational products. Plan your launch for a Tuesday (highest traffic day).

**Reddit** -- The most underrated channel for digital products. The key: provide genuine value first, sell second. A detailed post that teaches 80% of the value for free and links to the product for the remaining 20% will do well. A post that is obviously just an ad will get downvoted into oblivion and potentially get you banned.

**Twitter/X** -- The "build in public" channel. The playbook: write threads that teach (using your product's framework), build an audience of people who trust your expertise, then sell to them. The thread-to-product pipeline is proven: Daniel Vassallo, Sahil Lavingia, and dozens of others have built six-figure product businesses this way.

**Email List** -- The ONLY distribution channel you actually own. Every other channel (Twitter, Reddit, Product Hunt) is rented. The algorithm can change. Your account can be suspended. Your email list is yours. Everyone in digital products says the same thing: "I wish I had started building my email list sooner." Start with a free lead magnet (decision tree, checklist, template) to collect emails.

**AppSumo** -- A marketplace for lifetime deals. Good for getting a burst of initial traction (hundreds or thousands of sales). Bad for long-term revenue (you are selling lifetime access at a deep discount). Best for: products that benefit from a large user base (tools, templates with network effects). Be cautious: AppSumo customers are deal-seekers, not your long-term audience.

---

## 9. Case Studies

Theory without examples is forgettable. Here are four real-world examples of offer design in action:

### Alex Hormozi: Gym Launch ($500 to $42,000)

Hormozi worked with gym owners who were selling $500 gym memberships. The PRODUCT did not change -- same gym, same equipment, same trainers. What changed was the OFFER.

The old offer: "$500 for a gym membership."
The new offer: "We guarantee you lose 20 pounds in 6 weeks or you don't pay. Includes: personalized meal plan, 3x/week personal training, weekly accountability calls, and a body composition analysis every 2 weeks. $42,000."

Same gym. 84x the price. The difference: the offer stacked value (meal plan, training, accountability), added a guarantee (risk reversal), specified the transformation (20 pounds in 6 weeks), and backed it with perceived likelihood (personalized, weekly check-ins).

This is the purest illustration of "you don't need a better product, you need a better offer."

### Daniel Vassallo: The Twitter Course ($0 to $250K+ in 16 Hours of Work)

Daniel Vassallo, an ex-Amazon engineer, grew his Twitter following to 30K and realized people wanted to know how. He wrote a short course -- essentially a guide with his frameworks and examples -- in about 16 hours of total work. He priced it at $30 on Gumroad.

The key to Vassallo's success was not the content (which was good but not revelatory). It was the offer design:
- **Dream outcome:** Grow a Twitter audience that generates income
- **Perceived likelihood:** High -- Vassallo had a public track record, growing from 0 to 30K
- **Time delay:** Low -- the course was short and actionable, not a 40-hour marathon
- **Effort:** Low -- specific tactics, not vague principles

He also benefited from distribution: his 30K Twitter followers were the exact audience for the product. He did not have to find them. They were already there.

### Thomas Frank: Notion Templates ($0 to $1M+/year)

Thomas Frank built a YouTube audience of millions by making videos about productivity. When Notion became popular, he started creating templates -- productivity dashboards, content calendars, habit trackers.

The templates themselves are well-designed but not technically complex. Any Notion power user could build them. What makes Frank's offer work:
- **Authority:** Millions of YouTube subscribers trust his productivity advice
- **Value stacking:** Each template comes with a detailed video walkthrough
- **Perceived likelihood:** "If Thomas Frank's system doesn't work, nothing will"
- **Low effort:** Duplicate the template, fill in your data, done

The lesson: the product is the template. The offer is the template + Thomas Frank's authority + the video walkthrough + the proven system. The offer is worth 100x the template alone.

### patio11: From $5/month to Enterprise Pricing

Patrick McKenzie's first product, Bingo Card Creator, charged $30 for a license. His later consulting work charged hundreds of dollars per hour. His key insight, repeated across hundreds of blog posts and conference talks: **the product barely changed. The offer did.**

At $5/month, Bingo Card Creator was "a tool that makes bingo cards." At $295/year, the same core product (with modest additions) was "appointment reminder software that reduces no-shows by 30%, saving medical practices $XX,000/year." The shift: from describing what the product IS to describing what the product DOES for the buyer, expressed in dollars.

For your 1-day product: do not describe what it is ("a Notion template for tracking deployments"). Describe what it does for the buyer ("save 4 hours per week on deployment coordination and never miss a rollback window again").

---

## 10. The Framework: Signal-to-Ship Architecture

Everything in this document synthesizes into a single, repeatable process. We call it the **Signal-to-Ship Architecture** because it converts market signals (persona data, pain stories, spending patterns) into shipped products in a single day.

### The Process

```
INPUT:  Persona data + decision points + SPEND signals + CHANNEL data
  |
  v
SCORE:  Hormozi Value Equation applied to each decision point
  |     - Which decision point has the highest dream outcome?
  |     - Which one has the highest perceived likelihood (you have credibility)?
  |     - Which one has the lowest time delay (you can build it fast)?
  |     - Which one requires the lowest effort from the buyer?
  |
  v
FILTER: Which of the top-scoring decision points is 1-day shippable?
  |     - Can you describe it on a napkin?
  |     - Does it require one product format (not three)?
  |     - Can you build the core in 3-4 hours?
  |
  v
DESIGN: Complete offer specification
  |     - Product: format, sections, scope
  |     - Positioning: headline, subheadline, bullets (using persona language)
  |     - Pricing: value-based, anchored to persona's current spend
  |     - Guarantee: what risk reversal can you offer?
  |     - Bonuses: what low-effort additions increase perceived value?
  |     - Distribution: where do these people already hang out?
  |
  v
OUTPUT: 1-Day Build Spec
        - Product title and subtitle
        - Format and components
        - Section-by-section outline with time estimates
        - Pricing (with tier structure if applicable)
        - Sales page copy outline (headline, subheadline, 5 bullets, CTA)
        - Distribution plan (3 specific channels with tactics)
        - Out-of-scope list (what you are NOT building)
```

### The Sources

This framework is a synthesis, not an invention. Here is what it draws from:

| Component | Source |
|---|---|
| Value scoring | Hormozi's Value Equation (*$100M Offers*) |
| Decision-point focus | Amy Hoy's "sell to people with the pain RIGHT NOW" (*Stacking the Bricks*) |
| 1-day scope filtering | Hoy's "Just F***ing Ship" + Rob Walling's Stair Step Method |
| Persona-language positioning | Dan Kennedy's "message to market match" (*No B.S. Direct Marketing*) |
| Value-based pricing | Patrick McKenzie's "charge more" + Hormozi's 10x value rule |
| Format selection | Nathan Barry's product ladder (*Authority*) |
| Distribution planning | Russell Brunson's funnel architecture (*DotCom Secrets*) |
| Starving crowd validation | Gary Halbert's "starving crowd" (*The Boron Letters*) |
| Smallest viable audience | Seth Godin's "minimum viable audience" (*This Is Marketing*) |
| Testing/iteration mindset | Claude Hopkins (*Scientific Advertising*) |
| Premium positioning | Ramit Sethi's "pay certainty" model |

### What This Skill Produces

When the offer-scope skill runs, it takes in persona data and produces a complete, buildable offer spec:

1. **Product Definition:** What you are building, in what format, with what sections
2. **Value Proposition:** The one-sentence transformation, written in the persona's language
3. **Pricing Recommendation:** Specific price point with justification (anchored to value and existing spend)
4. **Sales Page Outline:** Headline, subheadline, 5 benefit bullets, guarantee, CTA
5. **Build Plan:** Section-by-section breakdown with time estimates, totaling one working day
6. **Distribution Plan:** 3 channels where the persona already spends time, with specific tactics
7. **Scope Boundaries:** Explicit list of what is not included (prevents scope creep)

---

## 11. Canonical Reading List

If you want to go deeper, here is the reading list in priority order. The first three are non-negotiable. The rest are for when you want to specialize.

| Priority | Book/Resource | Author | Key Lesson |
|---|---|---|---|
| 1 | *$100M Offers* | Alex Hormozi | The Value Equation. How to design offers people feel stupid refusing. |
| 2 | *Just F\*\*\*ing Ship* | Amy Hoy | Ship small, ship fast, sell to people with the pain right now. |
| 3 | *Authority* | Nathan Barry | The product ladder. Blog -> guide -> course -> workshop. |
| 4 | *DotCom Secrets* | Russell Brunson | Funnel architecture. Value ladders. Traffic and conversion. |
| 5 | *The Boron Letters* | Gary Halbert | Copywriting fundamentals. "Starving crowd" market selection. |
| 6 | *No B.S. Direct Marketing* | Dan Kennedy | Every dollar must produce a measurable result. Message to market match. |
| 7 | kalzumeus.com | Patrick McKenzie | Pricing for developers. "Charge more." Software as business. |
| 8 | *Scientific Advertising* | Claude Hopkins | Test everything. Measure everything. Advertising is salesmanship in print. |
| 9 | *This Is Marketing* | Seth Godin | Smallest viable audience. Be remarkable to someone, not mediocre to everyone. |
| 10 | *I Will Teach You To Be Rich* | Ramit Sethi | Premium pricing. People pay for certainty. Scripted systems sell. |
| 11 | *Start Small, Stay Small* | Rob Walling | Stair Step Method. One-time product -> SaaS -> bigger SaaS. |
| 12 | *$100M Leads* | Alex Hormozi | After you have the offer: how to get people to see it. Lead generation at scale. |
| 13 | *Expert Secrets* | Russell Brunson | Positioning yourself as the expert. Story-based selling. |
| 14 | stackingthebricks.com | Amy Hoy | "Sales Safari" -- researching your audience in their natural habitat. |

---

## Final Note

You are an engineer. You already know how to build. This document teaches you the other half: what to build, for whom, at what price, in what format, and why someone would buy it.

The single biggest shift is this: stop thinking about what is interesting to build and start thinking about what is painful to NOT have. Pain is the market signal. Your product is the painkiller. The offer is how you make someone believe, in 30 seconds of reading a sales page, that this specific painkiller will work for them, starting today, with minimal effort.

Build the smallest thing. Ship it in a day. Charge more than you think you should. Listen to what buyers tell you. Build the next thing. That is the entire game.
