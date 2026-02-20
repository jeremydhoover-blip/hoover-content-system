# Templates

## Default status structure

```md
**[Status label]**
[Detail text - optional]
```

## Structured output format

```yaml
status:
  type: "<system|task|sync|connection>"
  state: "<pending|in-progress|completed|failed|paused>"
  label: "<what's happening - max 30 chars>"
  detail: "<additional info - max 100 chars, optional>"
  progress:
    type: "<determinate|indeterminate|none>"
    value: <0-100>  # only for determinate
```

## Variations by status type

### Task progress (determinate)
```yaml
status:
  type: "task"
  state: "in-progress"
  label: "Uploading..."
  detail: "3 of 10 files"
  progress:
    type: "determinate"
    value: 30
```

### Task progress (indeterminate)
```yaml
status:
  type: "task"
  state: "in-progress"
  label: "Processing..."
  detail: "This may take a few minutes."
  progress:
    type: "indeterminate"
```

### Sync status
```yaml
status:
  type: "sync"
  state: "completed"
  label: "All changes saved"
  detail: null
  progress:
    type: "none"
```

### Connection status
```yaml
status:
  type: "connection"
  state: "failed"
  label: "Offline"
  detail: "Changes will sync when you're back online."
  progress:
    type: "none"
```

### System state
```yaml
status:
  type: "system"
  state: "in-progress"
  label: "Maintenance in progress"
  detail: "Some features may be unavailable."
  progress:
    type: "indeterminate"
```

## Progress indicator guidelines
- **Determinate**: Use when you know total work (file count, percentage)
- **Indeterminate**: Use when duration unknown (spinner, pulse)
- **None**: Use for static states (connected, offline, saved)

## Allowed variations
- "Saving..." → "Saved" state transition
- Include timestamp for completed states: "Saved at 2:34 PM"
- Add retry action for failed states
