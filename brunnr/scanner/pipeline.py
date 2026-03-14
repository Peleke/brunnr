"""Pipeline — sequential rule executor."""

from __future__ import annotations

from brunnr.scanner.context import ScanContext
from brunnr.scanner.types import ScanResult


class Pipeline:
    """Runs registered rules against content, collects findings."""

    def __init__(self, rules: list | None = None) -> None:
        if rules is None:
            from brunnr.scanner.rules import DEFAULT_RULES

            rules = [cls() for cls in DEFAULT_RULES]
        self._rules = list(rules)

    def scan(self, content: str) -> ScanResult:
        ctx = ScanContext.from_content(content)
        result = ScanResult()
        for rule in self._rules:
            findings = rule.scan(ctx)
            result.findings.extend(findings)
        return result
