"""URL domain allowlist check — flags non-allowlisted domains."""

from __future__ import annotations

import re
from urllib.parse import urlparse

from brunnr.scanner.context import ScanContext
from brunnr.scanner.types import Finding, Severity, ThreatClass

_URL_DOMAIN_ALLOWLIST = {
    "github.com",
    "gitlab.com",
    "bitbucket.org",
    "docs.python.org",
    "docs.astral.sh",
    "pypi.org",
    "npmjs.com",
    "npmjs.org",
    "registry.npmjs.org",
    "developer.mozilla.org",
    "stackoverflow.com",
    "wikipedia.org",
    "en.wikipedia.org",
    "anthropic.com",
    "docs.anthropic.com",
    "openai.com",
    "platform.openai.com",
    "agentskills.io",
    "docs.openclaw.ai",
    "clawhub.ai",
    "example.com",
    "example.org",
}

_URL_RE = re.compile(r"https?://[^\s\)\]\"'`>]+")


class UrlDomainRule:
    name = "url_domains"

    def scan(self, ctx: ScanContext) -> list[Finding]:
        findings: list[Finding] = []
        for match in _URL_RE.finditer(ctx.body):
            url = match.group(0).rstrip(".,;:!?)")
            try:
                parsed = urlparse(url)
                domain = parsed.netloc.lower()
                if ":" in domain:
                    domain = domain.split(":")[0]
                allowed = any(
                    domain == d or domain.endswith("." + d) for d in _URL_DOMAIN_ALLOWLIST
                )
                if not allowed and domain:
                    line_num = ctx.body[: match.start()].count("\n") + 1
                    findings.append(
                        Finding(
                            threat_class=ThreatClass.SEMANTIC_MISMATCH,
                            severity=Severity.INFO,
                            description=f"URL to non-allowlisted domain: {domain}",
                            evidence=url[:100],
                            line=line_num,
                        )
                    )
            except Exception:
                pass
        return findings
