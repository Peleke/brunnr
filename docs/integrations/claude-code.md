# Claude Code Integration

brunnr skills work as custom slash commands in [Claude Code](https://docs.anthropic.com/en/docs/claude-code). Install a skill, and it becomes a command your agent can invoke.

---

## How it works

Claude Code supports custom slash commands through Markdown files in specific directories. brunnr skills are SKILL.md files -- Markdown documents with YAML frontmatter that serve as system prompts.

When you install a skill with `brunnr install`, it writes the SKILL.md to `skills/<slug>/SKILL.md`. To use it as a Claude Code slash command, you can either:

1. **Reference it directly** -- Point Claude Code at the skill file.
2. **Copy to Claude Code's command directory** -- Place it where Claude Code discovers custom commands.

---

## Setup

### Option 1: Project-level commands

Copy or symlink installed skills to your project's `.claude/commands/` directory:

```bash
# Install the skill
brunnr install ax-rubric

# Create the commands directory
mkdir -p .claude/commands

# Symlink or copy
cp skills/ax-rubric/SKILL.md .claude/commands/ax-rubric.md
```

Now you can use it in Claude Code:

```
/ax-rubric "Query the knowledge base for structured learnings."
```

### Option 2: Global commands

For skills you want available across all projects, use Claude Code's global command directory:

```bash
mkdir -p ~/.claude/commands
cp skills/ax-rubric/SKILL.md ~/.claude/commands/ax-rubric.md
```

---

## Workflow

The typical workflow combines brunnr's security scanning with Claude Code's skill execution:

### 1. Browse and install

```bash
# List available skills
brunnr install --list

# Install with review
brunnr install ax-rubric
```

### 2. Scan before using

```bash
# Always scan skills before giving them to your agent
brunnr scan skills/ax-rubric/SKILL.md
```

```
=== brunnr scan ===

  CLEAN  SKILL

  Scanned 1 files: 1 clean, 0 flagged, 0 blocked
```

### 3. Deploy to Claude Code

```bash
cp skills/ax-rubric/SKILL.md .claude/commands/ax-rubric.md
```

### 4. Use in your agent session

```
/ax-rubric
```

---

## Security considerations

!!! warning "Scan before you deploy"
    A SKILL.md file becomes a system prompt for your agent. If it contains malicious instructions (prompt overrides, credential theft patterns, data exfiltration commands), the agent will follow them. Always run `brunnr scan` before deploying a skill to Claude Code.

### Defense in depth

1. **brunnr scan** catches known attack patterns (7+1 threat classes)
2. **Review-before-install** lets you read the skill content before writing it to disk
3. **brunnr eval** validates that the skill produces expected output
4. **Manual review** remains essential for novel attack patterns the scanner hasn't seen

---

## Writing skills for Claude Code

When writing skills intended for Claude Code, keep these points in mind:

- **Use standard Markdown** -- Claude Code renders the skill as a system prompt. Stick to headers, lists, tables, and code blocks.
- **Be explicit about phases** -- Sequential instructions work better than unstructured prose.
- **Specify the output format** -- Tell the agent exactly what to produce (tables, scores, rewrites, etc.).
- **Include trigger conditions** -- "Use when reviewing tool descriptions" is better than "use when relevant."

See [Writing Skills](../skills/writing-skills.md) for the full guide.
