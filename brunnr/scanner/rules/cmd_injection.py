"""Command injection detection — shell commands, reverse shells, base64 payloads."""

from brunnr.scanner.pattern_rule import PatternRule
from brunnr.scanner.types import Severity, ThreatClass


class CommandInjectionRule(PatternRule):
    name = "command_injection"
    threat_class = ThreatClass.COMMAND_INJECTION
    severity = Severity.BLOCK
    patterns = [
        (r"curl\s+[^\s]+\s*\|\s*(?:ba)?sh", "curl pipe to shell"),
        (r"wget\s+[^\s]+\s*(?:-O\s*-\s*)?\|\s*(?:ba)?sh", "wget pipe to shell"),
        (r"(?:bash|sh)\s+-[ci]\s+['\"].*(?:\/dev\/tcp|nc\s|ncat\s|netcat\s)", "reverse shell"),
        (r"nc\s+-[elp]+\s+.*\d{2,5}", "netcat listener"),
        (r"python[3]?\s+-c\s+['\"].*(?:socket|subprocess|os\.system)", "python inline execution"),
        (
            r"(?:echo|printf)\s+['\"]?[A-Za-z0-9+/]{20,}={0,2}['\"]?\s*\|\s*base64\s+-d\s*\|\s*(?:ba)?sh",
            "base64 decode to shell",
        ),
        (r"base64\s+-d\s*<<<?\s*['\"]?[A-Za-z0-9+/]{20,}", "base64 decode suspicious payload"),
        (r"rm\s+-rf\s+[/~]", "recursive delete from root or home"),
        (r"mkfifo\s+/tmp/", "named pipe creation (common in reverse shells)"),
        (r"eval\s*\$\(", "eval with command substitution"),
    ]
