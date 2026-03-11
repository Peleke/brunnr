"""Compatibility shim — scanner has moved to brunnr.scanner."""

from brunnr.scanner import (  # noqa: F401
    Finding,
    ScanResult,
    Severity,
    ThreatClass,
    scan_skill_md,
)
