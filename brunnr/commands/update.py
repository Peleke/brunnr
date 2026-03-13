"""brunnr update — update installed skills to latest."""

from __future__ import annotations

import sys
from pathlib import Path

from brunnr.registry import fetch, registry_base, fetch_skill_content
from brunnr.lockfile import read_lockfile, add_skill, content_hash
from brunnr.scanner import scan_skill_md


def run(args) -> int:
    base = registry_base(args.registry)
    target_slug = getattr(args, "skill", None)
    dry_run = getattr(args, "dry_run", False)
    force = getattr(args, "force", False)

    lockdata = read_lockfile(".")
    skills = lockdata.get("skills", {})

    if not skills:
        print("No skills in lockfile. Run `brunnr list` to check.", file=sys.stderr)
        return 0

    slugs = [target_slug] if target_slug else sorted(skills.keys())
    updated = 0

    for slug in slugs:
        local_meta = skills.get(slug)
        if not local_meta:
            print(f"  {slug}: not installed, skipping", file=sys.stderr)
            continue

        local_hash = local_meta.get("source_hash", "")

        # Fetch latest from registry
        content = fetch_skill_content(base, slug)
        if content is None:
            print(f"  {slug}: not found in registry, skipping")
            continue

        remote_hash = content_hash(content)

        if local_hash == remote_hash:
            print(f"  {slug}: up to date")
            continue

        # Run scanner on new content
        scan = scan_skill_md(content)
        verdict = scan.get("verdict", "UNKNOWN")
        if verdict == "BLOCK":
            print(f"  {slug}: BLOCKED by scanner — skipping update", file=sys.stderr)
            continue

        if dry_run:
            print(f"  {slug}: update available ({local_hash[:15]}… → {remote_hash[:15]}…) [scan: {verdict}]")
            updated += 1
            continue

        # Prompt unless --force
        if not force and sys.stdin.isatty():
            try:
                answer = input(f"  Update {slug}? (scan: {verdict}) [y/N] ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print("\nAborted.", file=sys.stderr)
                return 1
            if answer not in ("y", "yes"):
                print(f"  {slug}: skipped")
                continue

        # Write updated SKILL.md
        skill_file = Path("skills") / slug / "SKILL.md"
        skill_file.parent.mkdir(parents=True, exist_ok=True)
        skill_file.write_text(content)

        # Update lockfile
        registry = local_meta.get("registry", "https://github.com/Peleke/brunnr")
        add_skill(".", slug, content, registry, scan_result=verdict.lower())

        print(f"  {slug}: updated ({verdict})")
        updated += 1

    action = "would update" if dry_run else "updated"
    print(f"\n{updated} skill(s) {action}")
    return 0
