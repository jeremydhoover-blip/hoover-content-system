# Transition Patterns

## Transition anatomy

Every transition must specify:

```yaml
transition:
  from: <source_state>
  to: <target_state>
  trigger:
    type: <user_action | system_event | time_based | external>
    description: <what causes this transition>
  conditions: <optional prerequisites>
  side_effects: <optional system behaviors>
```

## Trigger types

### User action triggers
Transitions caused by explicit user interaction.

| Trigger | Description | Example states |
|---------|-------------|----------------|
| click | Button or link activation | idle → loading |
| submit | Form submission | editing → validating |
| cancel | User abandons operation | loading → idle |
| select | Choice from options | selecting → selected |
| input | Text or data entry | empty → has_input |
| gesture | Swipe, drag, etc. | collapsed → expanded |
| navigate | Page or view change | list → detail |

### System event triggers
Transitions caused by application or server events.

| Trigger | Description | Example states |
|---------|-------------|----------------|
| request_success | API call completed successfully | loading → success |
| request_failure | API call failed | loading → error |
| validation_pass | Input validated successfully | validating → submitting |
| validation_fail | Input validation failed | validating → invalid |
| permission_granted | Access approved | pending_access → accessible |
| data_received | Websocket or push update | stale → updated |

### Time-based triggers
Transitions caused by elapsed time.

| Trigger | Description | Example states |
|---------|-------------|----------------|
| timeout | Operation exceeded time limit | loading → timeout_error |
| auto_dismiss | Notification disappears | toast_visible → dismissed |
| session_expiry | Authentication timeout | active → session_expired |
| poll_interval | Periodic refresh | current → refreshing |

### External triggers
Transitions caused by events outside the application.

| Trigger | Description | Example states |
|---------|-------------|----------------|
| network_change | Connectivity lost/restored | online → offline |
| external_update | Another user changed data | current → conflict |
| webhook | External service callback | pending → processed |

## Common transition patterns

### Optimistic update
Show success immediately, rollback on failure.

```
editing → saving (UI shows success) → [background: save_request]
                                           ↓ success: stay in saved
                                           ↓ failure: revert to editing + error
```

### Pessimistic update
Wait for confirmation before showing success.

```
editing → saving (UI shows loading) → [wait for response]
                                           ↓ success: → saved
                                           ↓ failure: → save_error
```

### Retry pattern
```
error → retrying → [attempt] → success
                       ↓
                  error (with retry count)
                       ↓ (max retries exceeded)
                  permanent_error
```

### Polling pattern
```
pending → checking → [poll] → still_pending (wait, re-check)
                         ↓
                    completed
```

## Transition validation rules

### Required checks
1. **Reachability:** Every state except entry must have at least one inbound transition
2. **No dead ends:** Non-terminal states must have at least one outbound transition
3. **No self-loops without purpose:** state → state transitions need justification
4. **Error recovery:** Every error state must have a path back to a non-error state

### Consistency checks
1. **Symmetric transitions:** If A → B exists on user action, consider if B → A is needed
2. **Cancel paths:** Any interruptible operation should have a cancel transition
3. **Error paths:** Any operation that can fail should have an error transition

## Transition documentation format

In state map documentation, use this format:

```md
**Exit transitions:**
- → <target_state>: <trigger_description>
- → <target_state>: <trigger_description>
```

Example:
```md
**Exit transitions:**
- → uploading: validation passes
- → validation_error: file type not supported
- → validation_error: file exceeds size limit
- → idle: user cancels
```
