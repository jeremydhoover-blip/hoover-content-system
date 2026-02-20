# Examples

## Example 1: Simple success
**Input:**
- Type: success
- Context: User saved a document
- Action required: None

**Output:**
```yaml
notification:
  type: "success"
  message: "Document saved"
  action: null
  persistence: "auto-dismiss"
  auto_dismiss_seconds: 4
```

---

## Example 2: Success with undo
**Input:**
- Type: success
- Context: User deleted an email
- Action required: Optional undo

**Output:**
```yaml
notification:
  type: "success"
  message: "Email deleted"
  action:
    label: "Undo"
    type: "undo"
  persistence: "auto-dismiss"
  auto_dismiss_seconds: 6
```

---

## Example 3: Error notification
**Input:**
- Type: error
- Context: Failed to send message due to network error
- Action required: Retry

**Output:**
```yaml
notification:
  type: "error"
  message: "Couldn't send message. Check your connection."
  action:
    label: "Retry"
    type: "retry"
  persistence: "manual-dismiss"
```

---

## Example 4: Warning notification
**Input:**
- Type: warning
- Context: User's storage is almost full
- Action required: Upgrade or clean up

**Output:**
```yaml
notification:
  type: "warning"
  message: "Storage almost full. 95% used."
  action:
    label: "Manage storage"
    type: "navigate"
  persistence: "manual-dismiss"
```

---

## Example 5: Info notification
**Input:**
- Type: info
- Context: New feature announcement
- Action required: None, but can learn more

**Output:**
```yaml
notification:
  type: "info"
  message: "New: Dark mode is now available"
  action:
    label: "Try it"
    type: "navigate"
  persistence: "auto-dismiss"
  auto_dismiss_seconds: 8
```

---

## Edge case: Copy to clipboard
**Input:**
- Type: success
- Context: User clicked "Copy link"
- Action required: None

**Output:**
```yaml
notification:
  type: "success"
  message: "Link copied to clipboard"
  action: null
  persistence: "auto-dismiss"
  auto_dismiss_seconds: 3
```
Note: Very brief confirmations can use 3-4 second dismiss.

---

## Edge case: Offline mode activated
**Input:**
- Type: info
- Context: Network lost, switching to offline mode
- Action required: None (informational)

**Output:**
```yaml
notification:
  type: "info"
  message: "You're offline. Changes will sync when you reconnect."
  action: null
  persistence: "manual-dismiss"
```
Note: Status changes that affect ongoing work should be manual-dismiss.

---

## Edge case: Bulk action
**Input:**
- Type: success
- Context: User archived 12 conversations
- Action required: Optional undo

**Output:**
```yaml
notification:
  type: "success"
  message: "12 conversations archived"
  action:
    label: "Undo"
    type: "undo"
  persistence: "auto-dismiss"
  auto_dismiss_seconds: 6
```
