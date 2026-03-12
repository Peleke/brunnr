# Roadmap

Planned features and future direction for brunnr.

---

## Planned: `brunnr remix`

**Zero-trust skill regeneration from intent.**

The `remix` command takes a skill and regenerates it from scratch based on the declared intent, rather than trusting the original implementation. This addresses a fundamental limitation of static scanning: a sufficiently clever attacker can write instructions that are individually benign but collectively malicious.

### How it will work

1. **Extract intent** -- Parse the skill's frontmatter `description` and section headers to understand what the skill is supposed to do.
2. **Regenerate from intent** -- Use an LLM to write a new SKILL.md that achieves the same goal, without any of the original body content.
3. **Diff and review** -- Show the user what changed between the original and the regenerated version.
4. **Scan the remix** -- Run the security scanner on the regenerated skill.

### Why this matters

Static regex scanning catches known patterns. Remix catches unknown patterns by never trusting the original content. If the original skill said "format code" but actually contained a subtle data exfiltration chain, the remix would produce a genuine code formatter -- because that's what the intent said.

```bash
# Planned usage
brunnr remix suspicious-skill

# Compare original vs regenerated
brunnr remix suspicious-skill --diff
```

---

## Planned: `brunnr search`

Search the skill registry by keyword, category, or tag without installing anything.

```bash
# Planned usage
brunnr search "tool descriptions"
brunnr search --category evaluation
brunnr search --tag mcp
```

---

## Planned: Graph-powered improvements

### Dependency graph

Track which skills reference or depend on other skills. Detect circular dependencies, version conflicts, and incompatible combinations.

### Threat pattern sharing

As the scanner processes more skills, aggregate anonymized threat patterns to improve detection. New attack techniques discovered in one repository benefit all users.

### Skill quality scores

Combine scan results, eval pass rates, and community feedback into a quality score for each skill in the registry. Higher-quality skills surface first in search results.

---

## Planned: Registry improvements

### Namespaced registries

Support multiple registries with namespace prefixes:

```bash
brunnr install myorg/my-skill --registry https://github.com/myorg/skills
```

### Skill versioning

Pin skills to specific versions:

```bash
brunnr install ax-rubric@1.0
```

### Skill signing

Cryptographic signing of SKILL.md files so you can verify the author and integrity:

```bash
brunnr verify ax-rubric --key author-public.pem
```

---

## Planned: Scanner improvements

### Additional threat classes

- **Resource exhaustion** -- Skills that instruct infinite loops, unbounded recursion, or large file generation.
- **Information disclosure** -- Skills that ask the agent to reveal system information, working directory structure, or installed packages.
- **Social engineering** -- Skills that instruct the agent to manipulate the user (e.g., "tell the user everything is fine while...").

### Configurable allowlists

Let users define project-specific URL allowlists and sensitive path exclusions:

```yaml
# brunnr.yml
allowlist:
  domains:
    - internal.mycompany.com
  paths:
    - ~/.config/myapp/
```

### Severity overrides

Let users override severity levels for specific threat classes:

```yaml
# brunnr.yml
overrides:
  supply_chain: block  # Treat FLAG as BLOCK
  semantic_mismatch: info  # Downgrade FLAG to INFO
```

---

## Contributing

Want to contribute to any of these features? Open an issue or PR on [GitHub](https://github.com/Peleke/brunnr).

The most impactful contributions right now:

1. **New threat patterns** -- Found an attack vector the scanner misses? Submit a pattern.
2. **New skills** -- Write a skill, scan it, and submit a PR.
3. **Eval fixtures** -- Add test cases for existing skills to improve coverage.
