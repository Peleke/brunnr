"""Supply chain poisoning detection — malicious hooks, custom indexes."""

from brunnr.scanner.pattern_rule import PatternRule
from brunnr.scanner.types import Severity, ThreatClass


class SupplyChainRule(PatternRule):
    name = "supply_chain"
    threat_class = ThreatClass.SUPPLY_CHAIN
    severity = Severity.FLAG
    patterns = [
        (
            r"(?:postinstall|preinstall|prepublish)\s*[\"':]\s*.*(?:curl|wget|fetch|node\s+-e|python)",
            "malicious install hook",
        ),
        (r"--(?:index-url|extra-index-url)\s+(?!https://pypi\.org)https?://", "custom PyPI index (not pypi.org)"),
        (r"npm\s+(?:install|i)\s+.*--registry\s+(?!https://registry\.npmjs\.org)", "custom npm registry"),
        (r"pip\s+install\s+.*-f\s+https?://(?!pypi\.org)", "pip install from custom find-links"),
        (
            r"(?:git\s+clone|pip\s+install\s+git\+)(?:https?://(?!github\.com|gitlab\.com|bitbucket\.org))",
            "install from unknown git host",
        ),
    ]
