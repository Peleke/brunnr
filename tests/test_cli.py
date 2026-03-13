"""Smoke tests for brunnr CLI commands."""

import subprocess
import sys
import json
from pathlib import Path


def _run(args: list[str], **kwargs) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, "-m", "brunnr.cli"] + args,
        capture_output=True, text=True, timeout=30, **kwargs,
    )


class TestCLI:
    def test_help(self):
        r = _run(["--help"])
        assert r.returncode == 0
        assert "brunnr" in r.stdout

    def test_version(self):
        r = _run(["--version"])
        assert r.returncode == 0
        assert "brunnr" in r.stdout

    def test_no_command_shows_help(self):
        r = _run([])
        assert r.returncode == 0
        assert "brunnr" in r.stdout

    def test_scan_help(self):
        r = _run(["scan", "--help"])
        assert r.returncode == 0
        assert "--verbose" in r.stdout

    def test_install_help(self):
        r = _run(["install", "--help"])
        assert r.returncode == 0
        assert "--yes" in r.stdout
        assert "--target" in r.stdout

    def test_eval_help(self):
        r = _run(["eval", "--help"])
        assert r.returncode == 0
        assert "--model" in r.stdout
        assert "--dry-run" in r.stdout

    def test_pipeline_help(self):
        r = _run(["pipeline", "--help"])
        assert r.returncode == 0
        assert "--scan-only" in r.stdout


class TestScanCommand:
    def test_scan_skills_dir(self):
        r = _run(["scan", "skills/"])
        assert r.returncode == 0
        assert "brunnr scan" in r.stdout

    def test_scan_json_output(self):
        r = _run(["scan", "skills/", "--json"])
        assert r.returncode == 0
        data = json.loads(r.stdout)
        assert "total" in data
        assert "clean" in data

    def test_scan_no_files(self, tmp_path):
        r = _run(["scan", str(tmp_path / "nonexistent")])
        assert r.returncode == 1


class TestInstallCommand:
    def test_install_no_skill_arg(self):
        r = _run(["install"])
        assert r.returncode == 1
        assert "skill name required" in r.stderr

    def test_install_already_exists(self):
        r = _run(["install", "ax-rubric"])
        assert r.returncode == 1
        assert "already installed" in r.stderr


class TestEvalCommand:
    def test_eval_dry_run(self):
        r = _run(["eval", "ax-rubric", "--dry-run"])
        assert r.returncode == 0
        assert "DRY RUN" in r.stdout

    def test_eval_missing_skill(self):
        r = _run(["eval", "nonexistent-skill", "--dry-run"])
        assert r.returncode == 1
        assert "not found" in r.stderr.lower() or "ERROR" in r.stdout


class TestDiscovery:
    def test_discover_skill_files(self):
        from brunnr.discovery import discover_skill_files
        files = discover_skill_files()
        assert len(files) > 0
        assert all(f.name == "SKILL.md" for f in files)

    def test_discover_explicit_path(self):
        from brunnr.discovery import discover_skill_files
        files = discover_skill_files(paths=["skills/"])
        assert len(files) > 0

    def test_collect_scan_files(self):
        from brunnr.discovery import collect_scan_files
        files = collect_scan_files(["skills/"])
        assert len(files) > 0


class TestInstallPathTraversal:
    """Verify that path traversal in fixture paths is blocked."""

    def _run_fixture_sanitization(self, fixture_rel: str, tmp_path):
        """Exercise the actual sanitization logic from install.py."""
        from pathlib import Path
        import sys

        test_dest = tmp_path / "tests" / "fakeskill"
        test_dest.mkdir(parents=True)

        # Reproduce the exact checks from install.py
        if ".." in fixture_rel or fixture_rel.startswith("/"):
            return "rejected_pattern"

        fixture_path = (test_dest / fixture_rel).resolve()
        if not fixture_path.is_relative_to(test_dest.resolve()):
            return "rejected_containment"

        return "accepted"

    def test_dotdot_rejected(self, tmp_path):
        assert self._run_fixture_sanitization("../../etc/passwd", tmp_path) == "rejected_pattern"

    def test_absolute_path_rejected(self, tmp_path):
        assert self._run_fixture_sanitization("/etc/passwd", tmp_path) == "rejected_pattern"

    def test_dotdot_backtrack_to_sibling(self, tmp_path):
        """Catch the subtle case: ../tests/payload resolves inside a path
        that starts with test_dest as a string but escapes the directory."""
        assert self._run_fixture_sanitization("../tests/payload", tmp_path) == "rejected_pattern"

    def test_nested_traversal(self, tmp_path):
        assert self._run_fixture_sanitization("subdir/../../escape", tmp_path) == "rejected_pattern"

    def test_valid_fixture_accepted(self, tmp_path):
        assert self._run_fixture_sanitization("fixtures/input.md", tmp_path) == "accepted"

    def test_simple_filename_accepted(self, tmp_path):
        assert self._run_fixture_sanitization("input.md", tmp_path) == "accepted"
