"""Lockfile management for installed brunnr skills."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

LOCKFILE_NAME = "skills.lock.json"


def _lockfile_path(workdir: str | Path = ".") -> Path:
    return Path(workdir) / LOCKFILE_NAME


def read_lockfile(workdir: str | Path = ".") -> dict:
    """Read the lockfile. Returns empty structure if missing."""
    path = _lockfile_path(workdir)
    if not path.exists():
        return {"version": 1, "skills": {}}
    return json.loads(path.read_text())


def write_lockfile(workdir: str | Path, data: dict) -> None:
    """Write the lockfile."""
    path = _lockfile_path(workdir)
    path.write_text(json.dumps(data, indent=2) + "\n")


def add_skill(
    workdir: str | Path,
    slug: str,
    content: str,
    registry: str,
    scan_result: str = "unknown",
    files: list[str] | None = None,
) -> None:
    """Add or update a skill entry in the lockfile."""
    data = read_lockfile(workdir)
    data["skills"][slug] = {
        "installed_at": datetime.now(timezone.utc).isoformat(),
        "source_hash": "sha256:" + hashlib.sha256(content.encode()).hexdigest()[:16],
        "registry": registry,
        "scan_result": scan_result,
        "files": files or [f"skills/{slug}/SKILL.md"],
    }
    write_lockfile(workdir, data)


def remove_skill(workdir: str | Path, slug: str) -> bool:
    """Remove a skill from the lockfile. Returns True if it existed."""
    data = read_lockfile(workdir)
    if slug in data["skills"]:
        del data["skills"][slug]
        write_lockfile(workdir, data)
        return True
    return False


def content_hash(content: str) -> str:
    """Compute the sha256 hash prefix used in lockfile entries."""
    return "sha256:" + hashlib.sha256(content.encode()).hexdigest()[:16]
