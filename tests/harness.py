#!/usr/bin/env python3
"""
brunnr skill test harness

Discovers test cases for a given skill, feeds each input to Claude with the
skill's SKILL.md prompt, then validates the output against the test spec's
assertions (format checks, score-band checks, required-field checks).

Usage:
    python tests/harness.py --skill ax-rubric
    python tests/harness.py --skill ax-rubric --output results.json
    python tests/harness.py --skill ax-rubric --dry-run  # validate fixtures only
"""

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"
TESTS_DIR = REPO_ROOT / "tests"

# ---------------------------------------------------------------------------
# Frontmatter parsing (lightweight, no pyyaml dependency for the basic case)
# ---------------------------------------------------------------------------

def parse_frontmatter(text: str) -> dict[str, str]:
    """Extract YAML frontmatter from a SKILL.md file."""
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


def load_skill_prompt(skill_slug: str) -> str:
    """Read the full SKILL.md file as the system prompt for the skill."""
    skill_path = SKILLS_DIR / skill_slug / "SKILL.md"
    if not skill_path.exists():
        raise FileNotFoundError(f"Skill not found: {skill_path}")
    return skill_path.read_text()


def load_test_spec(skill_slug: str) -> dict[str, Any]:
    """Load the test-spec.json for a skill."""
    spec_path = TESTS_DIR / skill_slug / "test-spec.json"
    if not spec_path.exists():
        raise FileNotFoundError(f"Test spec not found: {spec_path}")
    return json.loads(spec_path.read_text())


def load_fixtures(skill_slug: str) -> list[dict[str, Any]]:
    """Load all fixture files referenced in the test spec."""
    spec = load_test_spec(skill_slug)
    fixtures = []
    for case in spec.get("cases", []):
        fixture_path = TESTS_DIR / skill_slug / case.get("fixture", "")
        if fixture_path.exists():
            fixture_data = json.loads(fixture_path.read_text())
            case["_fixture_data"] = fixture_data
        fixtures.append(case)
    return fixtures


# ---------------------------------------------------------------------------
# Claude API interaction
# ---------------------------------------------------------------------------

def call_claude(
    system_prompt: str,
    user_message: str,
    model: str = "claude-sonnet-4-20250514",
) -> str:
    """Send a message to Claude and return the text response."""
    try:
        from anthropic import Anthropic
    except ImportError:
        print("ERROR: anthropic package not installed. Run: pip install anthropic")
        sys.exit(1)

    client = Anthropic()
    response = client.messages.create(
        model=model,
        max_tokens=4096,
        system=system_prompt,
        messages=[{"role": "user", "content": user_message}],
    )

    return response.content[0].text


# ---------------------------------------------------------------------------
# Assertion engine
# ---------------------------------------------------------------------------

def extract_score(text: str) -> int | None:
    """Extract the primary score (N/5) from skill output."""
    # Match "Score: N/5" or "**Score: N/5**" or "Score: N / 5"
    match = re.search(r"[Ss]core:\s*\**\s*(\d)\s*/\s*5", text)
    if match:
        return int(match.group(1))
    return None


def extract_criteria_results(text: str) -> dict[str, str]:
    """Extract per-criterion pass/fail from the output table."""
    results = {}
    # Match table rows: | Criterion | pass/fail | notes |
    for match in re.finditer(
        r"\|\s*([\w\s]+?)\s*\|\s*(pass|fail)\s*\|",
        text,
        re.IGNORECASE,
    ):
        criterion = match.group(1).strip().lower()
        result = match.group(2).strip().lower()
        results[criterion] = result
    return results


def check_has_rewrite(text: str) -> bool:
    """Check if the output contains a rewrite section."""
    return bool(
        re.search(r"[Rr]ewr(itten|ite)", text)
        and re.search(r"[45]/5", text[text.lower().find("rewrit"):] if "rewrit" in text.lower() else text)
    )


def run_assertion(assertion: dict[str, Any], output: str) -> dict[str, Any]:
    """
    Run a single assertion against the output.

    Assertion types:
      - score_range: { "min": 0, "max": 2 } — extracted score must be in range
      - score_exact: 5 — extracted score must match exactly
      - has_rewrite: true — output must contain a rewrite section
      - has_table: true — output must contain a criterion table
      - contains: "string" — output must contain the string (case-insensitive)
      - criteria_fail: ["output shape", "cost signal"] — these criteria must show "fail"
      - criteria_pass: ["trigger clarity"] — these criteria must show "pass"
      - format_valid: true — output must follow the expected markdown format
    """
    atype = assertion["type"]
    expected = assertion["expected"]
    result = {"assertion": assertion, "passed": False, "detail": ""}

    if atype == "score_range":
        score = extract_score(output)
        if score is None:
            result["detail"] = "Could not extract score from output"
        elif expected["min"] <= score <= expected["max"]:
            result["passed"] = True
            result["detail"] = f"Score {score} is in range [{expected['min']}, {expected['max']}]"
        else:
            result["detail"] = f"Score {score} is NOT in range [{expected['min']}, {expected['max']}]"

    elif atype == "score_exact":
        score = extract_score(output)
        if score is None:
            result["detail"] = "Could not extract score from output"
        elif score == expected:
            result["passed"] = True
            result["detail"] = f"Score {score} matches expected {expected}"
        else:
            result["detail"] = f"Score {score} does not match expected {expected}"

    elif atype == "has_rewrite":
        has_it = check_has_rewrite(output)
        if has_it == expected:
            result["passed"] = True
            result["detail"] = f"Rewrite section {'found' if has_it else 'not found'} as expected"
        else:
            result["detail"] = f"Rewrite section {'found' if has_it else 'not found'}, expected {'present' if expected else 'absent'}"

    elif atype == "has_table":
        has_table = bool(re.search(r"\|.*\|.*\|.*\|", output))
        if has_table == expected:
            result["passed"] = True
            result["detail"] = f"Criteria table {'found' if has_table else 'not found'} as expected"
        else:
            result["detail"] = f"Criteria table {'found' if has_table else 'not found'}, expected {'present' if expected else 'absent'}"

    elif atype == "contains":
        found = expected.lower() in output.lower()
        if found:
            result["passed"] = True
            result["detail"] = f"Output contains '{expected}'"
        else:
            result["detail"] = f"Output does NOT contain '{expected}'"

    elif atype == "criteria_fail":
        criteria = extract_criteria_results(output)
        all_failed = True
        missing = []
        for crit in expected:
            crit_lower = crit.lower()
            matched = False
            for key, val in criteria.items():
                if crit_lower in key:
                    if val != "fail":
                        all_failed = False
                        missing.append(f"{crit} is '{val}', expected 'fail'")
                    matched = True
                    break
            if not matched:
                all_failed = False
                missing.append(f"{crit} not found in output table")
        if all_failed:
            result["passed"] = True
            result["detail"] = f"All expected criteria marked fail: {expected}"
        else:
            result["detail"] = f"Criteria mismatch: {'; '.join(missing)}"

    elif atype == "criteria_pass":
        criteria = extract_criteria_results(output)
        all_passed = True
        missing = []
        for crit in expected:
            crit_lower = crit.lower()
            matched = False
            for key, val in criteria.items():
                if crit_lower in key:
                    if val != "pass":
                        all_passed = False
                        missing.append(f"{crit} is '{val}', expected 'pass'")
                    matched = True
                    break
            if not matched:
                all_passed = False
                missing.append(f"{crit} not found in output table")
        if all_passed:
            result["passed"] = True
            result["detail"] = f"All expected criteria marked pass: {expected}"
        else:
            result["detail"] = f"Criteria mismatch: {'; '.join(missing)}"

    elif atype == "format_valid":
        # Check for the core structure: tool name header, score line, table, rewrite
        has_header = bool(re.search(r"^###?\s+", output, re.MULTILINE))
        has_score = extract_score(output) is not None
        has_table = bool(re.search(r"\|.*[Cc]riterion.*\|", output))
        checks = {
            "has_header": has_header,
            "has_score_line": has_score,
            "has_criteria_table": has_table,
        }
        if all(checks.values()):
            result["passed"] = True
            result["detail"] = "Output format valid: header, score, table all present"
        else:
            failed = [k for k, v in checks.items() if not v]
            result["detail"] = f"Format invalid — missing: {', '.join(failed)}"

    else:
        result["detail"] = f"Unknown assertion type: {atype}"

    return result


# ---------------------------------------------------------------------------
# Test runner
# ---------------------------------------------------------------------------

def run_test_case(
    skill_slug: str,
    skill_prompt: str,
    case: dict[str, Any],
    model: str,
    dry_run: bool = False,
) -> dict[str, Any]:
    """Run a single test case and return results."""
    case_id = case["id"]
    description = case.get("description", "")
    input_text = case.get("input", "")

    # If fixture reference, load from fixture data
    if "_fixture_data" in case:
        fixture = case["_fixture_data"]
        if "input" in fixture:
            input_text = fixture["input"]
        elif "description" in fixture:
            input_text = fixture["description"]

    print(f"\n  [{case_id}] {description}")

    if dry_run:
        print(f"    DRY RUN — skipping API call")
        return {
            "case_id": case_id,
            "description": description,
            "skipped": True,
            "assertions": [],
        }

    # Call Claude with the skill prompt
    start = time.time()
    try:
        output = call_claude(skill_prompt, input_text, model=model)
    except Exception as e:
        return {
            "case_id": case_id,
            "description": description,
            "error": str(e),
            "assertions": [],
            "duration_s": time.time() - start,
        }
    duration = time.time() - start

    # Run assertions
    assertion_results = []
    for assertion in case.get("assertions", []):
        result = run_assertion(assertion, output)
        status = "PASS" if result["passed"] else "FAIL"
        print(f"    {status}: [{assertion['type']}] {result['detail']}")
        assertion_results.append(result)

    return {
        "case_id": case_id,
        "description": description,
        "output": output[:2000],  # Truncate for storage
        "assertions": assertion_results,
        "duration_s": duration,
        "all_passed": all(r["passed"] for r in assertion_results),
    }


def run_skill_tests(
    skill_slug: str,
    model: str = "claude-sonnet-4-20250514",
    output_path: str | None = None,
    dry_run: bool = False,
) -> dict[str, Any]:
    """Run all test cases for a skill."""
    print(f"=== Testing skill: {skill_slug} ===")

    skill_prompt = load_skill_prompt(skill_slug)
    spec = load_test_spec(skill_slug)
    cases = load_fixtures(skill_slug)

    print(f"  Loaded {len(cases)} test cases")
    print(f"  Model: {model}")

    results = []
    for case in cases:
        result = run_test_case(skill_slug, skill_prompt, case, model, dry_run)
        results.append(result)

    # Summary
    passed = sum(1 for r in results if r.get("all_passed", False))
    failed = sum(1 for r in results if not r.get("all_passed", True) and not r.get("skipped", False))
    skipped = sum(1 for r in results if r.get("skipped", False))
    total = len(results) - skipped

    report = {
        "skill": skill_slug,
        "model": model,
        "spec_version": spec.get("version", "1.0"),
        "summary": {
            "pass": passed,
            "fail": failed,
            "skipped": skipped,
            "total": total,
        },
        "cases": results,
    }

    print(f"\n=== Results: {passed}/{total} passed", end="")
    if skipped:
        print(f" ({skipped} skipped)", end="")
    print(f" ===")

    if output_path:
        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(report, indent=2, default=str))
        print(f"Results written to {output_path}")

    return report


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="brunnr skill test harness",
    )
    parser.add_argument(
        "--skill",
        required=True,
        help="Skill slug to test (must match directory name in skills/)",
    )
    parser.add_argument(
        "--model",
        default="claude-sonnet-4-20250514",
        help="Claude model to use (default: claude-sonnet-4-20250514)",
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Path to write JSON results",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate fixtures and config without calling the API",
    )
    args = parser.parse_args()

    report = run_skill_tests(
        skill_slug=args.skill,
        model=args.model,
        output_path=args.output,
        dry_run=args.dry_run,
    )

    if report["summary"]["fail"] > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
