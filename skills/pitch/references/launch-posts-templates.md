# Launch Posts Templates

> Phase 2 of the pitch skill. Contains platform-specific launch post templates,
> the 80/20 value-first rule, Obsidian seed output format, and LinkedIn pipeline integration.

## Phase 2: Launch Posts

Generate 2-3 platform-specific posts, ready to publish. Each follows the 80/20 value-first rule: give 80% of the core insight for free in the post itself, sell the organized/actionable version.

### 2.1 Primary Channel Post

From offer-scope distribution plan, identify the primary launch channel (e.g., r/devops, dev.to, LinkedIn). Generate the full post:

- **Title/Hook**: Platform-appropriate. Reddit titles are direct and specific. LinkedIn hooks are pattern-interrupts. dev.to titles are tutorial-style.
- **Body**: The core insight, framework, or decision logic from the product -- presented as a genuine, valuable standalone post. The reader should benefit even if they never click the link.
- **CTA placement**: Natural transition from "here is the free insight" to "here is the organized/complete version." Never bait-and-switch.
- **Engagement hooks**: Questions, calls for discussion, requests for feedback -- things that drive comments and shares.
- **Formatting notes**: Platform-specific formatting (Reddit markdown, paragraph breaks, header usage).

### 2.2 LinkedIn Version

LinkedIn-specific formatting and tone:
- Opening hook (first 2 lines are visible before "see more" -- must be compelling)
- Short paragraphs (1-2 sentences each)
- Story arc: problem -> insight -> framework -> result -> CTA
- Professional but not corporate. Practitioner voice, not thought-leader voice.
- Hashtag strategy (3-5 relevant hashtags)

### 2.3 Twitter/X Thread Version

5-8 tweet thread:
- Tweet 1: The hook -- a bold, specific claim or observation. Must stand alone as engaging content.
- Tweets 2-5: The framework/insight. Each tweet is self-contained and valuable. Use numbered lists, examples, and specific details.
- Tweet 6-7: The personal experience or credibility signal. Why you built this.
- Final tweet: The CTA. Link to product or landing page. Retweet request.
- Thread pacing: alternate between insight tweets and example tweets. Do not front-load all the value or back-load all the value.

### Launch Post Rules

- Posts must provide GENUINE value. Someone who never buys should still benefit from reading the post.
- The CTA should feel like a natural next step, not a sales pitch grafted onto content.
- Follow platform norms: no self-promo spam on Reddit (provide value first, link second), no clickbait on LinkedIn (be direct), no engagement-bait on Twitter (be authentic).
- Each post must be ready to publish. Not an outline, not a draft. The final words.

### 2.4 Obsidian Seed Output

After generating launch posts, write each post as a **content seed** to the Obsidian vault. These are NOT finished briefs -- they are raw seeds for the operator to review and refine. The `content-planner` skill picks these up later for full brief generation.

Write each post to: `{vault}/Writing/Content-Briefs/{product-slug}-{platform}-seed-{YYYY-MM-DD}.md`

Frontmatter:
```yaml
---
type: content-brief
date: YYYY-MM-DD
status: backlog
tags:
  - content/brief
  - content/channel/{platform}
  - hunter/domain/{domain-slug}
source_skill: pitch
pitch_ref: "{pitch-slug}"
platform: reddit | linkedin | twitter
---
```

Body: The full post text from Phase 2, preceded by a `## Seed Context` section with:
- Target platform and subreddit/hashtags
- Persona being addressed
- Key offer-scope positioning points used
- Suggested posting time (from launch checklist if available)

These seeds flow into the content-planner pipeline: seed -> operator review (via PR) -> content-planner generates full brief -> schedule -> publish.

### 2.5 LinkedIn Launch Post Convention (`::linkedin`)

For LinkedIn launch posts, write them to Obsidian with the `::linkedin` prefix in the note body (before the post content). This triggers the OpenClaw ambient pipeline:

1. OpenClaw detects the `::linkedin` prefix in the Obsidian note
2. Pipes the note content to LinWheel (the LinkedIn content generator + scheduler)
3. The operator reviews and approves the post in LinWheel
4. LinWheel schedules and publishes to LinkedIn

**Format**: Write the LinkedIn seed to `{vault}/Writing/Content-Briefs/{product-slug}-linkedin-seed-{YYYY-MM-DD}.md` with `::linkedin` as the **very first line of the file** (line 1, before frontmatter). NOT after frontmatter -- BEFORE it. The `::linkedin` trigger must be byte 0 of the file or the OpenClaw pipeline won't fire. Frontmatter follows on line 2+. This makes it a live launch post that can be approved and scheduled, not just a draft.

The full pipeline: pitch skill -> Obsidian seed -> OpenClaw -> LinWheel -> LinkedIn publication.
