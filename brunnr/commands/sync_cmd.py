"""brunnr sync — discover local skills and publish new/updated ones."""

from __future__ import annotations

import sys
from pathlib import Path

from brunnr.registry import registry_base, list_skills, fetch_skill_content
from brunnr.lockfile import content_hash
from brunnr.discovery import discover_skill_files
from brunnr.frontmatter import parse_frontmatter


def run(args) -> int:
    base = registry_base(args.registry)
    dry_run = getattr(args, "dry_run", False)

    # Discover local skills
    local_files = discover_skill_files()
    if not local_files:
        print("No local skills found in ./skills/", file=sys.stderr)
        return 0

    local_slugs = {}
    for f in local_files:
        slug = f.parent.name
        local_slugs[slug] = f

    # Get registry skills
    print("Checking registry...")
    remote_slugs = set(list_skills(base))

    new_skills = []
    updated_skills = []

    for slug, skill_file in sorted(local_slugs.items()):
        content = skill_file.read_text()
        local_hash = content_hash(content)

        if slug not in remote_slugs:
            new_skills.append(slug)
            continue

        # Check if updated
        remote_content = fetch_skill_content(base, slug)
        if remote_content is None:
            new_skills.append(slug)
            continue

        remote_hash = content_hash(remote_content)
        if local_hash != remote_hash:
            updated_skills.append(slug)

    if not new_skills and not updated_skills:
        print("All local skills are in sync with the registry.")
        return 0

    if new_skills:
        print(f"\nNew skills (not in registry):")
        for s in new_skills:
            print(f"  + {s}")

    if updated_skills:
        print(f"\nUpdated skills (local differs from registry):")
        for s in updated_skills:
            print(f"  ~ {s}")

    if dry_run:
        total = len(new_skills) + len(updated_skills)
        print(f"\n{total} skill(s) would be published. Use without --dry-run to publish.")
        return 0

    # Publish each via the publish command
    from argparse import Namespace
    from brunnr.commands.publish import run as publish_run

    failed = []
    for slug in new_skills + updated_skills:
        skill_path = local_slugs[slug].parent
        pub_args = Namespace(
            path=str(skill_path),
            dry_run=False,
        )
        print(f"\n--- Publishing {slug} ---")
        rc = publish_run(pub_args)
        if rc != 0:
            failed.append(slug)

    if failed:
        print(f"\nFailed to publish: {', '.join(failed)}", file=sys.stderr)
        return 1

    print(f"\nSync complete. {len(new_skills) + len(updated_skills)} skill(s) published.")
    return 0
