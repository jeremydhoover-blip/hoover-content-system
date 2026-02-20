# Examples

## Example 1: GitHub Actions workflow for docs

**Input:**
- Platform: GitHub
- Generator: Docusaurus
- Hosting: GitHub Pages
- Requirements: Lint, link check, spell check, build, deploy

**Output:**

```yaml
# .github/workflows/docs.yml
name: Documentation

on:
  push:
    branches: [main]
    paths:
      - 'docs/**'
      - 'website/**'
  pull_request:
    paths:
      - 'docs/**'
      - 'website/**'

env:
  NODE_VERSION: '20'

jobs:
  lint:
    name: Lint and validate
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: npm
          cache-dependency-path: website/package-lock.json

      - name: Install dependencies
        run: npm ci
        working-directory: website

      - name: Lint Markdown
        run: npm run lint:md
        working-directory: website

      - name: Check spelling
        run: npm run lint:spelling
        working-directory: website

      - name: Check links
        run: npm run lint:links
        working-directory: website

  build:
    name: Build
    runs-on: ubuntu-latest
    needs: lint
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: npm
          cache-dependency-path: website/package-lock.json

      - name: Install dependencies
        run: npm ci
        working-directory: website

      - name: Build website
        run: npm run build
        working-directory: website

      - name: Upload build artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: website/build

  deploy:
    name: Deploy
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'
    needs: build
    runs-on: ubuntu-latest
    permissions:
      pages: write
      id-token: write
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

**package.json scripts:**

```json
{
  "scripts": {
    "dev": "docusaurus start",
    "build": "docusaurus build",
    "lint:md": "markdownlint-cli2 'docs/**/*.md'",
    "lint:spelling": "cspell 'docs/**/*.md'",
    "lint:links": "lychee --no-progress 'docs/**/*.md'",
    "lint": "npm run lint:md && npm run lint:spelling && npm run lint:links"
  }
}
```

---

## Example 2: Markdownlint configuration

**Input:**
- Need to enforce consistent Markdown style
- Some rules need customization for documentation

**Output:**

```json
// .markdownlint.json
{
  "default": true,
  "MD013": false,
  "MD024": {
    "siblings_only": true
  },
  "MD033": {
    "allowed_elements": ["details", "summary", "kbd", "br", "img"]
  },
  "MD041": false,
  "MD046": {
    "style": "fenced"
  }
}
```

**Explanation for each rule:**

| Rule | Setting | Reason |
|------|---------|--------|
| MD013 | Disabled | Line length varies in code blocks |
| MD024 | siblings_only | Allow same heading in different sections |
| MD033 | Allow specific HTML | Need callouts, images, keyboard shortcuts |
| MD041 | Disabled | Frontmatter may precede first heading |
| MD046 | fenced | Consistent code block style |

---

## Example 3: Edge case — versioned documentation

**Input:**
- Multiple product versions need separate docs
- Users must be able to access old versions
- Latest version is default

**Output:**

**Directory structure:**

```
docs/
├── versioned_docs/
│   ├── version-2.0/
│   │   └── [all docs for v2.0]
│   └── version-1.0/
│       └── [all docs for v1.0]
├── docs/
│   └── [current/next version docs]
├── versions.json
└── docusaurus.config.js
```

**versions.json:**

```json
["2.0", "1.0"]
```

**Version dropdown configuration:**

```javascript
// docusaurus.config.js
module.exports = {
  themeConfig: {
    navbar: {
      items: [
        {
          type: 'docsVersionDropdown',
          position: 'right',
          dropdownActiveClassDisabled: true,
        },
      ],
    },
  },
};
```

**Workflow for new version:**

```bash
# When releasing new version
npm run docusaurus docs:version 3.0
```

This creates:
- `versioned_docs/version-3.0/` with snapshot of current docs
- Updates `versions.json` to include "3.0"
- Current `/docs` becomes "Next" for development

**CI consideration for versioned docs:**

```yaml
# Only build changed versions to save time
- name: Detect changed versions
  id: changes
  run: |
    echo "versions=$(git diff --name-only ${{ github.event.before }} ${{ github.sha }} | grep -oP 'version-\d+\.\d+' | sort -u | tr '\n' ' ')" >> $GITHUB_OUTPUT

- name: Build changed versions
  run: |
    for version in ${{ steps.changes.outputs.versions }}; do
      npm run build -- --out-dir build/$version
    done
```

---

## Anti-pattern example

**Bad output (do not produce):**

```
Documentation Setup

Just write markdown files and commit them. You can use any structure you want.

To deploy:
1. SSH into the server
2. Pull the latest changes
3. Run the build script
4. Restart nginx

Make sure to check your spelling before committing!
```

**Why this fails:**
- No automated validation
- Manual deployment process
- No contribution guide
- No review workflow
- No structure guidance
- "Check your spelling" is not enforcement
- No CI/CD pipeline
- No preview environment
