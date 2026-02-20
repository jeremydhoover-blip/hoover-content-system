# State Taxonomy

## State type classification

Every state in a state map must be assigned one of these types:

| Type | Definition | Content characteristics | Examples |
|------|------------|------------------------|----------|
| **standard** | Normal operating state where user can take actions | Neutral tone, action-oriented CTAs | idle, viewing, editing, browsing |
| **loading** | System processing, user waiting | Progress indication, reassurance, optional cancel | uploading, saving, fetching, validating |
| **success** | Operation completed successfully | Confirmation, next steps, celebration (if appropriate) | upload_complete, saved, sent |
| **error** | Operation failed or invalid state | Clear problem statement, recovery action, empathy | network_error, validation_failed, permission_denied |
| **empty** | No content or data to display | Explanation, guidance to populate, illustration | no_results, first_use, no_items |
| **permission** | Access restricted by role or status | Clear explanation of restriction, path to access | view_only, locked, requires_upgrade |
| **edge** | Unusual or boundary condition | Context-specific handling, may need special UX | rate_limited, maintenance, deprecated |

## State naming conventions

### Format
- Use `snake_case` for programmatic references
- Use lowercase
- Be specific: `upload_error` not `error`

### Naming patterns
| Pattern | Use when | Examples |
|---------|----------|----------|
| `<action>_<status>` | Result of user action | upload_success, save_error |
| `<object>_<condition>` | Object-based state | file_selected, form_invalid |
| `<verb>ing` | In-progress states | loading, uploading, saving |
| `<adjective>` | Condition-based states | idle, empty, locked |

### Avoid
- Generic names: `error`, `done`, `state1`
- Implementation details: `api_response_pending`
- UI-specific names: `modal_open` (unless modal is the feature)

## Required states checklist

For any feature, verify these state categories are addressed:

### Always required
- [ ] **Entry state:** First state users encounter
- [ ] **Primary action states:** States for main user workflows

### Required if applicable
- [ ] **Loading states:** For any async operation (API calls, file operations)
- [ ] **Error states:** For any operation that can fail
  - [ ] Network/connectivity errors
  - [ ] Validation errors
  - [ ] Permission errors
  - [ ] Server errors
- [ ] **Empty states:** For any list, search, or data display
  - [ ] First use (never had data)
  - [ ] No results (had data, now empty)
  - [ ] Filtered empty (data exists but filter excludes all)
- [ ] **Permission states:** For role-gated features
- [ ] **Success states:** For operations needing confirmation

### Often overlooked
- [ ] **Pending states:** Awaiting external action (approval, verification)
- [ ] **Partial states:** Incomplete data or partial success
- [ ] **Degraded states:** Feature working with reduced functionality
- [ ] **Timeout states:** Operation took too long
- [ ] **Conflict states:** Concurrent edit, version mismatch

## State lifecycle patterns

### Simple CRUD
```
idle → creating → validating → saving → success → idle
                     ↓            ↓
              validation_error  save_error
```

### Async operation
```
idle → initiating → pending → processing → success → idle
                       ↓           ↓
                    timeout    error → retry → pending
```

### Permission-gated
```
loading → [permission check] → editable (admin)
                             → view_only (non-admin)
                             → access_denied (no access)
```

## Content requirements matrix

| State type | Headline | Body | Primary CTA | Secondary CTA | Progress |
|------------|----------|------|-------------|---------------|----------|
| standard | Optional | Optional | Usually | Optional | No |
| loading | Optional | Often | Cancel (if interruptible) | No | Yes |
| success | Often | Brief | Next action or dismiss | No | No |
| error | Yes | Yes (recovery guidance) | Primary recovery | Alternative | No |
| empty | Yes | Yes (guidance) | Population action | No | No |
| permission | Yes | Yes (explanation) | Access path if exists | No | No |
| edge | Context-dependent | Context-dependent | Context-dependent | Context-dependent | No |
