# Templates

## Documentation repository structure

```
docs/
├── README.md                    # Contribution guide
├── .github/
│   ├── workflows/
│   │   ├── docs-build.yml      # Build and deploy
│   │   └── docs-lint.yml       # Validation
│   └── PULL_REQUEST_TEMPLATE.md
├── config/
│   └── [site-generator-config]
├── content/
│   ├── index.md
│   ├── getting-started/
│   ├── guides/
│   ├── reference/
│   └── changelog/
├── static/
│   └── images/
└── scripts/
    └── validate-links.js
```

---

## CI workflow — linting

```yaml
# .github/workflows/docs-lint.yml
name: Docs Lint

on:
  pull_request:
    paths:
      - 'docs/**'

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Lint Markdown
        uses: DavidAnson/markdownlint-cli2-action@v14
        with:
          globs: 'docs/**/*.md'
      
      - name: Check links
        uses: lycheeverse/lychee-action@v1
        with:
          args: --no-progress 'docs/**/*.md'
          fail: true
      
      - name: Check spelling
        uses: streetsidesoftware/cspell-action@v5
        with:
          files: 'docs/**/*.md'
```

---

## CI workflow — build and deploy

```yaml
# .github/workflows/docs-build.yml
name: Docs Build

on:
  push:
    branches: [main]
    paths:
      - 'docs/**'
  pull_request:
    paths:
      - 'docs/**'

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
        working-directory: docs
      
      - name: Build docs
        run: npm run build
        working-directory: docs
      
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: docs/dist

  deploy:
    if: github.ref == 'refs/heads/main'
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

---

## Contributing guide template

```md
# Contributing to Documentation

## Quick edits

1. Click "Edit this page" on any documentation page.
2. Make your changes in the GitHub editor.
3. Submit a pull request.

## Local development

### Prerequisites

- Node.js 18+
- npm or yarn

### Setup

```bash
git clone [repo-url]
cd docs
npm install
npm run dev
```

Visit `http://localhost:3000` to preview.

### Commands

| Command | Description |
|---------|-------------|
| `npm run dev` | Start development server |
| `npm run build` | Build for production |
| `npm run lint` | Run linting checks |
| `npm run lint:fix` | Auto-fix linting issues |

## Writing guidelines

- Follow the [style guide](./STYLE.md)
- Use [templates](./templates/) for new pages
- Include code examples where applicable

## Pull request process

1. Create a branch: `docs/description-of-change`
2. Make changes and test locally
3. Run `npm run lint` and fix issues
4. Submit PR with description of changes
5. Request review from @docs-team
6. Address feedback
7. Merge after approval

## Review criteria

PRs are reviewed for:

- [ ] Technical accuracy
- [ ] Style guide compliance
- [ ] Link validity
- [ ] Build success
```

---

## Pull request template

```md
## Description

[What does this PR change?]

## Type of change

- [ ] New documentation
- [ ] Update existing documentation
- [ ] Fix (typo, broken link, etc.)
- [ ] Structural change

## Related

- Related issue: #
- Related code PR: #

## Checklist

- [ ] Tested locally with `npm run dev`
- [ ] Links are valid
- [ ] Follows style guide
- [ ] No spelling errors
```

---

## Variation rules
- All documentation must pass lint checks before merge.
- PR template is required for documentation repositories.
- Preview environment required for non-trivial changes.
- Version control branching strategy documented in CONTRIBUTING.
