"""Keyword divergence detection — Jaccard similarity between description and body."""

from __future__ import annotations

import re

from brunnr.scanner.context import ScanContext
from brunnr.scanner.types import Finding, Severity, ThreatClass

_STOPWORDS = {
    "a", "an", "the", "and", "or", "but", "in", "on", "at", "to", "for",
    "of", "with", "by", "from", "is", "are", "was", "were", "be", "been",
    "being", "have", "has", "had", "do", "does", "did", "will", "would",
    "could", "should", "may", "might", "shall", "can", "it", "its",
    "this", "that", "these", "those", "i", "you", "he", "she", "we",
    "they", "me", "him", "her", "us", "them", "my", "your", "his",
    "our", "their", "not", "no", "if", "then", "else", "when", "while",
    "as", "so", "than", "each", "every", "all", "any", "some", "such",
    "only", "also", "very", "just", "about", "into", "through", "during",
    "before", "after", "above", "below", "up", "down", "out", "off",
    "over", "under", "between", "same", "other", "new", "use", "using",
}


def _tokenize(text: str) -> set[str]:
    words = re.findall(r"[a-z][a-z0-9_-]+", text.lower())
    return {w for w in words if len(w) > 2 and w not in _STOPWORDS}


class KeywordDivergenceRule:
    name = "keyword_divergence"

    def scan(self, ctx: ScanContext) -> list[Finding]:
        if not ctx.description:
            return []

        desc_tokens = _tokenize(ctx.description)
        body_tokens = _tokenize(ctx.body)

        if not desc_tokens or not body_tokens:
            return []

        intersection = desc_tokens & body_tokens
        union = desc_tokens | body_tokens
        jaccard = len(intersection) / len(union) if union else 0

        if jaccard < 0.02 and len(body_tokens) > 20:
            return [
                Finding(
                    threat_class=ThreatClass.SEMANTIC_MISMATCH,
                    severity=Severity.FLAG,
                    description=f"keyword divergence: description/body Jaccard={jaccard:.3f} (threshold: 0.02)",
                    evidence=f"desc tokens: {sorted(desc_tokens)[:10]}, body sample: {sorted(body_tokens)[:10]}",
                )
            ]
        return []
