# Templates

## Navigation specification document

```md
# Navigation Design: [Site Name]

## Navigation architecture

### Primary navigation (header)

| Position | Element | Behavior |
|----------|---------|----------|
| Left | Logo | Link to docs home |
| Center | Main nav items | [List items] |
| Right | Search + utilities | Search, version, theme |

**Items:**
1. [Item 1] — [destination]
2. [Item 2] — [destination]
3. [Item 3] — [destination]

### Secondary navigation (sidebar)

| Section | Behavior |
|---------|----------|
| Position | Left sidebar, [width]px |
| Collapse | Collapsible on mobile |
| State | Preserves expanded state |

**Hierarchy:**
- Section (expandable)
  - Page (link)
  - Page (link)
  - Subsection (expandable)
    - Page (link)

### Tertiary navigation (in-page)

| Element | Position | Behavior |
|---------|----------|----------|
| On this page | Right sidebar | Tracks scroll position |
| Previous/Next | Footer | Sequential navigation |

## Breadcrumbs

**Format:** Home > Section > Subsection > Page

**Rules:**
- Always visible on content pages
- Clickable except current page
- Max items: 4 (truncate middle if needed)

## Search

| Property | Value |
|----------|-------|
| Placement | Header, right side |
| Shortcut | `/` or `Cmd+K` |
| Scope | Current section or all docs |
| Results | Inline dropdown with preview |

## Mobile navigation

| Viewport | Behavior |
|----------|----------|
| < 768px | Hamburger menu, full-screen nav |
| 768-1024px | Collapsed sidebar, toggleable |
| > 1024px | Full sidebar visible |

## Version selector

| Property | Value |
|----------|-------|
| Placement | Header, near search |
| Default | Latest stable version |
| Options | [Version list] |
| Behavior | Maintains current page path if exists |
```

---

## Sidebar navigation configuration

```yaml
# sidebar.yaml (example for Docusaurus)
sidebar:
  - type: category
    label: Getting Started
    collapsed: false
    items:
      - getting-started/overview
      - getting-started/installation
      - getting-started/quick-start
  
  - type: category
    label: Guides
    collapsed: true
    items:
      - type: category
        label: Authentication
        items:
          - guides/auth/api-keys
          - guides/auth/oauth
      - type: category
        label: Data
        items:
          - guides/data/importing
          - guides/data/exporting
  
  - type: category
    label: Reference
    collapsed: true
    items:
      - type: link
        label: API Reference
        href: /api
      - reference/configuration
      - reference/cli
```

---

## Breadcrumb implementation

```md
## Breadcrumb specification

### Structure

```html
<nav aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Docs</a></li>
    <li><a href="/guides">Guides</a></li>
    <li><a href="/guides/auth">Authentication</a></li>
    <li aria-current="page">OAuth Setup</li>
  </ol>
</nav>
```

### Rules

| Rule | Implementation |
|------|----------------|
| Home link | Always "Docs" or product name |
| Separator | `>` or `/` or chevron icon |
| Current page | Not linked, `aria-current="page"` |
| Truncation | Middle items, show "..." |
| Max visible | 4 items |
```

---

## "On this page" navigation

```md
## Table of contents specification

### Extraction

- Include: H2 and H3 headings
- Exclude: H1 (page title), H4+ (too granular)

### Display

| Property | Value |
|----------|-------|
| Position | Right sidebar, sticky |
| Title | "On this page" |
| Highlight | Current section highlighted |
| Scroll | Smooth scroll to section |

### Mobile

- Hidden by default
- Accessible via dropdown or expand
```

---

## Variation rules
- Primary navigation: 5-7 items maximum.
- Sidebar depth: 3 levels maximum.
- Breadcrumbs: Required on all content pages.
- On-this-page: Required for pages with 3+ headings.
- Search: Must be accessible from every page.
