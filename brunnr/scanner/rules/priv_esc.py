"""Privilege escalation detection — sudo abuse, permission changes."""

from brunnr.scanner.pattern_rule import PatternRule
from brunnr.scanner.types import Severity, ThreatClass


class PrivilegeEscalationRule(PatternRule):
    name = "privilege_escalation"
    threat_class = ThreatClass.PRIVILEGE_ESCALATION
    severity = Severity.FLAG
    patterns = [
        (r"sudo\s+chmod\s+(?:-R\s+)?[67]77\s+/", "sudo chmod 777 on root paths"),
        (r"sudo\s+(?:chown|chgrp)\s+.*\s+/(?:etc|usr|var|bin|sbin)", "sudo ownership change on system dirs"),
        (
            r"(?:echo|cat|tee)\s+.*(?:>>?\s*)?/etc/(?:hosts|passwd|shadow|sudoers|crontab)",
            "modify system configuration files",
        ),
        (r"sudo\s+(?:bash|sh|su)\s", "sudo to shell"),
        (r"chmod\s+[ugo]?\+s\s", "setuid/setgid bit modification"),
        (r"crontab\s+-[lr]?\s*(?:<<|<\(|.*curl|.*wget)", "crontab modification with download"),
    ]
