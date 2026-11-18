"""Variation selector detection — byte-level payloads hidden in invisible Unicode.

The Glassworm technique maps every byte to one variation selector:
bytes 0-15 to U+FE00-U+FE0F and bytes 16-255 to U+E0100-U+E01EF. A payload
is therefore a run of invisible selectors.

Legitimate text uses one selector after a visible base character: emoji
presentation (U+FE0F, as in "✍️"), text presentation (U+FE0E), standardized
variants (U+FE00-U+FE0D), or ideographic variants (U+E0100-U+E01EF after a
CJK ideograph). This rule flags what that usage never produces: two or more
selectors in a row, or a supplementary selector that does not follow a CJK
ideograph.
"""

from __future__ import annotations

from brunnr.scanner.context import ScanContext
from brunnr.scanner.types import Finding, Severity, ThreatClass


def _is_selector(ch: str) -> bool:
    cp = ord(ch)
    return 0xFE00 <= cp <= 0xFE0F or 0xE0100 <= cp <= 0xE01EF


def _is_supplementary_selector(ch: str) -> bool:
    return 0xE0100 <= ord(ch) <= 0xE01EF


def _is_cjk_ideograph(ch: str) -> bool:
    cp = ord(ch)
    return (
        0x3400 <= cp <= 0x4DBF
        or 0x4E00 <= cp <= 0x9FFF
        or 0xF900 <= cp <= 0xFAFF
        or 0x20000 <= cp <= 0x3134F
    )


class VariationSelectorRule:
    name = "variation_selectors"

    def scan(self, ctx: ScanContext) -> list[Finding]:
        findings: list[Finding] = []
        text = ctx.raw
        i = 0
        while i < len(text):
            if not _is_selector(text[i]):
                i += 1
                continue
            start = i
            while i < len(text) and _is_selector(text[i]):
                i += 1
            run = i - start
            base = text[start - 1] if start > 0 else ""
            lone_supplementary = (
                run == 1
                and _is_supplementary_selector(text[start])
                and not _is_cjk_ideograph(base)
            )
            if run >= 2 or lone_supplementary:
                findings.append(
                    Finding(
                        threat_class=ThreatClass.STEGANOGRAPHIC,
                        severity=Severity.FLAG,
                        description=(
                            f"{run} consecutive variation selector(s) starting at "
                            f"U+{ord(text[start]):04X}; can encode {run} hidden byte(s)"
                        ),
                        evidence=f"...{text[max(0, start - 10) : start]}"
                        f"<{run} invisible>{text[i : i + 10]}...",
                        line=text[:start].count("\n") + 1,
                    )
                )
        return findings
