# Examples

## Example 1: File upload (determinate)
**Input:**
- Status type: task
- Context: Uploading 10 files, 3 complete
- Duration: User can estimate from count

**Output:**
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

---

## Example 2: Processing (indeterminate)
**Input:**
- Status type: task
- Context: Server processing a request, unknown duration
- Duration: Could be seconds or minutes

**Output:**
```yaml
status:
  type: "task"
  state: "in-progress"
  label: "Processing..."
  detail: "This may take a moment."
  progress:
    type: "indeterminate"
```

---

## Example 3: Auto-save status
**Input:**
- Status type: sync
- Context: Document auto-saved
- State: Completed

**Output:**
```yaml
status:
  type: "sync"
  state: "completed"
  label: "Saved"
  detail: null
  progress:
    type: "none"
```
Alternate with timestamp: `"Saved at 2:34 PM"`

---

## Example 4: Connection lost
**Input:**
- Status type: connection
- Context: Network disconnected, offline mode active
- State: Failed (degraded)

**Output:**
```yaml
status:
  type: "connection"
  state: "failed"
  label: "Offline"
  detail: "Your changes will sync when you reconnect."
  progress:
    type: "none"
```

---

## Example 5: Export completed
**Input:**
- Status type: task
- Context: Data export finished, download ready
- State: Completed

**Output:**
```yaml
status:
  type: "task"
  state: "completed"
  label: "Export ready"
  detail: "Your download should start automatically."
  progress:
    type: "none"
```

---

## Edge case: Pending state (queued)
**Input:**
- Status type: task
- Context: Task queued behind others, not yet started
- State: Pending

**Output:**
```yaml
status:
  type: "task"
  state: "pending"
  label: "Queued"
  detail: "Your export will start soon."
  progress:
    type: "none"
```

---

## Edge case: Paused state
**Input:**
- Status type: task
- Context: User paused a large download
- State: Paused

**Output:**
```yaml
status:
  type: "task"
  state: "paused"
  label: "Paused"
  detail: "2.3 GB of 5 GB downloaded"
  progress:
    type: "determinate"
    value: 46
  action:
    label: "Resume"
```

---

## Edge case: Long-running task
**Input:**
- Status type: task
- Context: Database migration, expected 30+ minutes
- State: In-progress

**Output:**
```yaml
status:
  type: "task"
  state: "in-progress"
  label: "Migration in progress"
  detail: "This usually takes 30-45 minutes. You can close this page."
  progress:
    type: "indeterminate"
```
Note: Set expectations and clarify user doesn't need to wait.
