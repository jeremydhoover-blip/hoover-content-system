# CTA Patterns

Call-to-action patterns for empty states.

---

## Table of contents
- [CTA types by empty state](#cta-types-by-empty-state)
- [Button label patterns](#button-label-patterns)
- [Placement guidelines](#placement-guidelines)
- [When to omit CTAs](#when-to-omit-ctas)

---

## CTA types by empty state

| Empty state type | Primary CTA | Secondary CTA |
|------------------|-------------|---------------|
| **first-run** | Create first item | Import / Learn more |
| **no-results** | Clear filters / Adjust search | Create new |
| **user-cleared** | Usually none | Create new (subtle) |
| **error-caused** | Retry | Report issue |

---

## Button label patterns

### First-run CTAs
| Context | Recommended | Avoid |
|---------|-------------|-------|
| Create first item | "Create project", "Add first [item]" | "Get started" (vague) |
| Import existing | "Import", "Import from [source]" | "Upload" (if not file-based) |
| Learn more | "Learn more", "See how it works" | "Help" (ambiguous) |

### No-results CTAs
| Context | Recommended | Avoid |
|---------|-------------|-------|
| Clear filters | "Clear filters", "Reset" | "Start over" |
| Broaden search | "Search all [items]" | "Try again" |
| Suggest correction | "Search '[correction]'" | — |

### Error-caused CTAs
| Context | Recommended | Avoid |
|---------|-------------|-------|
| Retry load | "Retry", "Try again" | "Refresh page" (if not needed) |
| Report issue | "Report issue", "Contact support" | "Help" |

---

## Button hierarchy

### Primary CTA (one per empty state)
- Prominent visual style (filled button)
- Most likely action user wants
- Verb-first label: "Create", "Add", "Import"

### Secondary CTA (optional)
- Subtle visual style (text link or outlined)
- Alternative or escape hatch
- Examples: "Learn more", "Skip", "Maybe later"

### No CTA states
Some empty states don't need CTAs:
- User-cleared states where content appears automatically (e.g., notifications)
- Informational empties that set expectations

---

## Placement guidelines

```
┌─────────────────────────────────────┐
│                                     │
│          [Illustration]             │
│                                     │
│         Headline text               │
│     Supporting text here            │
│                                     │
│      [ Primary CTA ]                │
│        Secondary link               │
│                                     │
└─────────────────────────────────────┘
```

- Center-align in the empty content area
- Primary CTA directly under supporting text
- Secondary CTA below primary (text link) or inline

---

## CTA copy formulas

### Create/Add actions
```
[Verb] + [object]
```
Examples: "Create project", "Add teammate", "Write first post"

### Import actions
```
Import from [source]
```
Examples: "Import from CSV", "Import from Trello"

### Filter actions
```
Clear [filter type] | Clear all
```
Examples: "Clear filters", "Clear date range", "Reset search"

### Exploration actions
```
[Browse/Explore] + [category]
```
Examples: "Browse templates", "Explore examples"

---

## When to omit CTAs

| Scenario | Example | Why no CTA |
|----------|---------|------------|
| Auto-populated content | "Notifications will appear here" | User can't take action |
| View-only contexts | "No shared files" (can't create here) | Action not available |
| Transient states | "No new messages" | Normal state, not actionable |
| Post-action confirmation | "All tasks complete" | User already did the action |

---

## Anti-patterns

| Pattern | Problem | Fix |
|---------|---------|-----|
| "Click here" | Vague, inaccessible | Use descriptive label |
| "Get started" for everything | Doesn't say what happens | Be specific: "Create first X" |
| Multiple primary CTAs | Confusing hierarchy | One primary, rest secondary |
| CTA that navigates away unexpectedly | Disorienting | Clarify destination or keep in context |
| No CTA when action is possible | Missed opportunity | Add relevant action |
