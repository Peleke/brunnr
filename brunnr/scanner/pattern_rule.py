"""PatternRule — shared base for regex-based scanner rules.

Subclasses set class attributes (name, threat_class, severity, patterns)
and inherit the scan() implementation.
"""

from __future__ import annotations

import re

from brunnr.scanner.context import ScanContext
from brunnr.scanner.types import Finding, Severity, ThreatClass


class PatternRule:
    """A rule that runs regex patterns against the body text."""

    name: str
    threat_class: ThreatClass
    severity: Severity
    patterns: list[tuple[str, str]]  # (regex_str, description)

    def __init_subclass__(cls, **kwargs: object) -> None:
        super().__init_subclass__(**kwargs)
        for attr in ("name", "threat_class", "severity", "patterns"):
            if attr not in cls.__dict__:
                raise TypeError(f"{cls.__name__} must define class attribute '{attr}'")

    def scan(self, ctx: ScanContext) -> list[Finding]:
        findings: list[Finding] = []
        for pattern, desc in self.patterns:
            for match in re.finditer(pattern, ctx.body, re.IGNORECASE | re.MULTILINE):
                line_num = ctx.body[: match.start()].count("\n") + 1
                findings.append(
                    Finding(
                        threat_class=self.threat_class,
                        severity=self.severity,
                        description=desc,
                        evidence=match.group(0),
                        line=line_num,
                    )
                )
        return findings
