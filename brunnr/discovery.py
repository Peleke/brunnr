"""Skill file discovery for scanning and evaluation."""

from __future__ import annotations

import sys
from pathlib import Path


def discover_skill_files(
    paths: list[str] | None = None,
    skills_dir: Path | None = None,
) -> list[Path]:
    """Return SKILL.md paths from explicit args or by scanning skills_dir/.

    Args:
        paths: Explicit files or directories to scan.
        skills_dir: Base skills directory (default: ./skills/).

    Returns:
        List of resolved SKILL.md paths.
    """
    if skills_dir is None:
        skills_dir = Path.cwd() / "skills"

    files: list[Path] = []

    if paths:
        for p in paths:
            path = Path(p)
            if path.is_file():
                files.append(path.resolve())
            elif path.is_dir():
                files.extend(sorted(path.rglob("SKILL.md")))
            else:
                print(f"WARNING: skipping {p} (not found)", file=sys.stderr)
    else:
        if skills_dir.exists():
            files = sorted(skills_dir.rglob("SKILL.md"))

    return files


def collect_scan_files(paths: list[str]) -> list[Path]:
    """Collect .md files for scanning (more permissive than discover_skill_files).

    Accepts any .md file, not just SKILL.md. Used by `brunnr scan`.
    """
    files: list[Path] = []
    for p in paths:
        path = Path(p)
        if path.is_file():
            files.append(path)
        elif path.is_dir():
            files.extend(sorted(path.rglob("*.md")))
        else:
            print(f"WARNING: {p} not found", file=sys.stderr)
    return files
