#!/usr/bin/env python3
"""Scan recent GH activity + buildlog entries across repos for content planning.

Usage:
    python scan_repos.py [--days N] [--repos path1,path2,...] [--format json|summary]

Output: JSON array of repo objects with merged PRs, open issues, commits,
        buildlog entries (with fan-out annotations), and .buildlog metadata.
"""

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path

PROJECTS_DIR = Path.home() / "Documents" / "Projects"

# Fan-out taxonomy: buildlog section patterns → content types they can generate
FANOUT_RULES = [
    {
        "pattern": r"(?:The Goal|Context)",
        "content_type": "provocation",
        "channel": "linkedin",
        "reason": "Goal/context framing → LinkedIn provocation post",
    },
    {
        "pattern": r"(?:Architecture|What We Built|Components)",
        "content_type": "architecture",
        "channel": "blog",
        "reason": "Architecture details → technical blog post",
    },
    {
        "pattern": r"(?:The Journey|What Happened|What Went Wrong)",
        "content_type": "build_log",
        "channel": "substack",
        "reason": "Journey narrative → Substack build-in-public post",
    },
    {
        "pattern": r"(?:Improvements|What I Learned|Lessons|Mistakes)",
        "content_type": "lessons",
        "channel": "linkedin",
        "reason": "Lessons learned → LinkedIn reflection post",
    },
    {
        "pattern": r"(?:Test Results|Cost.*Performance|Benchmarks)",
        "content_type": "results",
        "channel": "blog",
        "reason": "Quantitative results → data-driven blog post",
    },
]


def run_gh(args: list[str], cwd: str) -> str | None:
    """Run a gh CLI command, return stdout or None on failure."""
    try:
        result = subprocess.run(
            ["gh", *args],
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=15,
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass
    return None


def run_git(args: list[str], cwd: str) -> str | None:
    """Run a git command, return stdout or None on failure."""
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=10,
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass
    return None


def detect_repos(projects_dir: Path) -> list[Path]:
    """Auto-detect git repos with GitHub remotes under projects_dir."""
    repos = []
    if not projects_dir.is_dir():
        return repos
    for d in sorted(projects_dir.iterdir()):
        if d.is_dir() and (d / ".git").is_dir():
            # Quick check for GH remote
            if run_gh(["repo", "view", "--json", "name"], cwd=str(d)):
                repos.append(d)
    return repos


def scan_buildlog_entries(repo_path: Path, since_date: str) -> list[dict]:
    """Scan buildlog/*.md entries, extract metadata + fan-out opportunities."""
    buildlog_dir = repo_path / "buildlog"
    if not buildlog_dir.is_dir():
        return []

    entries = []
    for f in sorted(buildlog_dir.glob("*.md")):
        # Skip templates and system files
        if f.name.startswith("_") or f.name == "BUILDLOG_SYSTEM.md":
            continue

        m = re.match(r"(\d{4}-\d{2}-\d{2})-(.+)\.md", f.name)
        if not m:
            continue

        entry_date = m.group(1)
        slug = m.group(2)

        if entry_date < since_date:
            continue

        content = f.read_text(errors="replace")

        # Extract title from first H1
        title = slug.replace("-", " ").title()
        title_match = re.search(r"^#\s+(.+)", content, re.MULTILINE)
        if title_match:
            title = title_match.group(1).strip()

        # Extract H2 sections
        sections = [
            sec.group(1).strip()
            for sec in re.finditer(r"^##\s+(.+)", content, re.MULTILINE)
        ]

        # Extract commit hashes (7+ hex chars in backticks)
        commits = re.findall(r"`([0-9a-f]{7,})`", content)[:10]

        # Extract PR/issue references
        gh_refs = re.findall(
            r"https://github\.com/[^\s)]+(?:pull|issues)/\d+", content
        )
        local_refs = re.findall(r"#(\d+)", content)

        # Word count as depth signal
        word_count = len(content.split())

        # Fan-out analysis: which content types can this entry generate?
        fanout = []
        sections_text = " ".join(sections)
        for rule in FANOUT_RULES:
            if re.search(rule["pattern"], sections_text, re.IGNORECASE):
                fanout.append(
                    {
                        "content_type": rule["content_type"],
                        "channel": rule["channel"],
                        "reason": rule["reason"],
                    }
                )

        # Depth classification
        if word_count > 800:
            depth = "deep"  # Full narrative, multiple content pieces
        elif word_count > 300:
            depth = "medium"  # Solid entry, 1-2 pieces
        else:
            depth = "shallow"  # Quick log, maybe 1 piece

        entries.append(
            {
                "date": entry_date,
                "slug": slug,
                "title": title,
                "file": str(f),
                "sections": sections,
                "commits": commits,
                "gh_refs": gh_refs,
                "issue_refs": local_refs,
                "word_count": word_count,
                "depth": depth,
                "fanout": fanout,
                "fanout_count": len(fanout),
            }
        )

    return entries


def scan_buildlog_metadata(repo_path: Path) -> dict:
    """Read .buildlog/ machine-readable metadata."""
    metadata = {}

    for meta_loc in [repo_path / "buildlog" / ".buildlog", repo_path / ".buildlog"]:
        if not meta_loc.is_dir():
            continue

        # review_learnings.json
        rl_path = meta_loc / "review_learnings.json"
        if rl_path.is_file():
            try:
                rl = json.loads(rl_path.read_text())
                learnings = rl.get("learnings", {})
                metadata["review_learnings_count"] = len(learnings)
                metadata["review_history_count"] = len(rl.get("review_history", []))
                # Extract top learnings by reinforcement count
                top = sorted(
                    learnings.values(),
                    key=lambda x: x.get("reinforcement_count", 0),
                    reverse=True,
                )[:5]
                metadata["top_learnings"] = [
                    {
                        "rule": l["rule"],
                        "category": l["category"],
                        "reinforcements": l.get("reinforcement_count", 0),
                    }
                    for l in top
                ]
            except (json.JSONDecodeError, KeyError):
                pass

        # promoted.json
        pr_path = meta_loc / "promoted.json"
        if pr_path.is_file():
            try:
                pr = json.loads(pr_path.read_text())
                metadata["promoted_skill_count"] = len(pr.get("skill_ids", []))
            except (json.JSONDecodeError, KeyError):
                pass

        # reward_events.jsonl
        re_path = meta_loc / "reward_events.jsonl"
        if re_path.is_file():
            try:
                lines = re_path.read_text().strip().split("\n")
                metadata["reward_event_count"] = len([l for l in lines if l.strip()])
            except Exception:
                pass

        # gauntlet_state.json
        gs_path = meta_loc / "gauntlet_state.json"
        if gs_path.is_file():
            try:
                gs = json.loads(gs_path.read_text())
                metadata["gauntlet_iteration"] = gs.get("iteration", 0)
            except (json.JSONDecodeError, KeyError):
                pass

        break  # Only need one metadata location

    return metadata


def scan_repo(repo_path: Path, since_date: str) -> dict:
    """Scan a single repo: GH activity + buildlog entries."""
    repo_name = repo_path.name
    cwd = str(repo_path)

    # Repo full name
    full_name = run_gh(
        ["repo", "view", "--json", "nameWithOwner", "-q", ".nameWithOwner"], cwd=cwd
    )
    if not full_name:
        full_name = repo_name

    # Merged PRs since date
    prs_raw = run_gh(
        [
            "pr",
            "list",
            "--state",
            "merged",
            "--limit",
            "20",
            "--json",
            "number,title,mergedAt,url,labels",
        ],
        cwd=cwd,
    )
    prs = []
    if prs_raw:
        try:
            all_prs = json.loads(prs_raw)
            prs = [p for p in all_prs if p.get("mergedAt", "") >= since_date]
        except json.JSONDecodeError:
            pass

    # Open issues
    issues_raw = run_gh(
        [
            "issue",
            "list",
            "--state",
            "open",
            "--limit",
            "10",
            "--json",
            "number,title,url,labels,createdAt",
        ],
        cwd=cwd,
    )
    issues = []
    if issues_raw:
        try:
            issues = json.loads(issues_raw)
        except json.JSONDecodeError:
            pass

    # Recent commits
    commits_raw = run_git(
        [
            "log",
            "--oneline",
            f"--since={since_date}",
            "--format=%H|||%h|||%s|||%ci",
            "HEAD",
        ],
        cwd=cwd,
    )
    commits = []
    if commits_raw:
        for line in commits_raw.split("\n")[:20]:
            parts = line.split("|||")
            if len(parts) == 4:
                commits.append(
                    {
                        "hash": parts[1],
                        "subject": parts[2],
                        "date": parts[3],
                    }
                )

    # Buildlog entries + metadata
    buildlog_entries = scan_buildlog_entries(repo_path, since_date)
    buildlog_metadata = scan_buildlog_metadata(repo_path)

    # Compute fan-out summary
    total_fanout = sum(e["fanout_count"] for e in buildlog_entries)

    return {
        "repo": repo_name,
        "full_name": full_name,
        "path": cwd,
        "merged_prs": prs,
        "open_issues": issues,
        "recent_commits": commits,
        "buildlog_entries": buildlog_entries,
        "buildlog_metadata": buildlog_metadata,
        "summary": {
            "pr_count": len(prs),
            "issue_count": len(issues),
            "commit_count": len(commits),
            "buildlog_entry_count": len(buildlog_entries),
            "total_fanout_opportunities": total_fanout,
            "deep_entries": len(
                [e for e in buildlog_entries if e["depth"] == "deep"]
            ),
        },
    }


def main():
    parser = argparse.ArgumentParser(
        description="Scan GH activity + buildlog entries for content planning."
    )
    parser.add_argument("--days", type=int, default=14, help="Look back N days")
    parser.add_argument("--repos", type=str, default="", help="Comma-separated paths")
    parser.add_argument(
        "--format",
        choices=["json", "summary"],
        default="json",
        help="Output format",
    )
    args = parser.parse_args()

    since = (datetime.now() - timedelta(days=args.days)).strftime("%Y-%m-%d")

    if args.repos:
        repo_paths = [Path(p.strip()) for p in args.repos.split(",")]
    else:
        repo_paths = detect_repos(PROJECTS_DIR)

    results = []
    for rp in repo_paths:
        if rp.is_dir():
            results.append(scan_repo(rp, since))

    if args.format == "json":
        json.dump(results, sys.stdout, indent=2, default=str)
        print()
    elif args.format == "summary":
        for r in results:
            s = r["summary"]
            print(f"\n{'='*60}")
            print(f"  {r['full_name']}")
            print(f"{'='*60}")
            print(
                f"  PRs: {s['pr_count']}  Issues: {s['issue_count']}  "
                f"Commits: {s['commit_count']}"
            )
            print(
                f"  Buildlog: {s['buildlog_entry_count']} entries "
                f"({s['deep_entries']} deep)  "
                f"Fan-out: {s['total_fanout_opportunities']} opportunities"
            )
            if r["buildlog_entries"]:
                print(f"\n  Recent entries:")
                for e in r["buildlog_entries"][-5:]:
                    fanout_str = (
                        ", ".join(f["content_type"] for f in e["fanout"])
                        if e["fanout"]
                        else "none"
                    )
                    print(
                        f"    [{e['date']}] {e['title'][:50]}"
                        f"  ({e['depth']}, {e['word_count']}w, fanout: {fanout_str})"
                    )
            meta = r["buildlog_metadata"]
            if meta:
                print(f"\n  Metadata:")
                if "review_learnings_count" in meta:
                    print(f"    Learnings: {meta['review_learnings_count']}")
                if "promoted_skill_count" in meta:
                    print(f"    Promoted skills: {meta['promoted_skill_count']}")
                if "reward_event_count" in meta:
                    print(f"    Reward events: {meta['reward_event_count']}")
        print()


if __name__ == "__main__":
    main()
