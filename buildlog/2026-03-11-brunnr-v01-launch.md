# Build Journal: brunnr v0.1 — Scanner, CLI, Docs, Marketplace

**Date:** 2026-03-11
**Duration:** ~6 hours (across two sessions)

## What I Did

Shipped brunnr v0.1: a complete foundation for agent skill security scanning and distribution. From a standalone scanner script to a full Python package with 4 subcommands (scan, install, eval, pipeline), a 14-page MkDocs documentation site, and a Claude Code plugin marketplace.

Parallel track: shipped Skillipedia UI overhaul (Falun Red + Ink + Parchment design system, dark mode, typography, collapsible install instructions showing both marketplace and CLI paths).

### Deliverables

- **7-class security scanner**: command injection, data exfiltration, credential theft, prompt override, supply chain, privilege escalation, steganographic + semantic mismatch. 55 tests, 0 false positives.
- **CLI restructure**: `brunnr scan/install/eval/pipeline` with argparse subcommands, review-before-install flow, `--yes`/`--force` flags.
- **Eval harness**: 7 assertion types (score_range, has_table, has_rewrite, contains, criteria_pass/fail, format_valid). Dry-run mode for CI.
- **MkDocs docs site**: ReadTheDocs theme, GitHub Pages deployment workflow, inline SVG architecture diagrams.
- **Claude Code plugin marketplace**: `.claude-plugin/marketplace.json`, proper plugin manifests, symlinked skill structure for slash command discovery.
- **Skillipedia updates**: consolidated ax-rubric (8 fragments → 1), collapsible install box with marketplace + CLI paths, clean card excerpts.

### Issues Filed

- #10: Zero-Trust Skill Remix — regenerate foreign skills from intent
- #11: CLI parity with ClawHub — search, list, inspect, update, explore, publish, sync

## What Went Wrong

1. **pluginRoot + source double-pathing**: Set `pluginRoot: "./skills"` and `source: "./skills/ax-rubric"`, which resolved to `./skills/skills/ax-rubric`. The docs say pluginRoot is *prepended* to source. Fixed by changing source to just `"ax-rubric"`.

2. **Module-level Path.cwd()**: eval.py computed `SKILLS_DIR = Path.cwd() / "skills"` at import time. If imported from a different CWD (e.g., via pipeline or test harness), paths would be wrong. Fixed by converting to functions that compute at call time.

3. **Path traversal in fixture downloads**: install.py used `fixture_rel` from untrusted JSON directly in path construction. A malicious test-spec.json could write to arbitrary locations. Fixed with `..` rejection + resolve() containment check.

4. **__pycache__ committed**: Forgot .gitignore before first commit of the package. Cleaned up in follow-up commit.

## What I Learned

- Claude Code's plugin system expects skills at `<plugin-root>/skills/<name>/SKILL.md` for slash command naming. The directory name becomes the command name.
- `pluginRoot` in marketplace.json is prepended to source paths — it's a convenience to avoid repeating a base directory, not a search path.
- Symlinks within plugin directories are followed during Claude Code's copy-to-cache step, so you can maintain two path conventions (brunnr CLI at root, Claude Code in nested `skills/` dir) without duplication.
- `uv tool install` is the recommended way to install Python CLI tools (isolated environment, no PEP 668 issues).

## Improvements

- Gauntlet caught a critical path traversal bug before it shipped to users — validates the review loop.
- Parallel agent execution (docs site + CLI parity plan + zero-trust issue) saved significant time.
- The review-before-install default (show preview, prompt for confirmation) is a strong UX pattern for security-sensitive tools.

## Next Steps

- Publish to PyPI (need CI/CD workflow, look at qortex's setup)
- End-to-end test: `uv tool install brunnr && brunnr install ax-rubric`
- End-to-end test: `/plugin marketplace add Peleke/brunnr && /plugin install ax-rubric@brunnr-skills`
- Merge PR #3 to main (triggers docs deployment + Skillipedia rebuild)
