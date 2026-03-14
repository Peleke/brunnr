"""Tests for brunnr install command with references/ support."""

from __future__ import annotations

import json
import os
import pytest
from pathlib import Path
from unittest.mock import patch
from types import SimpleNamespace

from brunnr.registry import list_directory


# ---------------------------------------------------------------------------
# list_directory
# ---------------------------------------------------------------------------


class TestListDirectory:
    """list_directory() should parse GitHub API directory listings."""

    def test_parses_github_api_response(self):
        mock_response = json.dumps([
            {"name": "guide.md", "type": "file", "download_url": "https://example.com/guide.md",
             "path": "skills/test/references/guide.md"},
            {"name": "schema.json", "type": "file", "download_url": "https://example.com/schema.json",
             "path": "skills/test/references/schema.json"},
        ])
        with patch("brunnr.registry.fetch", return_value=mock_response):
            base = "https://raw.githubusercontent.com/Peleke/brunnr/main"
            result = list_directory(base, "skills/test/references")
            assert result is not None
            assert len(result) == 2
            assert result[0]["name"] == "guide.md"

    def test_returns_none_on_404(self):
        with patch("brunnr.registry.fetch", return_value=None):
            base = "https://raw.githubusercontent.com/Peleke/brunnr/main"
            result = list_directory(base, "skills/nonexistent/references")
            assert result is None

    def test_returns_none_on_invalid_json(self):
        with patch("brunnr.registry.fetch", return_value="not json"):
            base = "https://raw.githubusercontent.com/Peleke/brunnr/main"
            result = list_directory(base, "skills/test/references")
            assert result is None

    def test_returns_none_for_invalid_base(self):
        result = list_directory("http://not-github.com/foo", "skills/test")
        assert result is None

    def test_handles_nested_directory(self):
        mock_response = json.dumps([
            {"name": "themes", "type": "dir", "path": "skills/test/references/themes"},
            {"name": "guide.md", "type": "file", "download_url": "https://example.com/guide.md",
             "path": "skills/test/references/guide.md"},
        ])
        with patch("brunnr.registry.fetch", return_value=mock_response):
            base = "https://raw.githubusercontent.com/Peleke/brunnr/main"
            result = list_directory(base, "skills/test/references")
            assert len(result) == 2
            dirs = [e for e in result if e["type"] == "dir"]
            assert len(dirs) == 1
            assert dirs[0]["name"] == "themes"

    def test_empty_directory(self):
        with patch("brunnr.registry.fetch", return_value="[]"):
            base = "https://raw.githubusercontent.com/Peleke/brunnr/main"
            result = list_directory(base, "skills/test/references")
            assert result == []


# ---------------------------------------------------------------------------
# Install with references
# ---------------------------------------------------------------------------


class TestInstallReferences:
    """Install command should fetch references/ subdirectory."""

    def _run_install(self, tmp_path, slug, fetch_map, list_dir_map=None):
        """Helper to run install with mocked network."""
        from brunnr.commands import install

        def mock_fetch(url):
            return fetch_map.get(url)

        def mock_list_dir(base, path):
            if list_dir_map and path in list_dir_map:
                return list_dir_map[path]
            return None

        args = SimpleNamespace(
            registry="https://github.com/Peleke/brunnr",
            skill=slug,
            yes=True,
            force=True,
            target=None,
            with_tests=False,
            list_skills=False,
        )

        original_cwd = os.getcwd()
        os.chdir(tmp_path)
        try:
            with patch("brunnr.commands.install.fetch", side_effect=mock_fetch), \
                 patch("brunnr.commands.install.list_directory", side_effect=mock_list_dir), \
                 patch("brunnr.registry.fetch", side_effect=mock_fetch):
                result = install.run(args)
        finally:
            os.chdir(original_cwd)

        return result

    def test_installs_skill_with_references(self, tmp_path):
        skill_content = "---\nname: test-skill\ndescription: Test\n---\n# Test"
        refs_listing = [
            {"name": "guide.md", "type": "file",
             "download_url": "https://example.com/guide.md",
             "path": "skills/test-skill/references/guide.md"},
            {"name": "schema.json", "type": "file",
             "download_url": "https://example.com/schema.json",
             "path": "skills/test-skill/references/schema.json"},
        ]

        fetch_map = {
            "https://raw.githubusercontent.com/Peleke/brunnr/main/skills/test-skill/SKILL.md": skill_content,
            "https://raw.githubusercontent.com/Peleke/brunnr/main/schemas/test-skill/output.schema.json": None,
            "https://example.com/guide.md": "# Guide content",
            "https://example.com/schema.json": '{"type": "object"}',
        }
        list_dir_map = {
            "skills/test-skill/references": refs_listing,
        }

        result = self._run_install(tmp_path, "test-skill", fetch_map, list_dir_map)

        assert result == 0
        assert (tmp_path / "skills" / "test-skill" / "SKILL.md").exists()
        assert (tmp_path / "skills" / "test-skill" / "references" / "guide.md").exists()
        assert (tmp_path / "skills" / "test-skill" / "references" / "schema.json").exists()
        assert (tmp_path / "skills" / "test-skill" / "references" / "guide.md").read_text() == "# Guide content"

    def test_installs_nested_references(self, tmp_path):
        """References with subdirectories (e.g., themes/) should be fetched."""
        skill_content = "---\nname: nested\ndescription: Nested refs\n---\n# Nested"
        refs_listing = [
            {"name": "themes", "type": "dir", "path": "skills/nested/references/themes"},
        ]
        themes_listing = [
            {"name": "modern.md", "type": "file",
             "download_url": "https://example.com/modern.md",
             "path": "skills/nested/references/themes/modern.md"},
        ]

        fetch_map = {
            "https://raw.githubusercontent.com/Peleke/brunnr/main/skills/nested/SKILL.md": skill_content,
            "https://raw.githubusercontent.com/Peleke/brunnr/main/schemas/nested/output.schema.json": None,
            "https://example.com/modern.md": "# Modern theme",
        }
        list_dir_map = {
            "skills/nested/references": refs_listing,
            "skills/nested/references/themes": themes_listing,
        }

        result = self._run_install(tmp_path, "nested", fetch_map, list_dir_map)

        assert result == 0
        assert (tmp_path / "skills" / "nested" / "references" / "themes" / "modern.md").exists()

    def test_install_without_references(self, tmp_path):
        """Skills without references/ should install normally."""
        skill_content = "---\nname: basic\ndescription: Basic\n---\n# Basic"

        fetch_map = {
            "https://raw.githubusercontent.com/Peleke/brunnr/main/skills/basic/SKILL.md": skill_content,
            "https://raw.githubusercontent.com/Peleke/brunnr/main/schemas/basic/output.schema.json": None,
        }

        result = self._run_install(tmp_path, "basic", fetch_map)

        assert result == 0
        assert (tmp_path / "skills" / "basic" / "SKILL.md").exists()
        assert not (tmp_path / "skills" / "basic" / "references").exists()

    def test_conventions_auto_installed(self, tmp_path):
        """Skills referencing _conventions.md should trigger auto-install."""
        skill_content = "---\nname: scanner\ndescription: Scanner\n---\nRead _conventions.md\n# Scanner"

        fetch_map = {
            "https://raw.githubusercontent.com/Peleke/brunnr/main/skills/scanner/SKILL.md": skill_content,
            "https://raw.githubusercontent.com/Peleke/brunnr/main/schemas/scanner/output.schema.json": None,
            "https://raw.githubusercontent.com/Peleke/brunnr/main/skills/_conventions.md": "# Shared conventions",
        }

        result = self._run_install(tmp_path, "scanner", fetch_map)

        assert result == 0
        assert (tmp_path / "skills" / "_conventions.md").exists()
        assert (tmp_path / "skills" / "_conventions.md").read_text() == "# Shared conventions"

    def test_conventions_not_re_downloaded(self, tmp_path):
        """If _conventions.md already exists, don't re-fetch."""
        (tmp_path / "skills").mkdir(parents=True)
        (tmp_path / "skills" / "_conventions.md").write_text("# Existing")

        skill_content = "---\nname: scanner\ndescription: Scanner\n---\nRead _conventions.md\n# Scanner"

        fetch_map = {
            "https://raw.githubusercontent.com/Peleke/brunnr/main/skills/scanner/SKILL.md": skill_content,
            "https://raw.githubusercontent.com/Peleke/brunnr/main/schemas/scanner/output.schema.json": None,
        }

        result = self._run_install(tmp_path, "scanner", fetch_map)

        assert result == 0
        # Should keep existing, not overwrite
        assert (tmp_path / "skills" / "_conventions.md").read_text() == "# Existing"

    def test_lockfile_records_references(self, tmp_path):
        """Lockfile should include reference file paths."""
        skill_content = "---\nname: tracked\ndescription: Tracked\n---\n# Tracked"
        refs_listing = [
            {"name": "guide.md", "type": "file",
             "download_url": "https://example.com/guide.md",
             "path": "skills/tracked/references/guide.md"},
        ]

        fetch_map = {
            "https://raw.githubusercontent.com/Peleke/brunnr/main/skills/tracked/SKILL.md": skill_content,
            "https://raw.githubusercontent.com/Peleke/brunnr/main/schemas/tracked/output.schema.json": None,
            "https://example.com/guide.md": "# Guide",
        }
        list_dir_map = {
            "skills/tracked/references": refs_listing,
        }

        self._run_install(tmp_path, "tracked", fetch_map, list_dir_map)

        lockfile = json.loads((tmp_path / "skills.lock.json").read_text())
        files = lockfile["skills"]["tracked"]["files"]
        assert "skills/tracked/SKILL.md" in files
        assert "skills/tracked/references/guide.md" in files

    def test_skill_not_found(self, tmp_path):
        """Should return 1 if SKILL.md can't be fetched."""
        from brunnr.commands import install

        fetch_map = {
            "https://raw.githubusercontent.com/Peleke/brunnr/main/skills/missing/SKILL.md": None,
        }

        def mock_fetch(url):
            return fetch_map.get(url)

        args = SimpleNamespace(
            registry="https://github.com/Peleke/brunnr",
            skill="missing",
            yes=True,
            force=True,
            target=None,
            with_tests=False,
            list_skills=False,
        )

        original_cwd = os.getcwd()
        os.chdir(tmp_path)
        try:
            with patch("brunnr.commands.install.fetch", side_effect=mock_fetch), \
                 patch("brunnr.commands.install.list_directory", return_value=None), \
                 patch("brunnr.registry.fetch", side_effect=mock_fetch):
                result = install.run(args)
        finally:
            os.chdir(original_cwd)

        assert result == 1


# ---------------------------------------------------------------------------
# Trigger workflow manifest logic
# ---------------------------------------------------------------------------


class TestTriggerManifest:
    """Validate the manifest generation logic from trigger-skillipedia.yml."""

    def test_only_includes_dirs_with_skill_md(self, tmp_path):
        """Simulate: for d in skills/*/; do [ -f "${d}SKILL.md" ] && basename "$d"; done"""
        skills = tmp_path / "skills"
        skills.mkdir()

        # Skill with SKILL.md
        (skills / "valid-skill").mkdir()
        (skills / "valid-skill" / "SKILL.md").write_text("# Valid")

        # Skill with references/ (still has SKILL.md)
        (skills / "with-refs").mkdir()
        (skills / "with-refs" / "SKILL.md").write_text("# Has refs")
        (skills / "with-refs" / "references").mkdir()
        (skills / "with-refs" / "references" / "guide.md").write_text("# Guide")

        # Directory without SKILL.md
        (skills / "no-skill-md").mkdir()

        # Convention file (not a directory)
        (skills / "_conventions.md").write_text("# Conventions")

        slugs = []
        for d in sorted(skills.iterdir()):
            if d.is_dir() and (d / "SKILL.md").exists():
                slugs.append(d.name)

        assert "valid-skill" in slugs
        assert "with-refs" in slugs
        assert "no-skill-md" not in slugs
        assert "_conventions.md" not in slugs
        assert len(slugs) == 2
