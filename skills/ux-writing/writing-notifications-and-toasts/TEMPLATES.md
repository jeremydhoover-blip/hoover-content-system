# Templates

## Default notification structure

```md
[Icon] **[Message]** [Action link - optional] [Dismiss X]
```

## Structured output format

```yaml
notification:
  type: "<success|error|warning|info>"
  message: "<what happened - max 80 chars>"
  action:
    label: "<action text - max 20 chars>"
    type: "<navigate|undo|retry|dismiss>"
  persistence: "<auto-dismiss|manual-dismiss|persistent>"
  auto_dismiss_seconds: <4-8>  # only for auto-dismiss
```

## Variations by notification type

### Success
```yaml
notification:
  type: "success"
  message: "Changes saved"
  action: null
  persistence: "auto-dismiss"
  auto_dismiss_seconds: 4
```

### Success with undo
```yaml
notification:
  type: "success"
  message: "Message archived"
  action:
    label: "Undo"
    type: "undo"
  persistence: "auto-dismiss"
  auto_dismiss_seconds: 6
```

### Error (requires attention)
```yaml
notification:
  type: "error"
  message: "Couldn't save changes. Check your connection."
  action:
    label: "Retry"
    type: "retry"
  persistence: "manual-dismiss"
```

### Warning
```yaml
notification:
  type: "warning"
  message: "Your session expires in 5 minutes"
  action:
    label: "Stay signed in"
    type: "navigate"
  persistence: "manual-dismiss"
```

### Info
```yaml
notification:
  type: "info"
  message: "New features available. See what's new."
  action:
    label: "Learn more"
    type: "navigate"
  persistence: "auto-dismiss"
  auto_dismiss_seconds: 8
```

## Persistence guidelines
- **auto-dismiss**: Success, info (no action required)
- **manual-dismiss**: Warnings, errors with optional actions
- **persistent**: Errors requiring action, critical warnings

## Allowed variations
- Omit action for simple confirmations
- Stack notifications if multiple (max 3 visible)
- Use longer auto-dismiss for messages with actions (6-8s)
