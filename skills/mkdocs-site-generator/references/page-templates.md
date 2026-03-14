# Page Templates

Templates for each documentation page type. Replace `{PLACEHOLDERS}` with project-specific content.

## Home Page (`docs/index.md`)

```markdown
# {PROJECT_NAME}

{ONE_LINE_DESCRIPTION}

## Features

- **{Feature 1}** — {brief description}
- **{Feature 2}** — {brief description}
- **{Feature 3}** — {brief description}

## Quick Install

    ```bash
    {INSTALL_COMMAND}
    ```

## Quick Example

    ```typescript
    {MINIMAL_WORKING_EXAMPLE}
    ```

## Next Steps

- [Installation](getting-started/installation.md) — setup and prerequisites
- [Quick Start](getting-started/quickstart.md) — build something in 5 minutes
- [Core Concepts](getting-started/concepts.md) — understand the architecture
```

**Rules:**
- Hero example must be copy-pasteable and actually work
- Features list: 3-6 items max, verb-first descriptions
- No marketing fluff — developers read this

## Installation Page (`docs/getting-started/installation.md`)

```markdown
# Installation

## Prerequisites

- Node.js {MIN_VERSION} or later
- {PACKAGE_MANAGER} (recommended) or npm

## Install

    ```bash
    # pnpm (recommended)
    pnpm add {PACKAGE_NAME}

    # npm
    npm install {PACKAGE_NAME}

    # yarn
    yarn add {PACKAGE_NAME}
    ```

## TypeScript Configuration

{PROJECT_NAME} is written in TypeScript with strict mode.
Ensure your `tsconfig.json` includes:

    ```json
    {
      "compilerOptions": {
        "strict": true,
        "moduleResolution": "{MODULE_RESOLUTION}",
        "module": "{MODULE_TYPE}"
      }
    }
    ```

## Verify Installation

    ```typescript
    import { {MAIN_EXPORT} } from '{PACKAGE_NAME}';
    console.log(typeof {MAIN_EXPORT}); // 'function'
    ```
```

## Quick Start Page (`docs/getting-started/quickstart.md`)

```markdown
# Quick Start

Build a working {USE_CASE} in under 5 minutes.

## Step 1: {First meaningful action}

    ```typescript
    {CODE}
    ```

{BRIEF_EXPLANATION — 1-2 sentences max}

## Step 2: {Second action}

    ```typescript
    {CODE}
    ```

## Step 3: {Third action}

    ```typescript
    {CODE}
    ```

## Complete Example

    ```typescript
    {FULL_WORKING_EXAMPLE}
    ```

## What's Next?

- [Core Concepts](concepts.md) — understand {KEY_ABSTRACTION}
- [{FEATURE} Guide](../guides/{feature}.md) — deep dive into {FEATURE}
```

**Rules:**
- Maximum 5 steps
- Every code block must be part of ONE runnable script
- "Complete Example" at the end assembles all steps

## Core Concepts Page (`docs/getting-started/concepts.md`)

```markdown
# Core Concepts

## Architecture Overview

    ```mermaid
    {ARCHITECTURE_DIAGRAM}
    ```

## {Core Abstraction 1}

{What it is, why it exists, one-paragraph explanation}

    ```typescript
    {INTERFACE_DEFINITION — from source}
    ```

{How users interact with it}

## How They Fit Together

{Paragraph explaining the flow / lifecycle / interaction pattern}

## Design Philosophy

- **{Principle 1}** — {explanation}
- **{Principle 2}** — {explanation}
```

**Rules:**
- Architecture diagram is MANDATORY (mermaid)
- Show actual interface definitions from source code
- Explain the WHY, not just the WHAT

## Guide Page (`docs/guides/{feature}.md`)

```markdown
# {Feature Name}

{What this feature does and when to use it — 2-3 sentences}

## Basic Usage

    ```typescript
    {SIMPLEST_WORKING_EXAMPLE}
    ```

## Configuration

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| {opt}  | {T}  | {def}   | {desc}      |

## {Pattern/Use Case 1}

{Explanation + code example}

## {Pattern/Use Case 2}

{Explanation + code example}

## See Also

- [{Related Feature}](../{path}) — {why it's related}
- [Types Reference](../reference/types.md#{anchor}) — {specific types}
```

**Rules:**
- Start with simplest possible example, build complexity
- Every configuration option must be documented
- Include at least 2 real-world patterns
- Link to relevant types in reference section

## Types Reference (`docs/reference/types.md`)

```markdown
# Type Reference

## {Module Group}

### `{TypeName}`

{Brief description}

    ```typescript
    {FULL_TYPE_DEFINITION — copied from source}
    ```

| Property | Type | Description |
|----------|------|-------------|
| {prop}   | {T}  | {desc}      |

**Used by:** [{Function/Interface}](#{anchor})
```

**Rules:**
- Copy type definitions EXACTLY from source (don't paraphrase)
- Include property tables for interfaces with 3+ properties
- Cross-reference everywhere
- Group by module/domain, not alphabetically

## Exports Reference (`docs/reference/exports.md`)

```markdown
# API Exports

Everything exported from `{PACKAGE_NAME}`:

## Functions

| Function | Module | Description |
|----------|--------|-------------|
| `{name}` | `{module}` | {brief} |

## Types

| Type | Module | Description |
|------|--------|-------------|
| `{name}` | `{module}` | {brief} |
```
