# Risk Levels

Classification of confirmation dialog risk levels and their UI treatment.

---

## Table of contents
- [Risk level definitions](#risk-level-definitions)
- [Classification criteria](#classification-criteria)
- [UI treatment by risk](#ui-treatment-by-risk)
- [Decision flowchart](#decision-flowchart)

---

## Risk level definitions

| Risk level | Definition | Example actions |
|------------|------------|-----------------|
| **low** | Easily reversible, minimal impact | Archive, hide, mute |
| **medium** | Reversible with effort, affects workflow | Remove from list, clear cache, reset preferences |
| **high** | Difficult to reverse, significant impact | Delete file, remove team member, cancel subscription |
| **critical** | Irreversible, major consequences | Delete account, permanent data loss, legal commitment |

---

## Classification criteria

### Reversibility
| Score | Reversibility | Examples |
|-------|---------------|----------|
| 1 | Instant undo available | Archive → unarchive |
| 2 | Reversible within time window | Trash with 30-day recovery |
| 3 | Reversible with effort | Restore from backup, re-invite user |
| 4 | Irreversible | Permanent delete, sent message |

### Impact scope
| Score | Scope | Examples |
|-------|-------|----------|
| 1 | Single item, user only | Delete own draft |
| 2 | Multiple items, user only | Bulk delete own files |
| 3 | Affects other users | Remove teammate, change shared settings |
| 4 | Account or organization-wide | Delete workspace, cancel plan |

### Risk level formula
```
Risk = max(Reversibility, Impact)

Low:      max ≤ 1
Medium:   max = 2
High:     max = 3
Critical: max = 4
```

---

## UI treatment by risk

| Risk level | Confirm button style | Require typing? | Cancel prominence |
|------------|---------------------|-----------------|-------------------|
| **low** | Default (primary) | No | Normal |
| **medium** | Default or warning | No | Normal |
| **high** | Destructive (red) | No | Equal or higher than confirm |
| **critical** | Destructive (red) | Yes — type to confirm | Higher than confirm |

### Confirm button labels by risk
| Risk level | Label pattern | Examples |
|------------|---------------|----------|
| low | Simple verb | "Archive", "Hide" |
| medium | Verb + object | "Remove from list", "Clear cache" |
| high | Verb + object | "Delete file", "Remove member" |
| critical | Full action phrase | "Delete my account", "Permanently delete" |

### Type-to-confirm patterns (critical only)
```
To confirm, type "[workspace-name]" below:
[________________]

[Cancel]  [Delete workspace]
```

---

## Decision flowchart

```
Is action reversible with simple undo?
├─ YES → Low risk
└─ NO ↓

Is action reversible within 30 days or with effort?
├─ YES → Does it affect other users?
│        ├─ NO → Medium risk
│        └─ YES → High risk
└─ NO ↓

Is action truly irreversible?
├─ YES → Does it have major consequences?
│        ├─ NO → High risk
│        └─ YES → Critical risk
└─ (shouldn't reach here)
```

---

## Examples by risk level

### Low risk
| Action | Reversibility | Scope | Treatment |
|--------|---------------|-------|-----------|
| Archive project | Instant undo | User only | Default confirm |
| Mute notifications | Instant undo | User only | Toggle, no dialog |
| Hide sidebar | Instant undo | User only | No dialog needed |

### Medium risk
| Action | Reversibility | Scope | Treatment |
|--------|---------------|-------|-----------|
| Clear browser cache | Effort to rebuild | User only | Warning confirm |
| Reset preferences | Can reconfigure | User only | Default confirm |
| Mark all as read | Cannot unread | User only | Default confirm |

### High risk
| Action | Reversibility | Scope | Treatment |
|--------|---------------|-------|-----------|
| Delete file (no trash) | From backup only | User only | Destructive confirm |
| Remove team member | Re-invite needed | Affects others | Destructive confirm |
| Revoke API key | Must regenerate | Affects integrations | Destructive confirm |

### Critical risk
| Action | Reversibility | Scope | Treatment |
|--------|---------------|-------|-----------|
| Delete account | Irreversible | Account-wide | Type to confirm |
| Delete workspace | Irreversible | Org-wide | Type workspace name |
| Transfer ownership | Cannot undo alone | Org-wide | Type to confirm |

---

## Anti-patterns

| Pattern | Problem | Fix |
|---------|---------|-----|
| Destructive style for low-risk | Creates unnecessary anxiety | Use default style |
| Default style for critical | Undersells severity | Use destructive + type to confirm |
| Skip confirmation for high-risk | Accidental destructive actions | Always confirm |
| Long delay on undo for critical | False sense of security | Don't offer undo if truly irreversible |
