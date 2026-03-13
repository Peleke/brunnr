"""brunnr search — find skills in the registry."""

from __future__ import annotations

import json
import sys

from brunnr.registry import fetch, registry_base, list_skills, fetch_skill_metadata


def run(args) -> int:
    base = registry_base(args.registry)
    query = getattr(args, "query", "")
    tag_filter = getattr(args, "tag", None)
    json_out = getattr(args, "json_out", False)

    if not query and not tag_filter:
        print("ERROR: provide a search query or --tag filter.", file=sys.stderr)
        return 1

    # Get all skills from registry, then filter locally
    all_slugs = list_skills(base)
    if not all_slugs:
        print("No skills found (or registry unreachable).", file=sys.stderr)
        return 1

    results = []
    for slug in all_slugs:
        meta = fetch_skill_metadata(base, slug)
        if meta is None:
            continue

        name = meta.get("name", slug)
        desc = meta.get("description", "")

        # Query match: slug or description
        if query and query.lower() not in name.lower() and query.lower() not in desc.lower():
            continue

        # Tag filter (check if tag appears in description as fallback — SKILL.md frontmatter is flat)
        if tag_filter and tag_filter.lower() not in desc.lower() and tag_filter.lower() not in name.lower():
            continue

        results.append({"slug": slug, "description": desc})

    if not results:
        print(f"No skills matching '{query or tag_filter}'.", file=sys.stderr)
        return 1

    if json_out:
        print(json.dumps({"results": results}, indent=2))
        return 0

    print(f"Skills matching '{query or tag_filter}':\n")
    for r in results:
        desc = r["description"][:80] + "…" if len(r["description"]) > 80 else r["description"]
        print(f"  {r['slug']:<20} {desc}")
    print(f"\n{len(results)} result(s)")
    return 0
