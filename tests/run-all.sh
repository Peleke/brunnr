#!/usr/bin/env bash
#
# Run all skill tests locally.
#
# Usage:
#   ./tests/run-all.sh              # Run all tests (requires ANTHROPIC_API_KEY)
#   ./tests/run-all.sh --dry-run    # Validate fixtures without API calls
#   ./tests/run-all.sh ax-rubric    # Run tests for a single skill
#
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

DRY_RUN=""
SKILL_FILTER=""

for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY_RUN="--dry-run" ;;
    *) SKILL_FILTER="$arg" ;;
  esac
done

# Step 0: Security Scan (deterministic, no API calls)
echo "=== Step 0: SKILL.md Security Scan ==="
python3 tests/scan-all-skills.py
echo ""

# Step 1: Frontmatter lint
echo "=== Step 1: Frontmatter Lint ==="
ERRORS=0
TOTAL=0

for skill_md in skills/*/SKILL.md; do
  [ -f "$skill_md" ] || continue
  TOTAL=$((TOTAL + 1))
  SKILL_DIR=$(dirname "$skill_md")
  SKILL_SLUG=$(basename "$SKILL_DIR")

  # Extract frontmatter
  FRONTMATTER=$(sed -n '/^---$/,/^---$/p' "$skill_md" | sed '1d;$d')

  NAME=$(echo "$FRONTMATTER" | grep "^name:" | sed 's/^name: *//' || true)
  DESC=$(echo "$FRONTMATTER" | grep "^description:" | head -1 || true)

  if [ -z "$NAME" ]; then
    echo "  FAIL: $skill_md -- missing 'name'"
    ERRORS=$((ERRORS + 1))
  elif [ "$NAME" != "$SKILL_SLUG" ]; then
    echo "  FAIL: $skill_md -- name '$NAME' != directory '$SKILL_SLUG'"
    ERRORS=$((ERRORS + 1))
  else
    echo "  OK: $NAME"
  fi

  if [ -z "$DESC" ]; then
    echo "  FAIL: $skill_md -- missing 'description'"
    ERRORS=$((ERRORS + 1))
  fi
done

echo "  $TOTAL skills checked, $ERRORS errors"
if [ $ERRORS -gt 0 ]; then
  echo "  Frontmatter lint FAILED"
  exit 1
fi
echo ""

# Step 2: Discover and run skill evals
echo "=== Step 2: Skill Evals ==="
OVERALL_EXIT=0

for test_dir in tests/*/; do
  [ -d "$test_dir" ] || continue
  SKILL_SLUG=$(basename "$test_dir")

  # Skip if filtering to a specific skill
  if [ -n "$SKILL_FILTER" ] && [ "$SKILL_SLUG" != "$SKILL_FILTER" ]; then
    continue
  fi

  # Skip non-skill directories (like lib/)
  if [ ! -f "skills/$SKILL_SLUG/SKILL.md" ]; then
    continue
  fi

  if [ ! -f "$test_dir/test-spec.json" ]; then
    echo "  SKIP: $SKILL_SLUG (no test-spec.json)"
    continue
  fi

  echo ""
  python3 tests/harness.py \
    --skill "$SKILL_SLUG" \
    --output "tests/$SKILL_SLUG/results.json" \
    $DRY_RUN || OVERALL_EXIT=1
done

echo ""
if [ $OVERALL_EXIT -eq 0 ]; then
  echo "=== All evals passed ==="
else
  echo "=== Some evals FAILED ==="
  exit 1
fi
