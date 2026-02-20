# Troubleshooting Documentation Patterns

## Table of contents
- [Guide structure selection](#guide-structure-selection)
- [Symptom documentation standards](#symptom-documentation-standards)
- [Diagnostic step design](#diagnostic-step-design)
- [Resolution verification patterns](#resolution-verification-patterns)
- [Escalation path requirements](#escalation-path-requirements)

---

## Guide structure selection

| Problem type | Recommended structure | Reason |
|--------------|----------------------|--------|
| Single error code | Error code reference | Direct lookup, one cause |
| Multiple possible causes | Symptom-based guide | Common case, progressive diagnosis |
| Complex system failures | Decision-tree guide | Branching logic, multiple paths |
| Recurring/known issues | FAQ format | Quick reference |

---

## Symptom documentation standards

### Good symptoms (observable, user-perspective)

| Category | Example |
|----------|---------|
| Visual | "Page shows blank white screen" |
| Error message | "Error message: `ECONNREFUSED`" |
| Behavior | "Button click has no response" |
| Performance | "Page takes more than 10 seconds to load" |
| State | "Data from yesterday is missing" |

### Bad symptoms (internal state, developer-only)

| Avoid | Why | Better alternative |
|-------|-----|-------------------|
| "Memory leak detected" | User can't observe this | "Application slows down over time" |
| "Null pointer exception" | Internal implementation | "Application crashes when clicking X" |
| "Database deadlock" | Requires server access | "Request hangs and eventually times out" |

---

## Diagnostic step design

### Progressive narrowing pattern

```
Symptom observed
    ↓
Quick check 1 → Rules out 50% of causes
    ↓
Quick check 2 → Rules out 25% more
    ↓
Detailed diagnostic → Identifies specific cause
    ↓
Resolution
```

### Diagnostic command requirements

Every diagnostic command must include:

1. **The command itself**
2. **Expected output for each outcome**
3. **What the output means**

Example:
```bash
# Command
curl -I https://api.example.com/health

# Healthy output
HTTP/2 200
# Means: API is reachable, proceed to next diagnostic

# Unhealthy output
curl: (7) Failed to connect
# Means: Network issue, go to Network troubleshooting section
```

---

## Resolution verification patterns

### Verification requirements

Every resolution must end with verification that confirms the problem is fixed, not just that the fix was applied.

| Fix type | Verification method |
|----------|-------------------|
| Configuration change | Restart + test affected functionality |
| Code change | Run failing test/scenario |
| Permission change | Attempt previously failing action |
| Network change | Repeat connectivity test |

### Verification phrasing

```
**Verify:** [How to confirm the fix worked]

You should see: [Expected successful outcome]
```

Do not use:
- "The problem should be resolved"
- "Try again and see if it works"
- "Let us know if you still have issues"

---

## Escalation path requirements

### Required elements

1. **What to collect** — Specific diagnostic data
2. **Where to go** — Exact support channel or resource
3. **What to include** — Template for support request

### Data collection checklist template

```md
## Collect before escalating

- [ ] Application logs from [time range]
- [ ] Error messages (exact text)
- [ ] Steps to reproduce
- [ ] Environment details (version, OS, etc.)
- [ ] What you've already tried
```

### Escalation path examples

| Support model | Escalation format |
|---------------|-------------------|
| Internal team | "Contact #team-channel with collected logs" |
| Ticketing system | "Open ticket at [URL] with category [X]" |
| Community forum | "Post to [forum URL] with [tag]" |
| External vendor | "Contact support@vendor.com with account ID" |

---

## Anti-patterns to avoid

| Anti-pattern | Problem | Fix |
|--------------|---------|-----|
| "Try this and see if it works" | No diagnosis | Add diagnostic step first |
| Listing causes without differentiation | User tries random fixes | Add diagnostic for each cause |
| "Contact support" without data | Wastes support time | Specify what data to collect |
| Prevention advice in troubleshooting | Wrong document type | Move to separate best practices doc |
| Assuming single cause | Misses actual issue | Always consider multiple causes |
