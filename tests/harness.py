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
    python tests/harness.py --skill learning-check --runner cli  # subscription, via `claude -p`

Runners:
    api  Anthropic SDK; needs ANTHROPIC_API_KEY and bills that key (default).
    cli  `claude --print` on the logged-in subscription. API-key, gateway (ANTHROPIC_BASE_URL) and
         cloud-provider (CLAUDE_CODE_USE_*) env vars are removed from the subprocess, and
         settings files are not loaded, so it runs on the login rather than a key or account.
         `--safe-mode`, `--strict-mcp-config` and `--disable-slash-commands` keep CLAUDE.md,
         auto-memory, skills, plugins, hooks and MCP servers out of the model's context, and the
         call runs from an empty temp directory so no repo or git state is visible. Never
         `--bare`: it forces API-key auth. What remains is Claude Code's own environment block
         (platform, date, the temp cwd) and the signed-in account's email.

    The judge uses --judge-model (default: same as --model). Pass a different model to avoid
    grading a report with the model that wrote it.
"""

import argparse
import json
import os
import subprocess
import sys
import tempfile
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
    KNOWN_TYPES,
    load_gold_row,
)

SKILLS_DIR = REPO_ROOT / "skills"
TESTS_DIR = REPO_ROOT / "tests"
CHAIN_DIR = TESTS_DIR / "sia-chain"


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
    """Load all fixture files referenced in the test spec.

    Cases may give their prompt inline as ``input`` instead of a ``fixture``
    file; those are returned unchanged.
    """
    spec = load_test_spec(skill_slug)
    fixtures = []
    for case in spec.get("cases", []):
        fixture_name = case.get("fixture")
        if fixture_name:
            fixture_path = TESTS_DIR / skill_slug / fixture_name
            if not fixture_path.is_file():
                raise FileNotFoundError(f"Fixture not found: {fixture_path}")
            case["_fixture_data"] = json.loads(fixture_path.read_text())
        fixtures.append(case)
    return fixtures


def upstream_sia(skill: str, fixture: dict[str, Any]) -> dict[str, Any]:
    """One upstream `sia` envelope built from a gold row (gold stands in for the upstream run)."""
    agent = fixture["agent"]
    row = load_gold_row(skill, agent)
    if row is None:
        raise FileNotFoundError(f"No gold row for upstream {skill}/{agent}")
    # Projection keys (`a[].b`, `x@includes`) are scoring paths, not envelope fields.
    out = {k: v for k, v in row["out"].items() if "[]" not in k and "@" not in k}
    out.update(row.get("context") or {})
    return {
        "skill": skill,
        "version": 1,
        "agent": {"name": agent, "summary": fixture["input"].splitlines()[0]},
        "deploymentType": fixture.get("deploymentType"),
        "in_ref": "gold",
        "out": out,
        "recommendations": [],
    }


def upstream_envelopes(skills: list[str], fixture: dict[str, Any]) -> str:
    """Upstream envelopes for a chain case, as the user would paste them."""
    import yaml

    blocks = []
    for skill in skills:
        env = {"sia": upstream_sia(skill, fixture)}
        blocks.append(f"Upstream envelope from {skill}:\n\n```yaml\n{yaml.safe_dump(env, sort_keys=False)}```")
    return "\n\n".join(blocks)


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
        max_tokens=16000,
        system=system_prompt,
        messages=[{"role": "user", "content": user_message}],
    )
    if response.stop_reason == "max_tokens":
        # A cut-off report would fail every envelope check and be blamed on the skill.
        raise RuntimeError("response hit max_tokens; report truncated")
    return response.content[0].text


CLI_ISOLATION = ["--safe-mode", "--strict-mcp-config", "--disable-slash-commands"]
CLI_STRIPPED_ENV = ("ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN", "ANTHROPIC_BASE_URL", "CLAUDECODE")


def cli_command(system_prompt: str, model: str) -> list[str]:
    return ["claude", "--print", "--model", model, "--tools", "", "--output-format", "text",
            "--setting-sources", "", *CLI_ISOLATION, "--system-prompt", system_prompt]


def cli_env() -> dict[str, str]:
    return {k: v for k, v in os.environ.items()
            if k not in CLI_STRIPPED_ENV and not k.startswith("CLAUDE_CODE_USE_")}


def call_cli(system_prompt: str, user_message: str, model: str) -> str:
    """Run one turn through `claude --print` on the subscription (no API key billing)."""
    with tempfile.TemporaryDirectory(prefix="brunnr-cli-") as cwd:
        proc = subprocess.run(
            cli_command(system_prompt, model),
            input=user_message, capture_output=True, text=True, env=cli_env(), cwd=cwd, timeout=600,
        )
    if proc.returncode != 0:
        raise RuntimeError(f"claude exited {proc.returncode}: {proc.stderr.strip()[:300]}")
    return proc.stdout


def call_model(runner: str, system_prompt: str, user_message: str, model: str) -> str:
    if runner == "cli":
        return call_cli(system_prompt, user_message, model)
    return call_claude(system_prompt, user_message, model=model)


JUDGE_REQUIRED = ("correct", "actionable", "honest")  # buyer rubric: sign-off needs 2, 4 and 5
JUDGE_MIN_SCORE = 0.7


def judge_message(report: str, agent_input: str | None) -> str:
    """What the judge reads: the agent material the skill saw, then the report."""
    if not agent_input:
        return report
    return ("## What the skill was given (the agent's files, logs and upstream envelopes)\n\n"
            f"{agent_input}\n\n## The report to grade\n\n{report}")


def judge_passes(verdict: dict[str, Any]) -> tuple[bool, str]:
    """Recompute sign-off from the criteria instead of trusting the judge's own `signOff`."""
    criteria = verdict.get("criteria") or {}
    try:
        score = float(verdict.get("score"))
    except (TypeError, ValueError):
        return False, "no numeric score"
    failed = [c for c in JUDGE_REQUIRED if criteria.get(c) is not True]
    ok = not failed and score >= JUDGE_MIN_SCORE
    said = str(verdict.get("signOff", "")).lower() == "yes"
    note = "" if ok == said else f" (judge said signOff={verdict.get('signOff')}; recomputed)"
    if failed:
        return False, f"failed required {', '.join(failed)}{note}"
    if score < JUDGE_MIN_SCORE:
        return False, f"score {score} < {JUDGE_MIN_SCORE}{note}"
    return True, note.strip()


def run_judge(runner: str, assertion: dict[str, Any], output: str, model: str,
              agent_input: str | None = None) -> dict[str, Any]:
    """Grade a report with a rubric file; record {score, signOff, feedback}."""
    result: dict[str, Any] = {"assertion": assertion, "passed": False, "detail": ""}
    result["judge_model"] = model
    rubric = (REPO_ROOT / assertion["expected"]["rubric"]).read_text()
    try:
        raw = call_model(runner, rubric, judge_message(output, agent_input), model)
    except Exception as e:  # a judge failure fails this assertion, not the whole run
        result["detail"] = f"judge error: {e}"
        return result
    try:
        # first JSON object in the reply; anything after it (a second object, prose) is ignored
        verdict, _ = json.JSONDecoder(strict=False).raw_decode(raw[raw.index("{"):])
    except ValueError as e:
        result["detail"] = f"judge returned no parseable JSON ({e}): {raw[:200]}"
        result["judge_raw"] = raw
        return result
    if not isinstance(verdict, dict):
        result["detail"] = f"judge returned JSON that is not an object: {raw[:200]}"
        result["judge_raw"] = raw
        return result
    result["judge"] = verdict
    result["passed"], why = judge_passes(verdict)
    result["detail"] = f"score={verdict.get('score')} signOff={verdict.get('signOff')}" + (f" {why}" if why else "")
    return result


def validate_case(skill_slug: str, case: dict[str, Any]) -> list[str]:
    """Dry-run checks: known assertion types, gold rows and rubric files exist."""
    problems = []
    agent = case.get("_fixture_data", {}).get("agent")
    for a in case.get("assertions", []):
        if a["type"] not in KNOWN_TYPES:
            problems.append(f"unknown assertion type {a['type']}")
        if a["type"] == "sia_gold" and load_gold_row(a["expected"]["skill"], a["expected"]["agent"]) is None:
            problems.append(f"no gold row {a['expected']}")
        if a["type"] == "judge" and not (REPO_ROOT / a["expected"]["rubric"]).is_file():
            problems.append(f"rubric missing: {a['expected']['rubric']}")
    for up in case.get("upstream", []):
        if agent is None or load_gold_row(up, agent) is None:
            problems.append(f"no upstream gold row {up}/{agent}")
    return problems


# ---------------------------------------------------------------------------
# Test runner
# ---------------------------------------------------------------------------

def run_test_case(
    skill_slug: str,
    skill_prompt: str,
    case: dict[str, Any],
    model: str,
    dry_run: bool = False,
    runner: str = "api",
    judge_model: str | None = None,
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
        problems = validate_case(skill_slug, case)
        judges = sum(1 for a in case.get("assertions", []) if a["type"] == "judge")
        for p in problems:
            print(f"    INVALID: {p}")
        note = f" ({judges} judge skipped: no model calls in a dry run)" if judges else ""
        print(f"    DRY RUN — skipping model call{note}")
        result = {
            "case_id": case_id,
            "description": description,
            "skipped": not problems,
            "invalid": problems,
            "assertions": [],
        }
        if problems:
            result["all_passed"] = False
        return result

    if case.get("upstream"):
        input_text = f"{input_text}\n\n{upstream_envelopes(case['upstream'], case['_fixture_data'])}"

    # Call Claude with the skill prompt
    start = time.time()
    try:
        output = call_model(runner, skill_prompt, input_text, model)
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
        if assertion["type"] == "judge":
            result = run_judge(runner, assertion, output, judge_model or model, input_text)
        else:
            result = run_assertion(assertion, output)
        status = "PASS" if result["passed"] else "FAIL"
        print(f"    {status}: [{assertion['type']}] {result['detail']}")
        assertion_results.append(result)

    return {
        "case_id": case_id,
        "description": description,
        "output": output,
        "assertions": assertion_results,
        "duration_s": duration,
        "all_passed": all(r["passed"] for r in assertion_results),
    }


def run_skill_tests(
    skill_slug: str,
    model: str = "claude-sonnet-4-20250514",
    output_path: str | None = None,
    dry_run: bool = False,
    runner: str = "api",
    judge_model: str | None = None,
) -> dict[str, Any]:
    """Run all test cases for a skill."""
    print(f"=== Testing skill: {skill_slug} ===")

    skill_prompt = load_skill_prompt(skill_slug)
    spec = load_test_spec(skill_slug)
    cases = load_fixtures(skill_slug)

    print(f"  Loaded {len(cases)} test cases")
    print(f"  Model: {model}" + (f" (judge: {judge_model})" if judge_model else ""))
    if runner == "api" and not dry_run and not os.environ.get("ANTHROPIC_API_KEY"):
        print("  No ANTHROPIC_API_KEY: validating cases only, as in --dry-run")
        dry_run = True

    results = []
    for case in cases:
        result = run_test_case(skill_slug, skill_prompt, case, model, dry_run, runner, judge_model)
        results.append(result)

    # Summary
    passed = sum(1 for r in results if r.get("all_passed", False))
    # A case whose model call raised has no `all_passed`; count it as a failure, not a pass.
    failed = sum(1 for r in results
                 if not r.get("skipped", False) and ("error" in r or not r.get("all_passed", True)))
    skipped = sum(1 for r in results if r.get("skipped", False))
    total = len(results) - skipped

    report = {
        "skill": skill_slug,
        "model": model,
        "judge_model": judge_model or model,
        "runner": runner,
        "dry_run": dry_run,
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
        help="Validate fixtures and config without calling a model",
    )
    parser.add_argument(
        "--runner",
        choices=["api", "cli"],
        default="api",
        help="api: Anthropic SDK (bills ANTHROPIC_API_KEY). cli: `claude --print` on the subscription.",
    )
    parser.add_argument(
        "--judge-model",
        help="Model for `judge` assertions (default: --model). Use a different one to avoid self-grading.",
    )
    args = parser.parse_args()

    report = run_skill_tests(
        skill_slug=args.skill,
        model=args.model,
        output_path=args.output,
        dry_run=args.dry_run,
        runner=args.runner,
        judge_model=args.judge_model,
    )

    if report["summary"]["fail"] > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
