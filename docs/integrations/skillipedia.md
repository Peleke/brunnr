# Skillipedia Integration

brunnr feeds [Skillipedia](https://github.com/Peleke/skillipedia) -- a knowledge graph and documentation site for agent skills. When you publish a skill through brunnr, it can be indexed and made discoverable through Skillipedia's catalog.

---

## What is Skillipedia

Skillipedia is a content-driven site that catalogs agent skills. Each skill entry includes:

- The skill's name and description
- What it does, when to use it, and how
- The source repository and installation instructions
- Related skills and cross-references

Think of it as a package registry, but for agent system prompts instead of code libraries.

---

## How brunnr connects

Skillipedia pulls from brunnr. Nothing in brunnr pushes to it.

1. **A skill lands on brunnr `main`** under `skills/<slug>/SKILL.md`, after passing the PR security scan.
2. **Every 6 hours**, Skillipedia's `Build Skillipedia` workflow checks out brunnr's `skills/` directory. brunnr is public, so no token is involved.
3. **`scripts/sync-from-brunnr.py`** converts each `SKILL.md` into an entry under `src/content/entries/`.
4. **The workflow commits changed entries** to Skillipedia `main`, and the site rebuilds.

To sync immediately, run the workflow by hand:

```bash
gh workflow run "Build Skillipedia" --repo Peleke/skillipedia
```

---

## Skillipedia content entries

Skillipedia entries are Markdown files in the `src/content/entries/` directory. Each entry follows a standard schema:

```markdown
---
title: AX Description Rubric
slug: ax-rubric
description: Score agent-facing tool descriptions against five criteria.
source: https://github.com/Peleke/brunnr
category: evaluation
tags: [ax, tool-descriptions, scoring, mcp]
---

# AX Description Rubric

Content about the skill...
```

---

## Manual publishing

If you prefer not to automate, you can manually submit a skill to Skillipedia:

1. Fork the Skillipedia repository
2. Create an entry in `src/content/entries/`
3. Open a pull request

The brunnr scan result (CLEAN, FLAG, BLOCK) is part of the entry metadata and displayed in the catalog.

---

## Knowledge graph

Skillipedia builds a knowledge graph from skill metadata:

- **Skills** are nodes
- **Tags** connect related skills
- **Categories** group skills by function (evaluation, security, formatting, etc.)
- **Source repositories** link skills to their origins

This graph powers Skillipedia's search and "related skills" recommendations. As the brunnr skill registry grows, the knowledge graph becomes more useful for discovering complementary tools.
