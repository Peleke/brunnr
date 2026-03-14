# Landing Page Template

> Phase 1 of the pitch skill. Contains the complete landing page copy structure,
> section-by-section breakdown, objection patterns, and copy rules.

## Phase 1: Landing Page Copy

Generate complete landing page copy that is ready to paste into any landing page builder (Carrd, Webflow, Framer, raw HTML). Every section must be standalone -- someone could build a full conversion page from this output alone.

### 1.1 Headline + Subheadline

Refine the headline and subheadline from offer-scope positioning. The headline from offer-scope is a draft; the pitch headline is the final version.

- **Headline**: Must stop the scroll. Pull directly from the persona's pain language. Test: if this headline appeared in the subreddit where the persona hangs out, would they stop scrolling and click?
- **Subheadline**: States the transformation in concrete terms -- what they get, what changes, how fast. No vague promises. Specificity is credibility.

### 1.2 Above-the-Fold Hook

The first 2-3 sentences below the headline. This is the "stay or bounce" copy. It must:
- Acknowledge the persona's current painful situation (using their exact words from pain stories)
- Promise a specific, believable outcome
- Create enough curiosity to scroll

### 1.3 Problem Section

Full copy for the "you know this feeling" section. Structure:
- **Situation**: What the persona is doing when the pain hits (from pain stories)
- **Pain**: What goes wrong, how it feels (using emotional state from persona data)
- **Failed workarounds**: What they have tried that does not work (from current_workaround in pain stories)
- **Emotional climax**: The moment of peak frustration -- this is where the persona thinks "this person has been in my shoes"

Rules:
- Use direct quotes or near-quotes from persona evidence
- Do NOT use generic pain language ("Are you tired of...?"). Use specific language ("You are staring at a Terraform plan that touches 47 resources and you have no idea which ones are safe to apply")
- Minimum 3 pain story references, cited from persona data

### 1.4 Solution Section

Full copy for "here is what changes." Structure:
- **The transformation**: Before state to after state (from offer-scope transformation)
- **How it works**: 3-step simplified explanation (not the full build spec, but the buyer's journey)
- **Speed**: How fast they see results (from value equation time_delay)
- **Effort required**: How little work they do (from value equation effort_sacrifice)

### 1.5 What's Inside Section

Section-by-section breakdown from the offer-scope build spec. For each section:
- **Section name**: From build spec section titles
- **What it does for them**: Translate the content_type into a buyer benefit
- **Key deliverable**: The specific thing they walk away with from this section

Rules:
- Use benefit language, not feature language ("A decision tree that tells you exactly which container orchestrator to use" not "Container orchestration decision tree")
- Each section description should make the buyer think "I need that specific thing"

### 1.6 Social Proof Strategy

For a zero-testimonial launch, build credibility through:
- **Credentials proof**: Operator's relevant experience, deployed to match persona's authority bias
- **Process proof**: How this was built -- research methodology, persona data, real-world grounding
- **Methodology proof**: The frameworks and thinking behind the product (named frameworks from the canon)

Do NOT fabricate testimonials. Do NOT use placeholder quotes. Honest credibility beats fake social proof.

### 1.7 Pricing Section

Full copy including:
- **Price anchor**: Show the value first (what this would cost as consulting, what comparable resources cost)
- **Value stack**: List everything they get with dollar values assigned to each component
- **The price**: Clear, prominent, no hiding
- **Guarantee**: From offer-scope, written as full copy (not just the policy, but the emotional reassurance)
- **Urgency element**: If applicable (launch pricing, early-bird, limited bonus) -- only if honest

### 1.8 FAQ Section

Built from persona objections. Each FAQ maps to one objection from persona data:
- **Question**: The objection reframed as a question the buyer would actually ask
- **Answer**: The counter from offer-scope objection handlers, expanded into conversational copy

Minimum 5 FAQs. Each must trace to a specific persona objection.

### 1.9 CTA Copy

- **Primary CTA**: The main action (buy, enroll, download). Button text + surrounding copy. Must be specific ("Get the DevOps Decision Kit" not "Buy Now")
- **Secondary CTA**: The lower-commitment action (email signup, free preview, GitHub repo). For people who are not ready to buy yet but are interested.

### Landing Page Copy Rules

- Every line must be traceable to persona data or offer-scope positioning. If you cannot cite the source, cut the line.
- No generic marketing fluff. No "In today's fast-paced world..." No "Are you ready to take your career to the next level?"
- The landing page must work as a standalone document -- someone could build a page from just this output.
- Write in the persona's register. If the persona is a senior engineer, write like a senior engineer talks, not like a marketer talks.
