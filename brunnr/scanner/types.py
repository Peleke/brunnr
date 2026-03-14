"""Scanner domain types — Severity, ThreatClass, Finding, ScanResult."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum


class Severity(StrEnum):
    BLOCK = "block"
    FLAG = "flag"
    INFO = "info"
    CLEAN = "clean"


class ThreatClass(StrEnum):
    COMMAND_INJECTION = "command_injection"
    DATA_EXFILTRATION = "data_exfiltration"
    CREDENTIAL_THEFT = "credential_theft"
    PROMPT_OVERRIDE = "prompt_override"
    SUPPLY_CHAIN = "supply_chain"
    PRIVILEGE_ESCALATION = "privilege_escalation"
    STEGANOGRAPHIC = "steganographic"
    SEMANTIC_MISMATCH = "semantic_mismatch"


@dataclass
class Finding:
    """A single scanner finding."""

    threat_class: ThreatClass
    severity: Severity
    description: str
    evidence: str
    line: int | None = None


@dataclass
class ScanResult:
    """Result of scanning a SKILL.md file."""

    findings: list[Finding] = field(default_factory=list)

    @property
    def blocked(self) -> bool:
        return any(f.severity == Severity.BLOCK for f in self.findings)

    @property
    def flagged(self) -> bool:
        return any(f.severity == Severity.FLAG for f in self.findings)

    @property
    def clean(self) -> bool:
        return not self.findings

    @property
    def severity(self) -> Severity:
        if self.blocked:
            return Severity.BLOCK
        if self.flagged:
            return Severity.FLAG
        if self.findings:
            return Severity.INFO
        return Severity.CLEAN

    @property
    def block_reasons(self) -> list[str]:
        return [f.description for f in self.findings if f.severity == Severity.BLOCK]

    @property
    def flag_reasons(self) -> list[str]:
        return [f.description for f in self.findings if f.severity == Severity.FLAG]

    def to_dict(self) -> dict:
        return {
            "severity": self.severity,
            "blocked": self.blocked,
            "flagged": self.flagged,
            "finding_count": len(self.findings),
            "findings": [
                {
                    "threat_class": f.threat_class,
                    "severity": f.severity,
                    "description": f.description,
                    "evidence": f.evidence[:200],
                    "line": f.line,
                }
                for f in self.findings
            ],
        }
