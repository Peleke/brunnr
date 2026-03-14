"""Steganographic pattern detection — hidden commands in HTML/CDATA."""

from brunnr.scanner.pattern_rule import PatternRule
from brunnr.scanner.types import Severity, ThreatClass


class StegPatternRule(PatternRule):
    name = "steg_patterns"
    threat_class = ThreatClass.STEGANOGRAPHIC
    severity = Severity.FLAG
    patterns = [
        (r"<!--.*(?:script|eval|exec|system|curl|wget|fetch).*-->", "hidden command in HTML comment"),
        (r"<!\[CDATA\[.*(?:script|eval|exec).*\]\]>", "hidden command in CDATA"),
    ]
