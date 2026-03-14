"""Tests for skill file discovery with references/ directory support."""

from __future__ import annotations

import shutil

import pytest
from pathlib import Path

from brunnr.discovery import discover_skill_files, collect_scan_files


@pytest.fixture
def skills_tree(tmp_path):
    """Create a realistic skill directory tree with references."""
    skills = tmp_path / "skills"
    skills.mkdir()

    # Simple skill (no references)
    simple = skills / "simple-skill"
    simple.mkdir()
    (simple / "SKILL.md").write_text("---\nname: simple-skill\ndescription: A simple skill\n---\n# Simple")

    # Skill with references
    with_refs = skills / "complex-skill"
    with_refs.mkdir()
    (with_refs / "SKILL.md").write_text("---\nname: complex-skill\ndescription: Complex\n---\n# Complex")
    refs = with_refs / "references"
    refs.mkdir()
    (refs / "output-schema.json").write_text('{"type": "object"}')
    (refs / "framework-guide.md").write_text("# Guide\nSome reference content.")
    (refs / "template.md").write_text("# Template\nBlank template.")

    # Skill with nested references (like slidev-deck/references/themes/)
    nested = skills / "nested-skill"
    nested.mkdir()
    (nested / "SKILL.md").write_text("---\nname: nested-skill\ndescription: Nested refs\n---\n# Nested")
    nested_refs = nested / "references"
    nested_refs.mkdir()
    themes = nested_refs / "themes"
    themes.mkdir()
    (themes / "modern.md").write_text("# Modern theme")

    # Convention file (should be skipped)
    (skills / "_conventions.md").write_text("# Conventions\nShared config.")
    (skills / "_educational-suite-conventions.md").write_text("# Educational conventions")

    # README in skill dir (not a SKILL.md, should not be discovered as skill)
    (with_refs / "README.md").write_text("# README")

    return skills


class TestDiscoverSkillFiles:
    """discover_skill_files() should find SKILL.md one level deep only."""

    def test_finds_all_skills(self, skills_tree):
        files = discover_skill_files(skills_dir=skills_tree)
        slugs = sorted(f.parent.name for f in files)
        assert slugs == ["complex-skill", "nested-skill", "simple-skill"]

    def test_does_not_find_reference_docs(self, skills_tree):
        files = discover_skill_files(skills_dir=skills_tree)
        for f in files:
            assert "references" not in f.parts
            assert "reference" not in f.parts

    def test_explicit_dir_path(self, skills_tree):
        files = discover_skill_files(paths=[str(skills_tree)])
        slugs = sorted(f.parent.name for f in files)
        assert slugs == ["complex-skill", "nested-skill", "simple-skill"]

    def test_explicit_file_path(self, skills_tree):
        skill_file = skills_tree / "simple-skill" / "SKILL.md"
        files = discover_skill_files(paths=[str(skill_file)])
        assert len(files) == 1
        assert files[0].name == "SKILL.md"

    def test_nonexistent_path_warns(self, skills_tree, capsys):
        files = discover_skill_files(paths=[str(skills_tree / "nonexistent")])
        assert files == []
        assert "WARNING" in capsys.readouterr().err

    def test_empty_skills_dir(self, tmp_path):
        empty = tmp_path / "skills"
        empty.mkdir()
        files = discover_skill_files(skills_dir=empty)
        assert files == []

    def test_deeply_nested_skill_md_excluded(self, skills_tree):
        """SKILL.md files more than one level deep should not be found."""
        deep = skills_tree / "outer" / "inner"
        deep.mkdir(parents=True)
        (deep / "SKILL.md").write_text("---\nname: deep\ndescription: too deep\n---\n# Deep")
        files = discover_skill_files(skills_dir=skills_tree)
        slugs = sorted(f.parent.name for f in files)
        # "inner" should not appear because it's two levels deep
        assert "inner" not in slugs

    def test_skill_md_in_references_excluded(self, skills_tree):
        """A SKILL.md inside references/ should never be discovered."""
        refs = skills_tree / "complex-skill" / "references"
        (refs / "SKILL.md").write_text("---\nname: fake\ndescription: fake\n---\n# Fake")
        files = discover_skill_files(skills_dir=skills_tree)
        for f in files:
            assert "references" not in f.parts


class TestCollectScanFiles:
    """collect_scan_files() should skip references/ and _-prefixed files."""

    def test_skips_reference_md_files(self, skills_tree):
        files = collect_scan_files([str(skills_tree)])
        filenames = [f.name for f in files]
        assert "framework-guide.md" not in filenames
        assert "template.md" not in filenames
        assert "modern.md" not in filenames

    def test_skips_convention_files(self, skills_tree):
        files = collect_scan_files([str(skills_tree)])
        filenames = [f.name for f in files]
        assert "_conventions.md" not in filenames
        assert "_educational-suite-conventions.md" not in filenames

    def test_finds_skill_md_files(self, skills_tree):
        files = collect_scan_files([str(skills_tree)])
        skill_files = [f for f in files if f.name == "SKILL.md"]
        assert len(skill_files) == 3

    def test_finds_readme_files(self, skills_tree):
        files = collect_scan_files([str(skills_tree)])
        readme_files = [f for f in files if f.name == "README.md"]
        assert len(readme_files) == 1

    def test_explicit_file_path_not_filtered(self, skills_tree):
        """Direct file path should always be included, even if in references/."""
        ref_file = skills_tree / "complex-skill" / "references" / "framework-guide.md"
        files = collect_scan_files([str(ref_file)])
        assert len(files) == 1
        assert files[0].name == "framework-guide.md"

    def test_empty_dir(self, tmp_path):
        empty = tmp_path / "empty"
        empty.mkdir()
        files = collect_scan_files([str(empty)])
        assert files == []

    def test_nonexistent_path_warns(self, tmp_path, capsys):
        files = collect_scan_files([str(tmp_path / "nope")])
        assert files == []
        assert "WARNING" in capsys.readouterr().err

    def test_reference_singular_skipped(self, tmp_path):
        """reference/ (singular) dirs should also be skipped."""
        skill_dir = tmp_path / "skill-x"
        skill_dir.mkdir()
        (skill_dir / "SKILL.md").write_text("# Skill")
        ref = skill_dir / "reference"
        ref.mkdir()
        (ref / "guide.md").write_text("# Guide")
        files = collect_scan_files([str(tmp_path)])
        filenames = [f.name for f in files]
        assert "guide.md" not in filenames
        assert "SKILL.md" in filenames


class TestPublishRecursiveCopy:
    """publish.py should copy subdirectories like references/."""

    def test_iterdir_copies_subdirs(self, tmp_path):
        """Verify the pattern used in publish.py handles directories."""
        # Create source skill with references/
        src = tmp_path / "src" / "my-skill"
        src.mkdir(parents=True)
        (src / "SKILL.md").write_text("# Skill")
        (src / "README.md").write_text("# README")
        refs = src / "references"
        refs.mkdir()
        (refs / "guide.md").write_text("# Guide")
        (refs / "schema.json").write_text("{}")

        # Simulate publish copy
        dest = tmp_path / "dest" / "my-skill"
        dest.mkdir(parents=True)
        (dest / "SKILL.md").write_text("# Skill")

        for extra in src.iterdir():
            if extra.name == "SKILL.md":
                continue
            dest_extra = dest / extra.name
            if extra.is_dir():
                shutil.copytree(extra, dest_extra, dirs_exist_ok=True)
            elif extra.is_file():
                shutil.copy2(extra, dest_extra)

        assert (dest / "README.md").exists()
        assert (dest / "references" / "guide.md").exists()
        assert (dest / "references" / "schema.json").exists()

    def test_copytree_overwrites_existing(self, tmp_path):
        """dirs_exist_ok=True should allow overwriting existing refs."""
        src = tmp_path / "src"
        src.mkdir()
        refs = src / "references"
        refs.mkdir()
        (refs / "old.md").write_text("# Old")

        dest = tmp_path / "dest"
        dest.mkdir()
        dest_refs = dest / "references"
        dest_refs.mkdir()
        (dest_refs / "existing.md").write_text("# Existing")

        shutil.copytree(refs, dest_refs, dirs_exist_ok=True)

        assert (dest_refs / "old.md").exists()
        assert (dest_refs / "existing.md").exists()
