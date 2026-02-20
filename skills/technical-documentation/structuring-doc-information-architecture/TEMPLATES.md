# Templates

## Standard documentation site structure

```
Documentation/
├── Home (landing page)
│
├── Getting Started
│   ├── Overview
│   ├── Installation
│   ├── Quick start
│   └── First project tutorial
│
├── Guides
│   ├── [Task-based guides organized by topic]
│   └── [Progressive complexity: basic → advanced]
│
├── Concepts
│   ├── [Core concepts and mental models]
│   └── [Architecture and design decisions]
│
├── Reference
│   ├── API reference
│   ├── Configuration reference
│   ├── CLI reference
│   └── Glossary
│
├── Troubleshooting
│   ├── Common issues
│   ├── Error reference
│   └── FAQ
│
└── Resources
    ├── Changelog
    ├── Migration guides
    └── Community
```

---

## Navigation specification template

```md
# Navigation Structure

## Primary navigation

| Label | Path | Purpose |
|-------|------|---------|
| Getting Started | /getting-started | First-time users, installation |
| Guides | /guides | Task-oriented how-tos |
| Reference | /reference | Lookup documentation |

## Secondary navigation (per section)

### Getting Started

| Order | Label | Path | Target user |
|-------|-------|------|-------------|
| 1 | Overview | /getting-started | All new users |
| 2 | Installation | /getting-started/install | Technical setup |
| 3 | Quick start | /getting-started/quickstart | Hands-on learners |

### Guides

[Section-specific navigation...]

## Cross-cutting navigation

| Element | Location | Purpose |
|---------|----------|---------|
| Search | Header | Quick access to any content |
| Version selector | Header | Switch documentation versions |
| Breadcrumbs | Below header | Location awareness |
| "On this page" | Right sidebar | In-page navigation |
| Previous/Next | Footer | Sequential navigation |
```

---

## Content inventory template

```md
# Content Inventory

## Current state

| Path | Title | Type | Status | Notes |
|------|-------|------|--------|-------|
| /install | Installation | How-to | Current | |
| /api/auth | Authentication | Reference | Outdated | Needs update for v3 |
| /faq | FAQ | Support | Deprecated | Merge into troubleshooting |

## Gap analysis

| User task | Content exists | Location | Quality |
|-----------|----------------|----------|---------|
| Install the product | Yes | /install | Good |
| Configure auth | Partial | /api/auth | Needs work |
| Debug errors | No | — | Create new |

## Migration plan

| Current path | New path | Redirect needed |
|--------------|----------|-----------------|
| /api/auth | /reference/api/auth | Yes |
| /faq | /troubleshooting/faq | Yes |
```

---

## Landing page template

```md
# [Section Name]

[One-sentence description of this section and who it's for.]

## [Category 1]

<cards>
- **[Page title]**: [One-line description]
- **[Page title]**: [One-line description]
</cards>

## [Category 2]

<cards>
- **[Page title]**: [One-line description]
- **[Page title]**: [One-line description]
</cards>

## Popular pages

- [Most visited page in section]
- [Second most visited]
- [Third most visited]

## Related sections

- [Related section 1]
- [Related section 2]
```

---

## Variation rules
- Primary navigation: 5-9 items maximum.
- Hierarchy depth: 3 levels maximum.
- Every section needs a landing page.
- Labels must be task-oriented or noun-based, not verb phrases.
- Internal paths must follow URL naming conventions (lowercase, hyphens).
