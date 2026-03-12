#!/usr/bin/env bash
#
# Scaffold test infrastructure for a new skill.
#
# Usage:
#   ./tests/lib/new-skill-test.sh <skill-slug>
#
# Creates:
#   tests/<skill-slug>/test-spec.json     (template)
#   tests/<skill-slug>/fixtures/           (empty directory)
#
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"

if [ -z "${1:-}" ]; then
  echo "Usage: $0 <skill-slug>"
  echo "Example: $0 ax-rubric"
  exit 1
fi

SKILL_SLUG="$1"
SKILL_DIR="$REPO_ROOT/skills/$SKILL_SLUG"
TEST_DIR="$REPO_ROOT/tests/$SKILL_SLUG"
FIXTURES_DIR="$TEST_DIR/fixtures"

if [ ! -f "$SKILL_DIR/SKILL.md" ]; then
  echo "ERROR: Skill not found at $SKILL_DIR/SKILL.md"
  echo "Create the skill first, then scaffold tests."
  exit 1
fi

if [ -d "$TEST_DIR" ]; then
  echo "WARNING: Test directory already exists at $TEST_DIR"
  echo "Aborting to avoid overwriting."
  exit 1
fi

mkdir -p "$FIXTURES_DIR"

cat > "$TEST_DIR/test-spec.json" << 'SPEC'
{
  "version": "1.0",
  "skill": "SKILL_SLUG_PLACEHOLDER",
  "description": "TODO: Describe what this test suite validates.",
  "model": "claude-sonnet-4-20250514",
  "cases": [
    {
      "id": "example-01",
      "description": "TODO: Describe this test case",
      "fixture": "fixtures/example-01.json",
      "assertions": [
        { "type": "format_valid", "expected": true },
        { "type": "contains", "expected": "TODO: expected string in output" }
      ]
    }
  ]
}
SPEC

# Replace placeholder
sed -i '' "s/SKILL_SLUG_PLACEHOLDER/$SKILL_SLUG/" "$TEST_DIR/test-spec.json" 2>/dev/null || \
  sed -i "s/SKILL_SLUG_PLACEHOLDER/$SKILL_SLUG/" "$TEST_DIR/test-spec.json"

cat > "$FIXTURES_DIR/example-01.json" << 'FIXTURE'
{
  "input": "TODO: The user message to send to the skill",
  "description": "TODO: What this fixture represents",
  "rationale": "TODO: Why you expect the output you expect"
}
FIXTURE

echo "Scaffolded test infrastructure for '$SKILL_SLUG':"
echo "  $TEST_DIR/test-spec.json"
echo "  $FIXTURES_DIR/example-01.json"
echo ""
echo "Next steps:"
echo "  1. Edit test-spec.json to define your test cases"
echo "  2. Create fixture files in fixtures/"
echo "  3. Run: python tests/harness.py --skill $SKILL_SLUG --dry-run"
echo "  4. Run: python tests/harness.py --skill $SKILL_SLUG"
