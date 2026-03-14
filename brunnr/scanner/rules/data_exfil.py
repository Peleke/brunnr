"""Data exfiltration detection — reading secrets, embedding in output."""

from brunnr.scanner.pattern_rule import PatternRule
from brunnr.scanner.types import Severity, ThreatClass


class DataExfiltrationRule(PatternRule):
    name = "data_exfiltration"
    threat_class = ThreatClass.DATA_EXFILTRATION
    severity = Severity.BLOCK
    patterns = [
        (
            r"(?:cat|read|head|tail|less|more)\s+~?/\.ssh/(?:id_rsa|id_ed25519|authorized_keys|known_hosts)(?!\.pub)",
            "SSH key file read",
        ),
        (
            r"(?:include|embed|attach|send|post|upload).*(?:response|output|reply|message).*(?:ssh|key|secret|token|credential)",
            "exfiltrate secrets in response",
        ),
        (
            r"(?:response|output|reply).*(?:include|contain|embed).*(?:ssh|key|secret|token|credential)",
            "embed secrets in output",
        ),
        (
            r"curl\s+.*-d\s+.*(?:\$\(cat|<\(|@).*(?:\.ssh|\.env|\.aws|\.gnupg|\.npmrc)",
            "POST secret files to external URL",
        ),
        (r"(?:cat|read)\s+.*\.(?:pem|key|crt)\s", "reading PKI files"),
    ]
