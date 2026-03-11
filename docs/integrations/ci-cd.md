# CI/CD Integration

brunnr is designed for CI pipelines. The scanner requires no API keys, no network access, and no third-party dependencies. It runs in milliseconds and uses deterministic exit codes.

---

## GitHub Actions

### Scan only (recommended for most projects)

```yaml
name: Skill Security Scan

on:
  push:
    paths:
      - 'skills/**'
  pull_request:
    paths:
      - 'skills/**'

jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install brunnr
        run: pip install brunnr

      - name: Scan skills
        run: brunnr scan --strict --json > scan-results.json

      - name: Upload results
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: scan-results
          path: scan-results.json
```

### Full pipeline (scan + eval)

```yaml
name: Skill Pipeline

on:
  push:
    paths:
      - 'skills/**'
      - 'tests/**'
  pull_request:
    paths:
      - 'skills/**'
      - 'tests/**'

jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install brunnr
        run: pip install brunnr

      - name: Security scan
        run: brunnr scan --strict

  eval:
    needs: scan
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install brunnr with eval support
        run: pip install brunnr[eval]

      - name: Run evaluations
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: brunnr pipeline
```

!!! warning "API key required for evals"
    The `eval` step requires an `ANTHROPIC_API_KEY` secret in your repository settings. The scan step does not require any secrets.

---

## Scan-only pipeline

For projects that don't need LLM evaluation, use the scan-only mode:

```yaml
- name: Security scan
  run: brunnr pipeline --scan-only
```

This is the fastest option. No API calls, no secrets, runs in under a second.

---

## Docker

### Minimal Dockerfile

```dockerfile
FROM python:3.12-slim
RUN pip install --no-cache-dir brunnr
WORKDIR /workspace
ENTRYPOINT ["brunnr"]
```

### Usage

```bash
# Build
docker build -t brunnr .

# Scan a local directory
docker run --rm -v "$(pwd)/skills:/workspace/skills" brunnr scan

# Full pipeline
docker run --rm \
  -v "$(pwd):/workspace" \
  -e ANTHROPIC_API_KEY \
  brunnr pipeline
```

---

## Exit codes reference

All brunnr commands use consistent exit codes suitable for CI:

| Command | Exit 0 | Exit 1 |
|---------|--------|--------|
| `brunnr scan` | All CLEAN (or FLAG without `--strict`) | Any BLOCK (or FLAG with `--strict`), or no files |
| `brunnr scan --strict` | All CLEAN | Any BLOCK or FLAG |
| `brunnr eval` | All assertions pass | Any assertion fails |
| `brunnr pipeline` | Scan passes and evals pass | Scan BLOCK or eval failure |
| `brunnr pipeline --scan-only` | Scan passes | Scan BLOCK or no files |

---

## JSON output for CI tools

Use `--json` with `brunnr scan` for machine-readable output:

```bash
brunnr scan --json --strict
```

```json
{
  "total": 3,
  "blocked": 0,
  "flagged": 1,
  "clean": 2,
  "skills": [
    {
      "file": "skills/ax-rubric/SKILL.md",
      "severity": "clean",
      "blocked": false,
      "flagged": false,
      "finding_count": 0,
      "findings": []
    },
    {
      "file": "skills/infra-setup/SKILL.md",
      "severity": "flag",
      "blocked": false,
      "flagged": true,
      "finding_count": 1,
      "findings": [
        {
          "threat_class": "semantic_mismatch",
          "severity": "flag",
          "description": "sensitive path reference without security context",
          "evidence": "~/.ssh/",
          "line": 42
        }
      ]
    }
  ]
}
```

You can parse this with `jq` in your CI scripts:

```bash
# Fail if any blocked skills
brunnr scan --json | jq -e '.blocked == 0'

# Get list of flagged files
brunnr scan --json | jq -r '.skills[] | select(.flagged) | .file'
```

---

## Pre-commit hook

Add brunnr as a pre-commit check for skill files:

```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: brunnr-scan
        name: brunnr security scan
        entry: brunnr scan --strict
        language: python
        additional_dependencies: ['brunnr']
        files: 'skills/.*\.md$'
        pass_filenames: true
```

Or as a simple git hook:

```bash
#!/bin/sh
# .git/hooks/pre-commit

if git diff --cached --name-only | grep -q '^skills/'; then
  brunnr scan --strict
fi
```

---

## GitLab CI

```yaml
skill-scan:
  image: python:3.12-slim
  script:
    - pip install brunnr
    - brunnr scan --strict --json > scan-results.json
  artifacts:
    reports:
      dotenv: scan-results.json
  rules:
    - changes:
        - skills/**
```
