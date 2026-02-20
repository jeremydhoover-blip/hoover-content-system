# Templates

## Default confirmation dialog structure

```md
## [Headline - what will happen?]
[Body - consequences or details]

[Cancel button] | [Confirm button]
```

## Structured output format

```yaml
confirmation_dialog:
  headline: "<what will happen - max 60 chars>"
  body: "<consequences - max 200 chars, optional>"
  confirm:
    label: "<specific verb - max 20 chars>"
    style: "<default|destructive>"
  cancel:
    label: "<safe exit - max 15 chars>"
```

## Variations by action type

### Destructive action (delete, remove permanently)
```yaml
confirmation_dialog:
  headline: "Delete [item name]?"
  body: "This can't be undone. All associated data will be permanently removed."
  confirm:
    label: "Delete"
    style: "destructive"
  cancel:
    label: "Cancel"
```

### Significant change (affects others or hard to reverse)
```yaml
confirmation_dialog:
  headline: "Remove [person] from [team]?"
  body: "They'll lose access to all team projects and files."
  confirm:
    label: "Remove"
    style: "destructive"
  cancel:
    label: "Cancel"
```

### Simple confirmation (reversible)
```yaml
confirmation_dialog:
  headline: "Archive this project?"
  body: "You can restore it anytime from the archive."
  confirm:
    label: "Archive"
    style: "default"
  cancel:
    label: "Cancel"
```

### Bulk action
```yaml
confirmation_dialog:
  headline: "Delete 15 items?"
  body: "This will permanently delete all selected items."
  confirm:
    label: "Delete 15 items"
    style: "destructive"
  cancel:
    label: "Cancel"
```

## Allowed variations
- Omit body for simple, reversible, single-item actions
- Include count in confirm button for bulk actions
- Use "Keep [item]" instead of "Cancel" when it's clearer
- Add checkbox for "Don't ask again" only for frequent, low-risk confirmations
