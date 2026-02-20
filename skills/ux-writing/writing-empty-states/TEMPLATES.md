# Templates

## Default empty state structure

```md
## [Headline]
[Support text explaining the state or next step]

**Action:** [Button label]
```

## Structured output format

```yaml
empty_state:
  type: "<first-run|no-results|user-cleared|error-caused>"
  headline: "<acknowledge state - max 50 chars>"
  support: "<explain or guide - max 120 chars, optional>"
  action:
    label: "<button text - max 25 chars>"
    type: "<create|search|import|navigate>"
```

## Variations by empty state type

### First-run (new user, no content yet)
```md
## Get started with [feature]
[Brief value prop or first step]

**Action:** [Create first item]
```

### No results (search/filter returned nothing)
```md
## No results for "[query]"
Try different keywords or remove filters.

**Action:** Clear filters
```

### User-cleared (user deleted all items)
```md
## No [items] yet
[Items] you create will appear here.

**Action:** [Create item]
```

### Error-caused (empty due to load failure)
```md
## Couldn't load [items]
Check your connection and try again.

**Action:** Retry
```

## Allowed variations
- Omit support text if headline + action are sufficient
- First-run can include illustration reference (implementation handles asset)
- No-results can suggest related queries if available
- Error-caused follows error message patterns (see writing-error-messages)
