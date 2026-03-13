"""brunnr inspect — preview a skill without installing."""

from __future__ import annotations

import json
import sys

from brunnr.registry import registry_base, fetch_skill_content, fetch_skill_metadata, repo_parts
from brunnr.scanner import scan_skill_md


def run(args) -> int:
    base = registry_base(args.registry)
    slug = args.skill
    full = getattr(args, "full", False)
    json_out = getattr(args, "json_out", False)

    print(f"Fetching {slug}...")
    content = fetch_skill_content(base, slug)
    if content is None:
        print(f"ERROR: skill '{slug}' not found in registry.", file=sys.stderr)
        return 1

    meta = fetch_skill_metadata(base, slug)
    if meta is None:
        meta = {"name": slug}

    # Run scanner
    scan = scan_skill_md(content)
    scan_verdict = scan.get("verdict", "UNKNOWN")

    if json_out:
        print(json.dumps({
            "slug": slug,
            "metadata": meta,
            "scan_result": scan_verdict,
            "lines": len(content.splitlines()),
        }, indent=2))
        return 0

    # Header
    rp = repo_parts(base)
    source_url = f"https://github.com/{rp[0]}/{rp[1]}/tree/main/skills/{slug}" if len(rp) >= 2 else "unknown"
    print(f"\n{'=' * 60}")
    print(f"  {meta.get('name', slug)}")
    print(f"{'=' * 60}")
    print(f"  Description: {meta.get('description', '—')}")
    print(f"  Source:      {source_url}")
    print(f"  Scan:        {scan_verdict}")
    print(f"  Lines:       {len(content.splitlines())}")
    print(f"{'=' * 60}\n")

    if full:
        print(content)
    else:
        lines = content.splitlines()
        preview = "\n".join(lines[:30])
        print(preview)
        if len(lines) > 30:
            print(f"\n  ... ({len(lines) - 30} more lines, use --full to see all)")

    return 0
