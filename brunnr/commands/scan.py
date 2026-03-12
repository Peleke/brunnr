"""brunnr scan — 7-class SKILL.md security scanner."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from brunnr.scanner import Severity, scan_skill_md
from brunnr.discovery import collect_scan_files, discover_skill_files

# ANSI colors
def _c(code: str, t: str, use_color: bool = True) -> str: return f"\033[{code}m{t}\033[0m" if use_color else t


def run(args) -> int:
    use_color = sys.stdout.isatty() and not getattr(args, "no_color", False)
    def _green(t: str) -> str: return _c("32", t, use_color)
    def _yellow(t: str) -> str: return _c("33", t, use_color)
    def _red(t: str) -> str: return _c("31", t, use_color)
    def _bold(t: str) -> str: return _c("1", t, use_color)
    _SEV = {Severity.BLOCK: _red, Severity.FLAG: _yellow, Severity.INFO: _yellow, Severity.CLEAN: _green}

    # Discover files
    if args.paths:
        files = collect_scan_files(args.paths)
    else:
        files = discover_skill_files()

    if not files:
        print("No files found.", file=sys.stderr)
        return 1

    results = []
    n_clean = n_flag = n_block = 0

    for path in files:
        content = path.read_text(encoding="utf-8")
        result = scan_skill_md(content)

        if result.blocked:
            n_block += 1
        elif result.flagged:
            n_flag += 1
        else:
            n_clean += 1

        results.append({"file": str(path), "result": result})

    # JSON output
    if getattr(args, "json_out", False):
        report = {
            "total": len(results),
            "blocked": n_block,
            "flagged": n_flag,
            "clean": n_clean,
            "skills": [{"file": r["file"], **r["result"].to_dict()} for r in results],
        }
        print(json.dumps(report, indent=2))
        if n_block:
            return 1
        if getattr(args, "strict", False) and n_flag:
            return 1
        return 0

    # Human output
    print(_bold("=== brunnr scan ==="))
    print()

    for r in results:
        res = r["result"]
        color = _SEV.get(res.severity, _green)
        label = color(res.severity.value.upper().ljust(5))
        name = Path(r["file"]).stem
        suffix = f" -- {len(res.findings)} findings" if res.findings else ""
        print(f"  {label}  {name}{suffix}")

        if getattr(args, "verbose", False) and res.findings:
            for f in res.findings:
                sev = _red("BLOCK") if f.severity == Severity.BLOCK else (
                    _yellow("FLAG") if f.severity == Severity.FLAG else "INFO")
                print(f"         {sev}: [{f.threat_class}] {f.description}")
                if f.evidence:
                    print(f"               {f.evidence[:80]}")

    print()
    print(f"  Scanned {len(files)} files: {_green(f'{n_clean} clean')}, {_yellow(f'{n_flag} flagged')}, {_red(f'{n_block} blocked')}")

    if n_block:
        return 1
    if getattr(args, "strict", False) and n_flag:
        return 1
    return 0
