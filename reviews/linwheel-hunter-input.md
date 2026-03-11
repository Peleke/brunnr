# LinWheel — Hunter Pipeline Input Brief

**Date**: 2026-03-09
**Product**: LinWheel (linwheel.io)
**Pipeline Run Type**: Signal Scan + Decision Log
**Focus**: LinkedIn content automation for technical creators who hate LinkedIn

---

## 1. Product Summary

LinWheel is a content transformation engine. It ingests arbitrary work artifacts — articles, buildlog entries, specs, PR histories, meeting notes — and produces LinkedIn-optimized posts across 7 psychological angles:

1. Contrarian
2. Field Note
3. Demystification
4. Identity Validation
5. Provocateur
6. Synthesizer
7. Curious Cat

Additional capabilities: AI cover images, carousels, voice profiles (sounds like the user, not like AI), brand styles, direct LinkedIn publishing (including articles — not available in LinkedIn's public API), and org-level publishing for teams/brands.

**Architecture**: MCP server with 15 tools. Agent-native by design — the agent is the primary user; the dashboard exists for human review.

---

## 2. Problem Statement

LinkedIn is a cesspool. But if you're building something people need to know about, you have to be there.

The core pain: **stopping your actual work to go perform for an algorithm that rewards charlatans.** You built something worth talking about — now you have to stop building it to impress people you don't respect, hoping the right person notices someday.

LinWheel is an indignity removal tool. Your work becomes your content automatically. The cesspool gets fed; you don't have to swim in it.

---

## 3. ICP Hypotheses (Validate)

### ICP-1: Technically-Inclined Solopreneurs

- Already sitting on a bulk of convertible work: code, PRs, buildlogs, specs, design docs
- Lean neurodivergent — the LinkedIn performance requirement is disproportionately painful
- For those who say "I don't have content": coding agent + gh CLI + LinWheel = done. Or buildlog captures it automatically.
- **Key signal to find**: Developers/founders expressing frustration at LinkedIn content requirements despite having deep technical work to show

### ICP-2: Technical Course Creators Switching from Competitors

- Especially Taplio users — investigate Taplio's reputation and churn signals
- Also artistically-leaning course creators who hate LinkedIn for different (aesthetic/authenticity) reasons
- **Key signal to find**: Taplio complaints, competitor dissatisfaction threads, "looking for alternative" posts

### ICP-3: Justin Welsh Course Graduates

- Buyers of linkedin-operating-system who learned the strategy but struggle with execution
- LinWheel automates the execution layer; borrowed authority from a proven methodology
- **Key signal to find**: Welsh course graduates asking about automation, execution fatigue, "I know what to post but can't make myself do it" signals

---

## 4. Pricing Hypothesis (Validate)

| Tier | Price | Access |
|------|-------|--------|
| Creator | $89/mo | Full transformation engine, voice profiles, direct publishing |
| Team | $179/mo | + MCP server access, org publishing, brand styles |

**Current price**: $29/mo (hypothesis: too low, undercuts perceived value)

**Value math**: 2 hrs/week saved at $50-100/hr = $400-800/mo value. $89-179 captures 11-45% of value created. ROI: 2-4.5x.

**Hunter should validate**:
- What do people actually pay for LinkedIn automation tools?
- Competitor pricing across the $29-179 range
- Willingness to pay among each ICP segment
- Whether MCP access / agent-native warrants a tier premium

---

## 5. Differentiation Claims (Stress Test)

| Claim | Evidence Needed |
|-------|----------------|
| 7-angle content decomposition (not "rewrite for LinkedIn") | Is multi-angle a real differentiator or a feature nobody asked for? |
| Voice profiles that sound like the user | Do competitors claim this too? What's Taplio's voice story? |
| Direct LinkedIn publishing including articles | Verify: does any competitor offer article publishing via API? |
| MCP server / agent-native architecture | Is "agent-native" a differentiator today or a premature bet? |
| Org publishing | What's the team/brand market look like for LinkedIn tools? |

---

## 6. Competitive Landscape (Investigate)

### Primary Competitors to Scan

- **Taplio** — Market leader? Reputation? Pricing? Churn signals?
- **Shield** — Analytics play, different angle?
- **AuthoredUp** — Formatting/preview tool
- **Publer / Buffer / Hootsuite** — Generic social schedulers with LinkedIn support
- **Jasper / Copy.ai** — AI writing tools with LinkedIn templates

### Specific Intel Needed

- Taplio pricing tiers and feature gaps
- Taplio complaint threads (Reddit, Twitter/X, Indie Hackers, Product Hunt reviews)
- Any competitor offering MCP / agent-native integration
- Any competitor offering direct article publishing (not just posts)
- Justin Welsh ecosystem: does he recommend/partner with any tool?

---

## 7. Hunter Investigation Scope

### 7a. Signal Scan

- LinkedIn content automation pain signals across Reddit, Twitter/X, Indie Hackers, Hacker News
- Taplio-specific complaints and switching signals
- Neurodivergent creator pain around LinkedIn specifically
- Competitor pricing data ($29-179 range)
- "I hate LinkedIn but I need LinkedIn" sentiment threads
- Justin Welsh course community discussions about tooling

### 7b. Decision Log

Score LinWheel against Hunter's 6 dimensions:

1. **Pain Intensity** — How acute is the "stop building to perform" problem?
2. **Spend Evidence** — Are people already paying for LinkedIn automation? How much?
3. **Edge Match** — Does the builder's stack (MCP, agent architecture, NLP background) create a defensible moat?
4. **Time to Ship** — Product exists and is functional. What's the gap to market-ready?
5. **Competition Gap** — Where do existing tools fail that LinWheel fills?
6. **Audience Fit** — Does the builder have credible access to the target ICPs?

### 7c. Persona Extract

Validate the 3 ICPs above with real community signals. Look for:
- Actual quotes expressing the pain
- Community size estimates
- Willingness-to-pay indicators
- Where they congregate (subreddits, Discords, Slack communities, Twitter circles)

### 7d. SWOT Stress Test

Full SWOT with external evidence. Pay special attention to:
- **Threat**: LinkedIn API changes / rate limiting / ToS enforcement
- **Threat**: Taplio or incumbent adding AI features
- **Weakness**: "Agent-native" as premature positioning if market isn't there yet
- **Opportunity**: Justin Welsh ecosystem as distribution channel
- **Opportunity**: Neurodivergent creator community as underserved niche

### 7e. Offer Scope

- Validate pricing tiers ($89 / $179)
- Lead magnet concept: cheatsheet SVG (7 angles breakdown, "turn your GitHub into LinkedIn content" visual)
- Email sequence angles for each ICP
- Launch channel strategy (where to announce, who to seed with)

---

## 8. Campaign Context: ACE

LinWheel sits inside the ACE (Agent-native Content Engine) campaign:

- Articles 1-3 build credibility: validation methodology, production hardening, proof of system
- Article 4 reveals LinWheel as the distribution layer
- Thesis: "Validation without distribution is a fancy journal entry."

The Hunter run on LinWheel should be tighter than the prior ACE signal scan. ACE is the narrative wrapper; LinWheel is the specific product bet that needs its own signal validation.

---

## 9. Demo / Proof Artifact

The proof demo should show:

1. Buildlog entry as input
2. LinWheel dashboard showing transformed output across multiple angles
3. Direct links to published LinkedIn posts
4. Highlight: a comment on one of those posts praising the voice as "original" or "refreshing"

This demo feeds Article 4 of the ACE campaign and doubles as the product landing page hero.

---

## 10. Key Questions for Hunter to Answer

1. Is $89/mo viable for ICP-1 (solopreneurs) or does it need a lower entry tier?
2. Is Taplio actually losing users, or is that wishful thinking?
3. Does the Justin Welsh ecosystem represent a real distribution channel or a dead end?
4. Is "agent-native" a selling point today, or should it be downplayed until the market catches up?
5. What's the LinkedIn API risk — is direct publishing via unofficial methods a ticking time bomb?
6. Are there adjacent ICPs we're missing (e.g., dev advocates, technical recruiters, VC content teams)?
