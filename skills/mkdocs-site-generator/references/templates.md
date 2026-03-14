# Configuration Templates

## mkdocs.yml — ReadTheDocs Theme

```yaml
site_name: {PROJECT_NAME}
site_url: https://{GITHUB_USER}.github.io/{REPO_NAME}/
site_description: {DESCRIPTION}
repo_url: https://github.com/{GITHUB_USER}/{REPO_NAME}
repo_name: {GITHUB_USER}/{REPO_NAME}

theme:
  name: readthedocs

markdown_extensions:
  - admonition
  - attr_list
  - md_in_html
  - tables
  - toc:
      permalink: true
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format
  - pymdownx.inlinehilite
  - pymdownx.tabbed:
      alternate_style: true

extra_javascript:
  - https://unpkg.com/mermaid@11/dist/mermaid.min.js

nav:
  {NAVIGATION}
```

## mkdocs.yml — Material Theme

```yaml
site_name: {PROJECT_NAME}
site_url: https://{GITHUB_USER}.github.io/{REPO_NAME}/
site_description: {DESCRIPTION}
repo_url: https://github.com/{GITHUB_USER}/{REPO_NAME}
repo_name: {GITHUB_USER}/{REPO_NAME}

theme:
  name: material
  palette:
    - scheme: default
      primary: {PRIMARY_COLOR}
      accent: {ACCENT_COLOR}
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    - scheme: slate
      primary: {PRIMARY_COLOR}
      accent: {ACCENT_COLOR}
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.expand
    - navigation.top
    - content.code.copy
    - content.tabs.link
    - search.suggest
    - search.highlight
  icon:
    repo: fontawesome/brands/github

markdown_extensions:
  - admonition
  - attr_list
  - md_in_html
  - tables
  - toc:
      permalink: true
  - pymdownx.details
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.inlinehilite
  - pymdownx.snippets
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format
  - pymdownx.tabbed:
      alternate_style: true

nav:
  {NAVIGATION}
```

## GitHub Actions — deploy-pages (Recommended)

```yaml
name: Deploy docs

on:
  push:
    branches: [main]
    paths:
      - 'docs/**'
      - 'mkdocs.yml'
      - 'requirements.txt'
      - '.github/workflows/docs.yml'
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: true

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Build docs
        run: mkdocs build --strict

      - uses: actions/upload-pages-artifact@v3
        with:
          path: site

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - id: deployment
        uses: actions/deploy-pages@v4
```

## GitHub Actions — mike (Versioned Docs)

```yaml
name: Deploy docs

on:
  push:
    branches: [main]
    tags: ['v*']
    paths:
      - 'docs/**'
      - 'mkdocs.yml'
      - 'requirements.txt'
      - '.github/workflows/docs.yml'
  workflow_dispatch:

permissions:
  contents: write

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Configure Git
        run: |
          git config user.name github-actions[bot]
          git config user.email 41898282+github-actions[bot]@users.noreply.github.com

      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Deploy dev docs (main branch)
        if: github.ref == 'refs/heads/main'
        run: mike deploy --push --update-aliases dev latest

      - name: Deploy release docs (tag)
        if: startsWith(github.ref, 'refs/tags/v')
        run: |
          VERSION=${GITHUB_REF#refs/tags/v}
          mike deploy --push --update-aliases $VERSION stable
          mike set-default --push stable
```
