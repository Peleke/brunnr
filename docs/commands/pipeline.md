# brunnr pipeline

Run the full scan + eval pipeline in one command. The pipeline first scans all skills for security threats, then runs evaluations for any skills that have test fixtures.

---

## Usage

```bash
brunnr pipeline [--scan-only] [--verbose]
```

---

## Flags

| Flag | Description |
|------|-------------|
| `--scan-only` | Run only the security scan step, skip evaluations |
| `--verbose` | Show detailed findings during the scan step |

---

## How it works

The pipeline runs two steps sequentially:

### Step 1: Security scan

Discovers all `SKILL.md` files in the `skills/` directory and scans each one. If any file has BLOCK-severity findings, the pipeline fails immediately and does not proceed to evals.

### Step 2: Skill evaluations

Discovers skills that have both:

- A `SKILL.md` in `skills/<slug>/`
- A `test-spec.json` in `tests/<slug>/`

For each evaluable skill, runs `brunnr eval` with the default model (`claude-sonnet-4-20250514`) and writes results to `tests/<slug>/results.json`.

---

## Examples

### Full pipeline

```bash
brunnr pipeline
```

```
=== brunnr pipeline ===

Step 1: Security scan...
  CLEAN  ax-rubric

Scan passed (1 files).

Step 2: Skill evaluations...
=== brunnr eval: ax-rubric ===
  2 test cases, model: claude-sonnet-4-20250514

  [case-1] Score a bad description
    PASS: [score_range] Score 1 in [1, 2]
    PASS: [has_table] Table found

  [case-2] Score a good description
    PASS: [score_range] Score 5 in [4, 5]

=== 2/2 passed ===

Pipeline complete.
```

### Scan-only mode

```bash
brunnr pipeline --scan-only
```

```
=== brunnr pipeline ===

Step 1: Security scan...
  CLEAN  ax-rubric

Scan passed (1 files).
Done (scan-only mode).
```

### Verbose scan

```bash
brunnr pipeline --verbose
```

```
=== brunnr pipeline ===

Step 1: Security scan...
  FLAG   suspicious-skill
         [supply_chain] custom PyPI index (not pypi.org)
  CLEAN  ax-rubric

Scan passed (2 files).

Step 2: Skill evaluations...
...
```

!!! note "Verbose only affects the scan step"
    The `--verbose` flag adds detail to the scan output. Eval output always shows assertion results.

---

## Pipeline failure

The pipeline fails (exit code `1`) in three cases:

1. **No SKILL.md files found** -- There is nothing to scan.
2. **BLOCK findings in scan** -- Dangerous patterns were detected. The pipeline stops before running evals.
3. **Eval failures** -- At least one test case assertion failed.

FLAG findings in the scan step do **not** cause pipeline failure. Use `brunnr scan --strict` separately if you want to fail on flags.

---

## Exit codes

| Code | Meaning |
|------|---------|
| `0` | Scan passed, all evals passed (or no evals to run) |
| `1` | Scan found BLOCK findings, eval failures detected, or no files found |

---

## CI usage

The pipeline command is designed for CI environments. See [CI/CD Integration](../integrations/ci-cd.md) for GitHub Actions examples.

```bash
# In CI: run the full pipeline with exit code propagation
brunnr pipeline --scan-only  # fast, no API calls needed
```
