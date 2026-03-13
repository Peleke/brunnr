"""brunnr CLI — subcommand dispatcher."""

from __future__ import annotations

import argparse
import sys

from brunnr import __version__

_DEFAULT_REGISTRY = "https://github.com/Peleke/brunnr"


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="brunnr",
        description="Security scanner and skill registry for agent tool descriptions.",
    )
    parser.add_argument("--version", action="version", version=f"brunnr {__version__}")
    parser.add_argument("--registry", default=_DEFAULT_REGISTRY, help="Skill registry URL")
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
    inst_p.add_argument("--with-tests", action="store_true", help="Also fetch test fixtures")
    inst_p.add_argument("--force", action="store_true", help="Overwrite existing skill")
    inst_p.add_argument("--list", action="store_true", dest="list_skills", help="List available skills")
    inst_p.add_argument("-y", "--yes", action="store_true", help="Skip review prompt")
    inst_p.add_argument(
        "-t", "--target",
        help="Install SKILL.md to this directory instead of ./skills/ (runtime use, skips schema/tests)",
    )

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

    # --- brunnr list ---
    list_p = sub.add_parser("list", help="List installed skills")
    list_p.add_argument("--json", action="store_true", dest="json_out", help="JSON output")

    # --- brunnr search ---
    search_p = sub.add_parser("search", help="Search the registry for skills")
    search_p.add_argument("query", nargs="?", default="", help="Search query")
    search_p.add_argument("--tag", help="Filter by tag")
    search_p.add_argument("--json", action="store_true", dest="json_out", help="JSON output")

    # --- brunnr inspect ---
    insp_p = sub.add_parser("inspect", help="Preview a skill without installing")
    insp_p.add_argument("skill", help="Skill slug to inspect")
    insp_p.add_argument("--full", action="store_true", help="Show entire SKILL.md")
    insp_p.add_argument("--json", action="store_true", dest="json_out", help="JSON output")

    # --- brunnr update ---
    upd_p = sub.add_parser("update", help="Update installed skills to latest")
    upd_p.add_argument("skill", nargs="?", help="Specific skill to update (default: all)")
    upd_p.add_argument("--dry-run", action="store_true", help="Show what would change")
    upd_p.add_argument("--force", action="store_true", help="Skip prompts")

    # --- brunnr explore ---
    exp_p = sub.add_parser("explore", help="Browse skills from the registry")
    exp_p.add_argument("--limit", type=int, default=20, help="Max skills to show")
    exp_p.add_argument("--json", action="store_true", dest="json_out", help="JSON output")

    # --- brunnr publish ---
    pub_p = sub.add_parser("publish", help="Publish a skill to the registry (PR-based)")
    pub_p.add_argument("path", help="Skill directory or SKILL.md path")
    pub_p.add_argument("--dry-run", action="store_true", help="Validate + scan only")

    # --- brunnr sync ---
    sync_p = sub.add_parser("sync", help="Discover and publish local skills")
    sync_p.add_argument("--dry-run", action="store_true", help="Show what would be published")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 0

    dispatch = {
        "scan": "brunnr.commands.scan",
        "install": "brunnr.commands.install",
        "eval": "brunnr.commands.eval",
        "pipeline": "brunnr.commands.pipeline",
        "list": "brunnr.commands.list_cmd",
        "search": "brunnr.commands.search",
        "inspect": "brunnr.commands.inspect_cmd",
        "update": "brunnr.commands.update",
        "explore": "brunnr.commands.explore",
        "publish": "brunnr.commands.publish",
        "sync": "brunnr.commands.sync_cmd",
    }

    module_name = dispatch.get(args.command)
    if module_name:
        import importlib
        mod = importlib.import_module(module_name)
        return mod.run(args)

    return 0


def cli():
    sys.exit(main())


if __name__ == "__main__":
    cli()
