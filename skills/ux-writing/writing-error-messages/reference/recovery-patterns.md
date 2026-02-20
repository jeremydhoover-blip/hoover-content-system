# Recovery Patterns

## Table of contents
- [Recovery action types](#recovery-action-types)
- [Patterns by error type](#patterns-by-error-type)
- [Action label guidelines](#action-label-guidelines)
- [Fallback chains](#fallback-chains)

---

## Recovery action types

| Type | Definition | Button pattern |
|------|------------|----------------|
| **retry** | Attempt same action again | "Try again", "Retry" |
| **fix-input** | User corrects their input | "Edit", "Fix", inline correction |
| **navigate** | Go somewhere else | "Go back", "Go to [place]" |
| **contact** | Reach human support | "Contact support", "Get help" |
| **dismiss** | Acknowledge and close | "Dismiss", "OK", "Close" |
| **wait** | Try again later | "Try again later" (with time hint) |
| **alternative** | Use different method | "Try [alternative method]" |

---

## Patterns by error type

### Validation errors
| Scenario | Primary recovery | Fallback |
|----------|------------------|----------|
| Invalid format | Fix input (inline) | Show format hint |
| Missing required | Fix input | Highlight field |
| Out of range | Fix input | Show valid range |

### System errors
| Scenario | Primary recovery | Fallback |
|----------|------------------|----------|
| Server error (5xx) | Retry | Wait and retry |
| Timeout | Retry | Check connection |
| Service unavailable | Wait | Check status page |

### Network errors
| Scenario | Primary recovery | Fallback |
|----------|------------------|----------|
| No connection | Check connection, retry | Work offline |
| DNS failure | Retry | Check network settings |
| SSL error | Contact support | Try different network |

### Permission errors
| Scenario | Primary recovery | Fallback |
|----------|------------------|----------|
| Role insufficient | Request access | Contact admin |
| Session expired | Sign in again | — |
| Account suspended | Contact support | — |

### Not found errors
| Scenario | Primary recovery | Fallback |
|----------|------------------|----------|
| Deleted item | Navigate to parent | Search |
| Invalid URL | Navigate to home | Search |
| Moved resource | Follow redirect | Navigate to parent |

---

## Action label guidelines

### Do
- Use specific verbs: "Retry upload", "Edit email", "Go to dashboard"
- Match label to actual action
- Keep under 25 characters

### Don't
- Generic labels: "OK", "Continue" (when more specific is possible)
- Vague: "Click here", "Submit"
- Misleading: "Done" when action still needed

### Label patterns by recovery type
| Recovery type | Recommended labels |
|---------------|-------------------|
| retry | "Try again", "Retry", "Refresh" |
| fix-input | "Edit", "Change", "Update" |
| navigate | "Go back", "Go to [X]", "Return to [X]" |
| contact | "Contact support", "Get help", "Chat with us" |
| dismiss | "Dismiss", "Close", "Got it" |

---

## Fallback chains

When primary recovery fails, provide fallback options.

### Standard fallback chain
```
1. Retry (automatic or manual)
   ↓ fails
2. Alternative method
   ↓ fails
3. Contact support
```

### Network error chain
```
1. Retry
   ↓ fails after 3 attempts
2. "Check your internet connection"
   ↓ still failing
3. "Work offline" (if supported)
   ↓ or
3. "Try again later"
```

### Permission error chain
```
1. "Request access" (if applicable)
   ↓ not applicable
2. "Sign in with different account"
   ↓ not applicable
3. "Contact your admin"
```

---

## Anti-patterns

| Pattern | Problem | Fix |
|---------|---------|-----|
| No recovery action | User stuck | Always provide at least dismiss |
| Only "OK" for fixable error | Missed opportunity to help | Offer specific action |
| Multiple competing actions | Decision paralysis | One primary, one secondary max |
| "Contact support" as first option | Burdens support unnecessarily | Try self-service first |
