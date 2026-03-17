#!/usr/bin/env python3
"""Generate MkDocs skill pages from skills/*/SKILL.md files.

Run this before `mkdocs build` or `mkdocs serve`:

    python scripts/generate_skill_pages.py

It reads every skills/*/SKILL.md, runs the scanner, and generates:
  - docs/skills/{slug}.md  (one per skill)
  - docs/skills/index.md   (browse page)
  - Updates mkdocs.yml nav  (Skills section)
"""

from __future__ import annotations

import hashlib
import re
import sys
from collections import OrderedDict
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"
DOCS_SKILLS_DIR = REPO_ROOT / "docs" / "skills"
MKDOCS_YML = REPO_ROOT / "mkdocs.yml"
TEMPLATES_DIR = Path(__file__).resolve().parent / "templates"

# Make brunnr importable
sys.path.insert(0, str(REPO_ROOT))
from brunnr.scanner import scan_skill_md  # noqa: E402

# ---------------------------------------------------------------------------
# Skill categories (slug -> category)
# ---------------------------------------------------------------------------

SKILL_CATEGORIES: dict[str, str] = {}

_HUNTER_SLUGS = [
    "signal-scan", "decision-log", "persona-extract", "offer-scope",
    "hunter-log", "community-pitch", "skool-pitch", "positioning",
    "pitch", "swot-analysis", "quote-to-persona",
]
_EDUCATIONAL_SLUGS = [
    "technical-tutorial", "lesson-generator", "chapter-generator",
    "curriculum-planner", "assessment-generator", "notebook-builder",
    "outline-writer", "scaffold-pass", "engagement-pass", "visual-pass",
]
_AX_SLUGS = ["ax-rubric", "ax-interview"]
_CONTENT_SLUGS = [
    "content-planner", "article-draft", "wild-scan", "reddit-harvest",
    "linwheel-content-engine", "linwheel-source-optimizer",
]
_TOOLS_SLUGS = [
    "runlet", "issue", "sketches", "slidev-deck",
    "inline-svg-architecture-diagrams", "llms-txt-generator",
    "mkdocs-site-generator", "travel-pulse",
]

for _slug in _HUNTER_SLUGS:
    SKILL_CATEGORIES[_slug] = "Hunter Pipeline"
for _slug in _EDUCATIONAL_SLUGS:
    SKILL_CATEGORIES[_slug] = "Educational Suite"
for _slug in _AX_SLUGS:
    SKILL_CATEGORIES[_slug] = "Agent Experience (AX)"
for _slug in _CONTENT_SLUGS:
    SKILL_CATEGORIES[_slug] = "Content & Research"
for _slug in _TOOLS_SLUGS:
    SKILL_CATEGORIES[_slug] = "Productivity & Tools"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def parse_yaml_frontmatter(content: str) -> dict:
    """Parse YAML frontmatter from SKILL.md content.

    Uses yaml.safe_load for proper nested structure support.
    """
    if not content.startswith("---"):
        return {}
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}
    try:
        return yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        return {}


def extract_body(content: str) -> str:
    """Extract markdown body after frontmatter."""
    match = re.match(r"^---\s*\n.*?\n---\s*\n?(.*)", content, re.DOTALL)
    return match.group(1).strip() if match else content.strip()


def adjust_headings(md: str, offset: int = 2) -> str:
    """Shift all markdown headings down by offset levels, capped at h6."""
    def replacer(m: re.Match) -> str:
        new_level = min(len(m.group(1)) + offset, 6)
        return "#" * new_level + m.group(2)
    return re.sub(r"^(#{1,6})([ \t])", replacer, md, flags=re.MULTILINE)


def compute_file_meta(path: Path) -> dict:
    """Compute size and SHA-256 for a file."""
    content = path.read_bytes()
    size = len(content)
    sha = hashlib.sha256(content).hexdigest()
    if size < 1024:
        display = f"{size} B"
    elif size < 1024 * 1024:
        display = f"{size / 1024:.1f} KB"
    else:
        display = f"{size / (1024 * 1024):.1f} MB"
    return {"size_bytes": size, "size_display": display, "sha256": sha}


def truncate_description(desc: str, max_len: int = 120) -> str:
    """Truncate description to first sentence or max_len chars."""
    # First sentence
    m = re.match(r"^(.+?[.!?])\s", desc)
    if m and len(m.group(1)) <= max_len:
        return m.group(1)
    if len(desc) <= max_len:
        return desc
    return desc[:max_len].rsplit(" ", 1)[0] + "..."


def scan_badge(scan_data: dict) -> str:
    """Return a short text badge for scan status."""
    sev = str(scan_data.get("severity", "clean"))
    count = scan_data.get("finding_count", 0)
    if count == 0:
        return "CLEAN"
    return f"{sev.upper()} ({count})"


def get_nested(d: dict, *keys, default=None):
    """Safely traverse nested dict keys."""
    for k in keys:
        if not isinstance(d, dict):
            return default
        d = d.get(k)
        if d is None:
            return default
    return d


# ---------------------------------------------------------------------------
# Skill loader
# ---------------------------------------------------------------------------


def load_skill(slug: str) -> dict | None:
    """Load all data for a single skill."""
    skill_dir = SKILLS_DIR / slug
    skill_md = skill_dir / "SKILL.md"
    readme_md = skill_dir / "README.md"

    if not skill_md.exists():
        return None

    content = skill_md.read_text(encoding="utf-8")
    fm = parse_yaml_frontmatter(content)
    body = extract_body(content)

    # Run scanner
    scan_result = scan_skill_md(content)
    scan_data = scan_result.to_dict()

    # Parse metadata
    name = fm.get("name", slug)
    description = fm.get("description", "")
    if isinstance(description, str):
        description = description.strip()
    license_val = fm.get("license", "")
    emoji = get_nested(fm, "metadata", "openclaw", "emoji", default="")
    bins = get_nested(fm, "metadata", "openclaw", "requires", "bins", default=[])
    env_vars = get_nested(fm, "metadata", "openclaw", "requires", "env", default=[])

    # README
    readme_content = None
    if readme_md.exists():
        readme_content = readme_md.read_text(encoding="utf-8").strip()

    # File metadata
    file_meta = compute_file_meta(skill_md)

    # Category tags
    category = SKILL_CATEGORIES.get(slug)
    tags = [category] if category else []

    return {
        "slug": slug,
        "name": name,
        "description": description,
        "description_short": truncate_description(description),
        "license": license_val,
        "license_badge": license_val if license_val else "—",
        "emoji": emoji,
        "bins": bins if isinstance(bins, list) else [],
        "env_vars": env_vars if isinstance(env_vars, list) else [],
        "tags": tags,
        "body": adjust_headings(body),
        "readme": adjust_headings(readme_content) if readme_content else None,
        "has_readme": readme_content is not None,
        "scan": {
            "clean": str(scan_data.get("severity", "clean")) == "clean",
            "blocked": scan_data.get("blocked", False),
            "flagged": scan_data.get("flagged", False),
            "finding_count": scan_data.get("finding_count", 0),
            "findings": [
                {k: str(v) for k, v in f.items()}
                for f in scan_data.get("findings", [])
            ],
            "severity": str(scan_data.get("severity", "clean")),
        },
        "scan_badge": scan_badge(scan_data),
        "file_meta": file_meta,
    }


# ---------------------------------------------------------------------------
# Generators
# ---------------------------------------------------------------------------


def generate_skill_page(skill: dict, env: Environment) -> None:
    """Write a single skill detail page."""
    template = env.get_template("skill_detail.md.j2")
    output = template.render(**skill)
    out_path = DOCS_SKILLS_DIR / f"{skill['slug']}.md"
    out_path.write_text(output, encoding="utf-8")


def generate_index_page(all_skills: list[dict], env: Environment) -> None:
    """Write the skills index/browse page."""
    template = env.get_template("skills_index.md.j2")

    # Group by category
    categories: OrderedDict[str, list[dict]] = OrderedDict()
    uncategorized: list[dict] = []

    # Define display order
    cat_order = [
        "Agent Experience (AX)",
        "Hunter Pipeline",
        "Content & Research",
        "Educational Suite",
        "Productivity & Tools",
    ]
    for cat in cat_order:
        categories[cat] = []

    for s in sorted(all_skills, key=lambda x: x["slug"]):
        cat = SKILL_CATEGORIES.get(s["slug"])
        if cat and cat in categories:
            categories[cat].append(s)
        else:
            uncategorized.append(s)

    # Remove empty categories
    categories = OrderedDict(
        (k, v) for k, v in categories.items() if v
    )

    output = template.render(
        skills=all_skills,
        categories=categories,
        uncategorized=uncategorized,
    )
    out_path = DOCS_SKILLS_DIR / "index.md"
    out_path.write_text(output, encoding="utf-8")


def update_mkdocs_nav(all_skills: list[dict]) -> None:
    """Update the Skills section of mkdocs.yml nav."""
    content = MKDOCS_YML.read_text(encoding="utf-8")

    # Build replacement block
    lines = ["  - Skills:"]
    lines.append("    - Browse All: skills/index.md")

    # Keep the hand-written writing-skills page
    lines.append("    - Writing Skills: skills/writing-skills.md")

    # All generated skill pages
    for s in sorted(all_skills, key=lambda x: x["slug"]):
        display = f"{s['emoji']} {s['name']}" if s["emoji"] else s["name"]
        # Escape quotes in display name
        display = display.replace('"', '\\"')
        lines.append(f'    - "{display}": skills/{s["slug"]}.md')

    new_block = "\n".join(lines)

    # Replace existing Skills block in nav.
    # Find "  - Skills:" and consume all subsequent lines indented deeper (4+ spaces).
    pattern = r"  - Skills:\n(?:    .*\n)*"
    replacement = new_block + "\n"
    new_content, count = re.subn(pattern, replacement, content)

    if count == 0:
        print("WARNING: Could not find Skills nav block to update in mkdocs.yml")
        print("  You may need to update the nav manually.")
        return

    MKDOCS_YML.write_text(new_content, encoding="utf-8")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    """Discover skills, scan, generate pages, update nav."""
    DOCS_SKILLS_DIR.mkdir(parents=True, exist_ok=True)

    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        keep_trailing_newline=True,
        trim_blocks=True,
        lstrip_blocks=True,
    )

    # Discover all skill directories (must contain SKILL.md)
    skill_dirs = sorted(
        d for d in SKILLS_DIR.iterdir()
        if d.is_dir() and not d.name.startswith("_") and (d / "SKILL.md").exists()
    )

    print(f"Found {len(skill_dirs)} skills")

    all_skills: list[dict] = []
    for skill_dir in skill_dirs:
        slug = skill_dir.name
        print(f"  Processing {slug}...", end=" ")
        skill = load_skill(slug)
        if skill is None:
            print("SKIP (no SKILL.md)")
            continue
        all_skills.append(skill)
        generate_skill_page(skill, env)
        print(f"{skill['scan_badge']}")

    # Generate index
    generate_index_page(all_skills, env)
    print(f"\nGenerated {len(all_skills)} skill pages + index")

    # Update nav
    update_mkdocs_nav(all_skills)
    print("Updated mkdocs.yml nav")

    print("\nDone. Run `mkdocs serve` to preview.")


if __name__ == "__main__":
    main()
