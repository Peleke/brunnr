"""brunnr list — show installed skills."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from brunnr.lockfile import read_lockfile


def run(args) -> int:
    workdir = getattr(args, "workdir", ".")
    json_out = getattr(args, "json_out", False)

    lockdata = read_lockfile(workdir)
    skills = lockdata.get("skills", {})

    # Fallback: scan filesystem if lockfile is empty
    if not skills:
        skills_dir = Path(workdir) / "skills"
        if skills_dir.is_dir():
            for d in sorted(skills_dir.iterdir()):
                if d.is_dir() and (d / "SKILL.md").exists():
                    skills[d.name] = {
                        "installed_at": "unknown",
                        "source_hash": "—",
                        "scan_result": "unknown",
                    }

    if not skills:
        print("No skills installed.", file=sys.stderr)
        return 0

    if json_out:
        print(json.dumps({"skills": skills}, indent=2))
        return 0

    print(f"Installed skills ({Path(workdir).resolve() / 'skills'}):\n")
    for slug, meta in sorted(skills.items()):
        status = meta.get("scan_result", "unknown")
        date = meta.get("installed_at", "unknown")[:10]
        hash_prefix = meta.get("source_hash", "—")
        if hash_prefix.startswith("sha256:"):
            hash_prefix = hash_prefix[:15] + "…"
        print(f"  {slug:<20} {status:<10} {date:<12} {hash_prefix}")

    print(f"\n{len(skills)} skill(s) installed")
    return 0
