"""Shared frontmatter parsing for SKILL.md files."""

from __future__ import annotations

import re


def parse_frontmatter(text: str) -> dict[str, str]:
    """Extract YAML frontmatter from a SKILL.md file.

    Returns a flat dict of key-value pairs. Values are stripped of quotes.
    """
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    fm = {}
    for line in parts[1].strip().splitlines():
        if ":" in line:
            key, val = line.split(":", 1)
            fm[key.strip()] = val.strip().strip('"').strip("'")
    return fm


def extract_body(content: str) -> str:
    """Extract body text after frontmatter."""
    match = re.match(r"^---\s*\n.*?\n---\s*\n?(.*)", content, re.DOTALL)
    return match.group(1) if match else content


def extract_description(content: str) -> str:
    """Extract description from frontmatter."""
    match = re.search(r"^description:\s*[\"']?(.+?)[\"']?\s*$", content, re.MULTILINE)
    return match.group(1) if match else ""
