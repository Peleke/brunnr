"""SIA audit chain: chain check, envelope checks, learning-check outcome, and the S2 gate."""

from __future__ import annotations

import itertools
import json
import re
from pathlib import Path

import pytest
import yaml

from brunnr import sia_chain
from brunnr.assertions import run_assertion

REPO = Path(__file__).resolve().parent.parent
CHAIN = yaml.safe_load((REPO / "tests/sia-chain/chain.yaml").read_text())["links"]
CHAIN_SKILLS = [link["skill"] for link in CHAIN]
AGENTS_DIR = REPO / "tests/sia-chain/agents"
GOLD_DIR = REPO / "tests/sia-chain/gold"


# ---------------------------------------------------------------------------
# Chain check
# ---------------------------------------------------------------------------


def test_chain_has_no_gaps():
    assert sia_chain.chain_gaps(CHAIN) == []


def test_chain_order_matches_conventions_table():
    table = (REPO / "skills/_sia-chain.md").read_text()
    positions = [table.index(f"`{s}`") for s in CHAIN_SKILLS]
    assert positions == sorted(positions)


@pytest.mark.parametrize(
    "bad_read",
    ["slots.budget", "verdicts.cost", "results", "plan.act", "reps.count"],
)
def test_chain_check_catches_a_planted_read(bad_read):
    """A read with no upstream writer must be reported, including siblings of written paths.

    Writing a whole object (`metrics`, `split`) covers its subfields, so planted reads are chosen
    outside every written subtree.
    """
    links = [dict(link, reads=list(link["reads"])) for link in CHAIN]
    links[-1]["reads"].append(bad_read)
    gaps = sia_chain.chain_gaps(links)
    assert any(bad_read in g for g in gaps), gaps


def test_chain_check_rejects_reading_your_own_write():
    links = [{"skill": "a", "reads": ["x"], "writes": ["x"]}]
    assert sia_chain.chain_gaps(links)


# ---------------------------------------------------------------------------
# learning-check outcome
# ---------------------------------------------------------------------------


def _oracle(q1, q2, q3, person_both):
    """Independent restatement of the sia-starter template's outcome rules."""
    learning_inputs = q1 in ("yes", "partial") and q2 in ("yes", "partial")
    if not learning_inputs or (person_both and q3 == "no"):
        return "not learning"
    out = {"yes": "learning, measured"}.get(q3, "learning, unmeasured")
    return out + (" (partial loop)" if "partial" in (q1, q2) else "")


ALL_INPUTS = list(itertools.product(sia_chain.VERDICTS, sia_chain.VERDICTS, sia_chain.VERDICTS, (True, False)))


def test_outcome_input_space_is_54():
    assert len(ALL_INPUTS) == 54


@pytest.mark.parametrize("q1,q2,q3,pb", ALL_INPUTS)
def test_outcome_matches_template_rules(q1, q2, q3, pb):
    assert sia_chain.learning_outcome(q1, q2, q3, pb) == _oracle(q1, q2, q3, pb)


@pytest.mark.parametrize(
    "q1,q2,q3,pb,expected",
    [  # the template's worked examples
        ("no", "yes", "no", False, "not learning"),
        ("yes", "partial", "no", False, "learning, unmeasured (partial loop)"),
        ("yes", "partial", "no", False, "learning, unmeasured (partial loop)"),
        ("yes", "partial", "yes", True, "learning, measured (partial loop)"),
        ("partial", "partial", "no", True, "not learning"),
    ],
)
def test_outcome_template_examples(q1, q2, q3, pb, expected):
    assert sia_chain.learning_outcome(q1, q2, q3, pb) == expected


def test_outcome_rejects_unknown_verdict():
    with pytest.raises(ValueError):
        sia_chain.learning_outcome("maybe", "yes", "yes", False)


def test_gold_outcomes_follow_the_rules():
    """Every learning-check gold row's outcome is consistent with its own verdicts."""
    rows = yaml.safe_load((GOLD_DIR / "learning-check.yaml").read_text())["rows"]
    for row in rows:
        v, outcome = row["out"]["verdicts"], row["out"]["outcome"]
        if outcome == "no loop found":
            assert set(v.values()) == {"no"}, row["agent"]
            continue
        possible = {sia_chain.learning_outcome(v["signal"], v["update"], v["convergence"], pb) for pb in (True, False)}
        assert outcome in possible, row["agent"]


# ---------------------------------------------------------------------------
# Envelope and recommendation checks
# ---------------------------------------------------------------------------

GOOD_REC = {
    "id": "x-1", "title": "t", "why": "w", "do": "d", "effort": "S", "impact": "high",
    "evidence": ["src/a.py:1"], "next_skill": "gold-set", "links": [],
}


def _report(sia: dict, prefix: str = "# Report\n\n```yaml\nexample: true\n```\n\n") -> str:
    return prefix + "```yaml\n" + yaml.safe_dump({"sia": sia}, sort_keys=False) + "```\n\n> Series and help: peleke.me · LinkedIn\n"


def _env(**over):
    base = {
        "skill": "learning-check", "version": 1, "agent": {"name": "a", "summary": "s"},
        "deploymentType": "framework-app", "in_ref": "none",
        "out": {"verdicts": {"signal": "yes", "update": "partial", "convergence": "no"},
                "loops": [], "outcome": "learning, unmeasured (partial loop)", "firstFix": "f"},
        "recommendations": [GOOD_REC],
    }
    base.update(over)
    return base


LC_WRITES = next(link["writes"] for link in CHAIN if link["skill"] == "learning-check")


def test_good_report_scores_one():
    score, problems = sia_chain.hard_check_score(_report(_env()), LC_WRITES)
    assert (score, problems) == (1.0, [])


def test_envelope_must_be_the_last_yaml_block():
    report = _report(_env()) + "\n```yaml\nnot: an envelope\n```\n"
    assert sia_chain.extract_envelope(report) is None


@pytest.mark.parametrize(
    "atype,expected,env,should_pass",
    [
        ("sia_envelope_valid", True, _env(), True),
        ("sia_envelope_valid", True, _env(deploymentType="saas"), False),
        ("sia_envelope_valid", True, {k: v for k, v in _env().items() if k != "in_ref"}, False),
        ("sia_out_fields", LC_WRITES, _env(), True),
        ("sia_out_fields", LC_WRITES, _env(out={"verdicts": {"signal": "yes"}}), False),
        ("sia_recommendations", True, _env(), True),
        ("sia_recommendations", True, _env(recommendations=[GOOD_REC] * 8), False),
        ("sia_recommendations", True, _env(recommendations=[dict(GOOD_REC, evidence=[])]), False),
        ("sia_recommendations", True, _env(recommendations=[dict(GOOD_REC, evidence="unknown (ask: who labels?)")]), True),
        ("sia_recommendations", True, _env(recommendations=[dict(GOOD_REC, effort="XL")]), False),
    ],
)
def test_sia_assertions(atype, expected, env, should_pass):
    result = run_assertion({"type": atype, "expected": expected}, _report(env))
    assert result["passed"] is should_pass, result["detail"]


def test_missing_envelope_fails_every_check():
    for atype, expected in (("sia_envelope_valid", True), ("sia_out_fields", LC_WRITES), ("sia_recommendations", True)):
        assert not run_assertion({"type": atype, "expected": expected}, "# Report\n\nno yaml")["passed"]


def test_gold_agreement_reads_yaml_booleans_as_verdicts():
    env = yaml.safe_load("out:\n  verdicts: {signal: yes, update: partial, convergence: no}\n")
    score, misses = sia_chain.gold_agreement(env, {"verdicts": {"signal": "yes", "update": "partial", "convergence": "no"}})
    assert (score, misses) == (1.0, [])


def test_gold_agreement_lists_are_sets_and_empty_means_none():
    env = {"out": {"fields": [{"field": "b"}, {"field": "a"}]}}
    assert sia_chain.gold_agreement(env, {"fields[].field": ["a", "b"]})[0] == 1.0
    assert sia_chain.gold_agreement({"out": {}}, {"claimVerdicts": []})[0] == 1.0
    assert sia_chain.gold_agreement(env, {"fields[].field": ["a"]})[0] == 0.0


# ---------------------------------------------------------------------------
# Fixtures, specs, skills
# ---------------------------------------------------------------------------


def _agents():
    return {p.stem: json.loads(p.read_text()) for p in sorted(AGENTS_DIR.glob("*.json"))}


def test_one_fixture_agent_per_deployment_type():
    types = sorted(a["deploymentType"] for a in _agents().values())
    assert types == sorted(sia_chain.DEPLOYMENT_TYPES)


@pytest.mark.parametrize("skill", CHAIN_SKILLS)
def test_spec_has_one_chain_case_per_agent(skill):
    spec = json.loads((REPO / f"tests/{skill}/test-spec.json").read_text())
    chain_cases = {c["fixture"].rsplit("/", 1)[-1][:-5] for c in spec["cases"] if c["id"].startswith("chain-")}
    assert chain_cases == set(_agents())


@pytest.mark.parametrize("skill", CHAIN_SKILLS)
def test_spec_requires_exactly_the_chain_writes(skill):
    spec = json.loads((REPO / f"tests/{skill}/test-spec.json").read_text())
    writes = next(link["writes"] for link in CHAIN if link["skill"] == skill)
    for case in spec["cases"]:
        for a in case["assertions"]:
            if a["type"] == "sia_out_fields":
                assert a["expected"] == writes, case["id"]


@pytest.mark.parametrize("skill", CHAIN_SKILLS)
def test_chain_skill_md_follows_conventions(skill):
    text = (REPO / f"skills/{skill}/SKILL.md").read_text()
    fm = yaml.safe_load(text.split("---", 2)[1])
    assert set(fm) == {"name", "description", "license"}, fm.keys()
    assert fm["name"] == skill
    for needle in ("Step 0", "sia:", f"skill: {skill}", "recommendations:", "at most seven", "Series and help: peleke.me"):
        assert needle in text, needle
    for path in next(link["writes"] for link in CHAIN if link["skill"] == skill):
        assert re.search(rf"\b{re.escape(path.split('.')[0].removesuffix('[]'))}:", text), path


# ---------------------------------------------------------------------------
# S2 gate: capture rule, metric in code, gold set (build rule, enforced here)
# ---------------------------------------------------------------------------

S2_KEYS = ("capture", "metric", "gold")


def s2_problems(spec: dict, skill: str) -> list[str]:
    s2 = spec.get("s2") or {}
    problems = [f"{skill}: s2.{k} missing or empty" for k in S2_KEYS if not str(s2.get(k, "")).strip()]
    if problems:
        return problems
    gold = REPO / s2["gold"]
    if not gold.is_file():
        return [f"{skill}: gold file {s2['gold']} not found"]
    rows = yaml.safe_load(gold.read_text()).get("rows", [])
    for row in rows:
        for key in ("agent", "drafted_by", "adjudicated_by", "out"):
            if key not in row:
                problems.append(f"{skill}: gold row {row.get('agent')} missing {key}")
    if {r.get("agent") for r in rows} != set(_agents()):
        problems.append(f"{skill}: gold rows don't cover every fixture agent")
    for fn in ("hard_check_score", "gold_agreement"):
        if f"sia_chain.{fn}" not in s2["metric"]:
            problems.append(f"{skill}: s2.metric doesn't name sia_chain.{fn}")
    return problems


@pytest.mark.parametrize("skill", CHAIN_SKILLS)
def test_s2_declared(skill):
    spec = json.loads((REPO / f"tests/{skill}/test-spec.json").read_text())
    assert s2_problems(spec, skill) == []


@pytest.mark.parametrize("key", S2_KEYS)
def test_s2_gate_fails_when_a_key_is_removed(key):
    spec = json.loads((REPO / "tests/gold-set/test-spec.json").read_text())
    del spec["s2"][key]
    assert s2_problems(spec, "gold-set")
