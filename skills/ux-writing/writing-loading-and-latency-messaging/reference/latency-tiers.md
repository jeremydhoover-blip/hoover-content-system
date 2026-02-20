# Latency Tiers

## Table of contents
- [Tier definitions](#tier-definitions)
- [Indicator guidelines](#indicator-guidelines)
- [Message patterns](#message-patterns)
- [Timeout strategy](#timeout-strategy)

---

## Tier definitions

| Tier | Duration | User perception | Indicator |
|------|----------|-----------------|-----------|
| **instant** | <300ms | Instantaneous | None |
| **short** | 300ms-2s | Brief pause | Spinner only |
| **medium** | 2-10s | Noticeable wait | Spinner + optional message |
| **long** | 10-60s | Significant wait | Progress bar + message |
| **very-long** | >60s | Extended operation | Message + time estimate + escape hatch |
| **unknown** | Variable | Unpredictable | Spinner + hedged message |

---

## Indicator guidelines

| Indicator | Use when | Avoid when |
|-----------|----------|------------|
| **none** | <300ms operations | Any perceptible wait |
| **spinner** | Duration unknown or <10s | You can show actual progress |
| **skeleton** | Loading content layouts | Single action responses |
| **progress-bar** | Duration known, >2s | Duration is unknown |
| **percentage** | File transfers, exports | Server processing (unreliable) |

### Indicator placement
- **Full-page**: Initial page load, major transitions
- **Inline**: Button actions, field validation
- **Overlay**: Modal content, focused operations
- **Background**: Non-blocking refreshes (minimal or no indicator)

---

## Message patterns

| Tier | Message | Detail |
|------|---------|--------|
| instant | None | None |
| short | None | None |
| medium | "Loading..." | Optional |
| long | "[Action] in progress..." | "This may take a moment." |
| very-long | "[Action]..." | "About X minutes. You can close this page." |
| unknown | "Working on it..." | "This may take a few moments." |

### Context-specific messages
| Context | Message |
|---------|---------|
| Search | None (inline spinner) |
| Save | "Saving..." |
| Upload | "Uploading..." |
| Download | "Preparing download..." |
| Export | "Generating export..." |
| Sync | "Syncing..." |
| Process | "Processing..." |

---

## Timeout strategy

Every loading state must have a timeout. Timeouts prevent infinite loading.

| Tier | Recommended timeout | Fallback action |
|------|---------------------|-----------------|
| short | 10s | Show error, allow retry |
| medium | 30s | Show error, allow retry |
| long | 120s | Show error, offer alternatives |
| very-long | 600s (10min) | Email on complete, allow check status |
| unknown | 180s | Show warning, allow continue waiting or cancel |

### Timeout copy patterns
- Short: "Couldn't [action]. Try again."
- Medium: "[Action] is taking longer than expected. Try again?"
- Long: "[Action] timed out. Your request may still be processing. Check back later or try again."

---

## Anti-patterns

| Pattern | Problem | Fix |
|---------|---------|-----|
| Spinner for <300ms | Feels laggy | Remove indicator |
| No indicator for >1s | Feels broken | Add spinner |
| "Loading..." for everything | No context | Specify what's loading |
| Fake progress | Erodes trust | Use indeterminate |
| No timeout | Infinite wait | Always set timeout |
| No cancel for long waits | User trapped | Allow cancel/close |
