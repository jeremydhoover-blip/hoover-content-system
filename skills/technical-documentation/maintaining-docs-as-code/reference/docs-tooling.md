# Documentation Tooling Patterns

## Table of contents
- [Static site generators](#static-site-generators)
- [Linting tools](#linting-tools)
- [Link checking](#link-checking)
- [Spell checking](#spell-checking)
- [Search integration](#search-integration)

---

## Static site generators

### Comparison

| Tool | Language | Best for | Learning curve |
|------|----------|----------|----------------|
| Docusaurus | JavaScript | React ecosystem, versioning | Medium |
| MkDocs | Python | Simple setup, Material theme | Low |
| Hugo | Go | Speed, large sites | Medium |
| Astro | JavaScript | Modern, flexible | Medium |
| GitBook | SaaS | Non-technical writers | Low |
| Sphinx | Python | Python projects, API docs | High |

### Selection criteria

| Requirement | Recommended |
|-------------|-------------|
| React/TypeScript ecosystem | Docusaurus |
| Python project | Sphinx or MkDocs |
| Fastest build times | Hugo |
| Versioned documentation | Docusaurus |
| Minimal setup | MkDocs with Material |
| Non-technical contributors | GitBook |

---

## Linting tools

### Markdown linting

**markdownlint-cli2**

```bash
npm install -D markdownlint-cli2
```

```json
// package.json
{
  "scripts": {
    "lint:md": "markdownlint-cli2 'docs/**/*.md'"
  }
}
```

**Common configuration:**

```json
{
  "default": true,
  "MD013": false,
  "MD033": {
    "allowed_elements": ["details", "summary", "br"]
  }
}
```

### Prose linting

**Vale** (style and grammar)

```bash
brew install vale
```

```yaml
# .vale.ini
StylesPath = styles
MinAlertLevel = suggestion

[*.md]
BasedOnStyles = Vale, Microsoft
```

---

## Link checking

### Tools comparison

| Tool | Type | Speed | Features |
|------|------|-------|----------|
| lychee | Rust binary | Fast | Async, configurable |
| markdown-link-check | Node.js | Medium | Simple config |
| htmltest | Go binary | Fast | HTML-focused |

### lychee configuration

```yaml
# lychee.toml
exclude = [
  "localhost",
  "127.0.0.1",
  "example.com"
]
accept = [200, 204, 301, 302]
timeout = 30
max_concurrency = 10
```

### CI integration

```yaml
- name: Check links
  uses: lycheeverse/lychee-action@v1
  with:
    args: --no-progress --exclude-all-private 'docs/**/*.md'
    fail: true
```

---

## Spell checking

### cspell configuration

```json
// cspell.json
{
  "version": "0.2",
  "language": "en",
  "words": [
    "docusaurus",
    "frontmatter",
    "monorepo"
  ],
  "ignorePaths": [
    "node_modules",
    "*.min.js"
  ],
  "dictionaries": [
    "typescript",
    "node",
    "npm"
  ]
}
```

### Project dictionary

```
// project-words.txt (one word per line)
docusaurus
frontmatter
monorepo
```

Reference in config:
```json
{
  "dictionaryDefinitions": [
    {
      "name": "project-words",
      "path": "./project-words.txt"
    }
  ],
  "dictionaries": ["project-words"]
}
```

---

## Search integration

### Options

| Solution | Type | Best for |
|----------|------|----------|
| Algolia DocSearch | Hosted | Public docs, free for OSS |
| Pagefind | Static | Privacy, self-hosted |
| Lunr.js | Client-side | Small sites |
| Meilisearch | Self-hosted | Full control |

### Algolia DocSearch setup

```javascript
// docusaurus.config.js
module.exports = {
  themeConfig: {
    algolia: {
      appId: 'YOUR_APP_ID',
      apiKey: 'YOUR_SEARCH_API_KEY',
      indexName: 'YOUR_INDEX_NAME',
    },
  },
};
```

### Pagefind setup (static)

```bash
npx pagefind --source "build" --bundle-dir "pagefind"
```

```html
<!-- Add to layout -->
<link href="/pagefind/pagefind-ui.css" rel="stylesheet">
<script src="/pagefind/pagefind-ui.js"></script>
<div id="search"></div>
<script>
  new PagefindUI({ element: "#search" });
</script>
```

---

## Hosting options

| Platform | Deployment | Custom domain | Features |
|----------|------------|---------------|----------|
| GitHub Pages | Git push | Yes | Free, GitHub integration |
| Netlify | Git push | Yes | Previews, forms, functions |
| Vercel | Git push | Yes | Previews, edge functions |
| Cloudflare Pages | Git push | Yes | Fast, analytics |
| S3 + CloudFront | CI/CD | Yes | Scalable, AWS ecosystem |

### GitHub Pages deployment

```yaml
# Required permissions
permissions:
  pages: write
  id-token: write

# Deploy step
- uses: actions/deploy-pages@v4
```

### Netlify deployment

```toml
# netlify.toml
[build]
  publish = "build"
  command = "npm run build"

[build.environment]
  NODE_VERSION = "20"
```
