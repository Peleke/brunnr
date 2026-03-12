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
import sys
import time
from pathlib import Path
from typing import Any

# Ensure brunnr package is importable when run as standalone script
REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from brunnr.assertions import (
    parse_frontmatter,
    extract_score,
    extract_criteria,
    check_has_rewrite,
    run_assertion,
)

SKILLS_DIR = REPO_ROOT / "skills"
TESTS_DIR = REPO_ROOT / "tests"


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

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
        "output": output[:2000],
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
