"""brunnr eval — run the skill evaluation harness."""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path
from typing import Any

from brunnr.assertions import parse_frontmatter, run_assertion


def _skills_dir() -> Path:
    return Path.cwd() / "skills"


def _tests_dir() -> Path:
    return Path.cwd() / "tests"


def _load_skill_prompt(slug: str) -> str:
    path = _skills_dir() / slug / "SKILL.md"
    if not path.exists():
        raise FileNotFoundError(f"Skill not found: {path}")
    return path.read_text()


def _load_test_spec(slug: str) -> dict[str, Any]:
    path = _tests_dir() / slug / "test-spec.json"
    if not path.exists():
        raise FileNotFoundError(f"Test spec not found: {path}")
    return json.loads(path.read_text())


def _load_fixtures(slug: str) -> list[dict[str, Any]]:
    spec = _load_test_spec(slug)
    cases = []
    for case in spec.get("cases", []):
        fixture_path = _tests_dir() / slug / case.get("fixture", "")
        if fixture_path.exists():
            case["_fixture_data"] = json.loads(fixture_path.read_text())
        cases.append(case)
    return cases


def _call_claude(system_prompt: str, user_message: str, model: str) -> str:
    try:
        from anthropic import Anthropic
    except ImportError:
        print("ERROR: anthropic package not installed. Run: pip install brunnr[eval]", file=sys.stderr)
        sys.exit(1)

    client = Anthropic()
    response = client.messages.create(
        model=model,
        max_tokens=4096,
        system=system_prompt,
        messages=[{"role": "user", "content": user_message}],
    )
    return response.content[0].text


def run(args) -> int:
    slug = args.skill
    model = args.model
    dry_run = args.dry_run

    print(f"=== brunnr eval: {slug} ===")

    try:
        prompt = _load_skill_prompt(slug)
        cases = _load_fixtures(slug)
    except FileNotFoundError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1

    print(f"  {len(cases)} test cases, model: {model}")

    results = []
    for case in cases:
        case_id = case["id"]
        desc = case.get("description", "")
        input_text = case.get("input", "")

        if "_fixture_data" in case:
            fx = case["_fixture_data"]
            input_text = fx.get("input", fx.get("description", input_text))

        print(f"\n  [{case_id}] {desc}")

        if dry_run:
            print("    DRY RUN — skipped")
            results.append({"case_id": case_id, "skipped": True, "assertions": []})
            continue

        start = time.time()
        try:
            output = _call_claude(prompt, input_text, model)
        except Exception as e:
            results.append({"case_id": case_id, "error": str(e), "assertions": []})
            continue

        duration = time.time() - start
        assertion_results = []
        for assertion in case.get("assertions", []):
            r = run_assertion(assertion, output)
            status = "PASS" if r["passed"] else "FAIL"
            print(f"    {status}: [{assertion['type']}] {r['detail']}")
            assertion_results.append(r)

        results.append({
            "case_id": case_id,
            "output": output[:2000],
            "assertions": assertion_results,
            "duration_s": duration,
            "all_passed": all(r["passed"] for r in assertion_results),
        })

    passed = sum(1 for r in results if r.get("all_passed", False))
    skipped = sum(1 for r in results if r.get("skipped", False))
    total = len(results) - skipped
    failed = total - passed

    print(f"\n=== {passed}/{total} passed", end="")
    if skipped:
        print(f" ({skipped} skipped)", end="")
    print(" ===")

    if args.output:
        report = {"skill": slug, "model": model, "summary": {"pass": passed, "fail": failed, "skipped": skipped}, "cases": results}
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        Path(args.output).write_text(json.dumps(report, indent=2, default=str))
        print(f"Results: {args.output}")

    return 1 if failed > 0 else 0
