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

The connection between brunnr and Skillipedia works through GitHub's cross-repository dispatch:

1. **You publish a skill** in a brunnr-compatible repository (skills in `skills/<slug>/SKILL.md`).
2. **brunnr scans it** for security threats and validates the structure.
3. **A GitHub Action dispatches** an event to the Skillipedia repository.
4. **Skillipedia ingests** the skill metadata and generates a catalog entry.

### Cross-repo dispatch

The dispatch event contains the skill's metadata:

```json
{
  "event_type": "skill_published",
  "client_payload": {
    "skill_slug": "ax-rubric",
    "source_repo": "Peleke/brunnr",
    "scan_result": "clean",
    "description": "Score agent-facing tool descriptions...",
    "version": "1.0"
  }
}
```

### GitHub Actions workflow

To enable automatic publishing to Skillipedia, add a workflow to your repository:

```yaml
name: Publish Skill

on:
  push:
    paths:
      - 'skills/*/SKILL.md'
    branches:
      - main

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install brunnr
        run: pip install brunnr

      - name: Scan
        run: brunnr scan --strict

      - name: Dispatch to Skillipedia
        if: success()
        uses: peter-evans/repository-dispatch@v3
        with:
          token: ${{ secrets.SKILLIPEDIA_TOKEN }}
          repository: Peleke/skillipedia
          event-type: skill_published
          client-payload: |
            {
              "skill_slug": "${{ github.event.head_commit.message }}",
              "source_repo": "${{ github.repository }}"
            }
```

!!! note "Token required"
    Cross-repository dispatch requires a personal access token with `repo` scope stored as a repository secret.

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
