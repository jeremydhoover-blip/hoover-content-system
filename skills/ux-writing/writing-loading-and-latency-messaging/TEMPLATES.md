# Templates

## Default loading structure

```md
[Loading indicator]
**[Loading message]**
[Detail text - for long waits]
```

## Structured output format

```yaml
loading_state:
  tier: "<instant|short|medium|long|unknown>"
  message: "<what's loading - max 40 chars>"
  detail: "<additional context - max 100 chars, optional>"
  indicator: "<spinner|skeleton|progress-bar|none>"
  interruptible: <true|false>
  timeout:
    duration_seconds: <number>
    fallback: "<error message>"
```

## Variations by latency tier

### Instant (<300ms) - no loading state
```yaml
loading_state:
  tier: "instant"
  message: null
  indicator: "none"
```

### Short (300ms-2s)
```yaml
loading_state:
  tier: "short"
  message: null
  indicator: "spinner"
  interruptible: false
```

### Medium (2-10s)
```yaml
loading_state:
  tier: "medium"
  message: "Loading..."
  detail: null
  indicator: "spinner"
  interruptible: true
```

### Long (10s-60s)
```yaml
loading_state:
  tier: "long"
  message: "Loading your data..."
  detail: "This may take a moment."
  indicator: "progress-bar"
  interruptible: true
```

### Very long (>60s)
```yaml
loading_state:
  tier: "long"
  message: "Processing your request..."
  detail: "This usually takes 2-3 minutes. You can close this page."
  indicator: "progress-bar"
  interruptible: true
```

### Unknown duration
```yaml
loading_state:
  tier: "unknown"
  message: "Working on it..."
  detail: "This may take a few moments."
  indicator: "spinner"
  interruptible: true
```

## Skeleton loading (for content areas)
```yaml
loading_state:
  tier: "medium"
  message: null
  indicator: "skeleton"
  skeleton_areas: ["header", "content-list", "sidebar"]
```

## Allowed variations
- Use skeleton screens for content-heavy pages
- Show partial content as it loads (progressive)
- Allow cancel for interruptible operations
