#!/usr/bin/env python3
"""Step 0: Deterministic security scan of all SKILL.md files.

Runs the 7-class scanner against every skills/*/SKILL.md in the repo.
No API calls — pure regex + keyword analysis.

Usage:
    python tests/scan-all-skills.py                           # Scan all skills
    python tests/scan-all-skills.py skills/ax-rubric/SKILL.md # Scan specific file
    python tests/scan-all-skills.py --json                    # JSON output
    python tests/scan-all-skills.py --strict                  # Fail on FLAG too
    python tests/scan-all-skills.py --fidelity                # Round-trip parse check
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Resolve repo root and ensure scanner is importable
REPO_ROOT = Path(__file__).resolve().parent.parent
TESTS_DIR = REPO_ROOT / "tests"
SKILLS_DIR = REPO_ROOT / "skills"
ARTIFACTS_DIR = TESTS_DIR / "artifacts"

sys.path.insert(0, str(REPO_ROOT))

from tests.scanner.scan import Severity, scan_skill_md

# ---------------------------------------------------------------------------
# Terminal colors (ANSI, degrades gracefully when piped)
# ---------------------------------------------------------------------------

_USE_COLOR = sys.stdout.isatty()


def _c(code: str, text: str) -> str:
    if not _USE_COLOR:
        return text
    return f"\033[{code}m{text}\033[0m"


def _green(t: str) -> str:
    return _c("32", t)


def _yellow(t: str) -> str:
    return _c("33", t)


def _red(t: str) -> str:
    return _c("31", t)


def _bold(t: str) -> str:
    return _c("1", t)


def _severity_color(sev: str, text: str) -> str:
    if sev == Severity.BLOCK:
        return _red(text)
    if sev == Severity.FLAG:
        return _yellow(text)
    if sev == Severity.INFO:
        return _yellow(text)
    return _green(text)


# ---------------------------------------------------------------------------
# File discovery
# ---------------------------------------------------------------------------


def discover_skill_files(paths: list[str]) -> list[Path]:
    """Return SKILL.md paths from explicit args or by scanning skills/."""
    files: list[Path] = []

    if paths:
        for p in paths:
            path = Path(p)
            if path.is_file() and path.name == "SKILL.md":
                files.append(path.resolve())
            elif path.is_dir():
                files.extend(sorted(path.rglob("SKILL.md")))
            else:
                print(f"WARNING: skipping {p} (not a SKILL.md file or directory)", file=sys.stderr)
    else:
        # Default: scan all skills/*/SKILL.md
        files = sorted(SKILLS_DIR.rglob("SKILL.md"))

    return files


# ---------------------------------------------------------------------------
# Fidelity check (optional, requires qortex)
# ---------------------------------------------------------------------------


def run_fidelity_check(path: Path, content: str) -> dict | None:
    """Round-trip parse -> render -> re-parse -> compare.

    Returns a dict with fidelity results, or None if qortex isn't installed.
    """
    try:
        from qortex.projectors.skillmd import parse_skill_md, render_skill_md
    except ImportError:
        return None

    try:
        parsed_1 = parse_skill_md(content)
        rendered = render_skill_md(parsed_1)
        parsed_2 = parse_skill_md(rendered)

        # Compare the two parsed results semantically
        d1 = parsed_1 if isinstance(parsed_1, dict) else vars(parsed_1) if hasattr(parsed_1, "__dict__") else str(parsed_1)
        d2 = parsed_2 if isinstance(parsed_2, dict) else vars(parsed_2) if hasattr(parsed_2, "__dict__") else str(parsed_2)

        match = d1 == d2
        return {
            "file": str(path),
            "match": match,
            "detail": None if match else "parsed structures differ after round-trip",
        }
    except Exception as exc:
        return {
            "file": str(path),
            "match": False,
            "detail": f"error: {exc}",
        }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Deterministic security scan of SKILL.md files."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="Specific SKILL.md files or directories to scan (default: all skills/*/SKILL.md)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        dest="json_output",
        help="Machine-readable JSON output",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit non-zero on FLAG (not just BLOCK)",
    )
    parser.add_argument(
        "--fidelity",
        action="store_true",
        help="Run round-trip parse fidelity check (requires qortex)",
    )
    args = parser.parse_args()

    files = discover_skill_files(args.paths)

    if not files:
        print("No SKILL.md files found.", file=sys.stderr)
        return 1

    # --- Scan ---
    results: list[dict] = []
    has_block = False
    has_flag = False

    for path in files:
        content = path.read_text(encoding="utf-8")
        result = scan_skill_md(content)

        # Relative path for display
        try:
            display_path = str(path.relative_to(REPO_ROOT))
        except ValueError:
            display_path = str(path)

        entry = {
            "file": display_path,
            **result.to_dict(),
        }
        results.append(entry)

        if result.blocked:
            has_block = True
        if result.flagged:
            has_flag = True

    # --- Fidelity (optional) ---
    fidelity_results: list[dict] = []
    fidelity_available = True

    if args.fidelity:
        try:
            from qortex.projectors.skillmd import parse_skill_md as _check  # noqa: F401
        except ImportError:
            fidelity_available = False

        if fidelity_available:
            for path in files:
                content = path.read_text(encoding="utf-8")
                fid = run_fidelity_check(path, content)
                if fid is not None:
                    try:
                        fid["file"] = str(path.relative_to(REPO_ROOT))
                    except ValueError:
                        pass
                    fidelity_results.append(fid)

    # --- Report artifact ---
    ARTIFACTS_DIR.mkdir(exist_ok=True)
    report = {
        "total": len(results),
        "blocked": sum(1 for r in results if r["blocked"]),
        "flagged": sum(1 for r in results if r["flagged"]),
        "clean": sum(1 for r in results if r["severity"] == Severity.CLEAN),
        "skills": results,
    }
    if args.fidelity:
        report["fidelity"] = {
            "available": fidelity_available,
            "results": fidelity_results,
        }

    artifact_path = ARTIFACTS_DIR / "scan-report.json"
    artifact_path.write_text(json.dumps(report, indent=2) + "\n")

    # --- Output ---
    if args.json_output:
        print(json.dumps(report, indent=2))
    else:
        print(_bold("=== SKILL.md Security Scan ==="))
        print()

        for entry in results:
            sev = entry["severity"]
            label = _severity_color(sev, sev.upper())
            print(f"  {label}  {entry['file']}")

            if entry["findings"]:
                for f in entry["findings"]:
                    marker = _red("BLOCK") if f["severity"] == Severity.BLOCK else (
                        _yellow("FLAG") if f["severity"] == Severity.FLAG else "INFO"
                    )
                    print(f"         {marker}: {f['description']}")
                    if f["evidence"]:
                        print(f"                evidence: {f['evidence'][:80]}")

        print()
        print(
            f"  {report['total']} scanned, "
            f"{_red(str(report['blocked']) + ' blocked') if report['blocked'] else _green('0 blocked')}, "
            f"{_yellow(str(report['flagged']) + ' flagged') if report['flagged'] else '0 flagged'}, "
            f"{_green(str(report['clean']) + ' clean') if report['clean'] else '0 clean'}"
        )

        # Fidelity summary
        if args.fidelity and not fidelity_available:
            print()
            print(f"  {_yellow('SKIP')}: qortex not installed (pip install qortex)")
        elif args.fidelity and fidelity_results:
            print()
            print(_bold("=== Fidelity Check ==="))
            for fid in fidelity_results:
                status = _green("PASS") if fid["match"] else _red("FAIL")
                print(f"  {status}  {fid['file']}")
                if not fid["match"] and fid.get("detail"):
                    print(f"         {fid['detail']}")

        print()
        print(f"  Report: {artifact_path.relative_to(REPO_ROOT)}")

    # --- Exit code ---
    if has_block:
        return 1
    if args.strict and has_flag:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
