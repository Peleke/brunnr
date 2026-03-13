"""brunnr explore — browse skills from the registry."""

from __future__ import annotations

import json
import sys

from brunnr.registry import registry_base, list_skills, fetch_skill_metadata


def run(args) -> int:
    base = registry_base(args.registry)
    limit = getattr(args, "limit", 20)
    json_out = getattr(args, "json_out", False)

    all_slugs = list_skills(base)
    if not all_slugs:
        print("No skills found (or registry unreachable).", file=sys.stderr)
        return 1

    results = []
    for slug in all_slugs[:limit]:
        meta = fetch_skill_metadata(base, slug)
        desc = meta.get("description", "—") if meta else "—"
        results.append({"slug": slug, "description": desc})

    if json_out:
        print(json.dumps({"skills": results}, indent=2))
        return 0

    print(f"Skills in registry ({len(all_slugs)} total):\n")
    for r in results:
        desc = r["description"][:70] + "…" if len(r["description"]) > 70 else r["description"]
        print(f"  {r['slug']:<20} {desc}")

    if len(all_slugs) > limit:
        print(f"\n  ... and {len(all_slugs) - limit} more (use --limit to see more)")
    print(f"\nRun `brunnr inspect <slug>` for details.")
    return 0
