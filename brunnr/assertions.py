"""Shared assertion and extraction logic for brunnr eval harness."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from brunnr.frontmatter import parse_frontmatter  # noqa: F401 — re-export for backwards compat


def extract_score(text: str) -> int | None:
    """Extract the primary score (N/5) from skill output."""
    match = re.search(r"[Ss]core:\s*\**\s*(\d)\s*/\s*5", text)
    return int(match.group(1)) if match else None


def extract_criteria(text: str) -> dict[str, str]:
    """Extract per-criterion pass/fail from the output table."""
    results = {}
    for match in re.finditer(
        r"\|\s*([\w\s]+?)\s*\|\s*(pass|fail)\s*\|",
        text,
        re.IGNORECASE,
    ):
        results[match.group(1).strip().lower()] = match.group(2).strip().lower()
    return results


def check_has_rewrite(text: str) -> bool:
    """Check if the output contains a rewrite section."""
    return bool(
        re.search(r"[Rr]ewr(itten|ite)", text)
        and re.search(
            r"[45]/5",
            text[text.lower().find("rewrit"):] if "rewrit" in text.lower() else text,
        )
    )


def run_assertion(assertion: dict[str, Any], output: str) -> dict[str, Any]:
    """Run a single assertion against eval output.

    Assertion types:
      - score_range: { "min": 0, "max": 2 }
      - score_exact: 5
      - has_rewrite: true
      - has_table: true
      - contains: "string"
      - criteria_fail: ["output shape", "cost signal"]
      - criteria_pass: ["trigger clarity"]
      - format_valid: true
    """
    atype = assertion["type"]
    expected = assertion["expected"]
    result: dict[str, Any] = {"assertion": assertion, "passed": False, "detail": ""}

    if atype == "score_range":
        score = extract_score(output)
        if score is None:
            result["detail"] = "Could not extract score"
        elif expected["min"] <= score <= expected["max"]:
            result["passed"] = True
            result["detail"] = f"Score {score} in [{expected['min']}, {expected['max']}]"
        else:
            result["detail"] = f"Score {score} NOT in [{expected['min']}, {expected['max']}]"

    elif atype == "score_exact":
        score = extract_score(output)
        if score is None:
            result["detail"] = "Could not extract score"
        elif score == expected:
            result["passed"] = True
            result["detail"] = f"Score {score} matches expected {expected}"
        else:
            result["detail"] = f"Score {score} does not match expected {expected}"

    elif atype == "has_table":
        has = bool(re.search(r"\|.*\|.*\|.*\|", output))
        result["passed"] = has == expected
        result["detail"] = f"Table {'found' if has else 'missing'}"

    elif atype == "has_rewrite":
        has = check_has_rewrite(output)
        result["passed"] = has == expected
        result["detail"] = f"Rewrite {'found' if has else 'missing'}"

    elif atype == "contains":
        found = expected.lower() in output.lower()
        result["passed"] = found
        result["detail"] = f"{'Contains' if found else 'Missing'} '{expected}'"

    elif atype in ("criteria_pass", "criteria_fail"):
        criteria = extract_criteria(output)
        target = "pass" if atype == "criteria_pass" else "fail"
        missing = []
        for crit in expected:
            matched = any(crit.lower() in k and v == target for k, v in criteria.items())
            if not matched:
                missing.append(crit)
        result["passed"] = len(missing) == 0
        result["detail"] = f"{'All match' if not missing else 'Missing: ' + ', '.join(missing)}"

    elif atype == "format_valid":
        has_header = bool(re.search(r"^###?\s+", output, re.MULTILINE))
        has_score = extract_score(output) is not None
        has_table = bool(re.search(r"\|.*[Cc]riterion.*\|", output))
        result["passed"] = all([has_header, has_score, has_table])
        result["detail"] = f"header={has_header} score={has_score} table={has_table}"

    elif atype in SIA_TYPES:
        _run_sia_assertion(atype, expected, output, result)

    elif atype == "judge":
        result["detail"] = "judge assertions run in the harness (needs a runner)"

    else:
        result["detail"] = f"Unknown assertion type: {atype}"

    return result


# SIA chain assertions (envelope convention: skills/_sia-chain.md)
SIA_TYPES = ("sia_envelope_valid", "sia_out_fields", "sia_recommendations", "sia_gold")
KNOWN_TYPES = (
    "score_range", "score_exact", "has_table", "has_rewrite", "contains",
    "criteria_pass", "criteria_fail", "format_valid", "judge", *SIA_TYPES,
)
GOLD_DIR = Path(__file__).resolve().parent.parent / "tests" / "sia-chain" / "gold"


def load_gold_row(skill: str, agent: str) -> dict[str, Any] | None:
    import yaml

    path = GOLD_DIR / f"{skill}.yaml"
    if not path.is_file():
        return None
    rows = (yaml.safe_load(path.read_text()) or {}).get("rows", [])
    return next((r for r in rows if r.get("agent") == agent), None)


def _run_sia_assertion(atype: str, expected: Any, output: str, result: dict[str, Any]) -> None:
    from brunnr import sia_chain

    env = sia_chain.extract_envelope(output)
    if atype == "sia_envelope_valid":
        # expected: true, or {skill, deploymentType} to also pin the envelope to this case
        pins = expected if isinstance(expected, dict) else {}
        problems = sia_chain.check_envelope(env, pins.get("skill"), pins.get("deploymentType"))
    elif atype == "sia_out_fields":
        problems = sia_chain.check_out_fields(env, list(expected))
    elif atype == "sia_recommendations":
        problems = sia_chain.check_recommendations(env)
    else:  # sia_gold
        row = load_gold_row(expected["skill"], expected["agent"])
        if row is None:
            result["detail"] = f"no gold row for {expected['skill']}/{expected['agent']}"
            return
        score, problems = sia_chain.gold_agreement(env, row["out"])
        result["score"] = score
        result["adjudicated"] = bool(row.get("adjudicated_by"))
    result["passed"] = not problems
    result["detail"] = "ok" if not problems else "; ".join(problems[:5])
