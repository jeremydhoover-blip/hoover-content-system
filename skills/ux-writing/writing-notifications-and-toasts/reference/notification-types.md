# Notification Types

## Table of contents
- [Type definitions](#type-definitions)
- [Visual treatment](#visual-treatment)
- [Persistence rules](#persistence-rules)
- [Placement guidelines](#placement-guidelines)

---

## Type definitions

| Type | Purpose | User expectation | Icon |
|------|---------|------------------|------|
| **success** | Confirm completed action | Brief acknowledgment, continue working | ✓ Checkmark |
| **error** | Alert to failure | Understand what failed, how to fix | ✕ X or ! |
| **warning** | Alert to potential issue | Decide whether to take action | ⚠ Triangle |
| **info** | Share non-critical information | Note and dismiss | ℹ Info circle |

---

## Visual treatment

| Type | Background | Icon color | Text color |
|------|------------|------------|------------|
| success | Green (light) | Green | Default |
| error | Red (light) | Red | Default |
| warning | Yellow/amber (light) | Amber | Default |
| info | Blue (light) | Blue | Default |

### Accessibility requirements
- Color must not be the only indicator (always include icon)
- Sufficient contrast (WCAG AA minimum)
- Screen reader announcements for all notifications
- Focus management for actionable notifications

---

## Persistence rules

| Type | Default persistence | Auto-dismiss timing |
|------|--------------------|--------------------|
| success | auto-dismiss | 4-5 seconds |
| success + undo | auto-dismiss | 6-8 seconds |
| error (minor) | manual-dismiss | — |
| error (critical) | persistent | — |
| warning | manual-dismiss | — |
| info | auto-dismiss | 6-8 seconds |

### Decision tree
```
Does user need to take action?
├─ YES → Does user have time pressure?
│        ├─ YES → persistent
│        └─ NO → manual-dismiss
│
└─ NO → Is there an undo option?
        ├─ YES → auto-dismiss (6-8s)
        └─ NO → auto-dismiss (4-5s)
```

---

## Placement guidelines

| Placement | Use for | Avoid for |
|-----------|---------|-----------|
| **Top-right** | General notifications, page-level feedback | Form errors |
| **Top-center** | Critical warnings, system messages | Routine success |
| **Bottom-left** | Background task completion | Urgent errors |
| **Inline** | Field validation, contextual feedback | System-wide alerts |

### Stacking behavior
- Maximum 3 visible notifications at once
- Newer notifications appear above older
- Queue excess notifications
- Dismiss oldest first when queue is full

---

## Anti-patterns

| Pattern | Problem | Fix |
|---------|---------|-----|
| Error auto-dismisses | User misses important info | Use manual-dismiss |
| Success for failed action | Misleading, erodes trust | Use correct type |
| Multiple simultaneous | Visual noise, overwhelming | Queue notifications |
| Undo with 3s dismiss | Not enough time to read + act | Use 6-8 seconds |
| No dismiss option | User feels trapped | Always allow dismiss |
| Generic "Error occurred" | Not actionable | Explain what and how to fix |
| Info used for errors | Downplays severity | Match type to content |
