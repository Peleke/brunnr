"""brunnr pipeline — full scan + eval orchestration."""

from __future__ import annotations

import sys
from pathlib import Path

from brunnr.scanner import Severity, scan_skill_md
from brunnr.discovery import discover_skill_files


def run(args) -> int:
    verbose = getattr(args, "verbose", False)
    scan_only = getattr(args, "scan_only", False)

    print("=== brunnr pipeline ===\n")

    # Step 1: Security scan
    print("Step 1: Security scan...")
    files = discover_skill_files()

    if not files:
        print("No SKILL.md files found.", file=sys.stderr)
        return 1

    has_block = False
    has_flag = False

    for path in files:
        content = path.read_text(encoding="utf-8")
        result = scan_skill_md(content)

        status = result.severity.value.upper()
        print(f"  {status}  {path.name}")

        if verbose and result.findings:
            for f in result.findings:
                print(f"         [{f.threat_class}] {f.description}")

        if result.blocked:
            has_block = True
        if result.flagged:
            has_flag = True

    if has_block:
        print("\nPipeline FAILED: blocked findings detected.")
        return 1

    print(f"\nScan passed ({len(files)} files).")

    if scan_only:
        print("Done (scan-only mode).")
        return 0

    # Step 2: Discover and run evals
    print("\nStep 2: Skill evaluations...")
    tests_dir = Path.cwd() / "tests"
    skills_dir = Path.cwd() / "skills"

    eval_slugs = []
    if tests_dir.exists():
        for spec in sorted(tests_dir.rglob("test-spec.json")):
            slug = spec.parent.name
            if (skills_dir / slug / "SKILL.md").exists():
                eval_slugs.append(slug)

    if not eval_slugs:
        print("  No evaluable skills found.")
        print("\nPipeline complete.")
        return 0

    from brunnr.commands.eval import run as run_eval
    from argparse import Namespace

    any_failed = False
    for slug in eval_slugs:
        eval_args = Namespace(
            skill=slug,
            model=getattr(args, "model", "claude-sonnet-4-20250514"),
            output=f"tests/{slug}/results.json",
            dry_run=False,
        )
        if run_eval(eval_args) != 0:
            any_failed = True

    if any_failed:
        print("\nPipeline FAILED: eval failures detected.")
        return 1

    print("\nPipeline complete.")
    return 0
