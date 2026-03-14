"""Centralized registry interaction for brunnr CLI."""

from __future__ import annotations

import json
from urllib.request import urlopen, Request
from urllib.error import URLError

from brunnr.frontmatter import parse_frontmatter

_GITHUB_RAW = "https://raw.githubusercontent.com"


def fetch(url: str) -> str | None:
    """Fetch a URL and return text content, or None on failure."""
    try:
        req = Request(url, headers={"User-Agent": "brunnr-cli"})
        with urlopen(req, timeout=15) as resp:
            return resp.read().decode("utf-8")
    except (URLError, OSError):
        return None


def registry_base(registry: str) -> str:
    """Convert a GitHub repo URL to raw content base URL."""
    if "github.com" in registry:
        parts = registry.rstrip("/").replace("https://github.com/", "").split("/")
        if len(parts) >= 2:
            return f"{_GITHUB_RAW}/{parts[0]}/{parts[1]}/main"
    return registry.rstrip("/")


def list_skills(base: str) -> list[str]:
    """List available skills from registry (via GitHub API)."""
    parts = base.replace(f"{_GITHUB_RAW}/", "").split("/")
    if len(parts) >= 3:
        api_url = f"https://api.github.com/repos/{parts[0]}/{parts[1]}/contents/skills"
        content = fetch(api_url)
        if content:
            entries = json.loads(content)
            return [e["name"] for e in entries if e["type"] == "dir"]
    return []


def fetch_skill_content(base: str, slug: str) -> str | None:
    """Fetch SKILL.md content for a skill from the registry."""
    url = f"{base}/skills/{slug}/SKILL.md"
    return fetch(url)


def fetch_skill_metadata(base: str, slug: str) -> dict[str, str] | None:
    """Fetch and parse frontmatter metadata for a skill."""
    content = fetch_skill_content(base, slug)
    if content is None:
        return None
    fm = parse_frontmatter(content)
    if not fm:
        fm = {"name": slug}
    return fm


def repo_parts(base: str) -> list[str]:
    """Extract [owner, repo] from a raw base URL."""
    return base.replace(f"{_GITHUB_RAW}/", "").split("/")[:2]


def list_directory(base: str, path: str) -> list[dict] | None:
    """List files in a directory via GitHub API.

    Returns a list of dicts with 'name', 'type', 'download_url', 'path' keys,
    or None if the directory doesn't exist or the request fails.
    """
    parts = base.replace(f"{_GITHUB_RAW}/", "").split("/")
    if len(parts) >= 3:
        api_url = f"https://api.github.com/repos/{parts[0]}/{parts[1]}/contents/{path}"
        content = fetch(api_url)
        if content:
            try:
                return json.loads(content)
            except (json.JSONDecodeError, ValueError):
                return None
    return None
