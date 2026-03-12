# brunnr eval

Run the evaluation harness for a skill. Sends test fixtures to a Claude model and checks the output against structured assertions.

---

## Usage

```bash
brunnr eval <skill> [--model MODEL] [-o PATH] [--dry-run]
```

---

## Prerequisites

The eval command requires the `anthropic` Python package:

```bash
pip install brunnr[eval]
```

You also need the `ANTHROPIC_API_KEY` environment variable set:

```bash
export ANTHROPIC_API_KEY=sk-ant-...
```

---

## Arguments

| Argument | Description |
|----------|-------------|
| `skill` | Skill slug to evaluate (e.g., `ax-rubric`). Must exist in `skills/<slug>/SKILL.md`. |

## Flags

| Flag | Short | Description |
|------|-------|-------------|
| `--model` | | Claude model to use. Default: `claude-sonnet-4-20250514` |
| `--output` | `-o` | Path to write JSON results file |
| `--dry-run` | | Validate fixtures without making API calls |

---

## How it works

### 1. Load the skill prompt

brunnr reads the SKILL.md from `skills/<slug>/SKILL.md` and uses it as the system prompt.

### 2. Load test fixtures

brunnr reads `tests/<slug>/test-spec.json` which defines test cases:

```json
{
  "cases": [
    {
      "id": "case-1",
      "description": "Score a bad description",
      "fixture": "fixtures/bad-description.json",
      "assertions": [
        {"type": "score_range", "expected": {"min": 1, "max": 2}},
        {"type": "has_table", "expected": true},
        {"type": "has_rewrite", "expected": true}
      ]
    }
  ]
}
```

Each case references an optional fixture file with input data. The fixture's `input` or `description` field becomes the user message sent to the model.

### 3. Call Claude

For each test case, brunnr sends the skill prompt as the system message and the fixture input as the user message. The model generates a response.

### 4. Run assertions

brunnr checks the model's output against each assertion in the test case.

---

## Assertion types

| Type | Expected | What it checks |
|------|----------|----------------|
| `score_range` | `{"min": N, "max": N}` | Extracts `Score: X/5` from output, checks X is in range |
| `has_table` | `true` or `false` | Checks for a markdown table (`\|...\|...\|...\|`) in output |
| `has_rewrite` | `true` or `false` | Checks for the word "rewrite" or "rewritten" in output |
| `contains` | `"string"` | Case-insensitive substring check |
| `format_valid` | (none) | Checks for markdown headers, a score line, and a criteria table |
| `criteria_pass` | `["criterion1", ...]` | Extracts criteria table rows, checks listed criteria have "pass" |
| `criteria_fail` | `["criterion1", ...]` | Extracts criteria table rows, checks listed criteria have "fail" |

---

## Examples

### Dry run (validate without API calls)

```bash
brunnr eval ax-rubric --dry-run
```

```
=== brunnr eval: ax-rubric ===
  2 test cases, model: claude-sonnet-4-20250514

  [case-1] Score a bad description
    DRY RUN - skipped

  [case-2] Score a good description
    DRY RUN - skipped

=== 0/0 passed (2 skipped) ===
```

### Full evaluation

```bash
brunnr eval ax-rubric
```

```
=== brunnr eval: ax-rubric ===
  2 test cases, model: claude-sonnet-4-20250514

  [case-1] Score a bad description
    PASS: [score_range] Score 1 in [1, 2]
    PASS: [has_table] Table found
    PASS: [has_rewrite] Rewrite found

  [case-2] Score a good description
    PASS: [score_range] Score 5 in [4, 5]

=== 2/2 passed ===
```

### Save results to file

```bash
brunnr eval ax-rubric -o results/ax-rubric.json
```

The output JSON includes the model's response (truncated to 2000 chars), assertion results, and timing:

```json
{
  "skill": "ax-rubric",
  "model": "claude-sonnet-4-20250514",
  "summary": {"pass": 2, "fail": 0, "skipped": 0},
  "cases": [
    {
      "case_id": "case-1",
      "output": "### knowledge_base_query\n\n**Score: 1/5**\n...",
      "assertions": [
        {"assertion": {"type": "score_range", "expected": {"min": 1, "max": 2}}, "passed": true, "detail": "Score 1 in [1, 2]"}
      ],
      "duration_s": 3.42,
      "all_passed": true
    }
  ]
}
```

### Use a different model

```bash
brunnr eval ax-rubric --model claude-opus-4-20250514
```

---

## Writing test specs

See [Writing Skills](../skills/writing-skills.md) for details on how to create test specifications and fixtures for your skills.

---

## Exit codes

| Code | Meaning |
|------|---------|
| `0` | All test cases passed |
| `1` | At least one test case failed, or skill/fixtures not found |
