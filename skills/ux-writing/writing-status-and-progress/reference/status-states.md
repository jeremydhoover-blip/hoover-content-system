# Status States

## Table of contents
- [State lifecycle](#state-lifecycle)
- [Status types](#status-types)
- [State definitions](#state-definitions)
- [Transition patterns](#transition-patterns)

---

## State lifecycle

```
pending → in-progress → completed
              ↓             ↓
           paused        failed
              ↓
         in-progress (resumed)
```

---

## Status types

| Type | Definition | Examples |
|------|------------|----------|
| **task** | User-initiated action with completion | Upload, download, export, import |
| **sync** | Background data synchronization | Auto-save, sync across devices |
| **connection** | Network or service connectivity | Online/offline, server status |
| **system** | Platform-wide state | Maintenance, degraded service |

---

## State definitions

| State | Meaning | User expectation |
|-------|---------|------------------|
| **pending** | Queued but not started | Will start automatically |
| **in-progress** | Currently executing | Wait or continue working |
| **completed** | Finished successfully | Action done, result available |
| **failed** | Could not complete | Needs attention or retry |
| **paused** | Stopped by user or system | Can resume |

---

## Transition patterns

### Task lifecycle
| From | To | Trigger | User sees |
|------|----|---------|-----------|
| — | pending | User initiates | "Queued" |
| pending | in-progress | System starts | "Uploading..." |
| in-progress | completed | Success | "Upload complete" |
| in-progress | failed | Error | "Upload failed" + reason |
| in-progress | paused | User pauses | "Paused" |
| paused | in-progress | User resumes | "Resuming..." |

### Sync lifecycle
| State | Label | Detail |
|-------|-------|--------|
| in-progress | "Saving..." | — |
| completed | "Saved" | Optional: timestamp |
| failed | "Couldn't save" | "Retrying..." or action |

### Connection lifecycle
| State | Label | Detail |
|-------|-------|--------|
| completed | "Connected" | Often hidden when healthy |
| in-progress | "Connecting..." | During reconnection |
| failed | "Offline" | "Changes saved locally" |

---

## Duration guidance

| Duration | Progress type | Copy pattern |
|----------|---------------|--------------|
| <2 seconds | None or indeterminate | No text needed |
| 2-10 seconds | Indeterminate | "Loading..." / "Processing..." |
| 10-60 seconds | Determinate if possible | "X of Y" or percentage |
| >60 seconds | Determinate + estimate | "About 5 minutes remaining" |
| Unknown/long | Indeterminate + context | "This may take a few minutes" |

---

## Anti-patterns

| Pattern | Problem | Fix |
|---------|---------|-----|
| Fake progress bar | Misleads user, erodes trust | Use indeterminate spinner |
| "Loading..." for everything | No context, user doesn't know what | "[Thing] loading..." |
| No failed state | User waits forever | Always handle errors |
| Completed but no confirmation | User unsure if it worked | Confirm: "Saved" / "Done" |
| Progress stuck at 99% | System doesn't know completion | Use indeterminate near end if unsure |
