"""Guard against committing local machine details to this public repo.

Fails if any tracked file contains an absolute home-directory path, an
iCloud/Obsidian vault path, or a raw Claude Code session transcript line.
Runs in CI on every pull request (see .github/workflows/test-skills.yml).
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SELF = Path(__file__).resolve().relative_to(REPO).as_posix()

PATTERNS = {
    "macOS home path": re.compile(r"/Users/[a-z][a-z0-9_-]+/"),
    "Linux home path": re.compile(r"/home/(?!runner/)[a-z][a-z0-9_-]+/"),
    "iCloud vault path": re.compile(r"Mobile Documents/iCloud~"),
    "session transcript": re.compile(r'"parentUuid"\s*:'),
}


def tracked_text_files() -> list[Path]:
    out = subprocess.run(
        ["git", "ls-files", "-z"], cwd=REPO, check=True, capture_output=True
    ).stdout.decode()
    return [REPO / p for p in out.split("\0") if p and p != SELF]


def test_no_local_details_in_tracked_files() -> None:
    hits: list[str] = []
    for path in tracked_text_files():
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, FileNotFoundError):
            continue
        for lineno, line in enumerate(text.splitlines(), 1):
            for label, pattern in PATTERNS.items():
                if pattern.search(line):
                    rel = path.relative_to(REPO).as_posix()
                    hits.append(f"{rel}:{lineno}: {label}")
    assert not hits, "Local details found in tracked files:\n" + "\n".join(hits)
