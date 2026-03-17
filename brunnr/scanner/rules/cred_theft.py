"""Credential theft detection — env/key enumeration, dotenv reads."""

from brunnr.scanner.pattern_rule import PatternRule
from brunnr.scanner.types import Severity, ThreatClass


class CredentialTheftRule(PatternRule):
    name = "credential_theft"
    threat_class = ThreatClass.CREDENTIAL_THEFT
    severity = Severity.BLOCK
    patterns = [
        (
            r"(?:env|printenv|set)\s*\|\s*grep\s+(?:KEY|SECRET|TOKEN|PASS|API|AUTH|CRED)",
            "grep environment for credentials",
        ),
        (r"(?:cat|read|head|source|\.)\s+\.env\b", "read .env file"),
        (
            r"(?:cat|read|head)\s+.*(?:credentials\.json|\.aws/credentials|\.netrc|\.npmrc)",
            "read credential files",
        ),
        (
            r"\$(?:AWS_SECRET|API_KEY|AUTH_TOKEN|DATABASE_URL|OPENAI_API_KEY|ANTHROPIC_API_KEY|SECRET_KEY)",
            "reference to sensitive environment variables",
        ),
        (r"printenv\s+(?:.*KEY|.*SECRET|.*TOKEN|.*PASS)", "printenv for credentials"),
        (r"keychain\s+.*(?:export|dump|list)", "keychain credential access"),
    ]
