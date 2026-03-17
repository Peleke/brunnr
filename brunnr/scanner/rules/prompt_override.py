"""Prompt override detection — jailbreaks, instruction bypass."""

from brunnr.scanner.pattern_rule import PatternRule
from brunnr.scanner.types import Severity, ThreatClass


class PromptOverrideRule(PatternRule):
    name = "prompt_override"
    threat_class = ThreatClass.PROMPT_OVERRIDE
    severity = Severity.BLOCK
    patterns = [
        (
            r"ignore\s+(?:all\s+)?(?:previous|prior|above|earlier)\s+(?:instructions|rules|guidelines|directives|constraints)",
            "ignore previous instructions",
        ),
        (
            r"you\s+are\s+now\s+(?:in\s+)?(?:unrestricted|unfiltered|jailbreak|DAN|developer)\s+mode",
            "unrestricted mode activation",
        ),
        (
            r"(?:new|override|replace|overwrite)\s+(?:system\s+)?(?:prompt|instructions|rules)",
            "system prompt override",
        ),
        (
            r"disregard\s+(?:all\s+)?(?:safety|ethical|content)\s+(?:guidelines|rules|filters|policies)",
            "disregard safety guidelines",
        ),
        (
            r"(?:act|behave|respond)\s+(?:as\s+if|like)\s+(?:you\s+have\s+)?no\s+(?:restrictions|limits|rules|constraints)",
            "act without restrictions",
        ),
        (
            r"do\s+not\s+(?:follow|obey|adhere\s+to)\s+(?:any|your)\s+(?:rules|guidelines|instructions|safety)",
            "do not follow rules",
        ),
    ]
