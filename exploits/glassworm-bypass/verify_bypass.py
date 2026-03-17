"""Verify that the Glassworm-encoded SKILL.md passes brunnr's scanner.

Imports brunnr's scanner, runs the full pipeline AND each rule
individually against the poisoned SKILL.md, and prints results.

Expected output: CLEAN with 0 findings across all 11 rules.
"""

from __future__ import annotations

import sys
from pathlib import Path

# Ensure brunnr is importable from the project root.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from brunnr.scanner import scan_skill_md  # noqa: E402
from brunnr.scanner.context import ScanContext  # noqa: E402
from brunnr.scanner.rules import DEFAULT_RULES  # noqa: E402


def main() -> None:
    skill_path = Path(__file__).parent / "SKILL.md"

    if not skill_path.exists():
        print("SKILL.md not found. Run encode_payload.py first to generate it.")
        sys.exit(1)

    content = skill_path.read_text(encoding="utf-8")

    # --- Full pipeline ---
    result = scan_skill_md(content)

    print("=" * 60)
    print("FULL PIPELINE RESULT")
    print("=" * 60)
    print(f"  Severity : {result.severity.name}")
    print(f"  Findings : {len(result.findings)}")
    print(f"  Blocked  : {result.blocked}")
    print(f"  Flagged  : {result.flagged}")
    print(f"  Clean    : {result.clean}")

    if result.findings:
        print("\n  Findings detail:")
        for f in result.findings:
            print(f"    [{f.severity.name}] {f.threat_class.name}: {f.description}")
            if f.evidence:
                print(f"      evidence: {f.evidence[:80]}")

    # --- Per-rule breakdown ---
    print()
    print("=" * 60)
    print("PER-RULE BREAKDOWN")
    print("=" * 60)

    ctx = ScanContext.from_content(content)
    all_clean = True

    for rule_cls in DEFAULT_RULES:
        rule = rule_cls()
        findings = rule.scan(ctx)
        status = "CLEAN" if not findings else f"{len(findings)} findings"
        marker = "+" if not findings else "!"
        print(f"  [{marker}] {rule.name:.<30s} {status}")
        if findings:
            all_clean = False
            for f in findings:
                print(f"      {f.severity.name}: {f.description}")

    # --- Verdict ---
    print()
    if all_clean and result.clean:
        print("VERDICT: CLEAN. Glassworm payload evaded all 11 scanner rules.")
    else:
        print("VERDICT: DETECTED. Exploit needs adjustment.")
        sys.exit(1)


if __name__ == "__main__":
    main()
