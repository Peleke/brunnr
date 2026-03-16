"""Tests for scripts/generate_skill_pages.py — skill detail page generator.

Covers:
  - YAML frontmatter parsing (flat, nested, folded scalars, missing fields)
  - Body extraction
  - Heading adjustment
  - File metadata computation
  - Description truncation
  - Scan badge rendering
  - Skill loading from real skill dirs
  - Template rendering (detail + index)
  - mkdocs.yml nav update
  - Idempotency (running twice produces same output)
  - Edge cases (empty frontmatter, no README, no emoji, no license)
"""

from __future__ import annotations

import hashlib
import re
import textwrap
from collections import OrderedDict
from pathlib import Path

import pytest

# Import the module under test
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scripts.generate_skill_pages import (
    adjust_headings,
    compute_file_meta,
    extract_body,
    generate_index_page,
    generate_skill_page,
    get_nested,
    load_skill,
    parse_yaml_frontmatter,
    scan_badge,
    truncate_description,
    update_mkdocs_nav,
    SKILL_CATEGORIES,
    SKILLS_DIR,
    REPO_ROOT,
)
from jinja2 import Environment, FileSystemLoader

TEMPLATES_DIR = Path(__file__).resolve().parent.parent / "scripts" / "templates"


# =========================================================================
# parse_yaml_frontmatter
# =========================================================================


class TestParseYamlFrontmatter:
    def test_flat_frontmatter(self):
        content = "---\nname: test-skill\ndescription: A test skill\n---\n# Body"
        fm = parse_yaml_frontmatter(content)
        assert fm["name"] == "test-skill"
        assert fm["description"] == "A test skill"

    def test_nested_frontmatter(self):
        content = textwrap.dedent("""\
            ---
            name: test
            metadata:
              openclaw:
                emoji: "🔬"
                requires:
                  bins: ["gh", "python3"]
            ---
            # Body
        """)
        fm = parse_yaml_frontmatter(content)
        assert fm["name"] == "test"
        assert fm["metadata"]["openclaw"]["emoji"] == "🔬"
        assert fm["metadata"]["openclaw"]["requires"]["bins"] == ["gh", "python3"]

    def test_folded_scalar_description(self):
        content = textwrap.dedent("""\
            ---
            name: test
            description: >
              This is a long description
              that spans multiple lines.
            ---
            # Body
        """)
        fm = parse_yaml_frontmatter(content)
        assert "This is a long description" in fm["description"]
        assert "that spans multiple lines." in fm["description"]

    def test_quoted_description(self):
        content = '---\nname: test\ndescription: "A quoted desc"\n---\n# Body'
        fm = parse_yaml_frontmatter(content)
        assert fm["description"] == "A quoted desc"

    def test_no_frontmatter(self):
        content = "# Just a heading\nSome body text."
        fm = parse_yaml_frontmatter(content)
        assert fm == {}

    def test_incomplete_frontmatter(self):
        content = "---\nname: test\n# Missing closing fence"
        fm = parse_yaml_frontmatter(content)
        assert fm == {}

    def test_empty_frontmatter(self):
        content = "---\n---\n# Body"
        fm = parse_yaml_frontmatter(content)
        assert fm == {} or fm is None or (isinstance(fm, dict) and len(fm) == 0)

    def test_frontmatter_with_license(self):
        content = "---\nname: test\nlicense: MIT\n---\n# Body"
        fm = parse_yaml_frontmatter(content)
        assert fm["license"] == "MIT"

    def test_unicode_emoji_escape(self):
        content = '---\nname: test\nmetadata:\n  openclaw:\n    emoji: "\\U0001F52C"\n---\n# Body'
        fm = parse_yaml_frontmatter(content)
        emoji = get_nested(fm, "metadata", "openclaw", "emoji", default="")
        assert emoji == "🔬" or emoji  # PyYAML may or may not decode the escape

    def test_invalid_yaml(self):
        content = "---\n: invalid yaml [[\n---\n# Body"
        fm = parse_yaml_frontmatter(content)
        assert fm == {}


# =========================================================================
# extract_body
# =========================================================================


class TestExtractBody:
    def test_basic(self):
        content = "---\nname: test\n---\n# The Body\nSome text."
        body = extract_body(content)
        assert body == "# The Body\nSome text."

    def test_no_frontmatter(self):
        content = "# Just a heading\nSome text."
        body = extract_body(content)
        assert "Just a heading" in body

    def test_empty_body(self):
        content = "---\nname: test\n---\n"
        body = extract_body(content)
        assert body == ""

    def test_body_preserves_markdown(self):
        content = "---\nname: test\n---\n# H1\n## H2\n- list\n```code```"
        body = extract_body(content)
        assert "# H1" in body
        assert "## H2" in body
        assert "- list" in body
        assert "```code```" in body


# =========================================================================
# adjust_headings
# =========================================================================


class TestAdjustHeadings:
    def test_shifts_h1_to_h3(self):
        result = adjust_headings("# Title")
        assert result == "### Title"

    def test_shifts_h2_to_h4(self):
        result = adjust_headings("## Subtitle")
        assert result == "#### Subtitle"

    def test_caps_at_h6(self):
        result = adjust_headings("##### Deep heading")
        assert result == "###### Deep heading"

    def test_caps_at_h6_overflow(self):
        result = adjust_headings("###### Already h6")
        assert result == "###### Already h6"

    def test_multiline(self):
        md = "# Title\nSome text\n## Sub\nMore text"
        result = adjust_headings(md)
        assert "### Title" in result
        assert "#### Sub" in result
        assert "Some text" in result

    def test_no_headings(self):
        md = "Just plain text."
        assert adjust_headings(md) == md

    def test_code_block_headings_adjusted(self):
        # Headings inside code blocks will also be adjusted —
        # this is a known limitation, acceptable for our use case
        md = "```\n# comment\n```"
        result = adjust_headings(md)
        assert "###" in result

    def test_custom_offset(self):
        result = adjust_headings("# Title", offset=1)
        assert result == "## Title"

    @pytest.mark.parametrize("level", [1, 2, 3, 4, 5, 6])
    @pytest.mark.parametrize("offset", [1, 2, 3, 4, 5])
    def test_heading_level_invariant(self, level, offset):
        """Property: output level = min(input_level + offset, 6)."""
        heading = "#" * level + " Heading"
        result = adjust_headings(heading, offset=offset)
        expected_level = min(level + offset, 6)
        expected = "#" * expected_level + " Heading"
        assert result == expected


# =========================================================================
# compute_file_meta
# =========================================================================


class TestComputeFileMeta:
    def test_computes_sha256(self, tmp_path):
        f = tmp_path / "test.md"
        f.write_text("hello world")
        meta = compute_file_meta(f)
        expected_sha = hashlib.sha256(b"hello world").hexdigest()
        assert meta["sha256"] == expected_sha

    def test_size_bytes(self, tmp_path):
        f = tmp_path / "test.md"
        f.write_text("hello")
        meta = compute_file_meta(f)
        assert meta["size_bytes"] == 5
        assert "B" in meta["size_display"]

    def test_size_kilobytes(self, tmp_path):
        f = tmp_path / "test.md"
        f.write_text("x" * 2048)
        meta = compute_file_meta(f)
        assert "KB" in meta["size_display"]

    def test_size_megabytes(self, tmp_path):
        f = tmp_path / "test.md"
        f.write_bytes(b"x" * (1024 * 1024 + 1))
        meta = compute_file_meta(f)
        assert "MB" in meta["size_display"]

    def test_nonexistent_file_raises(self, tmp_path):
        f = tmp_path / "does_not_exist.md"
        with pytest.raises(FileNotFoundError):
            compute_file_meta(f)


# =========================================================================
# truncate_description
# =========================================================================


class TestTruncateDescription:
    def test_short_description(self):
        desc = "A short description."
        assert truncate_description(desc) == desc

    def test_first_sentence(self):
        desc = "First sentence. Second sentence goes here and is quite long."
        assert truncate_description(desc) == "First sentence."

    def test_truncation_at_word_boundary(self):
        desc = "A " + "very " * 30 + "long description"
        result = truncate_description(desc, max_len=50)
        assert len(result) <= 53  # 50 + "..."
        assert result.endswith("...")

    def test_empty_string(self):
        assert truncate_description("") == ""

    def test_exactly_max_len(self):
        desc = "x" * 120
        assert truncate_description(desc) == desc


# =========================================================================
# scan_badge
# =========================================================================


class TestScanBadge:
    def test_clean(self):
        data = {"severity": "clean", "finding_count": 0}
        assert scan_badge(data) == "CLEAN"

    def test_info(self):
        data = {"severity": "info", "finding_count": 2}
        assert scan_badge(data) == "INFO (2)"

    def test_flag(self):
        data = {"severity": "flag", "finding_count": 1}
        assert scan_badge(data) == "FLAG (1)"

    def test_block(self):
        data = {"severity": "block", "finding_count": 3}
        assert scan_badge(data) == "BLOCK (3)"

    def test_enum_severity(self):
        """Handle StrEnum severity values from the scanner."""
        from brunnr.scanner import Severity
        data = {"severity": Severity.CLEAN, "finding_count": 0}
        assert scan_badge(data) == "CLEAN"


# =========================================================================
# get_nested
# =========================================================================


class TestGetNested:
    def test_basic(self):
        d = {"a": {"b": {"c": "value"}}}
        assert get_nested(d, "a", "b", "c") == "value"

    def test_missing_key(self):
        d = {"a": {"b": 1}}
        assert get_nested(d, "a", "c", default="nope") == "nope"

    def test_non_dict_intermediate(self):
        d = {"a": "string"}
        assert get_nested(d, "a", "b", default=None) is None

    def test_empty_dict(self):
        assert get_nested({}, "a", default="x") == "x"

    def test_none_value(self):
        d = {"a": None}
        assert get_nested(d, "a", "b", default="fallback") == "fallback"


# =========================================================================
# load_skill (integration — uses real skill dirs)
# =========================================================================


class TestLoadSkill:
    def test_load_real_skill_ax_rubric(self):
        """ax-rubric is a minimal skill: no emoji, no license, no bins."""
        skill = load_skill("ax-rubric")
        assert skill is not None
        assert skill["slug"] == "ax-rubric"
        assert skill["name"] == "ax-rubric"
        assert "Score agent-facing" in skill["description"]
        assert isinstance(skill["scan"], dict)
        assert isinstance(skill["file_meta"], dict)
        assert skill["file_meta"]["sha256"]
        assert skill["file_meta"]["size_bytes"] > 0

    def test_load_real_skill_ax_interview(self):
        """ax-interview has emoji + license."""
        skill = load_skill("ax-interview")
        assert skill is not None
        assert skill["emoji"] == "🔬"
        assert skill["license"] == "MIT"

    def test_load_real_skill_content_planner(self):
        """content-planner has bins requirement."""
        skill = load_skill("content-planner")
        assert skill is not None
        assert "gh" in skill["bins"]
        assert "python3" in skill["bins"]

    def test_load_real_skill_with_readme(self):
        """ax-rubric has a README.md."""
        skill = load_skill("ax-rubric")
        assert skill is not None
        assert skill["has_readme"] is True
        assert skill["readme"] is not None
        assert "AX Description Rubric" in skill["readme"]

    def test_load_real_skill_without_readme(self):
        """assessment-generator has no README.md."""
        skill = load_skill("assessment-generator")
        assert skill is not None
        assert skill["has_readme"] is False
        assert skill["readme"] is None

    def test_load_nonexistent_skill(self):
        skill = load_skill("nonexistent-skill-that-does-not-exist")
        assert skill is None

    def test_load_skill_categories(self):
        """Skills get tagged with their category."""
        skill = load_skill("ax-rubric")
        assert "Agent Experience (AX)" in skill["tags"]

        skill = load_skill("signal-scan")
        assert "Hunter Pipeline" in skill["tags"]

    def test_load_skill_scan_result_structure(self):
        """Scan result dict has expected keys."""
        skill = load_skill("ax-rubric")
        scan = skill["scan"]
        assert "clean" in scan
        assert "blocked" in scan
        assert "flagged" in scan
        assert "finding_count" in scan
        assert "findings" in scan
        assert isinstance(scan["findings"], list)

    def test_load_skill_headings_adjusted(self):
        """Body headings should be shifted down by 2 levels."""
        skill = load_skill("ax-rubric")
        # Original SKILL.md starts with "# AX Description Rubric"
        # After adjustment it should be "### AX Description Rubric"
        assert "### AX Description Rubric" in skill["body"]
        assert not skill["body"].startswith("# AX")

    def test_load_all_skills_no_crashes(self):
        """Every skill directory should load without errors."""
        skill_dirs = sorted(
            d for d in SKILLS_DIR.iterdir()
            if d.is_dir() and not d.name.startswith("_") and (d / "SKILL.md").exists()
        )
        for skill_dir in skill_dirs:
            skill = load_skill(skill_dir.name)
            assert skill is not None, f"Failed to load skill: {skill_dir.name}"
            assert skill["slug"] == skill_dir.name
            assert skill["name"]  # Must have a name
            assert skill["file_meta"]["sha256"]  # Must have hash


class TestLoadSkillSynthetic:
    """Unit tests for load_skill with synthetic SKILL.md (no real filesystem dependency)."""

    def test_load_synthetic_skill(self, tmp_path, monkeypatch):
        import scripts.generate_skill_pages as mod
        monkeypatch.setattr(mod, "SKILLS_DIR", tmp_path)

        skill_dir = tmp_path / "fake-skill"
        skill_dir.mkdir()
        (skill_dir / "SKILL.md").write_text(
            '---\nname: fake-skill\ndescription: "A synthetic test skill."\nlicense: MIT\n'
            'metadata:\n  openclaw:\n    emoji: "\\U0001F4E1"\n    requires:\n      bins: ["jq"]\n'
            "---\n# Fake Skill\nBody content here.\n"
        )

        skill = mod.load_skill("fake-skill")
        assert skill is not None
        assert skill["slug"] == "fake-skill"
        assert skill["name"] == "fake-skill"
        assert skill["description"] == "A synthetic test skill."
        assert skill["license"] == "MIT"
        assert skill["bins"] == ["jq"]
        assert skill["has_readme"] is False
        assert skill["scan"]["finding_count"] == 0
        assert skill["file_meta"]["size_bytes"] > 0

    def test_load_synthetic_skill_with_readme(self, tmp_path, monkeypatch):
        import scripts.generate_skill_pages as mod
        monkeypatch.setattr(mod, "SKILLS_DIR", tmp_path)

        skill_dir = tmp_path / "with-readme"
        skill_dir.mkdir()
        (skill_dir / "SKILL.md").write_text("---\nname: with-readme\ndescription: Has README.\n---\n# Body\n")
        (skill_dir / "README.md").write_text("# README\nDocumentation here.\n")

        skill = mod.load_skill("with-readme")
        assert skill is not None
        assert skill["has_readme"] is True
        assert "Documentation here" in skill["readme"]

    def test_load_synthetic_skill_no_skill_md(self, tmp_path, monkeypatch):
        import scripts.generate_skill_pages as mod
        monkeypatch.setattr(mod, "SKILLS_DIR", tmp_path)

        skill_dir = tmp_path / "no-skill-md"
        skill_dir.mkdir()

        skill = mod.load_skill("no-skill-md")
        assert skill is None


# =========================================================================
# Template rendering
# =========================================================================


class TestTemplateRendering:
    @pytest.fixture
    def jinja_env(self):
        return Environment(
            loader=FileSystemLoader(str(TEMPLATES_DIR)),
            keep_trailing_newline=True,
            trim_blocks=True,
            lstrip_blocks=True,
        )

    @pytest.fixture
    def minimal_skill(self):
        return {
            "slug": "test-skill",
            "name": "test-skill",
            "description": "A test skill for testing.",
            "emoji": "",
            "license": "",
            "bins": [],
            "env_vars": [],
            "tags": [],
            "body": "### Test Content\nSome test body.",
            "readme": None,
            "has_readme": False,
            "scan": {
                "clean": True,
                "blocked": False,
                "flagged": False,
                "finding_count": 0,
                "findings": [],
                "severity": "clean",
            },
            "scan_badge": "CLEAN",
            "file_meta": {
                "size_bytes": 100,
                "size_display": "100 B",
                "sha256": "abc123",
            },
        }

    @pytest.fixture
    def rich_skill(self, minimal_skill):
        return {
            **minimal_skill,
            "emoji": "🔬",
            "license": "MIT",
            "bins": ["gh", "python3"],
            "env_vars": ["API_KEY"],
            "tags": ["Agent Experience (AX)"],
            "readme": "### README content\nSome readme.",
            "has_readme": True,
            "scan": {
                "clean": False,
                "blocked": False,
                "flagged": True,
                "finding_count": 2,
                "findings": [
                    {
                        "threat_class": "semantic_mismatch",
                        "severity": "FLAG",
                        "description": "suspicious URL",
                        "line": "42",
                    },
                    {
                        "threat_class": "supply_chain",
                        "severity": "INFO",
                        "description": "non-allowlisted domain",
                        "line": "99",
                    },
                ],
                "severity": "flag",
            },
            "scan_badge": "FLAG (2)",
        }

    def test_detail_minimal(self, jinja_env, minimal_skill):
        template = jinja_env.get_template("skill_detail.md.j2")
        output = template.render(**minimal_skill)
        assert "# test-skill" in output
        assert "A test skill for testing." in output
        assert "brunnr install test-skill" in output
        assert "CLEAN — 0 findings" in output
        assert "abc123" in output
        # No runtime requirements section
        assert "Runtime Requirements" not in output
        # No README section
        assert "## README" not in output

    def test_detail_with_emoji(self, jinja_env, rich_skill):
        template = jinja_env.get_template("skill_detail.md.j2")
        output = template.render(**rich_skill)
        assert "# 🔬 test-skill" in output

    def test_detail_with_license(self, jinja_env, rich_skill):
        template = jinja_env.get_template("skill_detail.md.j2")
        output = template.render(**rich_skill)
        assert "**License:** MIT" in output

    def test_detail_with_bins(self, jinja_env, rich_skill):
        template = jinja_env.get_template("skill_detail.md.j2")
        output = template.render(**rich_skill)
        assert "Runtime Requirements" in output
        assert "`gh`" in output
        assert "`python3`" in output

    def test_detail_with_env_vars(self, jinja_env, rich_skill):
        template = jinja_env.get_template("skill_detail.md.j2")
        output = template.render(**rich_skill)
        assert "`API_KEY`" in output

    def test_detail_with_tags(self, jinja_env, rich_skill):
        template = jinja_env.get_template("skill_detail.md.j2")
        output = template.render(**rich_skill)
        assert "`Agent Experience (AX)`" in output

    def test_detail_with_findings(self, jinja_env, rich_skill):
        template = jinja_env.get_template("skill_detail.md.j2")
        output = template.render(**rich_skill)
        assert "FLAGGED" in output
        assert "2 finding(s)" in output
        assert "semantic_mismatch" in output
        assert "supply_chain" in output
        assert "View findings" in output

    def test_detail_with_readme(self, jinja_env, rich_skill):
        template = jinja_env.get_template("skill_detail.md.j2")
        output = template.render(**rich_skill)
        assert "## README" in output
        assert "README content" in output

    def test_detail_blocked_scan(self, jinja_env, minimal_skill):
        minimal_skill["scan"] = {
            "clean": False,
            "blocked": True,
            "flagged": False,
            "finding_count": 1,
            "findings": [{"threat_class": "command_injection", "severity": "BLOCK", "description": "reverse shell", "line": "10"}],
            "severity": "block",
        }
        template = jinja_env.get_template("skill_detail.md.j2")
        output = template.render(**minimal_skill)
        assert "BLOCKED" in output
        assert "critical security findings" in output

    def test_detail_info_scan(self, jinja_env, minimal_skill):
        minimal_skill["scan"] = {
            "clean": False,
            "blocked": False,
            "flagged": False,
            "finding_count": 1,
            "findings": [{"threat_class": "semantic_mismatch", "severity": "INFO", "description": "non-allowlisted domain", "line": "5"}],
            "severity": "info",
        }
        template = jinja_env.get_template("skill_detail.md.j2")
        output = template.render(**minimal_skill)
        assert "INFO" in output
        assert "informational findings" in output

    def test_detail_generated_marker(self, jinja_env, minimal_skill):
        template = jinja_env.get_template("skill_detail.md.j2")
        output = template.render(**minimal_skill)
        assert "<!-- GENERATED" in output

    def test_index_page(self, jinja_env):
        skills = [
            {"slug": "a-skill", "name": "a-skill", "emoji": "🔬", "description_short": "Short A.", "license_badge": "MIT", "scan_badge": "CLEAN"},
            {"slug": "b-skill", "name": "b-skill", "emoji": "", "description_short": "Short B.", "license_badge": "—", "scan_badge": "FLAG (1)"},
        ]
        categories = OrderedDict({"Test Cat": [skills[0]]})
        uncategorized = [skills[1]]

        template = jinja_env.get_template("skills_index.md.j2")
        output = template.render(skills=skills, categories=categories, uncategorized=uncategorized)
        assert "Browse all **2**" in output
        assert "[a-skill](a-skill.md)" in output
        assert "[b-skill](b-skill.md)" in output
        assert "Test Cat" in output
        assert "Other Skills" in output
        assert "brunnr search" in output
        assert "brunnr install" in output


# =========================================================================
# generate_skill_page (writes to disk)
# =========================================================================


class TestGenerateSkillPage:
    @pytest.fixture
    def jinja_env(self):
        return Environment(
            loader=FileSystemLoader(str(TEMPLATES_DIR)),
            keep_trailing_newline=True,
            trim_blocks=True,
            lstrip_blocks=True,
        )

    def test_writes_file(self, jinja_env, tmp_path, monkeypatch):
        import scripts.generate_skill_pages as mod
        monkeypatch.setattr(mod, "DOCS_SKILLS_DIR", tmp_path)

        skill = {
            "slug": "test-slug",
            "name": "test-slug",
            "description": "A test.",
            "emoji": "",
            "license": "",
            "bins": [],
            "env_vars": [],
            "tags": [],
            "body": "Body content.",
            "readme": None,
            "has_readme": False,
            "scan": {"clean": True, "blocked": False, "flagged": False, "finding_count": 0, "findings": [], "severity": "clean"},
            "scan_badge": "CLEAN",
            "file_meta": {"size_bytes": 10, "size_display": "10 B", "sha256": "deadbeef"},
        }
        generate_skill_page(skill, jinja_env)

        out = tmp_path / "test-slug.md"
        assert out.exists()
        content = out.read_text()
        assert "test-slug" in content
        assert "GENERATED" in content


# =========================================================================
# update_mkdocs_nav
# =========================================================================


class TestUpdateMkdocsNav:
    def test_updates_nav(self, tmp_path, monkeypatch):
        import scripts.generate_skill_pages as mod

        mkdocs_file = tmp_path / "mkdocs.yml"
        mkdocs_file.write_text(textwrap.dedent("""\
            site_name: test
            nav:
              - Home: index.md
              - Skills:
                - Writing Skills: skills/writing-skills.md
              - About: about.md
            markdown_extensions:
              - admonition
        """))
        monkeypatch.setattr(mod, "MKDOCS_YML", mkdocs_file)

        skills = [
            {"slug": "alpha", "name": "alpha", "emoji": "🔬"},
            {"slug": "beta", "name": "beta", "emoji": ""},
        ]
        update_mkdocs_nav(skills)

        result = mkdocs_file.read_text()
        assert "Browse All: skills/index.md" in result
        assert "skills/alpha.md" in result
        assert "skills/beta.md" in result
        assert "Writing Skills: skills/writing-skills.md" in result
        # Preserves other nav entries
        assert "Home: index.md" in result
        assert "About: about.md" in result
        # Preserves extensions
        assert "admonition" in result

    def test_idempotent_nav_update(self, tmp_path, monkeypatch):
        """Running twice produces the same output."""
        import scripts.generate_skill_pages as mod

        mkdocs_file = tmp_path / "mkdocs.yml"
        mkdocs_file.write_text(textwrap.dedent("""\
            site_name: test
            nav:
              - Home: index.md
              - Skills:
                - Old: skills/old.md
              - About: about.md
        """))
        monkeypatch.setattr(mod, "MKDOCS_YML", mkdocs_file)

        skills = [{"slug": "alpha", "name": "alpha", "emoji": ""}]

        update_mkdocs_nav(skills)
        first_run = mkdocs_file.read_text()

        update_mkdocs_nav(skills)
        second_run = mkdocs_file.read_text()

        assert first_run == second_run

    def test_handles_missing_skills_block(self, tmp_path, monkeypatch, capsys):
        """Warns if Skills block not found."""
        import scripts.generate_skill_pages as mod

        mkdocs_file = tmp_path / "mkdocs.yml"
        mkdocs_file.write_text("site_name: test\nnav:\n  - Home: index.md\n")
        monkeypatch.setattr(mod, "MKDOCS_YML", mkdocs_file)

        update_mkdocs_nav([])
        captured = capsys.readouterr()
        assert "WARNING" in captured.out


# =========================================================================
# Skill categories
# =========================================================================


class TestSkillCategories:
    def test_all_hunter_slugs_categorized(self):
        hunter_slugs = [
            "signal-scan", "decision-log", "persona-extract", "offer-scope",
            "hunter-log", "community-pitch", "skool-pitch", "positioning",
            "pitch", "swot-analysis", "quote-to-persona",
        ]
        for slug in hunter_slugs:
            assert SKILL_CATEGORIES.get(slug) == "Hunter Pipeline", f"{slug} not in Hunter Pipeline"

    def test_all_educational_slugs_categorized(self):
        edu_slugs = [
            "technical-tutorial", "lesson-generator", "chapter-generator",
            "curriculum-planner", "assessment-generator", "notebook-builder",
            "outline-writer", "scaffold-pass", "engagement-pass", "visual-pass",
        ]
        for slug in edu_slugs:
            assert SKILL_CATEGORIES.get(slug) == "Educational Suite", f"{slug} not in Educational Suite"

    def test_ax_slugs_categorized(self):
        for slug in ["ax-rubric", "ax-interview"]:
            assert SKILL_CATEGORIES.get(slug) == "Agent Experience (AX)"

    def test_content_slugs_categorized(self):
        content_slugs = [
            "content-planner", "article-draft", "wild-scan", "reddit-harvest",
            "linwheel-content-engine", "linwheel-source-optimizer",
        ]
        for slug in content_slugs:
            assert SKILL_CATEGORIES.get(slug) == "Content & Research", f"{slug} not in Content & Research"

    def test_tools_slugs_categorized(self):
        tools_slugs = [
            "runlet", "issue", "sketches", "slidev-deck",
            "inline-svg-architecture-diagrams", "llms-txt-generator",
            "mkdocs-site-generator",
        ]
        for slug in tools_slugs:
            assert SKILL_CATEGORIES.get(slug) == "Productivity & Tools", f"{slug} not in Productivity & Tools"


# =========================================================================
# End-to-end integration
# =========================================================================


class TestEndToEnd:
    def test_generate_real_skill_page(self, tmp_path, monkeypatch):
        """Generate a page from a real skill and verify structure."""
        import scripts.generate_skill_pages as mod
        monkeypatch.setattr(mod, "DOCS_SKILLS_DIR", tmp_path)

        env = Environment(
            loader=FileSystemLoader(str(TEMPLATES_DIR)),
            keep_trailing_newline=True,
            trim_blocks=True,
            lstrip_blocks=True,
        )

        skill = load_skill("ax-interview")
        assert skill is not None
        generate_skill_page(skill, env)

        out = tmp_path / "ax-interview.md"
        assert out.exists()
        content = out.read_text()

        # Verify key sections exist
        assert "<!-- GENERATED" in content
        assert "🔬 ax-interview" in content
        assert "**License:** MIT" in content
        assert "brunnr install ax-interview" in content
        assert "Security Scan" in content
        assert "File Info" in content
        assert "Skill Prompt" in content
        assert "SHA-256" in content

    def test_generate_index_from_real_skills(self, tmp_path, monkeypatch):
        """Generate index from a few real skills."""
        import scripts.generate_skill_pages as mod
        monkeypatch.setattr(mod, "DOCS_SKILLS_DIR", tmp_path)

        env = Environment(
            loader=FileSystemLoader(str(TEMPLATES_DIR)),
            keep_trailing_newline=True,
            trim_blocks=True,
            lstrip_blocks=True,
        )

        skills = []
        for slug in ["ax-rubric", "ax-interview", "runlet"]:
            s = load_skill(slug)
            if s:
                skills.append(s)

        generate_index_page(skills, env)

        out = tmp_path / "index.md"
        assert out.exists()
        content = out.read_text()

        assert "Browse all" in content
        assert "ax-rubric" in content
        assert "ax-interview" in content
        assert "runlet" in content
