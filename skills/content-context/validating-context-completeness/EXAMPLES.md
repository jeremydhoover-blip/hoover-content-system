# Examples

## Example 1: Clean pass

**Input:** Context pack for "File Upload" feature

```yaml
feature:
  name: file-upload
  purpose: Allow users to upload files to their workspace
  
user_goals:
  - Upload a single file
  - Upload multiple files
  - Cancel an upload in progress

core_actions:
  - select_files
  - upload
  - cancel
  - retry

states:
  idle:
    entry: Page load or upload complete
    exit: User selects files
    content_guidance: Show drop zone with supported formats
  
  selecting:
    entry: User opens file picker
    exit: User confirms selection or cancels
    content_guidance: List selected files with sizes
  
  uploading:
    entry: Upload begins
    exit: Upload completes, fails, or user cancels
    error_handling: Show progress, allow cancel
    content_guidance: Progress indicator with percentage
  
  success:
    entry: Upload completes
    exit: User acknowledges or starts new upload
    content_guidance: Confirmation with file details
  
  error:
    entry: Upload fails
    exit: User retries or cancels
    error_handling: Show specific error, offer retry
    content_guidance: Error message with recovery action

transitions:
  - from: idle, to: selecting, trigger: click_drop_zone
  - from: selecting, to: uploading, trigger: confirm_selection
  - from: uploading, to: success, trigger: upload_complete
  - from: uploading, to: error, trigger: upload_failed
  - from: error, to: uploading, trigger: retry
  - from: any, to: idle, trigger: cancel

error_taxonomy:
  - code: FILE_TOO_LARGE
    message_pattern: "File exceeds [limit]. Choose a smaller file."
    recovery: Select different file
  - code: UNSUPPORTED_TYPE
    message_pattern: "File type not supported. Supported: [types]."
    recovery: Select different file
  - code: NETWORK_ERROR
    message_pattern: "Upload interrupted. Check connection and retry."
    recovery: Retry action
  - code: QUOTA_EXCEEDED
    message_pattern: "Storage full. Delete files or upgrade plan."
    recovery: Manage storage

vocabulary:
  drop_zone: The target area where users drag files
  file_picker: System dialog for selecting files
  upload: The action of transferring files to server
```

**Output:**

```md
# Context Pack Validation Report

**Pack:** file-upload
**Version:** 1.0
**Validated:** 2026-02-20
**Status:** PASS

## Summary
- Blocking issues: 0
- Warnings: 0
- Suggestions: 0

## Blocking Issues
No blocking issues found.

## Warnings
No warnings.

## Suggestions
No suggestions.

## Coverage Matrix

| Section | Required | Present | Status |
|---------|----------|---------|--------|
| Feature purpose | Yes | Yes | ✓ |
| User goals | Yes | Yes | ✓ |
| Core actions | Yes | Yes | ✓ |
| States | Yes | Yes | ✓ |
| Transitions | Yes | Yes | ✓ |
| Error taxonomy | Yes | Yes | ✓ |
| Vocabulary | Yes | Yes | ✓ |
| Tone boundaries | No | No | — |
| Constraints | No | No | — |

## State Coverage

| State | Entry defined | Exit defined | Error handling | Content guidance |
|-------|---------------|--------------|----------------|------------------|
| idle | Yes | Yes | N/A | Yes |
| selecting | Yes | Yes | N/A | Yes |
| uploading | Yes | Yes | Yes | Yes |
| success | Yes | Yes | N/A | Yes |
| error | Yes | Yes | Yes | Yes |

## Next Steps
None required. Pack is ready for use.
```

---

## Example 2: Blocking failures

**Input:** Incomplete context pack for "Password Reset" feature

```yaml
feature:
  name: password-reset
  
user_goals:
  - Reset forgotten password

states:
  request:
    entry: User clicks forgot password
    content_guidance: Ask for email
  
  email_sent:
    content_guidance: Confirmation message
  
  new_password:
    entry: User clicks reset link
    content_guidance: Password form
  
  complete:
    content_guidance: Success message

vocabulary:
  reset_link: Email link to reset password
  token: The verification_token in the URL
```

**Output:**

```md
# Context Pack Validation Report

**Pack:** password-reset
**Version:** unknown
**Validated:** 2026-02-20
**Status:** FAIL

## Summary
- Blocking issues: 6
- Warnings: 2
- Suggestions: 1

## Blocking Issues

### [BLOCK-001] Missing feature purpose
- **Location:** feature.purpose
- **Problem:** Feature purpose not defined
- **Impact:** Writers cannot understand the feature's goal; AI will guess intent
- **Remediation:** Add `purpose: Allow users to regain access when they forget their password`

### [BLOCK-002] Missing core actions
- **Location:** core_actions
- **Problem:** No core actions defined
- **Impact:** State transitions have no action mapping; writers cannot reference canonical action names
- **Remediation:** Add core_actions section: request_reset, verify_email, set_password, confirm

### [BLOCK-003] State missing exit condition: request
- **Location:** states.request
- **Problem:** No exit condition defined for "request" state
- **Impact:** Unclear when state ends; no transition guidance
- **Remediation:** Add `exit: Form submitted or user cancels`

### [BLOCK-004] State missing entry condition: email_sent
- **Location:** states.email_sent
- **Problem:** No entry condition defined for "email_sent" state
- **Impact:** Unclear how user reaches this state
- **Remediation:** Add `entry: Reset request submitted successfully`

### [BLOCK-005] Missing transitions section
- **Location:** transitions
- **Problem:** No transitions defined
- **Impact:** State flow is undefined; no guidance on allowed paths
- **Remediation:** Add transitions array mapping state changes to triggers

### [BLOCK-006] Missing error taxonomy
- **Location:** error_taxonomy
- **Problem:** No error taxonomy defined
- **Impact:** Error states have no content patterns; AI will invent error messages
- **Remediation:** Add error_taxonomy covering: invalid_email, expired_token, weak_password, rate_limited

### [BLOCK-007] Undefined vocabulary term used
- **Location:** vocabulary
- **Problem:** Term "verification_token" used in token definition but not defined
- **Impact:** Inconsistent terminology; circular reference
- **Remediation:** Define verification_token or remove reference from token definition

## Warnings

### [WARN-001] States missing error handling
- **Location:** states.request, states.new_password
- **Problem:** No error_handling defined for states that can fail
- **Recommendation:** Add error_handling for form validation failures

### [WARN-002] States missing exit conditions
- **Location:** states.email_sent, states.new_password, states.complete
- **Problem:** Exit conditions not defined
- **Recommendation:** Define exit conditions for complete state flow

## Suggestions

### [SUGG-001] Add tone boundaries
- **Location:** tone_boundaries
- **Opportunity:** Security-sensitive flow would benefit from explicit tone guidance (reassuring but not casual)

## Coverage Matrix

| Section | Required | Present | Status |
|---------|----------|---------|--------|
| Feature purpose | Yes | No | ✗ |
| User goals | Yes | Yes | ✓ |
| Core actions | Yes | No | ✗ |
| States | Yes | Yes | ✓ |
| Transitions | Yes | No | ✗ |
| Error taxonomy | Yes | No | ✗ |
| Vocabulary | Yes | Yes | ✓ |
| Tone boundaries | No | No | — |
| Constraints | No | No | — |

## State Coverage

| State | Entry defined | Exit defined | Error handling | Content guidance |
|-------|---------------|--------------|----------------|------------------|
| request | Yes | No | No | Yes |
| email_sent | No | No | No | Yes |
| new_password | Yes | No | No | Yes |
| complete | No | No | No | Yes |

## Next Steps
1. Add feature.purpose field
2. Add core_actions section
3. Add transitions section with all state flows
4. Add error_taxonomy with at least 4 error types
5. Add entry/exit conditions to all states
6. Add error_handling to request and new_password states
7. Fix vocabulary circular reference
8. Re-run validation
```

---

## Example 3: Edge case — semantic inconsistency

**Input:** Context pack with conflicting definitions

```yaml
feature:
  name: user-invite
  purpose: Allow workspace admins to invite new members

vocabulary:
  member: A user who belongs to a workspace
  user: A member of the workspace
  invite: Send membership request to email
  invitation: The invite sent to a user

states:
  pending:
    entry: Invitation sent
    exit: User accepts or invitation expires
    content_guidance: Show pending status

transitions:
  - from: pending, to: active, trigger: member_accepts
  - from: pending, to: expired, trigger: timeout
```

**Output:**

```md
# Context Pack Validation Report

**Pack:** user-invite
**Version:** 1.0
**Validated:** 2026-02-20
**Status:** FAIL

## Summary
- Blocking issues: 3
- Warnings: 1
- Suggestions: 1

## Blocking Issues

### [BLOCK-001] Circular vocabulary definition
- **Location:** vocabulary.member, vocabulary.user
- **Problem:** "member" is defined as "a user" and "user" is defined as "a member" — circular reference
- **Impact:** No canonical term; writers will use inconsistently; AI cannot resolve
- **Remediation:** Choose one canonical term. Recommended: define "member" as primary, remove "user" or define as "person with account (may or may not be member)"

### [BLOCK-002] Conflicting vocabulary terms
- **Location:** vocabulary.invite, vocabulary.invitation
- **Problem:** "invite" and "invitation" both defined with overlapping meaning
- **Impact:** Inconsistent usage across content; ambiguous action vs object
- **Remediation:** Distinguish clearly: "invite (verb): action of sending" vs "invitation (noun): the request object"

### [BLOCK-003] Transition references undefined state
- **Location:** transitions[0]
- **Problem:** Transition targets "active" state which is not defined
- **Impact:** State flow incomplete; unreachable state
- **Remediation:** Add "active" state definition with entry, exit, and content_guidance

### [BLOCK-004] Transition references undefined state
- **Location:** transitions[1]
- **Problem:** Transition targets "expired" state which is not defined
- **Impact:** State flow incomplete; unreachable state
- **Remediation:** Add "expired" state definition

## Warnings

### [WARN-001] Missing user goals
- **Location:** user_goals
- **Problem:** No user goals defined
- **Recommendation:** Add user_goals: invite team member, resend invitation, revoke invitation

## Suggestions

### [SUGG-001] Vocabulary completeness
- **Location:** vocabulary
- **Opportunity:** Consider adding: workspace, admin, role, permission

## Next Steps
1. Resolve circular member/user definition
2. Clarify invite vs invitation usage
3. Add missing states: active, expired
4. Add user_goals section
5. Re-run validation
```
