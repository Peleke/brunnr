"""SIA audit chain: envelope parsing, hard checks, chain check, learning-check outcome.

The envelope convention lives in skills/_sia-chain.md. The reads/writes table lives in
tests/sia-chain/chain.yaml. PyYAML is imported lazily so the core CLI keeps zero dependencies
(install with `pip install brunnr[eval]`).
"""

from __future__ import annotations

import re
from typing import Any

MAX_RECOMMENDATIONS = 7
DEPLOYMENT_TYPES = (
    "coding-harness",
    "gateway-agent",
    "framework-app",
    "prompt-program",
    "hosted-nocode",
)
VERDICTS = ("yes", "partial", "no")
OUTCOMES = ("no loop found", "not learning", "learning, unmeasured", "learning, measured")
ENVELOPE_KEYS = ("skill", "version", "agent", "deploymentType", "in_ref", "out", "recommendations")
RECOMMENDATION_KEYS = ("id", "title", "why", "do", "effort", "impact", "evidence", "next_skill")

_FENCE = re.compile(r"```ya?ml[ \t]*\n(.*?)```", re.DOTALL)


def _yaml():
    try:
        import yaml
    except ImportError as exc:  # pragma: no cover - exercised only without the extra
        raise RuntimeError("PyYAML is required: pip install 'brunnr[eval]'") from exc
    return yaml


# ---------------------------------------------------------------------------
# Envelope
# ---------------------------------------------------------------------------


def extract_envelope(report: str) -> dict[str, Any] | None:
    """Return the `sia` mapping from the last fenced YAML block of a report, or None.

    The envelope must be the last fenced YAML block. Earlier YAML blocks (examples) are ignored.
    """
    blocks = _FENCE.findall(report)
    if not blocks:
        return None
    try:
        data = _yaml().safe_load(blocks[-1])
    except Exception:
        return None
    if not isinstance(data, dict) or not isinstance(data.get("sia"), dict):
        return None
    return data["sia"]


def get_path(data: Any, path: str) -> Any:
    """Resolve a dotted path; `name[]` maps over a list and needs every item to have the rest.

    Returns a sentinel `_MISSING` when any step is absent.
    """
    parts = path.split(".")
    cur: Any = data
    for i, part in enumerate(parts):
        is_list = part.endswith("[]")
        key = part[:-2] if is_list else part
        if not isinstance(cur, dict) or key not in cur:
            return _MISSING
        cur = cur[key]
        if is_list:
            if not isinstance(cur, list) or not cur:
                return _MISSING
            rest = ".".join(parts[i + 1 :])
            if not rest:
                return cur
            vals = [get_path(item, rest) for item in cur]
            return _MISSING if any(v is _MISSING for v in vals) else vals
    return cur


class _Missing:
    def __repr__(self) -> str:
        return "<missing>"


_MISSING = _Missing()


def check_envelope(env: dict[str, Any] | None) -> list[str]:
    """Structural problems with an envelope (empty list means valid)."""
    if env is None:
        return ["no `sia:` envelope in the last fenced YAML block"]
    problems = [f"missing top-level key `{k}`" for k in ENVELOPE_KEYS if k not in env]
    dt = env.get("deploymentType")
    if dt is not None and dt not in DEPLOYMENT_TYPES:
        problems.append(f"deploymentType `{dt}` not in {DEPLOYMENT_TYPES}")
    if "out" in env and not isinstance(env["out"], dict):
        problems.append("`out` is not a mapping")
    return problems


def check_out_fields(env: dict[str, Any] | None, required: list[str]) -> list[str]:
    """Required `out` paths that are missing."""
    if env is None or not isinstance(env.get("out"), dict):
        return [f"missing out.{p}" for p in required]
    return [f"missing out.{p}" for p in required if get_path(env["out"], p) is _MISSING]


def _has_evidence(item: dict[str, Any]) -> bool:
    ev = item.get("evidence")
    if isinstance(ev, list):
        return any(isinstance(e, str) and e.strip() for e in ev)
    if isinstance(ev, str):
        return ev.strip().lower().startswith("unknown (ask:")
    return False


def check_recommendations(env: dict[str, Any] | None) -> list[str]:
    """Problems with the recommendations list (spec section 4)."""
    if env is None:
        return ["no envelope"]
    recs = env.get("recommendations")
    if not isinstance(recs, list):
        return ["`recommendations` is not a list"]
    problems: list[str] = []
    if len(recs) > MAX_RECOMMENDATIONS:
        problems.append(f"{len(recs)} recommendations; at most {MAX_RECOMMENDATIONS}")
    for n, item in enumerate(recs, 1):
        if not isinstance(item, dict):
            problems.append(f"item {n} is not a mapping")
            continue
        missing = [k for k in RECOMMENDATION_KEYS if k not in item]
        if missing:
            problems.append(f"item {n} missing {', '.join(missing)}")
        if not _has_evidence(item):
            problems.append(f"item {n} has no evidence and no 'unknown (ask: ...)'")
        if item.get("effort") not in ("S", "M", "L"):
            problems.append(f"item {n} effort `{item.get('effort')}` not S|M|L")
        if item.get("impact") not in ("high", "medium", "low"):
            problems.append(f"item {n} impact `{item.get('impact')}` not high|medium|low")
    return problems


def hard_check_score(report: str, required_out: list[str]) -> tuple[float, list[str]]:
    """Fraction of the three hard checks passed (envelope, out fields, recommendations).

    This is the code metric every chain skill declares for S2.
    """
    env = extract_envelope(report)
    groups = [check_envelope(env), check_out_fields(env, required_out), check_recommendations(env)]
    passed = sum(1 for g in groups if not g)
    return passed / len(groups), [p for g in groups for p in g]


def _norm(value: Any) -> Any:
    if isinstance(value, list):
        return sorted({_norm(v) for v in value if not isinstance(v, (list, dict))})
    if isinstance(value, bool):  # YAML 1.1 reads unquoted yes/no as booleans
        return "yes" if value else "no"
    return re.sub(r"\s+", " ", str(value).strip().lower())


def _flatten(out: dict[str, Any], prefix: str = "") -> dict[str, Any]:
    flat: dict[str, Any] = {}
    for key, value in out.items():
        path = f"{prefix}{key}"
        if isinstance(value, dict) and value:
            flat.update(_flatten(value, path + "."))
        else:
            flat[path] = value
    return flat


def gold_agreement(env: dict[str, Any] | None, gold_out: dict[str, Any]) -> tuple[float, list[str]]:
    """Fraction of gold `out` leaves the envelope matches (case- and order-insensitive).

    Lists compare as sets of scalars; `[]` in the gold means "no items".
    """
    flat = _flatten(gold_out)
    if not flat:
        return 1.0, []
    out = (env or {}).get("out") or {}
    misses = []
    for path, want in flat.items():
        got = get_path(out, path)
        if got is _MISSING:
            got = [] if want == [] else None
        if _norm(got) != _norm(want):
            misses.append(f"out.{path}: expected {want!r}, got {got!r}")
    return 1 - len(misses) / len(flat), misses


# ---------------------------------------------------------------------------
# Chain check
# ---------------------------------------------------------------------------


def _covers(write: str, read: str) -> bool:
    """A write covers a read when it is the same path or an ancestor of it."""
    return read == write or read.startswith(write + ".") or read.startswith(write + "[]")


def chain_gaps(links: list[dict[str, Any]]) -> list[str]:
    """Reads with no writer before the reading link.

    `links` is ordered; each item has `skill`, `reads`, `writes`. A read is covered when an
    earlier link writes the same path or an ancestor (`metrics` covers `metrics[].tier`;
    `slots.signal` does not cover `slots.budget`).
    """
    written: list[str] = []
    gaps: list[str] = []
    for link in links:
        for read in link.get("reads") or []:
            if not any(_covers(w, read) for w in written):
                gaps.append(f"{link['skill']} reads `{read}` but no earlier link writes it")
        written.extend(link.get("writes") or [])
    return gaps


# ---------------------------------------------------------------------------
# learning-check outcome (matches the sia-starter learning-check template)
# ---------------------------------------------------------------------------


def learning_outcome(q1: str, q2: str, q3: str, person_both: bool) -> str:
    """Outcome for one loop from its three verdicts.

    person_both: a person both carries the signal and applies the change.

    - not learning: Q1 no, or Q2 no, or (person_both and Q3 no)
    - learning, unmeasured: Q1, Q2 in {yes, partial}; Q3 in {no, partial}
    - learning, measured: Q1, Q2 in {yes, partial}; Q3 yes
    - append " (partial loop)" to a learning outcome when Q1 or Q2 is partial
    """
    for q in (q1, q2, q3):
        if q not in VERDICTS:
            raise ValueError(f"verdict must be one of {VERDICTS}, got {q!r}")
    if q1 == "no" or q2 == "no" or (person_both and q3 == "no"):
        return "not learning"
    base = "learning, measured" if q3 == "yes" else "learning, unmeasured"
    if "partial" in (q1, q2):
        base += " (partial loop)"
    return base
