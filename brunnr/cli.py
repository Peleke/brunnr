"""brunnr CLI — subcommand dispatcher."""

from __future__ import annotations

import argparse
import sys

from brunnr import __version__


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="brunnr",
        description="Security scanner and skill registry for agent tool descriptions.",
    )
    parser.add_argument("--version", action="version", version=f"brunnr {__version__}")
    sub = parser.add_subparsers(dest="command")

    # --- brunnr scan ---
    scan_p = sub.add_parser("scan", help="Scan SKILL.md files for security threats")
    scan_p.add_argument("paths", nargs="*", default=None, help="Files or directories to scan (default: skills/)")
    scan_p.add_argument("-v", "--verbose", action="store_true", help="Show finding details")
    scan_p.add_argument("--json", action="store_true", dest="json_out", help="JSON output")
    scan_p.add_argument("--strict", action="store_true", help="Fail on FLAG (not just BLOCK)")
    scan_p.add_argument("--no-color", action="store_true", help="Disable color output")

    # --- brunnr install ---
    inst_p = sub.add_parser("install", help="Install a skill from the registry")
    inst_p.add_argument("skill", nargs="?", help="Skill slug to install (e.g., ax-rubric)")
    inst_p.add_argument("--registry", default="https://github.com/Peleke/brunnr", help="Skill registry URL")
    inst_p.add_argument("--with-tests", action="store_true", help="Also fetch test fixtures")
    inst_p.add_argument("--force", action="store_true", help="Overwrite existing skill")
    inst_p.add_argument("--list", action="store_true", dest="list_skills", help="List available skills")
    inst_p.add_argument("-y", "--yes", action="store_true", help="Skip review prompt, install immediately")

    # --- brunnr eval ---
    eval_p = sub.add_parser("eval", help="Run eval harness for a skill")
    eval_p.add_argument("skill", help="Skill slug to evaluate")
    eval_p.add_argument("--model", default="claude-sonnet-4-20250514", help="Claude model to use")
    eval_p.add_argument("-o", "--output", help="Path to write JSON results")
    eval_p.add_argument("--dry-run", action="store_true", help="Validate fixtures without API calls")

    # --- brunnr pipeline ---
    pipe_p = sub.add_parser("pipeline", help="Run the full scan + eval pipeline")
    pipe_p.add_argument("--scan-only", action="store_true", help="Security scan only, skip evals")
    pipe_p.add_argument("--verbose", action="store_true")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 0

    if args.command == "scan":
        from brunnr.commands.scan import run
        return run(args)
    elif args.command == "install":
        from brunnr.commands.install import run
        return run(args)
    elif args.command == "eval":
        from brunnr.commands.eval import run
        return run(args)
    elif args.command == "pipeline":
        from brunnr.commands.pipeline import run
        return run(args)

    return 0


def cli():
    sys.exit(main())


if __name__ == "__main__":
    cli()
