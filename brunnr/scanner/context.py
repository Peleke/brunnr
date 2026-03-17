"""ScanContext — pre-parsed, immutable view of SKILL.md content.

Computed once by the Pipeline, shared across all rules.
"""

from __future__ import annotations

from dataclasses import dataclass

from brunnr.frontmatter import extract_body, extract_description


@dataclass(frozen=True)
class ScanContext:
    """Immutable, pre-parsed SKILL.md content.

    Rules receive this instead of raw strings, avoiding redundant parsing.
    """

    raw: str
    body: str
    description: str

    @classmethod
    def from_content(cls, content: str) -> ScanContext:
        return cls(
            raw=content,
            body=extract_body(content),
            description=extract_description(content),
        )
