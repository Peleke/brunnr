# GitHub README Template

> Phase 3 of the pitch skill. Contains the GitHub product README structure,
> product structure sketch, hero image generation, launchpad branch workflow,
> and landing page HTML generation.

## Phase 3: GitHub Product README

This phase has multiple sub-phases. Phase 3a produces the product architecture; Phase 3b produces the README that serves as both documentation and conversion engine; Phase 3c generates a hero image; Phase 3d deploys to the launchpad repo; Phase 3e generates a landing page HTML file.

### Phase 3a: Product Structure Sketch

**ACTIVATES for technical domains**: DevOps, security, coding, architecture, STEM, data engineering, ML/AI, infrastructure. Skip for non-technical domains (business coaching, creative writing, etc.).

This sub-phase produces the actual PRODUCT DESIGN for the GitHub repo. It is the blueprint for what the repo contains and how it is structured.

#### Buildlog Integration (Ambient Data Enrichment)

Before sketching the structure, check buildlog for real engineering material to instrument the product with:

1. **Scan buildlog entries**: Use `buildlog_entry_list()` and `buildlog_overview()` to find entries relevant to the product domain
2. **Pull decision narratives**: Extract "we chose X over Y because Z" stories from buildlog entries and reward events -- these become case studies and decision annotations in the product
3. **Harvest real code examples**: Find real build errors, debugging sessions, and solutions from buildlog -- these replace hypothetical examples with authentic, battle-tested ones
4. **Collect learnings and mistakes**: Real "what went wrong" stories from buildlog entries are more valuable than invented scenarios
5. **Reference specific entries**: In the file manifest, note which buildlog entries source each example (e.g., `buildlog://hunter/terraform-ecs-vs-eks-decision`)

The goal: every example, narrative, and code snippet in the product should come from REAL engineering work captured by buildlog, not from hypothetical scenarios. This is the operator's unfair advantage -- authentic practitioner content that "course creators" cannot replicate.

#### Directory Layout

Generate the actual directory tree:
```
repo-name/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── docs/
│   ├── getting-started.md
│   └── ...
├── frameworks/
│   ├── ...
│   └── ...
├── checklists/
│   ├── ...
│   └── ...
├── templates/
│   ├── ...
│   └── ...
└── examples/
    ├── ...
    └── ...
```

The directory layout must reflect the build spec sections from offer-scope. Each section maps to a directory or file.

#### File Manifest

Key files with one-line descriptions:
- List every file that will exist in the repo
- Each file gets a one-line description of what it contains and why it matters
- Include both free-tier files (the 80% value) and premium-tier files (the 20% that people pay for)

#### Learning Path

How someone progresses through the repo:
- Step 1: Start Here (README orientation)
- Step 2: [First framework/tool]
- Step 3: [Second framework/tool]
- ...
- Step N: Get the complete kit (CTA for paid product)

#### Prerequisites

What the user needs to know before using this repo:
- Technical prerequisites (tools, languages, concepts)
- Experience level assumed
- Time commitment expected

### Phase 3b: README Conversion Copy

Generate the full README.md content that combines the product structure with conversion-optimized copy.

#### Hero Section
- What this is (one sentence)
- Why it matters (the pain it solves, using persona language)
- The transformation (before/after)
- Badges: stars, license, last commit -- the trust signals for technical audiences

#### Product Structure Preview
- The directory tree from Phase 3a
- Brief description of what each top-level directory contains
- "What You Get" summary

#### Decision Framework Preview
- The free 80%. Include enough of the actual framework, decision tree, or checklist to be genuinely useful.
- This is NOT a teaser. This is real, usable content. A developer who reads only the README should learn something valuable.
- Format: tables, decision trees (text-based), checklists, or annotated examples -- whatever matches the product format

#### "Get the Full Kit" CTA Section
- What the paid product includes beyond the free preview
- Price and link
- Guarantee
- Keep it brief -- 3-5 lines. The README proved the value; the CTA collects the conversion.

#### Email Signup CTA
- For the lead magnet funnel
- What they get for signing up (specific deliverable, not "updates")
- Link to signup form

#### Social Proof / Credentials Section
- Operator background relevant to this product
- Methodology description
- Any metrics (stars, forks, community size) once available

#### Contributing Section
- How to contribute (report issues, suggest frameworks, submit case studies)
- Code of conduct reference
- This section encourages organic growth through community participation

#### License Section
- License type and brief explanation

### GitHub README Rules

- The README must be excellent technical documentation FIRST, marketing second.
- DevOps engineers (and engineers generally) judge README quality as a proxy for product quality. Sloppy README = sloppy product.
- Code examples, directory trees, and technical precision matter more than sales language.
- The free preview must be genuinely valuable. This is the "give 80%" principle in action.
- Markdown formatting must be flawless. Broken tables, inconsistent headers, or missing code fences will cost credibility.

### Phase 3c: Hero Image Generation

After creating the README, generate a hero image for the product repo.

**If ComfyUI MCP is available:**
1. Use `mcp__comfyui__generate_image` to generate a product-appropriate hero image
2. Prompt should match the product domain: for DevOps/infrastructure, use isometric technical illustrations with dark backgrounds and teal/blue accents; for programming, use code-themed abstract art; for security, use shield/lock motifs
3. Dimensions: 1280x640 (GitHub README hero ratio)
4. Save to the product branch root as `hero.png`
5. Reference in README: `![{Product Name}](hero.png)` immediately after the H1 title

**If ComfyUI MCP is NOT available:**
Insert an HTML comment in the README immediately after the H1 title with the image intent:
```html
<!-- IMAGE_INTENT: {describe the ideal hero image -- style, colors, elements, mood}
     PROMPT: {the exact ComfyUI prompt to use when generation becomes available}
     DIMENSIONS: 1280x640 -->
```

This allows a future run (or a human designer) to generate the image from the intent.

### Phase 3d: Launchpad Branch + PR

After generating the README and product structure, deploy to the `launchpad` repo:

1. **Clone `launchpad`**: `git clone https://github.com/Peleke/launchpad.git`
2. **Create product branch**: `git checkout -b {product-slug}`
3. **Scaffold the directory structure** from Phase 3a: create all directories and placeholder READMEs
4. **Write the full README.md** from Phase 3b
5. **Add hero image** from Phase 3c (or the HTML comment fallback)
6. **Add scaffolding files**: LICENSE, CONTRIBUTING.md, issue templates
7. **Commit and push** the branch
8. **Open a PR against main** using `gh pr create`:
   - Title: `{Product Name}: Product Structure + README + Hero`
   - Body: Product summary, file list, review checklist with checkboxes, pipeline refs (offer_ref, persona_ref, swot_ref)
   - The PR is the operator's review surface for line-by-line feedback

The PR stays open until the operator reviews and merges. The operator can comment on specific files, and the agent can address feedback in subsequent commits to the same branch.

### Phase 3e: Landing Page HTML

After the launchpad branch exists (Phase 3d), generate a complete, single-file `index.html` from the Phase 1 landing page copy and commit it to the branch root. Vercel auto-deploys every branch, so this file immediately becomes a live landing page at the branch preview URL.

**This phase converts Phase 1 copy into a deployable page. It does NOT rewrite copy.** The HTML is a faithful rendering of the Phase 1 output. If the copy needs revision, revise Phase 1 first, then re-run Phase 3e.

#### 3e.1 Design System

Generate a single `<style>` tag inside `<head>` with these design tokens and components. No external CSS, no JavaScript frameworks, no CDN links. The page must work as a standalone file with zero dependencies.

**Color tokens (CSS custom properties on `:root`):**

| Token | Value | Usage |
|-------|-------|-------|
| `--bg` | `#0d1117` | Page background |
| `--surface` | `#161b22` | Cards, blockquotes, FAQ panels |
| `--border` | `#30363d` | All borders |
| `--text` | `#e6edf3` | Primary text |
| `--text-muted` | `#8b949e` | Secondary text, descriptions, citations |
| `--accent` | `#58a6ff` | Links, module names, interactive highlights |
| `--accent-hover` | `#79c0ff` | Link hover state |
| `--green` | `#3fb950` | Primary CTA buttons, "after" cards, checkmarks |
| `--orange` | `#d29922` | Warning or emphasis accents |
| `--red` | `#f85149` | "Before" cards, problem emphasis |

**Typography:**
- Font stack: `-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif`
- Line height: `1.6`
- `-webkit-font-smoothing: antialiased`
- Hero h1: `2.8rem`, weight `800`, letter-spacing `-0.02em`
- Section h2: `1.8rem`, weight `700`, letter-spacing `-0.01em`
- Body text: `1.05rem`, color `var(--text-muted)`

**Layout:**
- `.container`: max-width `720px`, centered, `24px` horizontal padding
- Sections separated by `border-top: 1px solid var(--border)` with `60px` vertical padding
- Mobile breakpoint at `640px`: reduce h1 to `2rem`, container padding to `16px`, collapse grids to single column

#### 3e.2 Section-to-HTML Mapping

Each Phase 1 section maps to a semantic HTML block. Generate every section that Phase 1 produced. If a section is empty or was not generated in Phase 1, skip it -- do not generate placeholder content.

| Phase 1 Section | HTML Element | Key Styling |
|-----------------|-------------|-------------|
| **Headline + Subheadline** | `<header class="hero">` containing `<h1>` and `<p class="sub">` | Centered, `80px` top padding, `60px` bottom |
| **Primary + Secondary CTA** | `<div class="cta-group">` with `<a class="btn btn-primary">` and `<a class="btn btn-secondary">` | Flex row, centered, wraps on mobile. Primary: green bg, black text. Secondary: surface bg with border. |
| **Problem Section** | `<section>` with prose `<p>` tags and `<blockquote>` elements | Blockquotes: `3px` left border in accent color, surface bg, `6px` right border-radius. Attribution in `<cite>`. |
| **Solution / Before-After** | `<section>` with `.before-after` grid (`1fr 1fr`) containing `.ba-card.before` and `.ba-card.after` | Before: red-tinted border/heading. After: green-tinted. Collapse to single column on mobile. |
| **How It Works** | `<ol class="steps">` with `<li>` items | CSS counter with numbered circles (accent text, surface bg) positioned left of each step. |
| **What's Inside / Modules** | `<table class="modules-table">` with `<thead>` and `<tbody>` | First column: accent color, `600` weight, no-wrap. Last column: muted, smaller. Hover: surface bg. |
| **Social Proof / Credibility** | `<section>` with `<div class="cred">` | Surface bg, bordered card, `28px` padding. |
| **Pricing** | `<section>` with `.pricing-cards` grid (`1fr 1fr`) | Each card: surface bg, bordered. Featured: green border. Price: `2rem` weight `800`. Checkmark list via `li::before`. |
| **Comparison List** | `<ul class="compare-list">` | Flexbox rows, space-between, border-bottom separator. |
| **FAQ** | `<details>` elements with `<summary>` and `<div>` | Surface bg, bordered, `6px` radius. Custom marker: `+`/`-`. No default webkit marker. |
| **Final CTA** | `<div class="final-cta">` with h2 + `<p>` + `.cta-group` | Centered, `60px` padding, mirrors hero CTA. |
| **Footer** | `<footer>` | Centered, muted, `40px` padding. Links to GitHub and author. |

#### 3e.3 Open Graph and Meta Tags

Generate in `<head>`:

```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{Product Name} — {Headline (truncated to ~60 chars)}</title>
<meta name="description" content="{Subheadline, max 160 chars}">
<meta property="og:title" content="{Product Name} — {Headline}">
<meta property="og:description" content="{Subheadline}">
<meta property="og:type" content="website">
<meta property="og:url" content="https://launchpad-git-{product-slug}-kwayet-fs-projects.vercel.app">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{Product Name} — {Headline}">
<meta name="twitter:description" content="{Subheadline}">
```

If a hero image was generated in Phase 3c, add `og:image` and `twitter:image` tags pointing to `/hero.png`. If not, omit them rather than linking to a nonexistent file.

#### 3e.4 CTA Link Targets

| CTA | Link Target | Fallback |
|-----|------------|----------|
| Primary ("Clone the Repo", "Get the Kit") | `https://github.com/Peleke/launchpad/tree/{product-slug}` | `#` with `<!-- TODO: update link -->` |
| Secondary ("Join the Community") | Skool community URL if known | `#community` anchor to pricing section |
| Email signup | ConvertKit/Buttondown URL if known | `#` with `<!-- TODO: add signup link -->` |

Every placeholder link must have an HTML comment explaining what URL to replace it with.

#### 3e.5 Content Fidelity Rules

- **Do not rewrite copy.** The HTML renders Phase 1 copy verbatim.
- **Typographic entities required.** Straight quotes -> curly (`&ldquo;`/`&rdquo;`, `&lsquo;`/`&rsquo;`), hyphens -> em-dashes (`&mdash;`), three dots -> ellipsis (`&hellip;`).
- **Preserve all persona quotes.** Every blockquote must include quote text in `<p>` and attribution in `<cite>` with em-dash prefix.
- **Preserve the module/feature table exactly.** Same columns, same rows as Phase 1.
- **Preserve all FAQ items.** Each FAQ becomes one `<details>/<summary>` element. Do not merge or split.

#### 3e.6 Responsive Behavior

The `@media (max-width: 640px)` breakpoint must:
- Reduce hero h1 to `2rem`, subtitle to `1.05rem`
- Collapse `.before-after` and `.pricing-cards` grids to single column
- Tighten module table padding (`10px 8px`) and font (`0.85rem`)
- Reduce container padding to `16px`
- No horizontal scrolling at any viewport width down to `320px`

#### 3e.7 File Output

Write `index.html` to the launchpad product branch root alongside `README.md`. If Phase 3d already ran and the branch exists, commit and push. If the PR is already open, this becomes an additional commit on the same PR.

#### 3e.8 Validation Checklist

- [ ] Valid HTML5 (`<!DOCTYPE html>`, `<html lang="en">`)
- [ ] All CSS inline in a single `<style>` tag -- no external stylesheets
- [ ] No JavaScript -- pure HTML + CSS
- [ ] No external dependencies -- no CDN, no Google Fonts, no analytics
- [ ] All Phase 1 sections present (unless empty in Phase 1)
- [ ] All persona quotes as `<blockquote>` with `<cite>`
- [ ] Module/feature table matches Phase 1 exactly
- [ ] All FAQs as `<details>/<summary>`
- [ ] Both CTAs in hero and final CTA sections
- [ ] Open Graph meta tags with correct product name and description
- [ ] Mobile responsive at 640px (no horizontal scroll, grids collapse)
- [ ] All placeholder links have HTML comments
- [ ] Typographic entities used throughout
- [ ] File under 30KB

#### Landing Page HTML Rules

- Page must render correctly as local file (`file://`) AND served by Vercel
- Page must look complete without hero image (no broken image placeholder)
- Semantic HTML: `<header>`, `<section>`, `<footer>`, `<blockquote>`, `<details>`, `<summary>`, `<table>`, `<cite>`
- Dark theme is non-negotiable. All launchpad products use the same visual identity.
