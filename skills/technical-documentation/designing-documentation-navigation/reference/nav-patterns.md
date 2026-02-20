# Navigation Patterns

## Table of contents
- [Primary navigation patterns](#primary-navigation-patterns)
- [Sidebar patterns](#sidebar-patterns)
- [In-page navigation](#in-page-navigation)
- [Search patterns](#search-patterns)
- [Mobile considerations](#mobile-considerations)

---

## Primary navigation patterns

### Horizontal header navigation

```
┌────────────────────────────────────────────────────────┐
│ [Logo] │ Item 1  Item 2  Item 3 │ [Search] [Utilities] │
└────────────────────────────────────────────────────────┘
```

**Best for:** 5-7 top-level items, standard documentation sites

**Specifications:**
| Property | Recommendation |
|----------|----------------|
| Max items | 7 |
| Dropdown | For grouped items only |
| Active state | Underline or background |
| Sticky | Yes, on scroll |

### Tabbed navigation

```
┌─────────────────────────────────────┐
│ [Tab 1] [Tab 2] [Tab 3]            │
├─────────────────────────────────────┤
│ Content changes based on tab       │
└─────────────────────────────────────┘
```

**Best for:** Distinct content categories (User Guide / Admin / API)

---

## Sidebar patterns

### Collapsible tree

```
▼ Getting Started
  • Overview
  • Installation
▶ Guides
▶ Reference
```

**Behavior rules:**
- Remember expanded state
- Current page highlighted
- Expand parent when landing on child

### Flat list with groups

```
GETTING STARTED
  Overview
  Installation

GUIDES
  Authentication
  Webhooks
```

**Best for:** Shallow sites (2 levels max)

### Depth limits

| Level | Element | Example |
|-------|---------|---------|
| 1 | Category | "Guides" |
| 2 | Page/Group | "Authentication" |
| 3 | Page | "OAuth Setup" |
| 4+ | ❌ Not allowed | Restructure instead |

---

## In-page navigation

### Table of contents (TOC)

**Extraction rules:**
| Include | Exclude |
|---------|---------|
| H2 headings | H1 (page title) |
| H3 headings | H4+ (too granular) |
| Meaningful text | Auto-generated headings |

**Behavior:**
- Highlight current section on scroll
- Smooth scroll on click
- Sticky position (right sidebar)

### Previous/Next links

**Placement:** Bottom of content, above footer

**Logic options:**
| Method | Pro | Con |
|--------|-----|-----|
| Sidebar order | Predictable | May not be logical |
| Manual | Intentional flow | Maintenance burden |
| Hybrid | Best of both | Complexity |

### Related links

**Position:** Bottom of content or sidebar

**Rules:**
- 3-5 related pages maximum
- Same section first
- Cross-section where relevant

---

## Search patterns

### Command palette style

```
┌─────────────────────────────────────┐
│ 🔍 Search docs...              ⌘K  │
├─────────────────────────────────────┤
│ Recent                              │
│  • OAuth Setup                      │
│  • API Reference                    │
│                                     │
│ Results                             │
│  • [Page title] - snippet...        │
│  • [Page title] - snippet...        │
└─────────────────────────────────────┘
```

**Requirements:**
| Feature | Implementation |
|---------|----------------|
| Keyboard shortcut | `/` or `Cmd+K` |
| Recent searches | Last 5 |
| Preview | Snippet in results |
| Navigation | Arrow keys + Enter |

### Inline search

**Position:** Header, always visible

**Behavior:**
- Expand on focus
- Dropdown results
- Category filters optional

---

## Mobile considerations

### Navigation transformation

| Desktop | Mobile |
|---------|--------|
| Horizontal nav | Hamburger menu |
| Left sidebar | Full-screen menu |
| Right TOC | Collapsed dropdown |
| Search in header | Icon + expand |

### Touch targets

| Element | Minimum size |
|---------|--------------|
| Nav item | 44px × 44px |
| Expand toggle | 44px × 44px |
| Search button | 44px × 44px |

### Gestures

| Gesture | Action |
|---------|--------|
| Swipe right | Open menu (optional) |
| Swipe left | Close menu |
| Tap outside | Close menu |

---

## Accessibility requirements

### Keyboard navigation

| Key | Action |
|-----|--------|
| Tab | Move through nav items |
| Enter | Activate link/expand |
| Escape | Close menu/search |
| Arrow keys | Navigate within menu |

### ARIA requirements

```html
<nav aria-label="Main navigation">
<nav aria-label="Section navigation">
<nav aria-label="Breadcrumb">
<nav aria-label="Table of contents">
```

### Focus management

| Scenario | Focus behavior |
|----------|----------------|
| Menu open | Focus first item |
| Menu close | Return to trigger |
| Search open | Focus input |
| Search close | Return to trigger |
