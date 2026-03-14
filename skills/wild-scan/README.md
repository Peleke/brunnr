# Wild Scan: Pain Quote Harvesting for the "From the Wild" Content Series

> The best content doesn't start with "I have an idea." It starts with "I found someone screaming into the void — and I know how to help."

---

## Table of Contents

1. [The Premise](#the-premise)
2. [The "From the Wild" Content Format](#the-from-the-wild-content-format)
3. [The Discipline: Why Quotes Beat Ideas](#the-discipline)
4. [The Canon: Who Does This Well](#the-canon)
5. [How the Skill Works](#how-the-skill-works)
6. [The Scoring System](#the-scoring-system)
7. [The Battle Axe Repo](#the-battle-axe-repo)
8. [The Weekly Loop](#the-weekly-loop)
9. [Integration with the Pipeline](#integration-with-the-pipeline)

---

## The Premise

Here is the content strategy most technical educators follow: sit down, think of something you know, write about it, publish it, hope someone cares. It works sometimes. It fails more often. The failure mode is always the same — you wrote about what *you* found interesting, not about what *they* are struggling with. The gap between those two things is the gap between content that resonates and content that disappears.

Wild Scan inverts the process. Instead of starting with your expertise and looking for an audience, you start with the audience's pain and bring your expertise to it. The raw material is not your knowledge. It is someone else's suffering. Specifically: real quotes from real humans in real communities — Reddit, Hacker News, Stack Overflow, dev.to, Twitter — expressing real frustration with real problems.

The output is a scored, themed index of pain quotes, each one a potential seed for a piece of content that writes itself. The format: "From the Wild." Found another one. Here is a real person struggling. Here is what is actually going wrong. Here is a GitHub repo that demolishes the problem. You are welcome.

---

## The "From the Wild" Content Format

Every "From the Wild" post follows the same structure. The structure is the brand.

### 1. THE QUOTE

Start with the real quote. Exact words. Unedited. Typos and all. This is the hook, the empathy signal, and the proof of market all in one.

> "I've been doing tutorials for 6 months and I still can't deploy a real app to production. Every tutorial stops at 'hello world' and I'm left with no idea how to handle logging, monitoring, secrets, or anything that matters in a real environment."
> — u/frustrated_junior, r/devops, 234 upvotes

The rawness is deliberate. A polished paraphrase says "I understand your problem." An exact quote says "I found you. You are not alone. And I am about to fix this."

### 2. THE DIAGNOSIS

Two to three sentences explaining the *structural* failure that creates this pain. Not "tutorials are bad." That is a complaint, not a diagnosis. The diagnosis identifies the mechanism:

> Every tutorial teaches tools in isolation. Docker over here. Terraform over there. GitHub Actions in a separate tab. Nobody shows the integration — the full path from code change to production deploy to observable system. The gap is not knowledge. It is assembly.

The diagnosis is what separates this format from every other "I feel your pain" content. You are not commiserating. You are explaining *why* the pain exists at a structural level.

### 3. THE HACK

"So we built this." Link to the repo. This is where the battle axe comes out.

The repo is not a tutorial. It is a working, production-grade reference implementation that happens to be teachable. The difference matters:

| Tutorial Repo | Battle Axe Repo |
|---------------|-----------------|
| `console.log("Hello World")` | Structured logging with correlation IDs |
| "Deploy to Heroku" | Multi-environment deploy pipeline with rollback |
| Single `main.tf` | Modular Terraform with remote state and locking |
| No tests | CI with test, lint, security scan, build |
| README says "getting started" | README says "here is what production looks like" |
| Stops at "it works on my machine" | Includes monitoring, alerting, and a runbook |

### 4. THE WALKTHROUGH

Three to five key steps from the repo, highlighted with code snippets. Enough to prove the repo works and to give the reader a taste of the depth. Not a full tutorial — just the critical path.

### 5. THE CTA

"Found another one? Drop it in the comments."

This is how you crowdsource future quotes. Every "From the Wild" post generates leads for the next one. The audience becomes the scanning engine.

---

## The Discipline

### Why Quotes Beat Ideas

The content marketing world runs on ideas. "I should write about Terraform state management." That is an idea. It might be good. It might not. You will not know until you publish it and watch the analytics.

Quotes are not ideas. Quotes are evidence. When you start with a quote — a real human, in a real community, expressing real frustration, validated by real engagement (upvotes, replies, "same here" responses) — you are not guessing whether the topic resonates. You know it resonates. The engagement metrics are right there. The emotional language is right there. The pain is pre-validated.

This is the same principle that drives product signal detection (see the [signal-scan](../signal-scan/) skill). The difference is scope and cadence:

| | Signal Scan | Wild Scan |
|---|---|---|
| **Scope** | Broad market analysis across 7 signal types | Focused pain-quote harvesting |
| **Output** | Market opportunities + ship candidates | Content briefs + repo specs |
| **Cadence** | Per-domain, as needed | Weekly, feeding the content loop |
| **Goal** | Decide what to build | Decide what to write about |

Wild Scan is the content engine that signal-scan is the product engine. Same philosophy — start with evidence, not assumptions — applied to a different problem.

### The Evidence Hierarchy

Not all quotes are equal. The scoring system (see [references/scoring-rubric.md](references/scoring-rubric.md)) formalizes this, but the intuition is simple:

**Strongest evidence:**
- Specific problem + emotional language + high engagement + directly solvable with a repo
- Example: "I spent 3 days debugging a YAML indentation error in my K8s manifest. I am losing my mind." (r/kubernetes, 189 upvotes)

**Strong evidence:**
- Specific problem + moderate engagement + solvable
- Example: "Does anyone have a working example of GitHub Actions deploying to EKS with secrets management? Every tutorial I find uses hardcoded values." (r/devops, 67 upvotes)

**Moderate evidence:**
- General frustration + high engagement
- Example: "Kubernetes has the worst learning curve of any tool I have ever used." (r/devops, 312 upvotes)

**Weak evidence:**
- Vague complaint + low engagement
- Example: "DevOps is hard." (r/devops, 4 upvotes)

The scoring system quantifies this intuition across four dimensions: specificity, intensity, solvability, and engagement. See the rubric for calibration tables.

---

## The Canon

The "From the Wild" format draws on several content strategy traditions. Understanding them helps you execute the format with more precision.

### Gary Vaynerchuk — Document, Don't Create

Vaynerchuk's core content philosophy: instead of sitting down to "create content," document what you are already doing. Wild Scan adapts this: instead of creating content from your expertise, document what you find in the wild. The shift from creation to documentation makes the process faster, more authentic, and more sustainable. You are a reporter, not an inventor.

### Nathan Barry — Teach Everything You Know

Barry's philosophy (which powered ConvertKit's growth): teach everything you know, publicly, for free. The generous act of teaching builds trust, audience, and eventually revenue. Wild Scan fits this perfectly — each "From the Wild" post is an act of generous teaching triggered by someone else's pain. You are not gatekeeping. You are responding to a cry for help with a working repo.

### Sahil Lavingia — The Minimalist Entrepreneur

Lavingia's framework: build in public, start with community, solve real problems for real people. Wild Scan is the content expression of this philosophy. The quotes come from the community. The repos solve real problems. The posts are public building. The CTA ("found another one?") closes the loop back to community.

### Patrick McKenzie (patio11) — Writing for Engineers

McKenzie demonstrated that engineers can build significant audiences by writing about the intersection of engineering and business with brutal honesty and specificity. His writing is never generic. It is always grounded in specific experiences, specific numbers, specific failures. Wild Scan enforces this discipline by starting every piece with a specific quote from a specific person in a specific community — not with a generic take.

### Swyx (Shawn Wang) — Learn in Public

Wang's "Learn in Public" essay argues that the fastest way to learn is to share what you learn as you learn it. Wild Scan extends this: learn what *others* are struggling with, publicly solve it, and document the solution. Every "From the Wild" post is a public learning artifact — you find a pain point, research the proper solution, build the repo, and publish both the problem and the solution. You learn by teaching. The audience learns by watching you solve real problems in real time.

### The Content-Market Fit Hypothesis

Just as products need product-market fit, content needs content-market fit. Most content fails not because it is bad, but because nobody needed it. Wild Scan's thesis is that content-market fit is achievable *before* you write a single word — by starting with validated demand (the quote, the upvotes, the engagement) rather than with your own sense of what might be interesting.

The quote is your content-market fit test. If 200 people upvoted someone's frustration with a topic, 200 people will read your solution to that frustration. The demand is pre-proven. All you have to do is supply the solution.

---

## How the Skill Works

### Phase 1: Search Planning

You provide a topic focus (e.g., "DevOps career transition for sysadmins learning to code"), a learning stage (e.g., "early career, some Linux experience, weak on coding"), and a repo angle (e.g., "production-ready infrastructure projects that double as portfolio pieces").

The skill builds a search plan: which platforms, which communities, which search queries, which pain-language indicators. See [references/search-playbook.md](references/search-playbook.md) for the full query template library.

### Phase 2: Quote Harvesting

Extensive web search across Reddit, HN, Stack Overflow, dev.to, and Twitter. Minimum 15 quotes per run, aiming for 20-30. Every quote captured with: exact text, author, platform, community, URL, engagement metrics, context, and pain category.

**Pain categories:**
- `tutorial-gap` — Tutorials exist but do not prepare you for real work
- `tool-complexity` — Tools are too complex to learn effectively
- `real-world-gap` — Gap between learning materials and production reality
- `career-transition` — Struggling to break into or transition within the field
- `information-overload` — Too many resources, no clear path
- `environment-setup` — Cannot get the tools working locally
- `debugging-hell` — Spending disproportionate time debugging config/infra
- `missing-fundamentals` — Lacking prerequisite knowledge that tutorials assume

### Phase 3: Quote Scoring

Four weighted dimensions:

| Dimension | Weight | What It Measures |
|-----------|--------|------------------|
| Specificity | 2x | How precisely does the quote identify a pain point? |
| Intensity | 2x | How much does this person actually hurt? |
| Solvability | 2x | Can we demolish this with a repo? |
| Engagement | 1x | Social proof that the pain is shared |

Overall: `(specificity*2 + intensity*2 + solvability*2 + engagement) / 7`

### Phase 4: Theme Clustering

Quotes are grouped into pain themes — recurring structural problems that multiple quotes point to. A theme needs at least 2 quotes. **Gold themes** (5+ quotes, avg score >= 7) are flagged for priority content.

### Phase 5: Content Brief Generation

For each theme scoring >= 6, a "From the Wild" content brief is generated with the post structure, channel adaptations (LinkedIn, blog, Reddit), and estimated word count.

### Phase 6: Repo Spec

For each brief, a detailed instructional repo spec: name, structure, progressive git tags, key architectural decisions ("why X not Y"), and battle-axe features that make it production-grade.

---

## The Scoring System

The scoring system is intentionally weighted toward **solvability**. A heartbreaking quote about imposter syndrome might score 10 on intensity, but if you cannot solve it with a repo, it scores 1-2 on solvability. The overall score drops. This is by design — the purpose of the score is not to measure how bad the pain is. It is to measure how good a "From the Wild" post it would make.

### Solvability Is the Filter

The solvability dimension has explicit **auto-caps** (maximum score of 3) for patterns that cannot be addressed with an instructional repo:

- "My company won't adopt DevOps" → organizational, not educational
- "Nobody is hiring juniors" → economic, not educational
- "Imposter syndrome is killing me" → psychological, not educational
- "I don't have time to learn" → scheduling, not educational
- "The technology keeps changing" → existential, not educational

And explicit **boosters** (+1-2 points) for patterns that map perfectly to a repo:

- Person names a specific template they wish existed (+2)
- Person describes exactly what the solution would look like (+2)
- Person has tried multiple resources and lists what is missing (+1)
- Person says "I would pay for..." (+1)

### The Engagement Paradox

High engagement (upvotes, replies) validates that the pain is shared. But engagement alone is not enough. "DevOps is hard" might get 500 upvotes because everyone agrees — but it scores 1 on specificity and 2 on solvability. The weighted formula ensures that viral-but-vague quotes do not dominate the index.

The ideal quote has *all four*: specific (you can build a repo for it), intense (the person is in real pain), solvable (a repo directly addresses it), and validated (others agree).

---

## The Battle Axe Repo

The repo is the product. The post is the wrapper. This inversion is critical. Most content creators write a blog post and maybe link to a repo as an afterthought. In "From the Wild," the repo is the main event. The post exists to explain why the repo exists and to give the reader enough context to use it.

### Progressive Git Tags

Every repo uses git tags to enable progressive learning:

```
step-01-scaffold     — Project structure, nothing works yet
step-02-local        — Works locally, manual everything
step-03-containerize — Dockerized, but still manual deploy
step-04-ci           — Automated tests on push
step-05-cd           — Automated deploy on merge
step-06-secrets      — Secrets management (not hardcoded)
step-07-monitor      — Logging, metrics, health checks
step-08-production   — The full thing: rollback, alerting, runbook
```

The reader can `git checkout step-01` and follow the progression. Each step has a README section explaining not just WHAT changed but WHY. The "why" is the differentiator. Every other tutorial shows you the commands. This shows you the reasoning.

### "Why X Not Y" Decisions

Every repo includes 3-5 explicit architectural decisions documented in a `DECISIONS.md` or in the README:

```markdown
## Decision: GitHub Actions over Jenkins
**Why**: Jenkins requires hosting and maintaining a server. For a repo
that teaches CI/CD concepts, the infrastructure meta-problem (maintaining
Jenkins itself) obscures the actual lesson. GitHub Actions is free for
public repos, zero-infrastructure, and YAML-based — which means the CI
config lives with the code and is version-controlled by default.

**Tradeoff**: GitHub Actions is GitHub-locked. Jenkins is portable. We
chose teachability over portability because the concepts (pipeline stages,
artifact management, environment promotion) transfer to any CI system.
```

These decisions are content in themselves. Each one is a potential LinkedIn post.

---

## The Weekly Loop

Wild Scan is designed for weekly cadence:

```
Monday:     Run /wild-scan "{topic focus}"
            → 20 scored quotes, 4 themes, 2 gold themes, 2 content briefs

Tuesday:    Pick the best brief. Start building the repo.
            (Or add to an existing repo — a new "step" or module)

Wednesday:  Finish the repo. Push to GitHub.
            Write the "From the Wild" post draft.

Thursday:   Publish on LinkedIn and/or blog.
            Cross-post the repo link in the subreddit where the quote came from.

Friday:     Check engagement. Read comments. Harvest new quotes from the comments
            for next week's scan.
```

The CTA at the end of every post — "Found another one? Drop it in the comments." — turns the audience into scanners. Each post generates leads for the next one. The flywheel accelerates.

### Over Time

After 12 weeks, you have:
- 12+ published "From the Wild" posts
- 12+ GitHub repos (or modules within repos)
- 200+ indexed pain quotes across themes
- A growing audience that sends you quotes proactively
- A portfolio of production-grade instructional repos
- Content-market fit data: which themes get the most engagement?

The repos compound. Each new repo links to related repos. The collection becomes a curriculum. The curriculum becomes the foundation for a paid product (course, community, or both). The content loop feeds the product pipeline.

---

## Integration with the Pipeline

Wild Scan is part of the hunter product-discovery pipeline:

```
signal-scan ──→ decision-log ──→ persona-extract ──→ offer-scope ──→ pitch
                                       │
                                       └──→ content-planner
                                                   ↑
                                            wild-scan ──→ Writing/From-The-Wild/
                                                     └──→ Writing/Content-Briefs/
```

**How it connects:**

- **Signal-scan** identifies broad market opportunities. Wild-scan dives deep into the pain language within those opportunities.
- **Persona-extract** defines who is hurting. Wild-scan finds their actual words.
- **Content-planner** schedules content from GitHub activity and buildlog. Wild-scan adds a third source: community pain quotes.
- **Content briefs** from wild-scan use the same format as content-planner briefs, so they appear on the same kanban board.

### Vault Structure

```
Writing/
├── From-The-Wild/                    ← wild-scan output (quote indices)
│   ├── devops-career-2026-02-11.md
│   ├── kubernetes-beginner-2026-02-18.md
│   └── wild-scan-*.json
├── Content-Briefs/                   ← shared with content-planner
│   ├── ftw-tutorial-gap-2026-02-11.md
│   └── ftw-k8s-complexity-2026-02-18.md
└── Content-Plan.kanban.md            ← content-planner picks up briefs
```

---

## Quick Start

```
/wild-scan "DevOps career entry — sysadmins learning to code"
```

The skill will:
1. Build a search plan targeting relevant subreddits and communities
2. Harvest 15-30 real pain quotes with engagement metrics
3. Score each quote on specificity, intensity, solvability, and engagement
4. Cluster quotes into pain themes
5. Generate "From the Wild" content briefs for themes scoring >= 6
6. Spec instructional repos for each brief
7. Save everything to the Obsidian vault

Then pick the best brief, build the repo, and write the post.
