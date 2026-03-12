# Bragi Review: productionizing-hunter
# Date: 2026-03-09
# Source: article-draft skill (28-rule Bragi Prose Gate)



## Bragi Review: "Productionizing Hunter"

### R1 — Em Dashes

The article is clean on em dashes in the prose shown. One potential violation in the subtitle: "it runs" and "it ships" use quotes, not dashes, so that passes. But watch the full draft for any that crept into the code-adjacent sections or the closing paragraph (the abbreviated text hides those). Verdict: **likely clean, verify full text.**

### R7 — Punchy Fragments

Strong in places. "It worked. The output was good. The problem was everything around it." is excellent Peleke cadence. "I started by counting lines." works. But the piece leans too heavily on explanation mode after Section II. The eval section (III) and auto-persist section (IV) read like documentation with editorial framing rather than prose with technical substance. Opportunities:

- Section III opener ("Here is the part that should bother you if you build agent systems") is good but the colon setup is soft. Try: "I had no way to know if editing a skill broke it. That should bother you if you build agent systems."
- Section V: "So I extracted it." is doing the right thing. More of this throughout.

### R8 — Specificity / Receipts

This is where the article is strongest. 50/60 validation score, three buyer personas, Reddit quotes with URLs, 989 lines, 1,034 lines, 40 hardcoded paths, 13 files, 500-line spec limit. The receipts are excellent. No notes.

### R17 — Anthropic Reference

The Anthropic eval guide citation is fine editorially but reads like a book report: "Anthropic's engineering team published a guide... that lays out the taxonomy clearly." That's deferential. Pelekification would be: state the taxonomy as your own framing, then footnote the source. You discovered these categories by doing the work; the Anthropic guide validates your framing, not the other way around. Flip the authority.

### R19 — Staleness

**"Last week"** is a time bomb. The moment this publishes more than seven days after the pipeline run, it reads stale. Replace with either a concrete date ("In early March 2026") or drop the temporal anchor entirely. "I ran a product discovery pipeline against my own business idea" works without "Last week."

The specific counts (989 lines, 40 paths) are fine because they describe a snapshot that was true at audit time. They don't rot.

### R22 — Wall Paragraphs

**Section I, paragraph 2** is a wall. Six sentences listing problems in a single block. This is a bullet list pretending to be prose. Either:
- Break into actual bullets (fits the audit tone), or
- Split after "The problem was everything around it." and start a new paragraph at "The skills had hardcoded absolute paths..."

**Section VI ("What I Learned")** is the worst offender. Three "First/Second/Third" paragraphs that are described as long in the abbreviated text. This pattern always produces walls. Options:
- H3 subheadings for each learning ("Paths and Schemas", "Eval-Driven Development", "Closing the Loop")
- Cut each to 2-3 sentences max. The learnings are restating what the article already demonstrated. Which leads to...

### R26 — Redundant Closing

Section VI restates Sections II-V. "The gap between 'works for me' and 'works for anyone' is mostly paths and schemas" summarizes Section II. "Eval-driven development is the right default" summarizes Section III. "The pipeline documents itself when you close the loop" summarizes Sections IV-V.

The reader already knows all of this. Two fixes:
1. **Kill Section VI entirely.** End on Section V's extraction narrative. The article's structure already teaches the lessons.
2. **Replace with forward-looking close.** What ships next? What does v1.1.0 look like? The reader wants trajectory, not recap.

### Pelekification Opportunities

- **Section III** cites Anthropic's eval taxonomy as external authority. Reframe: you built the pipeline, hit the eval gap, and arrived at the same taxonomy independently. The guide confirmed your instinct. That's a stronger narrative.
- **Section IV** ("I forget about half the time") is honest but undersells. Peleke voice would be: "I forget. Every time. So the fix can't depend on me remembering." Same content, more punch.
- **The subtitle** ("On the gap between 'it runs' and 'it ships'") is good but generic. Consider: "On the gap between 'it runs on my machine' and 'it ships.'" The extra phrase adds the specificity that makes the article's core tension concrete.

### MDX Conversion

Not needed yet. The SVGs are already inline. If you add interactive components (collapsible code blocks, toggleable before/after views of the refactored skills), then convert. For now, plain `.md` with inline SVG is the right format. Convert when you have a reason, not preemptively.

### Summary Verdicts

| Rule | Status |
|------|--------|
| R1 (em dashes) | Likely clean, verify full text |
| R7 (fragments) | Good in I-II, soft in III-IV |
| R8 (receipts) | Excellent throughout |
| R17 (Anthropic cite) | Flip the authority direction |
| R19 (staleness) | Kill "Last week" |
| R22 (walls) | Section I para 2 + all of Section VI |
| R26 (redundant close) | Kill or replace Section VI |

**Top three actions:** (1) Delete or rewrite Section VI. (2) Kill "Last week." (3) Flip the Anthropic eval cite from deference to confirmation.