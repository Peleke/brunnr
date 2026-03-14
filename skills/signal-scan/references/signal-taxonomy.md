# Signal Taxonomy

The 7 canonical input types for product signal scanning. Every raw signal collected during a scan maps to exactly one of these types.

Load this file at the start of every scan to ensure consistent categorization and normalization.

---

## 1. PAIN

What people complain about, struggle with, or spend disproportionate time on.

**Where to find it:**
- Reddit threads (sort by top/controversial for strong opinions)
- Forum posts and community discussions
- Support tickets and help desk data
- Review complaints (1-2 star reviews on competing products)
- Social media rants and complaint threads

**What to capture:**
| Field | Type | Description |
|-------|------|-------------|
| signal | string | Description of the pain point |
| intensity | number (1-10) | How severe the pain is, justified by evidence |
| source | string | Specific platform, subreddit, URL |
| evidence | string | Actual quote, data point, or concrete observation |
| recurrence | enum | isolated, occasional, frequent, pervasive |

**Intensity calibration:**
- 1-3: Minor annoyance, people mention it but move on
- 4-6: Real friction, people spend time complaining or working around it
- 7-8: Significant pain, emotional language, multiple threads, people actively seeking alternatives
- 9-10: Dealbreaker-level pain, people abandon workflows, switch tools, or hire someone to solve it

**Recurrence guide:**
- **isolated**: Seen once or twice, could be an edge case
- **occasional**: Appears in a few threads/sources, some pattern emerging
- **frequent**: Multiple threads across different communities, clear pattern
- **pervasive**: Everywhere you look, almost universal complaint in the domain

**Evidence quality bar:**
Good: "u/sre_engineer on r/devops: 'I've spent the last 3 weekends trying to get Terraform state management right. I'm about to just use ClickOps.' (127 upvotes, 43 comments)"
Bad: "Many DevOps engineers find Terraform state management challenging."

---

## 2. DEMAND

Evidence that people are actively seeking a solution.

**Where to find it:**
- Google Trends data and search volume
- "I wish...", "Does anyone know...", "Looking for..." posts
- Waitlist signups for upcoming products
- Pre-sales or crowdfunding campaigns
- Feature requests on competitor products

**What to capture:**
| Field | Type | Description |
|-------|------|-------------|
| signal | string | Description of the demand signal |
| volume | enum | low, moderate, high, extreme |
| source | string | Specific platform, subreddit, URL |
| evidence | string | Actual quote, data point, or concrete observation |
| trend | enum | declining, stable, growing, exploding |

**Volume calibration:**
- **low**: Niche interest, a few people asking
- **moderate**: Regular questions, noticeable search volume
- **high**: Many people asking, trending topics, significant search volume
- **extreme**: Viral demand, waitlists filling, search volume spiking

**Trend guide:**
- **declining**: Search volume or mentions dropping over 6+ months
- **stable**: Consistent interest, no significant change
- **growing**: Upward trajectory over past 6-12 months
- **exploding**: Sharp recent spike, often tied to a market event or technology shift

---

## 3. SPEND

What people actually pay for right now. The most important signal for validating willingness-to-pay.

**Where to find it:**
- Udemy / Skillshare / Coursera bestseller lists and student counts
- Gumroad trending products and revenue data
- AppSumo deals and review counts
- Competitor pricing pages
- Job postings (companies spending on hiring = budget exists)
- Conference ticket prices and attendance

**What to capture:**
| Field | Type | Description |
|-------|------|-------------|
| signal | string | What people are paying for |
| price_range | string | Observed price range, e.g. "$10-25" |
| volume_evidence | string | Student counts, revenue data, bestseller status |
| source | string | Specific platform, URL |
| platform | enum | Udemy, Gumroad, Skillshare, AppSumo, direct, other |

**What counts as volume evidence:**
- "47,000 students enrolled" (Udemy)
- "Bestseller badge, 4.6 stars, 2,300 ratings" (Udemy)
- "$12K+ revenue shown on creator profile" (Gumroad)
- "847 reviews on AppSumo" (AppSumo)
- "Pricing page shows $49/mo, $99/mo, $249/mo tiers" (competitor)

**What does NOT count:**
- "Probably makes good money" (speculation)
- "The market is worth $X billion" (TAM numbers are useless for product validation)

---

## 4. BEHAVIOR

What people do (not what they say) -- workarounds, tool-switching, hiring patterns, and duct-tape solutions.

**Where to find it:**
- Stack Overflow workaround answers (high-vote hacky solutions)
- Zapier / Make / automation communities (what people automate = what is painful to do manually)
- Job postings (what companies hire for = what they cannot solve with existing tools)
- GitHub repos (what people build themselves)
- "I built a script that..." posts

**What to capture:**
| Field | Type | Description |
|-------|------|-------------|
| signal | string | Description of the behavior |
| source | string | Specific platform, URL |
| evidence | string | Actual quote, data point, or concrete observation |
| effort_level | enum | low, moderate, high, extreme |

**Effort level calibration:**
- **low**: Quick workaround, takes minutes
- **moderate**: Notable effort, takes hours, involves multiple steps
- **high**: Significant investment, custom scripts, multi-day projects
- **extreme**: People hire contractors, build internal tools, or dedicate entire roles to the problem

**Why behavior signals matter:**
People lie about what they want. They do not lie about what they do. A Stack Overflow answer with 500 upvotes showing a hacky workaround is stronger evidence than a survey saying "I would pay for X."

---

## 5. SENTIMENT

How people feel about existing solutions -- satisfaction, frustration, trust, and switching intent.

**Where to find it:**
- Review sites (G2, Capterra, TrustPilot, app store reviews)
- NPS data (if accessible)
- Social media sentiment around specific tools or brands
- Forum tone when discussing existing solutions
- "I switched from X to Y because..." posts

**What to capture:**
| Field | Type | Description |
|-------|------|-------------|
| signal | string | How people feel about existing solutions |
| valence | enum | positive, mixed, negative, hostile |
| source | string | Specific platform, URL |
| evidence | string | Actual quote, data point, or concrete observation |

**Valence guide:**
- **positive**: Generally satisfied, minor complaints at most
- **mixed**: Split opinions, significant praise AND significant complaints
- **negative**: Majority dissatisfied, common complaints, low review scores
- **hostile**: Active anger, public callouts, organized complaints, boycott energy

**What makes sentiment actionable:**
- Negative sentiment + high spend = people pay despite hating the solution (huge opportunity)
- Hostile sentiment + no alternatives = captive market desperate for an option
- Mixed sentiment = room for a differentiated entrant
- Positive sentiment = hard to compete, look elsewhere

---

## 6. COMPETITIVE

What the market landscape is doing -- gaps, moves, collapses, and strategic shifts.

**Where to find it:**
- Competitor product launches and feature announcements
- Funding rounds and acquisitions
- Product shutdowns and pivots
- Pricing changes (especially price increases)
- Feature gap analysis (what competitors do NOT offer)
- Market consolidation patterns

**What to capture:**
| Field | Type | Description |
|-------|------|-------------|
| signal | string | Description of the competitive signal |
| type | enum | gap, new_entrant, exit, price_change, feature_launch, consolidation |
| source | string | Specific platform, URL |
| impact | enum | low, moderate, high, critical |

**Type definitions:**
- **gap**: Something the market needs that no competitor provides well
- **new_entrant**: A new player entering the space (could be threat or validation)
- **exit**: A competitor shutting down, pivoting away, or being acquired
- **price_change**: A competitor raising or lowering prices significantly
- **feature_launch**: A competitor shipping something new that changes dynamics
- **consolidation**: Multiple players merging, reducing competition

**Impact calibration:**
- **low**: Minor shift, does not change the opportunity landscape
- **moderate**: Noticeable change, worth factoring into strategy
- **high**: Significant shift, directly creates or closes an opportunity
- **critical**: Market-defining event, must respond or capitalize immediately

---

## 7. AUDIENCE

Your relationship with people who trust you -- the distribution advantage.

**Where to find it:**
- DMs and replies (what people ask you about)
- Email list engagement (open rates, click rates by topic)
- Social media engagement patterns (what gets reactions)
- Direct requests ("Can you make a course on X?")
- Community membership and participation data

**What to capture:**
| Field | Type | Description |
|-------|------|-------------|
| signal | string | Description of the audience signal |
| source | string | Specific platform, channel |
| evidence | string | Actual data point, quote, or observation |
| strength | enum | weak, moderate, strong |

**Strength calibration:**
- **weak**: Occasional interest, low engagement on the topic
- **moderate**: Regular engagement, some direct requests, topic resonates
- **strong**: Repeated direct requests, high engagement, audience actively asks for this

**Why audience matters for scoring:**
A mediocre opportunity with a strong audience signal often beats a great opportunity with no audience signal. Distribution is the bottleneck for most products. If people already trust you on a topic, the path to revenue is shorter.

**Special case -- no existing audience:**
If the operator has no existing audience in the domain, note this explicitly. Audience signals still matter (they just come from analyzing where the target audience already gathers, not from the operator's own following). Score audience_fit based on how reachable the audience is, not just whether the operator already has one.

---

## Cross-Signal Patterns

The most valuable insights come from signals that reinforce each other across types:

| Pattern | What It Means | Opportunity Strength |
|---------|--------------|---------------------|
| High PAIN + High SPEND + Negative SENTIMENT | People pay for bad solutions because nothing better exists | Very strong |
| High DEMAND + Low SPEND | People want it but have not found a way to pay for it yet | Strong (pricing innovation needed) |
| High BEHAVIOR + Low COMPETITIVE | People build their own because nothing exists | Strong (productize the workaround) |
| High PAIN + No SPEND | People suffer but will not pay -- dangerous | Weak (free/freemium or avoid) |
| High AUDIENCE + Moderate PAIN | Your audience has a problem only you have noticed | Strong (trust advantage) |
| COMPETITIVE exit + High DEMAND | A player left and demand remains | Very strong (timing-dependent) |
