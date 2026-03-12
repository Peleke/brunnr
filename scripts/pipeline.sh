#!/usr/bin/env bash
set -euo pipefail

# Brunnr pipeline — scan skills, report results, optionally trigger downstream.
# Usage:
#   scripts/pipeline.sh                 # full pipeline
#   scripts/pipeline.sh --scan-only     # scan only, no downstream
#   scripts/pipeline.sh --verbose       # verbose output

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"

SCAN_ONLY=false
VERBOSE=false

for arg in "$@"; do
  case "$arg" in
    --scan-only) SCAN_ONLY=true ;;
    --verbose)   VERBOSE=true ;;
    --full)      SCAN_ONLY=false ;;
    *)           echo "Unknown option: $arg"; exit 1 ;;
  esac
done

log() { echo "==> $*"; }

# Step 1: Security scan
log "Scanning all skills..."
SCAN_FLAGS="--strict"
if [ "$VERBOSE" = true ]; then
  SCAN_FLAGS="$SCAN_FLAGS --verbose"
fi

python3 "$ROOT_DIR/tests/scan-all-skills.py" $SCAN_FLAGS
SCAN_EXIT=$?

if [ $SCAN_EXIT -ne 0 ]; then
  log "Scan failed (exit $SCAN_EXIT). Aborting pipeline."
  exit $SCAN_EXIT
fi

log "Scan passed."

if [ "$SCAN_ONLY" = true ]; then
  log "Done (scan-only mode)."
  exit 0
fi

# Step 2: Export scan report
log "Exporting scan report..."
python3 "$ROOT_DIR/tests/scan-all-skills.py" --json > "$ROOT_DIR/tests/artifacts/scan-report.json"
log "Report saved to tests/artifacts/scan-report.json"

log "Pipeline complete."
