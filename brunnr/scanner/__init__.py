"""brunnr.scanner — 7-class deterministic SKILL.md security scanner.

Usage:
    from brunnr.scanner import scan_skill_md, ScanResult

    result = scan_skill_md(content)
    if result.blocked:
        print(f"BLOCKED: {result.block_reasons}")
    elif result.flagged:
        print(f"FLAGGED: {result.flag_reasons}")
    else:
        print("CLEAN")
"""

from brunnr.scanner.types import (  # noqa: F401
    Finding,
    ScanResult,
    Severity,
    ThreatClass,
)
from brunnr.scanner.pipeline import Pipeline  # noqa: F401

__all__ = ["scan_skill_md", "Finding", "ScanResult", "Severity", "ThreatClass", "Pipeline"]

_pipeline = Pipeline()


def scan_skill_md(content: str) -> ScanResult:
    """Scan SKILL.md content for security threats."""
    return _pipeline.scan(content)
