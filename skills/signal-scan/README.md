# Signal Scan: A Masterclass in Product Signal Detection and Market Sensing

> Written for the engineer who can build anything but has never had to figure out *what* to build.

---

## Table of Contents

1. [The Discipline](#the-discipline)
2. [The Canon: Thinkers, Texts, and Frameworks](#the-canon)
3. [The 7 Signal Types](#the-7-signal-types)
4. [The Lingo](#the-lingo)
5. [The Process: How Signal Scanning Actually Works](#the-process)
6. [Tools of the Trade](#tools-of-the-trade)
7. [Case Studies](#case-studies)
8. [The Framework This Skill Implements](#the-framework-this-skill-implements)

---

## The Discipline

Here is the uncomfortable truth about software: building the product is rarely the hard part. Figuring out what product to build -- and for whom, and why they would pay for it, and how they would find it -- that is the hard part. Most engineers skip it entirely. They build something clever, launch it into silence, and conclude that "marketing is broken" or "people don't appreciate good engineering." The actual problem is that they never detected a signal worth building for in the first place.

**Product signal detection** is the discipline of systematically finding evidence that an opportunity exists before you commit to building something. It sits at the intersection of several fields that rarely talk to each other:

- **Product management** asks "what should we build and why?" Product discovery -- the practice of Teresa Torres and Marty Cagan -- is about continuously talking to users and testing assumptions so you build things people actually want. Signal detection is the first phase of product discovery: identifying which assumptions are even worth testing.

- **Marketing** asks "who wants this and how do we reach them?" Market research, competitive intelligence, and demand generation are all signal-detection activities wearing different hats. When a marketer runs a keyword research report or analyzes competitor positioning, they are collecting signals. When they run a demand gen campaign, they are testing whether a signal is real.

- **Sales** asks "who is ready to buy right now?" Buying signals, intent data, and lead scoring are signal detection applied to individual prospects rather than markets. When a sales team tracks that a prospect visited their pricing page three times this week, downloaded the comparison whitepaper, and their company just posted a job for the role your product serves -- those are signals.

- **Growth** asks "what makes people stay and pay?" Product-led growth, activation metrics, and retention analysis are signal detection applied to behavior inside your own product. When a growth team discovers that users who complete three actions in their first session retain at 80% while users who complete one action retain at 20%, they have found a signal.

Signal detection is upstream of all of these. It is the practice of listening before speaking, observing before building, and measuring before committing. The reason most products fail is not that they were built badly. It is that nobody checked whether the world actually needed them.

Market sensing is the broader discipline: the ongoing practice of monitoring a market for shifts, opportunities, threats, and patterns. Signal detection is the specific act of identifying and evaluating individual signals within that practice. Think of market sensing as the radar system and signal detection as the act of reading what appears on the screen.

If you are an engineer who has never done go-to-market (GTM) work, product discovery, or market research, this document will teach you the entire vocabulary, the canonical frameworks, and the specific process this skill uses to scan a domain for opportunities. By the end, you will be able to hold your own in any conversation about product strategy, market analysis, or competitive intelligence -- not because you memorized jargon, but because you understand the underlying structure of how markets produce signals and how people who are good at this read those signals.

---

## The Canon

Every discipline has its foundational thinkers. Product signal detection draws from several traditions. Here are the people whose work you need to know, what they contributed, and how each feeds into what this skill does.

### Teresa Torres -- Continuous Discovery Habits (2021)

**Key insight**: Product teams should talk to customers every single week, not in quarterly research bursts. Discovery is a continuous habit, not a project.

**Framework**: The **Opportunity Solution Tree (OST)**. You start with a desired outcome, branch into opportunities (customer needs, pain points, desires), and then branch into solutions and experiments. The tree forces you to separate the problem space (opportunities) from the solution space (what you build) and to generate multiple solutions before committing to one.

**Feed into signal detection**: Torres teaches you that the raw material of product decisions is opportunities, not ideas. Signal scanning is how you populate the top of an Opportunity Solution Tree when you do not yet have a customer base to interview. Her interview techniques -- asking about specific past behaviors rather than hypothetical futures -- directly inform what counts as quality evidence in a signal scan.

### Marty Cagan -- Inspired (2008, revised 2017) and Empowered (2020)

**Key insight**: The best product teams are empowered to solve problems, not handed feature lists. Product discovery -- the process of determining whether a solution is valuable, usable, feasible, and viable -- should happen before engineering commits to building anything.

**Framework**: The **Four Risks of Product Discovery**: value risk (will people buy or use it?), usability risk (can they figure out how to use it?), feasibility risk (can we build it?), and viability risk (does it work for our business?). Cagan argues that most product failures are value risk failures -- you built something nobody wanted.

**Feed into signal detection**: Signal scanning is almost entirely about value risk. When you detect pain signals, spend signals, and demand signals, you are gathering evidence that the value risk is low. When you check competitive signals and sentiment, you are assessing whether the market structure supports a new entrant. Cagan is the reason product people obsess over "evidence of value" before writing a single line of code.

### April Dunford -- Obviously Awesome (2019)

**Key insight**: Positioning is not messaging. Positioning is the fundamental act of defining what your product is, who it is for, and why they should care. Most products are poorly positioned -- not poorly built or poorly marketed, but poorly defined in the mind of the buyer.

**Framework**: The **Positioning Canvas**, which asks five questions: (1) What are the competitive alternatives? (2) What are your unique attributes? (3) What value do those attributes enable? (4) Who are the customers who care most about that value? (5) What market category makes your value obvious?

**Feed into signal detection**: Dunford teaches you that the same product can succeed or fail depending on how it is positioned. Signal scanning collects the raw material for positioning: competitive alternatives come from COMPETITIVE signals, unique attributes come from your operator edge, customer segments come from AUDIENCE and PAIN signals, and market category comes from the meta-signal synthesis. You cannot position well without first scanning the landscape.

### Bob Moesta and Clayton Christensen -- Jobs to Be Done (JTBD)

**Key insight**: People do not buy products. They hire products to do a job. A "job" is a progress that a person is trying to make in a particular circumstance. The milkshake is not competing with other milkshakes -- it is competing with bananas, bagels, boredom, and the steering wheel that needs a free hand.

**Framework**: The **Forces of Progress** diagram. Four forces act on a buyer: (1) push of the current situation (dissatisfaction), (2) pull of the new solution (attraction), (3) anxiety of the new solution (fear of switching), and (4) habit of the current situation (inertia). A sale happens when push + pull exceeds anxiety + habit.

Christensen originally articulated the theory; Moesta operationalized it through **Switch Interviews** -- structured conversations that reconstruct the timeline of how someone decided to switch from one solution to another, revealing the true causal forces behind purchase decisions.

**Feed into signal detection**: PAIN signals map directly to "push of the current situation." DEMAND signals map to "pull of a new solution." SENTIMENT signals (especially around existing tools) reveal anxiety and habit forces. When you see high pain plus negative sentiment toward existing solutions, you are seeing a JTBD where push is high and habit is weakening. That is a strong signal.

### Anthony Ulwick -- Outcome-Driven Innovation (ODI) and What Customers Want (2005)

**Key insight**: Innovation is predictable when you measure what customers are trying to accomplish, not what they say they want. Customers have "desired outcomes" -- measurable statements of what success looks like for a job -- and you can survey them to find which outcomes are underserved (high importance, low satisfaction).

**Framework**: The **Opportunity Algorithm**: `Opportunity = Importance + (Importance - Satisfaction)`. Outcomes that are very important but very unsatisfied are underserved -- prime territory for innovation. Outcomes that are overserved (low importance, high satisfaction) are features you can cut.

**Feed into signal detection**: Ulwick's Opportunity Algorithm is the direct ancestor of the scoring matrix this skill uses. The signal-scan scoring system measures pain intensity (analogous to importance), competition gap (analogous to dissatisfaction with current solutions), and spend evidence (proof that the job is important enough to pay for). The weighted formula `(pain*2 + spend*2 + edge + time + gap + audience) / 8` is a practical adaptation of Ulwick's insight that importance and dissatisfaction should be weighted more heavily than other factors.

### Sean Ellis -- Hacking Growth (2017) and the PMF Survey

**Key insight**: Product-market fit is not a feeling. It is measurable. Ellis developed the now-canonical PMF survey question: "How would you feel if you could no longer use this product?" If 40% or more of users say "very disappointed," you have product-market fit.

**Framework**: The **ICE Score** (Impact, Confidence, Ease) for prioritizing growth experiments. Also popularized the concept of the **North Star Metric** -- the single metric that best captures the core value your product delivers.

**Feed into signal detection**: Ellis proved that you can quantify product-market fit with a single question. Signal scanning is the pre-product version of the same impulse: instead of asking existing users "would you miss this?", you are asking the market "does this problem hurt enough that someone would pay to solve it?" The intensity and recurrence fields in PAIN signals are doing the same work as Ellis's PMF survey, just before the product exists.

### Arvid Kahl -- The Embedded Entrepreneur (2020)

**Key insight**: The best businesses are built by people who are embedded in a community before they start building. Find an audience, understand their problems intimately, and build solutions that sell themselves through the community.

**Framework**: **Audience-first entrepreneurship**. Instead of idea-first ("I had an idea, now I need to find customers"), start with a group of people you understand deeply. Kahl's framework: (1) find a niche audience, (2) understand their critical problems, (3) build a solution that fits their workflow, (4) sell to them through channels they already use.

**Feed into signal detection**: Kahl is the reason the AUDIENCE signal type exists in this taxonomy. His core argument -- that distribution is the bottleneck, not product quality -- is why this skill weights audience_fit in the scoring matrix. A mediocre opportunity with a strong audience signal often beats a great opportunity with no distribution path.

### Daniel Vassallo -- Small Bets (2021)

**Key insight**: Instead of making one big bet on a single product, make many small bets. Each bet should be cheap to produce, have uncapped upside, and teach you something about what the market wants. The portfolio approach reduces risk and accelerates learning.

**Framework**: The **Small Bets Portfolio**. Ship fast, ship cheap, let the market tell you what works, then double down on winners. Vassallo explicitly rejects business plans, market sizing, and extensive pre-launch research in favor of rapid experimentation. His philosophy: you learn more from shipping a $20 PDF in one weekend than from six months of market research.

**Feed into signal detection**: Vassallo represents the "just ship it" school, which seems to contradict signal scanning. But it actually complements it. Signal scanning is how you decide *which* small bets to make. Vassallo's key practice -- observing what gets engagement on Twitter/X before deciding what to productize -- is signal detection done informally. This skill formalizes and systematizes the same intuition. The requirement in this skill that "at least one ship candidate per opportunity must be shippable in 1-3 days" is pure Vassallo.

### Rob Walling -- Start Small, Stay Small (2010) and the Stair Step Method

**Key insight**: Most software entrepreneurs should not start with a SaaS. They should start with a small, one-time purchase product (an ebook, a plugin, a template), use the revenue and audience from that to fund a slightly bigger product, and stair-step their way up to recurring revenue.

**Framework**: The **Stair Step Method of Entrepreneurship**. Step 1: one-time purchase product in a market with existing demand (WordPress plugin, info product). Step 2: subscription product with a small audience. Step 3: larger SaaS with marketing and possibly funding. Each step funds the next and builds skills.

Walling also runs **MicroConf**, the conference for bootstrapped SaaS founders, which has become the central gathering point for the indie SaaS community and a rich source of tactical knowledge about finding and validating product opportunities.

**Feed into signal detection**: Walling's Stair Step Method is why the ship candidates in this skill span formats from PDFs and templates to courses to tools to SaaS. The skill deliberately generates candidates at multiple levels of effort and revenue model because the right first ship is often not the big product you eventually want to build -- it is the small product that validates demand, builds audience, and generates revenue while you learn.

---

## The 7 Signal Types

This skill uses a taxonomy of 7 signal types. Every piece of evidence you collect during a scan maps to exactly one of these types. Together, they form a complete picture of a market opportunity.

The taxonomy is a synthesis. It draws on Ulwick's outcome-driven thinking (importance and satisfaction), Christensen and Moesta's forces of progress (push and pull), Kahl's audience-first framework, and competitive intelligence from the strategic marketing tradition. It is not a copy of any single framework. It is a practical merger designed for a specific use case: a solo operator or small team scanning a domain for what to build and sell.

### 1. PAIN -- What Hurts

**Definition**: Evidence that people are struggling, complaining, suffering, or spending disproportionate time on something. Pain is the most important signal type because pain creates urgency. People pay to make pain go away faster than they pay to gain pleasure.

**Examples**:
- A Reddit post in r/devops with 200+ upvotes titled "I am losing my mind trying to manage Terraform state across teams"
- A Twitter/X thread where 15 people reply to "What's your biggest frustration with [tool]?" with the same answer
- A G2 review that says "We spent 6 weeks trying to migrate and almost gave up"

**Where to find it**: Reddit threads (sort by top and controversial -- both surface strong pain), forum posts, 1-2 star reviews on G2/Capterra/Trustpilot/app stores, support forum complaints, social media rants, Hacker News complaint threads.

**How to measure intensity**: On a 1-10 scale, calibrated by evidence.
- 1-3: Minor annoyance. People mention it and move on. "It's a bit clunky."
- 4-6: Real friction. People spend time complaining or building workarounds. "I wasted half a day on this."
- 7-8: Significant pain. Emotional language, multiple threads, people actively seeking alternatives. "This is a nightmare. I'm switching as soon as I can."
- 9-10: Dealbreaker. People abandon workflows, switch tools at great cost, or hire someone to solve it. "We hired a full-time person just to manage this."

**Common mistakes**:
- Confusing volume with intensity. A thousand people mildly annoyed is a weaker signal than fifty people in agony. Intensity matters more than volume for small operators.
- Treating "I wish [product] had [feature]" as a pain signal. That is a demand signal. Pain is about what hurts, not what would be nice.
- Hallucinating pain from your own experience. "I find X annoying, so others must too" is not evidence. Find the posts. Quote the people.

**The lingo**: Product people call these "user pain points" or "friction points." Marketers call them "customer challenges" or "objections." Indie hackers call them "hair-on-fire problems." In JTBD terminology, pain is the "push of the current situation" -- the force that pushes someone away from what they are doing now.

### 2. DEMAND -- Who Is Actively Looking

**Definition**: Evidence that people are actively seeking a solution. Demand differs from pain in an important way: pain is about suffering, demand is about seeking. Someone can be in pain without seeking a solution (they have accepted it) and someone can be seeking a solution without being in pain (they want improvement, not relief).

**Examples**:
- Google Trends showing "terraform state management tool" at a 3-year high
- Reddit posts saying "Does anyone know a good tool for X?" appearing weekly in three different subreddits
- A waitlist for an upcoming product that has 5,000 signups in two weeks
- Feature requests on a competitor's public roadmap with hundreds of upvotes

**Where to find it**: Google Trends and keyword research tools, "I wish..." and "looking for..." posts on Reddit and forums, Product Hunt launches with high engagement, waitlist numbers, crowdfunding campaigns, feature request boards for existing products.

**How to measure volume and trend**: Volume (low/moderate/high/extreme) captures how many people are looking. Trend (declining/stable/growing/exploding) captures the direction. The combination matters: high volume + declining trend means the market is saturated or the problem is being solved. Moderate volume + exploding trend means you are early to a rising wave.

**Common mistakes**:
- Treating Google Trends absolute numbers as meaningful. Google Trends shows *relative* interest, not absolute search volume. "100" on Google Trends means "the peak of interest for this term in the selected time range," not "100 searches." Pair Trends with actual search volume data from a keyword tool.
- Confusing curiosity with demand. High search volume for "what is [X]" indicates curiosity. High search volume for "[X] tool" or "best [X] software" indicates demand. The difference between someone researching a topic and someone shopping for a solution is the difference between informational intent and commercial intent.

**The lingo**: Product people call this "user demand" or "market pull." Marketers call it "demand signals" or "search intent" (specifically "commercial intent" or "transactional intent"). In advertising, this maps to "bottom-of-funnel keywords." Growth people track this as "organic demand."

### 3. SPEND -- Where Money Already Changes Hands

**Definition**: Evidence that people are already paying for something in or adjacent to this problem space. Spend is the most reliable signal type because it eliminates the gap between what people say and what people do. Talk is cheap. Credit card transactions are not.

**Examples**:
- A Udemy course on the topic with 47,000 students at $19.99 and a 4.6-star rating
- Gumroad creator pages showing $12K+ in revenue for a template pack
- An AppSumo deal with 800+ reviews
- Competitor pricing at $49/mo, $99/mo, $249/mo tiers

**Where to find it**: Udemy/Skillshare/Coursera bestseller lists (student counts, ratings, price points), Gumroad trending products and creator profiles, AppSumo deals and review counts, competitor pricing pages, job postings (companies hiring for this = budget exists), conference ticket prices and attendance numbers.

**How to measure it**: Capture the actual price range and the volume evidence. "47,000 students at $10-25" is a data point. "Bestseller badge with 2,300 ratings" is a data point. "Probably makes good money" is not a data point. TAM numbers ("the market is worth $50 billion") are useless for product validation because they tell you nothing about what individual humans will pay for a specific product at a specific price.

**Common mistakes**:
- Assuming willingness-to-pay from willingness-to-complain. People who complain loudly about a problem on Reddit are not necessarily people who will pay to solve it. SPEND data is the antidote to this illusion.
- Ignoring price anchoring. If every existing course on the topic sells for $10-15 on Udemy, you need a very strong differentiation story to sell a $200 course. Spend data tells you not just that people pay, but how much and in what formats.
- Confusing venture-backed spending with organic spending. A VC-funded competitor offering a free tier is not evidence that users will pay. Look for evidence of actual cash transactions from end users.

**The lingo**: Marketers call this "WTP" (willingness to pay) or "market validation." Product people call it "revenue evidence" or "monetization signal." Indie hackers say "people are already paying for this" or "there's money on the table." In the JTBD world, existing spend reveals the "budget" the job already has.

### 4. BEHAVIOR -- What People Actually Do

**Definition**: Observable actions people take -- workarounds they build, tools they switch to, things they automate, people they hire. Behavior is more reliable than stated preferences because people lie about what they want but do not lie about what they do. A Stack Overflow answer with 500 upvotes showing a hacky three-step workaround is stronger evidence than a survey saying "I would pay for a solution to this."

**Examples**:
- A Stack Overflow answer with 1,200 upvotes that shows a 47-line bash script to work around a limitation
- Zapier templates for automating a manual process that have thousands of users
- GitHub repos with names like "my-janky-[X]-solution" that have hundreds of stars
- Job postings for "DevOps Engineer" that list a specific manual task as a core responsibility

**Where to find it**: Stack Overflow workaround answers (high-vote hacky solutions), Zapier/Make/n8n automation templates, GitHub repos (especially personal tools that people built for themselves and open-sourced), job postings, "I built a script that..." posts on Reddit, forum threads showing multi-step manual processes.

**How to measure effort level**: How much effort did people invest in the workaround? Low (minutes), moderate (hours), high (days, custom scripts), extreme (hired a contractor, built an internal tool, dedicated an entire role). Higher effort = stronger signal. If someone spent a weekend building a script to solve a problem, the problem is real.

**Common mistakes**:
- Overlooking workarounds because they look unimpressive. The uglier and more duct-taped the workaround, the stronger the signal. Beautiful, well-maintained workarounds mean the problem is solved. Ugly, fragile workarounds mean the problem is screaming for a real solution.
- Missing the "build vs. buy" threshold. When companies hire a full-time person to do something that could be a product, that is an extreme behavior signal. The company is spending $80K-150K per year on a salary to solve a problem. That is your TAM denominator.

**The lingo**: Product people call these "workarounds" or "compensating behaviors." In the JTBD framework, these are "current solutions to the job" -- even when the person doing them would not describe them as "solutions." UX researchers call this "observational research" or "contextual inquiry." Growth teams talk about "revealed preferences" (what people do) versus "stated preferences" (what people say).

### 5. SENTIMENT -- How People Feel About What Exists

**Definition**: The emotional orientation of a market toward existing solutions. Sentiment tells you whether there is room for a new entrant and what angle they should take. It is not about whether a market exists (that is DEMAND) or whether people are paying (that is SPEND) -- it is about whether people are *happy* paying, *tolerant* while paying, or *furious* while paying.

**Examples**:
- G2 reviews averaging 3.2 stars with recurring complaints about onboarding difficulty
- Reddit threads where mentioning a specific tool triggers a pile-on of complaints
- An app store with hundreds of 1-star reviews all mentioning the same issue
- NPS scores below 20 for a market-leading product

**Where to find it**: Review sites (G2, Capterra, TrustPilot, app store reviews), NPS data (when accessible), social media sentiment, "I switched from X to Y because..." posts, forum threads about specific tools, Hacker News discussions.

**Valence scale**:
- **Positive**: People are satisfied. Minor complaints at most. This market is hard to enter.
- **Mixed**: Real praise AND real complaints. There is room for a differently-positioned entrant.
- **Negative**: Majority dissatisfied. Common complaints, low review scores. Strong opening for a competitor.
- **Hostile**: Active anger. Public callouts, organized complaints, "boycott" energy, migration threads. The market is desperate for an alternative.

**The actionable pattern**: The most lucrative signal combination in all of product strategy is **negative sentiment + high spend**. This means people are paying for something they hate because nothing better exists. They are captive customers. Build the better version and they will switch. This is the pattern that created Slack (people hated email for team communication but used it constantly), Figma (designers were frustrated with Sketch's collaboration limitations but paid for it), and countless smaller products.

**Common mistakes**:
- Treating positive sentiment as "good." If everyone loves the existing solutions, there is no opening. Positive sentiment is a stop signal for entering a market, not a go signal. You want mixed or negative sentiment.
- Reading sentiment without reading volume. Ten hostile reviews on a product with 100,000 users is noise. Ten hostile reviews on a product with 200 users is a structural problem.

**The lingo**: Marketers call this "brand sentiment" or "brand perception." Product people call it "user satisfaction" or "NPS." Competitive analysts call it "competitive vulnerability." VCs call it "switching propensity." If you hear someone say "there's blood in the water," they are describing hostile sentiment.

### 6. COMPETITIVE -- What the Landscape Is Doing

**Definition**: Observable movements in the competitive landscape -- who is entering, who is leaving, who is raising prices, who is shipping new features, where the gaps are. Competitive signals tell you about market structure and timing.

**Examples**:
- A major player shutting down a product line, leaving customers stranded
- Two competitors merging, which usually means price increases follow
- A feature that every competitor lacks, despite users requesting it publicly
- A new entrant raising a $10M Series A in a space you were considering

**Where to find it**: Competitor product announcements and changelogs, funding news (Crunchbase, TechCrunch), product shutdowns and sunset announcements, pricing page changes (use the Wayback Machine), feature comparison matrices, market consolidation news.

**Signal subtypes**:
- **Gap**: Something the market needs that nobody provides well. The most valuable competitive signal.
- **New entrant**: Someone new entering the space. Could be a threat (well-funded competitor) or validation (someone else sees the same opportunity).
- **Exit**: A player leaving. Creates orphaned users who need a new solution.
- **Price change**: A competitor raising prices. Creates price-sensitive segment looking for alternatives.
- **Feature launch**: A competitor shipping something new. Changes what "table stakes" means.
- **Consolidation**: Players merging. Usually leads to price increases, feature cuts, and customer dissatisfaction.

**Common mistakes**:
- Treating a crowded market as a "no" signal. A crowded market with negative sentiment is actually a strong signal -- it means demand is proven but nobody is serving it well. An empty market might mean nobody wants what you are building.
- Ignoring adjacent competitors. Your competition is not just the products that do exactly what you plan to do. It is everything your potential customer might use instead, including doing nothing, using a spreadsheet, or hiring a freelancer.

**The lingo**: Strategists call this "competitive intelligence" or "CI." Product people talk about "competitive landscape" or "comp analysis." Marketers call it "market positioning" or "share of voice." Michael Porter's Five Forces framework -- threat of new entrants, bargaining power of suppliers, bargaining power of buyers, threat of substitutes, and competitive rivalry -- is the classic strategic framework for analyzing competitive dynamics.

### 7. AUDIENCE -- Your Distribution Advantage

**Definition**: Evidence of your ability to reach the people who would buy what you build. This is the most personal signal type because it depends on your existing relationships, following, reputation, and community presence. Two operators scanning the same domain will get different audience scores.

**Examples**:
- Your Twitter/X posts about a topic consistently get 3-5x the engagement of your other posts
- You receive DMs asking "Can you make a course on X?" more than once a month
- Your email list has a 45% open rate on newsletters about a specific subtopic
- You are a recognized contributor in a relevant subreddit or Discord community

**Where to find it**: Your own social media analytics, email list engagement data, DMs and direct requests, community reputation and karma, past content performance, speaking invitations, and organic inbound.

**Why audience is in the scoring matrix**: Arvid Kahl's core insight: distribution is the bottleneck, not product quality. A mediocre product with a strong distribution channel will outperform an excellent product with no distribution channel. If you have an audience that trusts you on a topic, the path to revenue is dramatically shorter. You do not need to prove credibility. You do not need to build awareness. You need to make something good and tell them about it.

**Special case -- no existing audience**: If you have no audience in the domain, AUDIENCE signals still matter. They just shift from "my audience wants this" to "the target audience is reachable." You scan for where the target audience gathers, how concentrated they are, how open those communities are to self-promotion, and what the cost of reaching them would be through paid channels.

**Common mistakes**:
- Building for a market you cannot reach. You might find a perfect PAIN + SPEND + COMPETITIVE signal configuration in enterprise healthcare compliance. But if you have no network in healthcare, no credentials, and no content footprint -- your audience score is a 1. The opportunity is real but not *for you*.
- Overvaluing vanity metrics. 100K Twitter followers who do not engage is a weaker audience signal than 2,000 email subscribers who open every email.

**The lingo**: Marketers call this "owned media" or "distribution channel" or "reach." Growth people call it "organic acquisition channel." Indie hackers call it "audience" or "community" or simply "distribution." VCs ask about "go-to-market motion" or "GTM advantage."

---

## The Lingo

If you have never worked in product, marketing, or sales, you will encounter terminology that sounds like it was designed to exclude outsiders. It was not. It evolved organically, and now it is just what people say. Here is the vocabulary you need, taught in the way people actually use these terms.

### Market Sizing

**TAM / SAM / SOM** -- Total Addressable Market / Serviceable Addressable Market / Serviceable Obtainable Market. TAM is the total revenue opportunity if you captured every possible customer on Earth. SAM is the portion you could realistically serve given your product, geography, and go-to-market. SOM is the portion you could realistically capture in the near term. VCs love these numbers. Operators should be skeptical. "The global cybersecurity market is $250 billion" (TAM) tells you absolutely nothing about whether 50 people will buy your $29 ebook. Use SPEND signals instead.

### Customer Definition

**ICP** -- Ideal Customer Profile. A specific description of the type of company or person who gets the most value from your product and is most likely to buy. Not "anyone who writes code" but "solo SaaS founders with $5K-50K MRR who manage their own infrastructure and do not have a dedicated DevOps hire." The tighter your ICP, the better your marketing, sales, and product decisions. When someone says "we need to narrow our ICP," they mean "we are trying to sell to everyone and therefore selling to no one."

### Product-Market Fit

**PMF** -- Product-Market Fit. The state where you have a product that a market genuinely wants. Sean Ellis's operational definition: if 40%+ of your users would be "very disappointed" if your product disappeared, you have PMF. Before PMF, nothing else matters -- not growth, not monetization, not hiring. After PMF, everything else becomes possible. The entire purpose of signal scanning is to increase the probability of finding PMF quickly by building for validated demand rather than guessing.

### Jobs to Be Done

**JTBD** -- Jobs to Be Done. The framework from Christensen and Moesta. Instead of asking "what features does our product need?" you ask "what job is the customer hiring this product to do?" A drill bit's job is not "being a drill bit." Its job is "making a hole." But actually, the job might be "hanging a family photo" or "assembling a bookshelf." When someone says "what's the job?" in a product meeting, they are asking about the underlying motivation and context, not the surface-level task.

### Voice of Customer

**VoC** -- Voice of Customer. The raw, unfiltered language customers use to describe their problems, desires, and experiences. VoC is the most valuable copywriting input in existence. When you use the exact words your customers use to describe their pain, your marketing converts dramatically better than when you use your own words. PAIN signals with direct quotes are VoC data. Marketers build entire campaigns around it.

### Willingness to Pay

**WTP** -- Willingness to Pay. What people will actually pay, not what you wish they would pay, not what the product is "worth," and not what a competitor charges. WTP is empirical. You discover it through SPEND signals (what do people already pay for similar things?), direct testing (price experiments, Van Westendorp surveys), and market behavior. WTP is context-dependent: people will pay $300 for a career certification but $0 for a blog post containing the same information.

### Lead Quality

**PQL** -- Product-Qualified Lead. A user who has experienced enough value in your product (usually through a free tier or trial) that they are likely to convert to a paying customer. Contrast with MQL (Marketing-Qualified Lead), which is someone who filled out a form. PQLs are a product-led growth concept: instead of sales deciding who is ready to buy, the product itself identifies ready buyers through their behavior. This matters for signal scanning because behavior signals (BEHAVIOR type) are the market-level equivalent of PQLs.

### Retention and Revenue

**NDR** -- Net Dollar Retention. The percentage of revenue retained from existing customers over a period, including expansion (upsells), contraction (downgrades), and churn (cancellations). NDR above 100% means you are growing even without new customers. NDR below 100% means you have a leaky bucket. When investors ask about NDR, they are asking: "Do customers love this enough to pay more over time?"

**CAC / LTV** -- Customer Acquisition Cost / Lifetime Value. CAC is how much it costs to acquire a customer (marketing spend + sales cost, divided by new customers). LTV is how much revenue a customer generates over their entire relationship with you. The fundamental unit economics equation: LTV must be significantly greater than CAC (typically 3x or more) or you will go bankrupt growing. Signal scanning addresses this indirectly: strong audience signals lower CAC (you already have distribution), and strong pain + spend signals increase LTV (customers stay because the problem is real and ongoing).

### Demand

**Demand sensing vs. demand generation**: Demand sensing is detecting demand that already exists (what signal scanning does). Demand generation is creating demand that did not exist before (what marketing campaigns do). The mistake most engineers make is trying to generate demand before sensing whether demand exists. Sense first, generate second.

**Signal stacking**: Layering multiple signal types on top of each other to increase confidence in an opportunity. A single PAIN signal is interesting. PAIN + SPEND is compelling. PAIN + SPEND + DEMAND + negative SENTIMENT + COMPETITIVE gap is a screaming opportunity. The more signal types that converge on the same opportunity, the higher the confidence.

**Buying intent**: Behavioral evidence that someone is moving toward a purchase decision. In B2B sales, this includes visiting pricing pages, downloading comparison guides, attending product demos, and engaging with bottom-of-funnel content. In signal scanning, buying intent shows up as DEMAND signals with commercial language ("best [X] tool," "alternative to [Y]," "[X] pricing").

### Competitive Intelligence

**Market sensing**: The ongoing practice of monitoring a market for shifts, threats, and opportunities. Signal scanning is a structured approach to market sensing. Competitive intelligence (CI) is the subset focused specifically on what competitors are doing.

**Win/loss analysis**: After every deal you win or lose, interviewing the buyer to understand why. What alternatives did they evaluate? What tipped the decision? What almost made them choose differently? Win/loss data is some of the highest-quality signal data available, but you can only collect it once you have a product and are making sales. Signal scanning is the pre-product substitute.

### Product and Marketing Strategy

**Feature-benefit matrix**: A grid mapping product features to customer benefits. Features are what the product does ("256-bit encryption"). Benefits are what the customer gets ("your data is safe from hackers"). People buy benefits. Engineers build features. The matrix forces translation between the two. In signal scanning, PAIN signals reveal benefits (pain relief), and ship candidates define features.

**Value proposition canvas**: Alexander Osterwalder's tool for aligning what you offer with what customers need. One side maps customer jobs, pains, and gains. The other side maps your products/services, pain relievers, and gain creators. The canvas visually shows whether you have fit between what you build and what customers need.

**Blue Ocean vs. Red Ocean**: From Kim and Mauborgne's *Blue Ocean Strategy*. A red ocean is a market with fierce competition, commoditized products, and margin pressure -- "bloody waters." A blue ocean is an uncontested market space you create by offering something categorically different. In signal scanning terms, a red ocean is high COMPETITIVE signal density with mixed or positive SENTIMENT (the market works well enough). A blue ocean is a COMPETITIVE gap with high PAIN and DEMAND but no adequate existing solution. Most real opportunities are somewhere in between -- not entirely uncontested, but differentiated enough to avoid direct competition.

**Category creation**: The most ambitious positioning strategy. Instead of competing in an existing category ("project management tool"), you create a new category ("team operating system"). Category creation requires significant marketing investment and is risky, but the payoff is enormous: the category creator typically captures the majority of the category's value. Play Bigger by Al Ramadan et al. is the canonical text. For solo operators and small teams, category creation is usually too expensive. Find an underserved position within an existing category instead.

**Positioning vs. messaging vs. copywriting**: Three distinct activities that people constantly conflate. Positioning is the strategic decision about what your product is and who it is for (April Dunford's domain). Messaging is the set of key points that communicate your positioning to the market -- the themes, the angles, the story. Copywriting is the specific words you put on a landing page, in an email, or in an ad. Positioning informs messaging, messaging informs copywriting. Most people jump straight to copywriting and wonder why nothing converts.

### The Funnel

**Top of funnel (TOFU) / middle of funnel (MOFU) / bottom of funnel (BOFU)**: The marketing and sales funnel describes the buyer's journey from "never heard of you" to "paying customer." Top of funnel is awareness: blog posts, social media, podcasts, SEO content. People are learning about a problem space. Middle of funnel is consideration: comparison guides, case studies, webinars, free trials. People are evaluating solutions. Bottom of funnel is decision: pricing pages, demos, sales conversations, purchase flows. People are ready to buy. Different signal types map to different funnel stages: PAIN and DEMAND signals are top/middle, SPEND and BEHAVIOR signals are middle/bottom, COMPETITIVE signals inform all stages.

### Offer Design

**Lead magnet**: A free resource offered in exchange for an email address. Serves as the entry point to a relationship. Common formats: checklists, templates, mini-courses, reports, calculators. A good lead magnet solves a specific, immediate problem for a tightly defined audience. A bad lead magnet is a generic PDF that nobody asked for. In signal scanning, PAIN signals directly generate lead magnet ideas.

**Tripwire offer**: A very low-priced product ($1-$19) designed not to generate profit but to convert a free subscriber into a paying customer. The psychology: once someone has entered their credit card for any amount, the friction for subsequent purchases drops dramatically. In the context of this skill, the ship candidate with the shortest ship time and lowest price point often serves as a tripwire.

**Anchor pricing**: Setting a high reference price so that other prices look reasonable by comparison. If you show a $299 option first, $99 looks like a deal. If you show a $29 option first, $99 looks expensive. Anchoring is not deception -- it is contextualization. Your SPEND data tells you what the current price anchors in a market are.

**Price discrimination**: Charging different prices to different customer segments based on their willingness to pay. Enterprise vs. individual pricing. Annual vs. monthly pricing. Purchasing power parity. A $49/mo tool that also offers a $499/year plan and a $199/mo enterprise tier is doing price discrimination. It is standard practice and usually good for both the business and the customer.

### Business Models

**Freemium vs. free trial**: Two different models that people constantly confuse. Freemium: the product is free forever at a limited tier, and you pay for more features or usage. Free trial: the full product is available for a limited time (7 days, 14 days, 30 days), after which you must pay. Freemium works when free users create value for the business (network effects, word of mouth, data). Free trial works when the product's value is obvious once you use it but hard to explain without using it.

### Acquisition

**Content marketing vs. direct response**: Two fundamentally different marketing philosophies. Content marketing creates valuable content that attracts an audience over time -- blog posts, videos, podcasts, newsletters. It is slow, compounding, and builds an owned audience. Direct response asks for an immediate action -- buy now, sign up now, click here. It is fast, measurable, and transactional. Most successful businesses use both: content marketing for top of funnel (building audience), direct response for bottom of funnel (converting to revenue).

**Organic vs. paid acquisition**: Organic acquisition means people find you without you paying for distribution -- through search engines, word of mouth, social media virality, or community presence. Paid acquisition means you buy traffic -- through ads on Google, Facebook, LinkedIn, or other platforms. Organic is cheaper per customer but slower and less predictable. Paid is immediate and scalable but requires budget and expertise. Your AUDIENCE signals indicate your organic acquisition potential. Weak audience signals usually mean you need a paid acquisition strategy or a community infiltration strategy.

---

## The Process

Here is how a professional runs a signal scan, step by step. This maps directly to the six-phase workflow this skill implements.

### Step 1: Define the Domain and Your Edge

Before you collect any data, you must define three things precisely.

**The domain**: What space are you scanning? "Cybersecurity" is too broad. "Cybersecurity certification prep for career-switching software engineers" is specific enough to scan. The domain should be narrow enough that you can identify specific communities, specific competitors, and specific pain points -- but broad enough that there are multiple possible products you could build within it.

**Your operator edge**: What makes you uniquely qualified to serve this domain? Technical skill is not an edge. Every engineer has technical skill. An edge is specific credibility, specific experience, or a specific audience relationship. "I spent 5 years as a DevOps lead at a mid-stage startup and have 4,000 Twitter followers who are DevOps engineers" is an edge. "I can code" is not.

**Your constraints**: How fast do you need to ship? What formats are you willing to create? What price range feels right? What distribution channels do you have access to? These constraints shape which opportunities are viable *for you*. A perfect opportunity that requires 6 months of development is not viable for someone who needs revenue in 30 days.

**What beginners get wrong**: They skip this step entirely and start collecting random data. Or they define the domain too broadly ("AI tools") and drown in noise. Or they lie to themselves about their edge ("I am passionate about this" is not an edge).

**What experts do differently**: They spend serious time on the edge assessment. They are honest about what they can and cannot reach. They constrain aggressively -- a tightly scoped scan with a clear edge beats a broad scan every time.

### Step 2: Identify Signal Sources

Now you decide *where* to look. This is not random browsing. You are building a source list.

For any given domain, you want sources across at least three categories:

1. **Community sources**: Where do the people in this domain gather? Which subreddits, Discord servers, Slack groups, forums, and mailing lists? These are your PAIN, DEMAND, and AUDIENCE signal sources.

2. **Commercial sources**: Where do people in this domain spend money? Which course platforms, marketplaces, tool categories, and service providers serve them? These are your SPEND and COMPETITIVE signal sources.

3. **Behavioral sources**: Where can you observe what people in this domain actually *do*? Stack Overflow, GitHub, automation platforms, job boards? These are your BEHAVIOR signal sources.

4. **Sentiment sources**: Where do people leave reviews or express opinions about existing solutions? G2, Capterra, TrustPilot, app store reviews, social media? These are your SENTIMENT signal sources.

**What beginners get wrong**: They search Google, read two blog posts, and declare the research done. They miss community sources entirely because they are not embedded in the domain.

**What experts do differently**: They spend time *finding* communities before reading them. They search Reddit for subreddit discovery. They search Twitter for relevant hashtags and influencers. They check SparkToro to see where an audience actually spends time. The source identification step is often where the most valuable insight happens, because the community you did not know existed is often the community with the strongest signals.

### Step 3: Collect Raw Signals

This is the most time-intensive phase. You are reading, searching, and extracting evidence.

**Rules of evidence**:
- Every signal must have a source. "People generally feel..." is not evidence. "u/devops_mike on r/devops wrote 'I spent 3 hours trying to...' (47 upvotes)" is evidence.
- Collect direct quotes when possible. The exact words people use are valuable -- not just as evidence, but as copywriting material later.
- Note recency. A complaint thread from 2019 is much less actionable than one from last month. Markets change. Pain moves.
- Collect across types. Do not just collect PAIN signals because they are the most emotionally engaging. Force yourself to look for all 7 types, even when some are harder to find. Gaps in your signal collection are themselves informative.

**Target**: 3-5 raw signals per type, minimum. If a type has fewer, note why.

**What beginners get wrong**: They collect opinions instead of evidence. They read a thread, form an impression, and write "many people are frustrated with X." That is an interpretation, not a signal. Go back and find the specific posts, the specific quotes, the specific numbers.

**What experts do differently**: They look for *convergence*. When three different communities, on three different platforms, independently express the same pain in the same language, that is a much stronger signal than one viral post. Experts also pay attention to what is *not* being said -- the problems nobody is complaining about might be the ones everybody has accepted, which is its own kind of opportunity.

### Step 4: Normalize Signals

Raw signals are messy. Different sources, different formats, different levels of detail. Normalization puts them into a consistent structure so you can compare and score.

Each signal type has a defined schema (see the signal taxonomy reference). You tag each signal with its type, assign calibrated scores or classifications (intensity, volume, valence, effort level, etc.), and ensure every required field is populated.

**Scoring discipline**: Every numerical score must be justified by evidence. "Intensity: 8" is meaningless. "Intensity: 8 -- three separate Reddit threads with 100+ upvotes describe spending 4+ hours on this task, with emotional language ('nightmare', 'insane', 'pulling my hair out')" is a calibrated judgment.

**What beginners get wrong**: They assign scores based on vibes instead of evidence. They give every pain signal an 8 because "it seems bad." Calibration matters. If everything is an 8, nothing is an 8.

**What experts do differently**: They use the calibration guides explicitly. They compare signals to each other: "Is this pain really as intense as that pain? The first one has 200 upvotes and emotional language; the second has 30 upvotes and clinical language. The first is a 7, the second is a 4." Relative calibration within a scan is more important than absolute accuracy.

### Step 5: Score Opportunities

Individual signals are ingredients. Opportunities are recipes. In this step, you cluster related signals into opportunity areas and score each opportunity using six weighted dimensions.

The scoring formula: `(pain_intensity * 2 + spend_evidence * 2 + edge_match + time_to_ship + competition_gap + audience_fit) / 8`

Pain and spend are double-weighted because they are the strongest predictors of viable products. A high-pain problem that people already pay to solve is the closest thing to a guaranteed opportunity. Edge, speed, gap, and audience are all important, but they are modifiers on the core signal of "painful problem with proven willingness to pay."

**What beginners get wrong**: They fall in love with the highest-scored opportunity without examining why it scored high. If an opportunity scores 8 because of sky-high pain but a 2 on audience fit, it is a great opportunity *for someone else*. Read the breakdown, not just the total.

**What experts do differently**: They look for opportunities where multiple dimensions are strong, not just one. An opportunity that scores 6 across the board is often more viable than one that scores 9 on pain but 2 on everything else. Consistency across dimensions means fewer things can go wrong.

### Step 6: Generate Offers and Validate

For every opportunity scoring 6 or above, you generate concrete ship candidates -- specific products with specific formats, prices, distribution channels, and timelines.

**The discipline of concreteness**: Not "create a course" but "create a 90-minute video course called 'Terraform State Management for Teams' sold on Gumroad for $49, distributed through a value-first thread in r/devops and a Twitter thread demonstrating the problem." Concreteness is what separates analysis from action.

**Validation before building**: Before you build the winning ship candidate, test the demand with lightweight methods. Options include:
- A landing page with an email capture ("Join the waitlist")
- A value-first social media post that teaches the core insight and gauges response
- A pre-sale announcement ("I am building X. It will cost $Y. Pay now and get it when it ships.")
- A DM conversation with 5-10 people in your target ICP

Vassallo's philosophy applies here: the validation test itself should be a small bet. Spend a weekend, not a quarter.

**What beginners get wrong**: They skip validation entirely and start building. Or they validate with friends and family, who will tell them everything is a great idea. Validate with strangers in the target community. If strangers give you money or their email address, the signal is real.

**What experts do differently**: They validate the riskiest assumption first. If the riskiest assumption is "will people pay?" they pre-sell. If it is "can I reach these people?" they test distribution. If it is "can I build this?" they prototype. The validation test should target the single biggest unknown.

---

## Tools of the Trade

These are the specific tools that product people, marketers, and indie hackers use for signal detection. You do not need all of them. Start with the free ones and add paid tools as your process matures.

### Research and Discovery

**Google Trends** (free) -- The most underused tool in signal detection. Most people type in a keyword and glance at the line chart. That is 10% of the value. The real value is in (1) "Related queries" (especially "Breakout" queries, which show explosive growth), (2) comparison mode (compare up to 5 terms to see relative interest), (3) geographic filtering (different regions have different pain), and (4) category filtering (separates "python" the language from "python" the snake). Pro tip: a term showing "Breakout" in Related Queries has seen growth of 5000%+ in the selected period. Those are your exploding DEMAND signals.

**SEMrush / Ahrefs** (paid, $99+/mo) -- Keyword research and competitive analysis tools. They show you search volume (how many people search for a term monthly), keyword difficulty (how hard it is to rank for that term), and the competitive landscape for any topic. Use them to quantify DEMAND signals (search volume = people actively looking for solutions) and to discover COMPETITIVE signals (who ranks for these terms, how much traffic they get, what pages they create). Ahrefs' Content Explorer feature lets you find the most shared and linked content on any topic -- useful for understanding what resonates.

**SparkToro** (free tier available, paid $50+/mo) -- Audience research tool created by Rand Fishkin. Enter a topic or a Twitter handle and SparkToro tells you where that audience spends time: which websites they visit, which podcasts they listen to, which YouTube channels they watch, which social accounts they follow. This is your AUDIENCE signal discovery tool. Instead of guessing where to distribute, SparkToro tells you where your target audience already gathers.

### Community Mining

**Reddit** -- The single richest source of PAIN signals on the internet. Effective Reddit search is a skill unto itself. Tips: (1) use site:reddit.com in Google instead of Reddit's native search, which is poor. (2) Search for specific phrases: "I wish," "frustrated with," "switching from," "alternative to," "anyone else." (3) Sort by top of all time to find the highest-signal threads. (4) Check the sidebar of relevant subreddits for related subreddits you did not know about. (5) Read the comments, not just the posts -- the most specific pain language is often three levels deep in a comment thread.

**Hacker News** (free) -- Use hn.algolia.com for search. HN's audience is technical and opinionated, which makes it a strong source for SENTIMENT signals (what do engineers think of existing tools?) and BEHAVIOR signals (what workarounds do they build?). The "Ask HN" threads are particularly rich.

**Discord / Slack communities** -- Many domains have active Discord or Slack communities. These are harder to search but often have the most candid conversations because they feel private. Join the relevant communities and read before you search. Watch for channel topics, pinned messages, and recurring questions.

### Commercial Intelligence

**G2 / Capterra / TrustPilot** -- Review mining platforms. Filter reviews by rating (1-2 star reviews are PAIN and SENTIMENT gold), by date (recent reviews reflect current reality), and by company size (different segments have different pain). Read the actual reviews, not just the star ratings. The specific language people use in negative reviews is your competitive positioning ammunition and your copywriting raw material.

**Gumroad / Lemon Squeezy** -- Browse by category to find what digital products people actually buy in your domain. Creator profiles sometimes show revenue data. Trending pages show what is selling right now. This is your SPEND signal source for digital products.

**Udemy / Skillshare / Coursera** -- Browse bestsellers in your domain's category. Student count, rating count, and star rating together tell you: (1) that people will pay to learn this topic, (2) how much they will pay, (3) how satisfied they are with existing options. A course with 50,000 students and a 3.8-star rating is a strong signal: demand is proven but satisfaction is only moderate.

**AppSumo** -- Lifetime deal marketplace. Review counts and ratings tell you about willingness to pay for tools in a space. AppSumo deals also reveal what category of product people are excited about. High review counts on an AppSumo deal mean strong demand for a new entrant in that category.

### Traffic and Technology Analysis

**SimilarWeb** (free tier available) -- Estimates website traffic volumes, traffic sources, and audience overlap. Use it to size up competitors: how much traffic do they get? Where does it come from? What are their top-performing pages? Useful for COMPETITIVE signals.

**BuiltWith** (free tier available) -- Detects what technologies a website uses. Useful for understanding the technical landscape: what stacks are popular? What tools have significant adoption? If you are building a tool that integrates with another tool, BuiltWith tells you how large the installed base is.

### Social Listening

**Brand24 / Mention** (paid) -- Monitor mentions of specific keywords, brands, or topics across social media, news, blogs, and forums in real time. Useful for ongoing market sensing once you have identified a domain. Less useful for initial scanning, more useful for staying current after you have launched.

### Survey and Interview

**Typeform / Google Forms** -- For running your own JTBD interviews or PMF surveys. The Sean Ellis PMF survey question ("How would you feel if you could no longer use this product?") requires only a single-question form. JTBD interviews follow a specific structure: "Tell me about the last time you [tried to solve this problem]. Walk me through what happened." Google Forms is free and sufficient. Typeform is prettier and has better conditional logic.

---

## Case Studies

### How Superhuman Used Sean Ellis's PMF Survey to Find Their Market

Superhuman, the premium email client, was not finding product-market fit with their initial broad audience. CEO Rahul Vohra read Sean Ellis's blog post about the 40% benchmark and built the PMF survey into Superhuman's onboarding flow. He asked every user: "How would you feel if you could no longer use Superhuman?"

The initial result was below 40%. But Vohra did something clever: he segmented the responses. He found that one specific user segment -- founders and executives who received 100+ emails per day and valued speed above all else -- was at 60%+ "very disappointed." The broader audience was diluting the signal.

This is signal detection in its purest form. The signal was not "people want a better email client." The signal was "a specific type of person with a specific usage pattern finds extreme value in speed." Superhuman repositioned around that segment, doubled down on keyboard shortcuts and speed, and charged $30/month in a market where every competitor was free.

The lesson: PMF is not a product-wide metric. It is a segment-specific metric. Signal scanning should always look for the segment where signals are strongest, not the broadest possible audience.

### How Daniel Vassallo Spotted the Signal for "Everyone Can Build a Twitter Audience"

Daniel Vassallo left a $500K/year job at AWS in 2019 to make small bets. He started tweeting about his journey and noticed something in his replies and DMs: people kept asking him how he was growing his Twitter following. Not about AWS. Not about software architecture. About Twitter.

He was receiving AUDIENCE signals (direct requests), PAIN signals (people struggling to grow on Twitter), and DEMAND signals (questions appearing in his mentions weekly). He had an operator edge: he had grown his own following from zero to tens of thousands while documenting the process publicly.

He shipped a $30 guide -- "Everyone Can Build a Twitter Audience" -- in a few days. It has generated hundreds of thousands of dollars in revenue. The key insight: the strongest signal was not in a Google Trends chart or a competitor analysis. It was in his own DMs. AUDIENCE signals from people who already trust you are the highest-conversion signal type.

The lesson: If people are literally telling you what they want to buy from you, and you have credibility on the topic, the signal does not get louder than that. Ship it.

### How the Notion Template Market Became a $50M+ Economy

Nobody at Notion planned this. The Notion template economy emerged from BEHAVIOR signals: users were building elaborate templates for personal productivity, project management, and content planning, then sharing them in forums and on Twitter. Some users started selling templates on Gumroad. Early sellers like Thomas Frank, Easlo, and Marie Poulin spotted the signal and productized it.

The signal stack was textbook:
- **PAIN**: People wanted to use Notion but found building systems from scratch overwhelming.
- **BEHAVIOR**: Power users were building templates and sharing them (extreme effort level -- some templates took weeks to build).
- **DEMAND**: "Notion template for [X]" search queries were exploding on Google Trends.
- **SPEND**: Early Gumroad listings were generating significant revenue, proving WTP.
- **COMPETITIVE**: No one was doing this systematically. Notion's own template gallery was sparse.
- **SENTIMENT**: Mixed -- people loved Notion but felt lost without structure.

The entrepreneurs who profited were not the earliest Notion adopters. They were the ones who saw the behavior signals (people building and sharing templates) and recognized them as productization opportunities before the market matured. By the time Notion launched its own marketplace, independent template creators had already built a multi-million-dollar economy.

The lesson: Watch what people build for themselves. When people invest significant effort creating personal tools, templates, or workflows, they are performing market research for you. The product is "the thing they built, but polished and packaged."

---

## The Framework This Skill Implements

This skill implements a framework called **Signal-Scored Opportunity Discovery (SSOD)**. It is a synthesis, not a copy of any single existing framework. Here is what it draws from and where it diverges.

### Intellectual Lineage

**From Ulwick's Outcome-Driven Innovation**: The scoring matrix is a direct descendant of Ulwick's Opportunity Algorithm (`Importance + max(Importance - Satisfaction, 0)`). The SSOD formula double-weights pain and spend for the same reason Ulwick double-weights importance: the severity of the need is the strongest predictor of willingness to adopt and pay. However, SSOD replaces Ulwick's survey-based measurement with observational signal collection, making it usable before you have customers to survey.

**From Torres's Opportunity Solution Tree**: The overall structure -- starting with a domain, branching into opportunities, generating solutions for each opportunity -- mirrors the OST. But where Torres's OST requires ongoing customer interviews (which requires having customers), SSOD works from public signal data. It is designed for the pre-customer phase.

**From Christensen and Moesta's JTBD**: The signal types map to the Forces of Progress. PAIN signals = push of the current situation. DEMAND signals = pull toward a new solution. SENTIMENT signals = anxiety and habit forces around existing solutions. COMPETITIVE signals = the landscape of current solutions being "hired" for the job. The SSOD framework operationalizes JTBD theory as a signal collection practice rather than an interview methodology.

**From Kahl's Embedded Entrepreneur**: The AUDIENCE signal type and the operator edge concept. Kahl's core argument -- that distribution matters as much as product quality -- is embedded in the scoring matrix. SSOD does not just ask "is this a good opportunity?" It asks "is this a good opportunity *for this specific operator with this specific audience*?"

**From Vassallo's Small Bets**: The requirement that ship candidates include at least one option shippable in 1-3 days. The philosophy that validation comes from shipping, not from analysis. The portfolio mindset: generate multiple candidates and let the market reveal the winner.

**From Walling's Stair Step Method**: The range of ship candidate formats (from PDF to SaaS) and the explicit recognition that the right *first* product is often not the product you ultimately want to build. It is the smallest viable product that validates demand, builds audience, and generates revenue to fund the next step.

### Where SSOD Diverges

**From traditional market research**: Traditional market research relies heavily on surveys, focus groups, and TAM analysis. SSOD treats these as low-signal inputs and prefers behavioral evidence: what people do (BEHAVIOR), what they pay (SPEND), what they build for themselves (BEHAVIOR), and what they say in unstructured environments where they are not being asked a research question (PAIN, DEMAND, SENTIMENT on Reddit and forums). The philosophy is that revealed behavior in natural contexts is more reliable than stated preferences in research contexts.

**From lean startup "build-measure-learn"**: Lean startup says build an MVP and measure response. SSOD adds a pre-build phase: scan for signals, score opportunities, *then* build the MVP. The argument is that the MVP itself should be informed by signal data, not randomly generated. You should not build-measure-learn from a random starting point. You should build-measure-learn from the most promising starting point that signal data can identify.

**From competitor-focused strategy**: Porter's Five Forces and other competitive strategy frameworks center the analysis on competitive dynamics. SSOD treats competitive signals as one of seven types -- important but not dominant. The SSOD framework centers on customer pain and willingness to pay, using competitive dynamics as context rather than foundation. The reasoning: for solo operators and small teams, competitive positioning matters less than finding genuine pain with proven spend. You do not need to "win" a market. You need to serve a segment that existing players are neglecting.

### The SSOD Lifecycle

```
1. DEFINE    ->  Domain + Edge + Constraints
2. COLLECT   ->  7 signal types from real sources with real evidence
3. NORMALIZE ->  Structured format with calibrated scores
4. SCORE     ->  Weighted opportunity matrix: (P*2 + S*2 + E + T + G + A) / 8
5. GENERATE  ->  Concrete ship candidates per opportunity
6. SYNTHESIZE -> Meta-signal: the structural thesis
7. VALIDATE  ->  Lightweight test of the top candidate
```

This is the process this skill automates. It is designed to be repeatable: you can run it against different domains, compare scores, and make portfolio-level decisions about where to invest your time.

The output is not a business plan. It is not a strategy document. It is a structured scan with scored opportunities and concrete next steps. The entire purpose is to reduce the time between "I wonder what to build" and "I am building this specific thing for this specific reason."

---

## Final Note

The discipline described in this document is not optional for people who want to build products that generate revenue. Engineers tend to treat market analysis as soft, subjective, or beneath them. It is none of those things. It is the empirical practice of gathering evidence about what the world needs before committing engineering time.

You would not ship code without testing it. Do not ship products without testing the market.

The thinkers listed here -- Torres, Cagan, Dunford, Christensen, Moesta, Ulwick, Ellis, Kahl, Vassallo, Walling -- have collectively spent decades codifying the practices that separate products that succeed from products that fail. This skill synthesizes their work into a repeatable process. Use it before you build. Use it honestly. And when the signals tell you that your idea is not as strong as you thought, listen to them. The market does not care about your feelings. It rewards people who listen.
