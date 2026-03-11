"""brunnr eval — run the skill evaluation harness."""

from __future__ import annotations

import json
import re
import sys
import time
from pathlib import Path
from typing import Any

SKILLS_DIR = Path.cwd() / "skills"
TESTS_DIR = Path.cwd() / "tests"


def _parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    fm = {}
    for line in parts[1].strip().splitlines():
        if ":" in line:
            key, val = line.split(":", 1)
            fm[key.strip()] = val.strip().strip('"').strip("'")
    return fm


def _load_skill_prompt(slug: str) -> str:
    path = SKILLS_DIR / slug / "SKILL.md"
    if not path.exists():
        raise FileNotFoundError(f"Skill not found: {path}")
    return path.read_text()


def _load_test_spec(slug: str) -> dict[str, Any]:
    path = TESTS_DIR / slug / "test-spec.json"
    if not path.exists():
        raise FileNotFoundError(f"Test spec not found: {path}")
    return json.loads(path.read_text())


def _load_fixtures(slug: str) -> list[dict[str, Any]]:
    spec = _load_test_spec(slug)
    cases = []
    for case in spec.get("cases", []):
        fixture_path = TESTS_DIR / slug / case.get("fixture", "")
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


def _extract_score(text: str) -> int | None:
    match = re.search(r"[Ss]core:\s*\**\s*(\d)\s*/\s*5", text)
    return int(match.group(1)) if match else None


def _extract_criteria(text: str) -> dict[str, str]:
    results = {}
    for match in re.finditer(r"\|\s*([\w\s]+?)\s*\|\s*(pass|fail)\s*\|", text, re.IGNORECASE):
        results[match.group(1).strip().lower()] = match.group(2).strip().lower()
    return results


def _run_assertion(assertion: dict, output: str) -> dict:
    atype = assertion["type"]
    expected = assertion["expected"]
    result = {"assertion": assertion, "passed": False, "detail": ""}

    if atype == "score_range":
        score = _extract_score(output)
        if score is None:
            result["detail"] = "Could not extract score"
        elif expected["min"] <= score <= expected["max"]:
            result["passed"] = True
            result["detail"] = f"Score {score} in [{expected['min']}, {expected['max']}]"
        else:
            result["detail"] = f"Score {score} NOT in [{expected['min']}, {expected['max']}]"

    elif atype == "has_table":
        has = bool(re.search(r"\|.*\|.*\|.*\|", output))
        result["passed"] = has == expected
        result["detail"] = f"Table {'found' if has else 'missing'}"

    elif atype == "has_rewrite":
        has = bool(re.search(r"[Rr]ewr(itten|ite)", output))
        result["passed"] = has == expected
        result["detail"] = f"Rewrite {'found' if has else 'missing'}"

    elif atype == "contains":
        found = expected.lower() in output.lower()
        result["passed"] = found
        result["detail"] = f"{'Contains' if found else 'Missing'} '{expected}'"

    elif atype == "format_valid":
        has_header = bool(re.search(r"^###?\s+", output, re.MULTILINE))
        has_score = _extract_score(output) is not None
        has_table = bool(re.search(r"\|.*[Cc]riterion.*\|", output))
        result["passed"] = all([has_header, has_score, has_table])
        result["detail"] = f"header={has_header} score={has_score} table={has_table}"

    elif atype in ("criteria_pass", "criteria_fail"):
        criteria = _extract_criteria(output)
        target = "pass" if atype == "criteria_pass" else "fail"
        missing = []
        for crit in expected:
            matched = any(crit.lower() in k and v == target for k, v in criteria.items())
            if not matched:
                missing.append(crit)
        result["passed"] = len(missing) == 0
        result["detail"] = f"{'All match' if not missing else 'Missing: ' + ', '.join(missing)}"

    return result


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
            r = _run_assertion(assertion, output)
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
