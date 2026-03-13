"""Shared assertion and extraction logic for brunnr eval harness."""

from __future__ import annotations

import re
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

    else:
        result["detail"] = f"Unknown assertion type: {atype}"

    return result
