# Error Categories

## Table of contents
- [Error types](#error-types)
- [Severity levels](#severity-levels)
- [Tone by severity](#tone-by-severity)
- [Recovery patterns](#recovery-patterns)

---

## Error types

| Type | Definition | Common causes | Typical action |
|------|------------|---------------|----------------|
| **validation** | User input doesn't meet requirements | Wrong format, missing required field, out of range | Fix input and resubmit |
| **system** | Internal failure, often unexpected | Server error, timeout, service down | Retry or wait |
| **network** | Connectivity issue | No internet, DNS failure, firewall | Check connection, retry |
| **permission** | User lacks access rights | Role restrictions, expired session, unverified account | Request access, sign in again |
| **not-found** | Requested resource doesn't exist | Deleted item, broken link, typo in URL | Navigate elsewhere |
| **conflict** | Action conflicts with current state | Duplicate entry, version mismatch, locked resource | Resolve conflict |
| **rate-limit** | Too many requests | API throttling, abuse prevention | Wait and retry |

---

## Severity levels

| Severity | Impact | UI treatment |
|----------|--------|--------------|
| **blocking** | User cannot proceed at all | Modal dialog, full-page error |
| **degraded** | Feature unavailable but app works | Banner, inline alert |
| **informational** | Minor issue, workaround exists | Toast, inline note |

---

## Tone by severity

| Severity | Tone | Example opener |
|----------|------|----------------|
| **blocking** | Direct, reassuring | "We couldn't..." / "Something went wrong" |
| **degraded** | Calm, factual | "This feature isn't available right now" |
| **informational** | Neutral, brief | "Heads up:" / "Note:" |

### Tone rules
- Never use humor in error states
- Never use exclamation points
- Never use all caps
- Blocking errors: empathize briefly, then focus on action
- Degraded errors: state fact, offer alternative
- Informational errors: state fact only

---

## Recovery patterns

| Error type | Primary recovery | Fallback recovery |
|------------|------------------|-------------------|
| validation | Correct input | Show format hint |
| system | Retry | Contact support |
| network | Check connection, retry | Work offline if possible |
| permission | Request access | Sign in with different account |
| not-found | Navigate to parent/home | Search |
| conflict | Refresh, resolve | Contact owner |
| rate-limit | Wait | Upgrade plan |

---

## Anti-patterns to avoid

| Pattern | Problem | Fix |
|---------|---------|-----|
| "Error 500" | Technical, meaningless to user | "Something went wrong. Please try again." |
| "Invalid input" | Vague, no guidance | Specify which input and what's wrong |
| "You failed to..." | Blames user | "Enter..." or "Check..." |
| "Oops!" | Trivializes user's problem | Remove |
| "Please try again later" (alone) | No context, no confidence | Add what happened and when to retry |
