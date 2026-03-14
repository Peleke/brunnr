"""brunnr publish — publish a skill to the registry via PR."""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

from brunnr.frontmatter import parse_frontmatter
from brunnr.scanner import scan_skill_md


def run(args) -> int:
    skill_path = Path(args.path).expanduser().resolve()
    dry_run = getattr(args, "dry_run", False)

    # Validate skill directory
    if skill_path.is_file() and skill_path.name == "SKILL.md":
        skill_dir = skill_path.parent
        skill_file = skill_path
    elif skill_path.is_dir():
        skill_dir = skill_path
        skill_file = skill_path / "SKILL.md"
    else:
        print(f"ERROR: {skill_path} is not a skill directory or SKILL.md file.", file=sys.stderr)
        return 1

    if not skill_file.exists():
        print(f"ERROR: {skill_file} not found.", file=sys.stderr)
        return 1

    content = skill_file.read_text()
    fm = parse_frontmatter(content)
    slug = fm.get("name", skill_dir.name)

    print(f"Publishing {slug}...")

    # Step 1: scan
    print("  Running security scan...")
    scan = scan_skill_md(content)
    verdict = scan.get("verdict", "UNKNOWN")
    print(f"  Scan: {verdict}")

    if verdict == "BLOCK":
        print("ERROR: skill blocked by scanner. Fix findings before publishing.", file=sys.stderr)
        return 1
    if verdict == "FLAG":
        print("WARNING: skill has flagged findings. Proceeding with caution.", file=sys.stderr)

    if dry_run:
        print(f"\n  [dry-run] Would publish {slug} (scan: {verdict})")
        print(f"  [dry-run] SKILL.md: {len(content.splitlines())} lines")
        return 0

    # Step 2: fork + branch + push + PR via gh CLI
    registry = "Peleke/brunnr"
    branch = f"skill/{slug}"

    print(f"  Creating PR to {registry}...")
    try:
        # Fork (idempotent)
        subprocess.run(
            ["gh", "repo", "fork", registry, "--clone=false"],
            check=False, capture_output=True,
        )

        # Clone to temp, create branch, copy skill, push, PR
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp) / "brunnr"
            subprocess.run(
                ["gh", "repo", "clone", registry, str(tmp_path)],
                check=True, capture_output=True,
            )

            # Create branch
            subprocess.run(
                ["git", "checkout", "-b", branch],
                cwd=tmp_path, check=True, capture_output=True,
            )

            # Copy skill files
            dest = tmp_path / "skills" / slug
            dest.mkdir(parents=True, exist_ok=True)
            (dest / "SKILL.md").write_text(content)

            # Copy other files and subdirectories
            for extra in skill_dir.iterdir():
                if extra.name == "SKILL.md":
                    continue
                dest_extra = dest / extra.name
                if extra.is_dir():
                    shutil.copytree(extra, dest_extra, dirs_exist_ok=True)
                elif extra.is_file():
                    shutil.copy2(extra, dest_extra)

            # Commit and push
            subprocess.run(["git", "add", "."], cwd=tmp_path, check=True, capture_output=True)
            subprocess.run(
                ["git", "commit", "-m", f"feat: add {slug} skill"],
                cwd=tmp_path, check=True, capture_output=True,
            )
            subprocess.run(
                ["git", "push", "-u", "origin", branch],
                cwd=tmp_path, check=True, capture_output=True,
            )

            # Create PR
            result = subprocess.run(
                ["gh", "pr", "create",
                 "--repo", registry,
                 "--title", f"feat: add {slug} skill",
                 "--body", f"Skill `{slug}` published via `brunnr publish`.\n\nScan result: **{verdict}**"],
                cwd=tmp_path, check=True, capture_output=True, text=True,
            )
            pr_url = result.stdout.strip()
            print(f"  PR created: {pr_url}")

    except FileNotFoundError:
        print("ERROR: `gh` CLI not found. Install: https://cli.github.com/", file=sys.stderr)
        return 1
    except subprocess.CalledProcessError as e:
        print(f"ERROR: git/gh command failed: {e.stderr}", file=sys.stderr)
        return 1

    print(f"\nPublished {slug}!")
    return 0
