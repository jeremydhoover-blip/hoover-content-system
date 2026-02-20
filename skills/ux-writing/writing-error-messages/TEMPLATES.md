# Templates

## Default error message structure

```md
## [Error Title]
[Body explaining cause or context - optional]

**Action:** [Button label or instruction]
```

## Structured output format

```yaml
error:
  title: "<what went wrong - max 60 chars>"
  body: "<why it happened - max 150 chars, optional>"
  action:
    label: "<button text - max 25 chars>"
    type: "<retry|dismiss|navigate|contact>"
```

## Variations by error type

### Validation error (inline)
```md
[Field-specific message under the input]
```
Example: "Enter a valid email address"

### System error (modal or banner)
```md
## Something went wrong
We couldn't complete your request. Please try again.

**Action:** Try again
```

### Network error
```md
## Connection lost
Check your internet connection and try again.

**Action:** Retry
```

### Permission error
```md
## Access denied
You don't have permission to [action]. Contact your admin for access.

**Action:** Request access
```

### Not found error
```md
## [Item] not found
This [item] may have been moved or deleted.

**Action:** Go back
```

## Allowed variations
- Omit body if the title + action make the situation and fix obvious
- Use inline format for field validation; use modal/banner for system-level errors
- Adjust formality based on product voice, but never add humor to errors
