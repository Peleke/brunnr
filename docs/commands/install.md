# brunnr install

Install skills from the brunnr registry. By default, brunnr shows you the skill content before installing so you can review it.

---

## Usage

```bash
brunnr install <skill> [--registry URL] [--with-tests] [--force] [--list] [-y]
```

---

## Arguments

| Argument | Description |
|----------|-------------|
| `skill` | Skill slug to install (e.g., `ax-rubric`). Required unless using `--list`. |

## Flags

| Flag | Short | Description |
|------|-------|-------------|
| `--registry` | | Registry URL. Default: `https://github.com/Peleke/brunnr` |
| `--with-tests` | | Also fetch test fixtures from `tests/<slug>/` |
| `--force` | | Overwrite an existing skill without prompting |
| `--list` | | List available skills in the registry |
| `--yes` | `-y` | Skip the review prompt and install immediately |

---

## How it works

### 1. Fetch the skill

brunnr fetches `SKILL.md` from the registry's GitHub raw content URL:

```
https://raw.githubusercontent.com/{owner}/{repo}/main/skills/{slug}/SKILL.md
```

### 2. Review before install

Unless `--yes` or `--force` is set, brunnr shows you the first 30 lines of the SKILL.md and provides a link to the full source on GitHub. You must type `y` to proceed.

```
--- ax-rubric/SKILL.md (first 30 of 142 lines) ---
---
name: ax-rubric
description: Score agent-facing tool descriptions against the AX Description Rubric...
---

# AX Description Rubric - Tool Description Reviewer

You are an agent experience (AX) reviewer...
  ... (22 more lines)

Full source: https://github.com/Peleke/brunnr/tree/main/skills/ax-rubric

Install ax-rubric to ./skills/ax-rubric/? [y/N]
```

!!! warning "Review your skills"
    The review step exists for a reason. Third-party skills run as system prompts inside your agent. A malicious skill could instruct the agent to exfiltrate data, ignore safety guidelines, or execute dangerous commands. Always read before installing.

### 3. Write files

brunnr writes the skill to `./skills/<slug>/SKILL.md` relative to your current directory. It also checks for an optional JSON schema at `schemas/<slug>/output.schema.json` in the registry.

### 4. Fetch test fixtures (optional)

With `--with-tests`, brunnr also fetches:

- `tests/<slug>/test-spec.json` -- The test specification
- Any fixture files referenced in the spec's `cases[].fixture` field

---

## Where files go

```
your-project/
  skills/
    ax-rubric/
      SKILL.md              # The skill prompt
  schemas/
    ax-rubric/
      output.schema.json    # Optional output schema
  tests/
    ax-rubric/
      test-spec.json        # Test specification (with --with-tests)
      fixtures/
        bad-description.json
        good-description.json
```

---

## Examples

### List available skills

```bash
brunnr install --list
```

```
Available skills:
  - ax-rubric
```

### Install a skill with review

```bash
brunnr install ax-rubric
```

### Install without review

```bash
brunnr install ax-rubric -y
```

### Install with test fixtures

```bash
brunnr install ax-rubric --with-tests
```

```
Fetching ax-rubric from https://github.com/Peleke/brunnr...
  -> skills/ax-rubric/SKILL.md (142 lines)
  -> schemas/ax-rubric/output.schema.json
  -> tests/ax-rubric/test-spec.json
  -> tests/ax-rubric/fixtures/bad-description.json
  -> tests/ax-rubric/fixtures/good-description.json

Installed ax-rubric to ./skills/ax-rubric/

Tip: Run `brunnr eval ax-rubric --dry-run` to validate locally.
```

### Overwrite an existing skill

```bash
brunnr install ax-rubric --force
```

### Use a custom registry

```bash
brunnr install my-skill --registry https://github.com/myorg/my-skills
```

The registry URL must point to a GitHub repository with skills in a `skills/` directory.

---

## Exit codes

| Code | Meaning |
|------|---------|
| `0` | Skill installed successfully |
| `1` | Error: skill not found, already installed (without `--force`), user aborted, or registry unreachable |
