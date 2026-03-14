"""brunnr install — fetch skills from the registry."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from brunnr.registry import fetch, registry_base, list_skills, repo_parts, list_directory
from brunnr.lockfile import add_skill


def run(args) -> int:
    base = registry_base(args.registry)

    # List mode
    if getattr(args, "list_skills", False):
        skills = list_skills(base)
        if not skills:
            print("No skills found (or registry unreachable).", file=sys.stderr)
            return 1
        print("Available skills:")
        for s in skills:
            print(f"  - {s}")
        return 0

    slug = args.skill
    if not slug:
        print("ERROR: skill name required. Use `brunnr install --list` to see available skills.", file=sys.stderr)
        return 1

    # When --target is set, install SKILL.md only (runtime use, not repo structure)
    target = getattr(args, "target", None)
    if target:
        dest = Path(target).expanduser() / slug
        skill_file = dest / "SKILL.md"
    else:
        dest = Path("skills") / slug
        skill_file = dest / "SKILL.md"

    if skill_file.exists() and not getattr(args, "force", False):
        print(f"Skill '{slug}' already installed at {skill_file}", file=sys.stderr)
        print("Use --force to overwrite.", file=sys.stderr)
        return 1

    # Fetch SKILL.md
    skill_url = f"{base}/skills/{slug}/SKILL.md"
    print(f"Fetching {slug} from {args.registry}...")
    content = fetch(skill_url)
    if not content:
        print(f"ERROR: Could not fetch {skill_url}", file=sys.stderr)
        return 1

    # Review before install (unless --yes)
    skip_review = getattr(args, "yes", False) or getattr(args, "force", False)
    if not skip_review and sys.stdin.isatty():
        lines = content.splitlines()
        preview = "\n".join(lines[:30])
        print(f"\n--- {slug}/SKILL.md (first 30 of {len(lines)} lines) ---")
        print(preview)
        if len(lines) > 30:
            print(f"  ... ({len(lines) - 30} more lines)")
        print("---")
        rp = repo_parts(base)
        if len(rp) >= 2:
            print(f"\nFull source: https://github.com/{rp[0]}/{rp[1]}/tree/main/skills/{slug}")
        try:
            answer = input(f"\nInstall {slug} to {dest}/? [y/N] ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nAborted.", file=sys.stderr)
            return 1
        if answer not in ("y", "yes"):
            print("Aborted.", file=sys.stderr)
            return 1

    dest.mkdir(parents=True, exist_ok=True)
    skill_file.write_text(content)
    print(f"  -> {skill_file} ({len(content.splitlines())} lines)")

    # Fetch references/ (optional)
    refs_entries = list_directory(base, f"skills/{slug}/references")
    ref_files_installed: list[str] = []
    if refs_entries and isinstance(refs_entries, list):
        ref_dest = dest / "references"
        ref_dest.mkdir(parents=True, exist_ok=True)
        for entry in refs_entries:
            if not isinstance(entry, dict):
                continue
            if entry.get("type") == "file" and entry.get("download_url"):
                ref_content = fetch(entry["download_url"])
                if ref_content:
                    ref_path = ref_dest / entry["name"]
                    ref_path.write_text(ref_content)
                    ref_files_installed.append(
                        f"skills/{slug}/references/{entry['name']}"
                    )
                    print(f"  -> references/{entry['name']}")
            elif entry.get("type") == "dir" and entry.get("path"):
                # One level of nesting (e.g., references/themes/)
                sub_entries = list_directory(base, entry["path"])
                if sub_entries and isinstance(sub_entries, list):
                    sub_dest = ref_dest / entry["name"]
                    sub_dest.mkdir(parents=True, exist_ok=True)
                    for sub in sub_entries:
                        if (
                            isinstance(sub, dict)
                            and sub.get("type") == "file"
                            and sub.get("download_url")
                        ):
                            sub_content = fetch(sub["download_url"])
                            if sub_content:
                                sub_path = sub_dest / sub["name"]
                                sub_path.write_text(sub_content)
                                ref_files_installed.append(
                                    f"skills/{slug}/references/{entry['name']}/{sub['name']}"
                                )
                                print(
                                    f"  -> references/{entry['name']}/{sub['name']}"
                                )

    # When --target is set, skip schema/test/lockfile (runtime-only install)
    if target:
        print(f"\nInstalled {slug} to {dest}/")
        return 0

    # Auto-install shared conventions if this skill references them
    if "_conventions.md" in content:
        conventions_path = Path("skills") / "_conventions.md"
        if not conventions_path.exists():
            conv_url = f"{base}/skills/_conventions.md"
            conv_content = fetch(conv_url)
            if conv_content:
                conventions_path.parent.mkdir(parents=True, exist_ok=True)
                conventions_path.write_text(conv_content)
                print("  -> skills/_conventions.md (shared conventions)")

    # Fetch schema (optional)
    schema_url = f"{base}/schemas/{slug}/output.schema.json"
    schema_content = fetch(schema_url)
    if schema_content:
        schema_dest = Path("schemas") / slug
        schema_dest.mkdir(parents=True, exist_ok=True)
        (schema_dest / "output.schema.json").write_text(schema_content)
        print(f"  -> schemas/{slug}/output.schema.json")

    # Fetch test fixtures (optional)
    if getattr(args, "with_tests", False):
        spec_url = f"{base}/tests/{slug}/test-spec.json"
        spec_content = fetch(spec_url)
        if spec_content:
            test_dest = Path("tests") / slug
            test_dest.mkdir(parents=True, exist_ok=True)
            (test_dest / "test-spec.json").write_text(spec_content)
            print(f"  -> tests/{slug}/test-spec.json")

            # Fetch fixtures referenced in spec
            spec = json.loads(spec_content)
            for case in spec.get("cases", []):
                fixture_rel = case.get("fixture", "")
                if not fixture_rel:
                    continue
                # Sanitize: reject path traversal and absolute paths
                if ".." in fixture_rel or fixture_rel.startswith("/"):
                    print(f"  WARNING: skipping suspicious fixture path: {fixture_rel}", file=sys.stderr)
                    continue
                fixture_path = (test_dest / fixture_rel).resolve()
                if not fixture_path.is_relative_to(test_dest.resolve()):
                    print(f"  WARNING: fixture escapes test dir: {fixture_rel}", file=sys.stderr)
                    continue
                fixture_url = f"{base}/tests/{slug}/{fixture_rel}"
                fixture_content = fetch(fixture_url)
                if fixture_content:
                    fixture_path.parent.mkdir(parents=True, exist_ok=True)
                    fixture_path.write_text(fixture_content)
                    print(f"  -> tests/{slug}/{fixture_rel}")

    # Update lockfile
    installed_files = [f"skills/{slug}/SKILL.md"]
    installed_files.extend(ref_files_installed)
    if schema_content:
        installed_files.append(f"schemas/{slug}/output.schema.json")
    add_skill(".", slug, content, args.registry, files=installed_files)

    print(f"\nInstalled {slug} to ./{dest}/")
    print(f"\nTip: Run `brunnr eval {slug} --dry-run` to validate locally.")
    return 0
