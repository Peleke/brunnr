"""brunnr install — fetch skills from the registry."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError

_GITHUB_RAW = "https://raw.githubusercontent.com"


def _fetch(url: str) -> str | None:
    """Fetch a URL and return text content, or None on failure."""
    try:
        req = Request(url, headers={"User-Agent": "brunnr-cli"})
        with urlopen(req, timeout=15) as resp:
            return resp.read().decode("utf-8")
    except (URLError, OSError):
        return None


def _registry_base(registry: str) -> str:
    """Convert a GitHub repo URL to raw content base URL."""
    # https://github.com/Peleke/brunnr -> https://raw.githubusercontent.com/Peleke/brunnr/main
    if "github.com" in registry:
        parts = registry.rstrip("/").replace("https://github.com/", "").split("/")
        if len(parts) >= 2:
            return f"{_GITHUB_RAW}/{parts[0]}/{parts[1]}/main"
    return registry.rstrip("/")


def _list_skills(base: str) -> list[str]:
    """List available skills from registry (via GitHub API)."""
    # Convert raw URL back to API URL
    # https://raw.githubusercontent.com/Peleke/brunnr/main -> https://api.github.com/repos/Peleke/brunnr/contents/skills
    parts = base.replace(f"{_GITHUB_RAW}/", "").split("/")
    if len(parts) >= 3:
        api_url = f"https://api.github.com/repos/{parts[0]}/{parts[1]}/contents/skills"
        content = _fetch(api_url)
        if content:
            entries = json.loads(content)
            return [e["name"] for e in entries if e["type"] == "dir"]
    return []


def run(args) -> int:
    base = _registry_base(args.registry)

    # List mode
    if getattr(args, "list_skills", False):
        skills = _list_skills(base)
        if not skills:
            print("No skills found (or registry unreachable).", file=sys.stderr)
            return 1
        print("Available skills:")
        for s in skills:
            print(f"  - {s}")
        return 0

    slug = args.skill
    if not slug:
        print("ERROR: skill name required. Use `brunnr install --list` to see available skills.", file=sys.stderr)
        return 1

    dest = Path("skills") / slug
    skill_file = dest / "SKILL.md"

    if skill_file.exists() and not getattr(args, "force", False):
        print(f"Skill '{slug}' already installed at {skill_file}", file=sys.stderr)
        print("Use --force to overwrite.", file=sys.stderr)
        return 1

    # Fetch SKILL.md
    skill_url = f"{base}/skills/{slug}/SKILL.md"
    print(f"Fetching {slug} from {args.registry}...")
    content = _fetch(skill_url)
    if not content:
        print(f"ERROR: Could not fetch {skill_url}", file=sys.stderr)
        return 1

    dest.mkdir(parents=True, exist_ok=True)
    skill_file.write_text(content)
    print(f"  -> {skill_file} ({len(content.splitlines())} lines)")

    # Fetch schema (optional)
    schema_url = f"{base}/schemas/{slug}/output.schema.json"
    schema_content = _fetch(schema_url)
    if schema_content:
        schema_dest = Path("schemas") / slug
        schema_dest.mkdir(parents=True, exist_ok=True)
        (schema_dest / "output.schema.json").write_text(schema_content)
        print(f"  -> schemas/{slug}/output.schema.json")

    # Fetch test fixtures (optional)
    if getattr(args, "with_tests", False):
        spec_url = f"{base}/tests/{slug}/test-spec.json"
        spec_content = _fetch(spec_url)
        if spec_content:
            test_dest = Path("tests") / slug
            test_dest.mkdir(parents=True, exist_ok=True)
            (test_dest / "test-spec.json").write_text(spec_content)
            print(f"  -> tests/{slug}/test-spec.json")

            # Fetch fixtures referenced in spec
            spec = json.loads(spec_content)
            for case in spec.get("cases", []):
                fixture_rel = case.get("fixture", "")
                if fixture_rel:
                    fixture_url = f"{base}/tests/{slug}/{fixture_rel}"
                    fixture_content = _fetch(fixture_url)
                    if fixture_content:
                        fixture_path = test_dest / fixture_rel
                        fixture_path.parent.mkdir(parents=True, exist_ok=True)
                        fixture_path.write_text(fixture_content)
                        print(f"  -> tests/{slug}/{fixture_rel}")

    print(f"\nInstalled {slug} to ./{dest}/")
    print(f"\nTip: Run `brunnr eval {slug} --dry-run` to validate locally.")
    return 0
