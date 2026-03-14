"""Zero-width character detection — steganographic hiding in Unicode."""

from __future__ import annotations

from brunnr.scanner.context import ScanContext
from brunnr.scanner.types import Finding, Severity, ThreatClass

_ZERO_WIDTH_CHARS = "\u200b\u200c\u200d\u2060\ufeff\u200e\u200f\u202a\u202b\u202c\u202d\u202e"


class ZeroWidthRule:
    name = "zero_width"

    def scan(self, ctx: ScanContext) -> list[Finding]:
        findings: list[Finding] = []
        for i, char in enumerate(ctx.raw):
            if char in _ZERO_WIDTH_CHARS:
                line_num = ctx.raw[:i].count("\n") + 1
                findings.append(
                    Finding(
                        threat_class=ThreatClass.STEGANOGRAPHIC,
                        severity=Severity.FLAG,
                        description=f"zero-width character U+{ord(char):04X}",
                        evidence=f"...{ctx.raw[max(0, i - 10) : i + 10]}...",
                        line=line_num,
                    )
                )
        return findings
