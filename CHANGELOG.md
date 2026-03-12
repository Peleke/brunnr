# Changelog

All notable changes to brunnr will be documented in this file.

## [Unreleased]

## [0.1.0] - 2026-03-11

### Added
- `brunnr scan` — pattern-based security scanner for agent tool descriptions (SKILL.md files)
- `brunnr install` — fetch and install skills from the brunnr registry with review-before-install
- `brunnr eval` — LLM-graded evaluation of tool descriptions against the ax-rubric
- `brunnr pipeline` — combined scan + eval in a single pass
- 26 built-in scan rules across 5 categories (prompt-injection, over-privilege, data-leak, ambiguity, missing-constraint)
- `ax-rubric` skill — score tool descriptions 0-5 on discoverability
- Claude Code plugin marketplace support (`.claude-plugin/marketplace.json`)
- Path traversal protection in install command
- MkDocs documentation site with ReadTheDocs theme
- PyPI publishing via OIDC trusted publisher (tag-triggered)
- GitHub Release with auto-generated changelog on tag push
- 74 tests (55 scanner + 19 CLI)

[Unreleased]: https://github.com/Peleke/brunnr/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/Peleke/brunnr/releases/tag/v0.1.0
