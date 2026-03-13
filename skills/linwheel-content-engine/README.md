<div align="center">

# linwheel-content-engine

**Turn any source material into polished, scheduled LinkedIn content.**

*One article. Six stages. Published post with carousel and follow-up comments.*

[![brunnr](https://img.shields.io/badge/brunnr-skill-4ade80)](https://github.com/Peleke/brunnr)
[![Version](https://img.shields.io/badge/v1.0.0-e88072)](https://github.com/Peleke/brunnr/tree/main/skills/linwheel-content-engine)

</div>

---

> *You wrote the article. You shipped the feature. You have something worth saying. The last thing you want to do is spend 45 minutes formatting a LinkedIn post. So you don't, and the work goes unseen.*

---

## What this does

You have content — articles, braindumps, buildlog entries, conversation threads. **linwheel-content-engine** takes that content and runs it through LinWheel's MCP server to produce LinkedIn posts, carousels, images, and timed follow-up comments.

<div align="center">
<img src="https://raw.githubusercontent.com/Peleke/brunnr/main/skills/linwheel-content-engine/assets/flow.svg" alt="linwheel-content-engine flow: analyze → reshape → refine → visuals → schedule → comments" width="100%" />
</div>

---

## How it works

LinWheel is an MCP server (`@linwheel/mcp-server` on npm). This skill teaches your agent how to orchestrate its 22 tools in the right order:

| Stage | What happens | Tools used |
|-------|-------------|-----------|
| **Analyze** | Extract angles, hooks, and format fit from source | `linwheel_analyze` |
| **Reshape** | Transform into specific post angles | `linwheel_reshape`, `linwheel_split` |
| **Refine** | Polish the draft — hook, structure, language | `linwheel_draft`, `linwheel_refine` |
| **Visuals** | Generate images or carousel slides | `linwheel_post_image`, `linwheel_post_carousel` |
| **Schedule** | Approve and time the post | `linwheel_post_approve`, `linwheel_post_schedule` |
| **Comments** | Queue follow-up comments for engagement | `linwheel_post_comment` |

---

## Install

### Claude Code

```bash
# If you haven't added the brunnr marketplace yet
/plugin marketplace add Peleke/brunnr

# Install
/plugin install linwheel-content-engine@brunnr-skills
```

### CLI

```bash
# Install brunnr
uv tool install brunnr    # or: pipx install brunnr

# Install the skill
brunnr install linwheel-content-engine
```

### Prerequisites

LinWheel's MCP server must be configured. See the [setup guide](https://www.linwheel.io/docs/setup).

```json
{
  "mcpServers": {
    "linwheel": {
      "command": "npx",
      "args": ["-y", "@linwheel/mcp-server"],
      "env": {
        "LINWHEEL_API_KEY": "your-api-key"
      }
    }
  }
}
```

---

## Usage

### Quick start

```
Post this article to LinkedIn: [paste or link]
```

The skill handles the rest — analysis, draft, approval prompt, scheduling.

### With options

```
Make a carousel from this article, schedule for tomorrow 9 AM.
```

```
Reshape this as a hot take. Keep it under 200 words.
```

```
What's scheduled for this week?
```

### Example session

```
User: Post this to LinkedIn — [pastes buildlog entry about shipping a feature]

Agent: Analyzing your content...
  → Found 3 angles: "shipping story", "technical deep-dive", "lesson learned"
  → Best format: text post with image
  → Recommended: "shipping story" angle (highest engagement potential)

  Here's the draft:

  "We shipped [feature] yesterday. Here's what actually happened..."
  [full draft]

  Schedule this? I'd suggest tomorrow (Thursday) at 9 AM ET.

User: Yes, but tighten the hook.

Agent: Refining the hook...
  → "Everyone talks about building features. Nobody talks about the 3 AM rewrite
     that made it work."

  Better? If so, I'll generate an image and schedule.

User: Ship it.

Agent: Done.
  → Post scheduled: Thu Mar 14, 9:00 AM ET
  → Image generated and attached
  → Follow-up comment queued for 9:30 AM:
    "Full buildlog: [link]. The debug session in section 3 is the real story."
```

---

## The 22 tools

Organized by function:

- **Content creation** (6): draft, analyze, reshape, refine, split, bundle
- **Post management** (5): list, get, update, approve, schedule
- **Visual content** (7): image, carousel create/companion/compile/regenerate/schedule/delete
- **Comments** (4): add, list, update, delete

Plus voice profile and brand style management for consistency across posts.

---

## Further reading

- [LinWheel setup guide](https://www.linwheel.io/docs/setup)
- [brunnr](https://github.com/Peleke/brunnr) — the skills marketplace

---

*Security-scanned by [brunnr](https://github.com/Peleke/brunnr). Seven threat classes. Zero LLM in the gate.*
