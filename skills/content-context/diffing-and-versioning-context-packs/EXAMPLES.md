# Examples

## Example 1: Minor version bump (additions only)

**Input:**

Base version (1.2.0):
```yaml
feature:
  name: file-upload
  purpose: Allow users to upload files
  version: 1.2.0

user_goals:
  - Upload a file
  - Cancel upload

states:
  idle:
    entry: Page load
    exit: User selects file
    content_guidance: Show drop zone
  
  uploading:
    entry: Upload starts
    exit: Upload completes or fails
    content_guidance: Show progress

vocabulary:
  drop_zone: Area to drag files
```

Head version:
```yaml
feature:
  name: file-upload
  purpose: Allow users to upload files
  version: 1.2.0

user_goals:
  - Upload a file
  - Cancel upload
  - Retry failed upload

states:
  idle:
    entry: Page load
    exit: User selects file
    content_guidance: Show drop zone
  
  uploading:
    entry: Upload starts
    exit: Upload completes or fails
    content_guidance: Show progress
  
  error:
    entry: Upload fails
    exit: User retries or cancels
    content_guidance: Show error with retry option

vocabulary:
  drop_zone: Area to drag files
  retry: Attempt upload again after failure
```

**Output:**

```md
# Context Pack Diff Report

**Pack:** file-upload
**Base version:** 1.2.0
**Head version:** 1.3.0
**Generated:** 2026-02-20
**Recommended version:** 1.3.0

## Summary
- Breaking changes: 0
- Additions: 3
- Corrections: 0
- Version increment: MINOR

## Breaking Changes
No breaking changes.

## Additions

### [ADD-001] New user goal: Retry failed upload
- **Section:** user_goals
- **Added:** "Retry failed upload"
- **Purpose:** Supports error recovery flow

### [ADD-002] New state: error
- **Section:** states.error
- **Added:** Complete error state definition
- **Purpose:** Handles upload failure scenario

### [ADD-003] New vocabulary term: retry
- **Section:** vocabulary.retry
- **Added:** "Attempt upload again after failure"
- **Purpose:** Defines retry action terminology

## Corrections
No corrections.

## Changelog Entry

### 1.3.0 - 2026-02-20

#### Added
- User goal: Retry failed upload
- State: error (handles upload failures)
- Vocabulary: retry
```

---

## Example 2: Major version bump (breaking changes)

**Input:**

Base version (2.1.0):
```yaml
feature:
  name: password-reset
  purpose: Reset forgotten password
  version: 2.1.0

states:
  request:
    entry: User clicks forgot password
    exit: Form submitted
    content_guidance: Ask for email
  
  verify:
    entry: User clicks email link
    exit: Code verified
    content_guidance: Enter verification code
  
  reset:
    entry: Code verified
    exit: Password changed
    content_guidance: Enter new password

error_taxonomy:
  - code: INVALID_EMAIL
    message_pattern: "Email not found"
    recovery: Try different email
  - code: CODE_EXPIRED
    message_pattern: "Code expired"
    recovery: Request new code

vocabulary:
  verification_code: 6-digit code sent to email
```

Head version:
```yaml
feature:
  name: password-reset
  purpose: Reset forgotten password
  version: 2.1.0

states:
  request:
    entry: User clicks forgot password
    exit: Form submitted
    content_guidance: Ask for email
  
  reset:
    entry: User clicks email link with token
    exit: Password changed
    content_guidance: Enter new password

error_taxonomy:
  - code: INVALID_EMAIL
    message_pattern: "Email not recognized"
    recovery: Try different email
  - code: TOKEN_INVALID
    message_pattern: "Link expired or invalid"
    recovery: Request new link

vocabulary:
  reset_token: Unique link token for password reset
```

**Output:**

```md
# Context Pack Diff Report

**Pack:** password-reset
**Base version:** 2.1.0
**Head version:** 3.0.0
**Generated:** 2026-02-20
**Recommended version:** 3.0.0

## Summary
- Breaking changes: 4
- Additions: 0
- Corrections: 1
- Version increment: MAJOR

## Breaking Changes

### [BREAK-001] State removed: verify
- **Section:** states.verify
- **Was:** Complete verify state (code entry flow)
- **Now:** Removed
- **Impact:** Content referencing verification code flow will break; user journey changes
- **Migration:** Remove all UI copy referencing verification codes; update flow to use direct link

### [BREAK-002] Error code removed: CODE_EXPIRED
- **Section:** error_taxonomy
- **Was:** CODE_EXPIRED error type
- **Now:** Removed (replaced by TOKEN_INVALID)
- **Impact:** Error handling logic referencing CODE_EXPIRED will not trigger
- **Migration:** Replace CODE_EXPIRED references with TOKEN_INVALID

### [BREAK-003] Vocabulary term removed: verification_code
- **Section:** vocabulary.verification_code
- **Was:** "6-digit code sent to email"
- **Now:** Removed (replaced by reset_token)
- **Impact:** Content using term "verification code" now undefined
- **Migration:** Replace all instances of "verification code" with "reset link"

### [BREAK-004] Error code changed: TOKEN_INVALID replaces CODE_EXPIRED
- **Section:** error_taxonomy
- **Was:** CODE_EXPIRED with "Code expired" message
- **Now:** TOKEN_INVALID with "Link expired or invalid" message
- **Impact:** Different error code and message pattern
- **Migration:** Update error handling to use new code; update UI strings

## Additions
No additions (new elements replace removed ones, classified as breaking).

## Corrections

### [CORR-001] Error message clarified: INVALID_EMAIL
- **Section:** error_taxonomy[0].message_pattern
- **Was:** "Email not found"
- **Now:** "Email not recognized"
- **Reason:** More accurate phrasing; email may exist but not be registered

## Detailed Diff

### states
| State | Status | Changes |
|-------|--------|---------|
| request | unchanged | — |
| verify | removed | BREAKING: entire state removed |
| reset | modified | entry condition changed (code → token) |

### error_taxonomy
| Status | Code | Change |
|--------|------|--------|
| ~ | INVALID_EMAIL | message_pattern updated |
| - | CODE_EXPIRED | removed |
| + | TOKEN_INVALID | added (replaces CODE_EXPIRED) |

### vocabulary
| Status | Term | Change |
|--------|------|--------|
| - | verification_code | removed |
| + | reset_token | added (replaces verification_code) |

## Changelog Entry

### 3.0.0 - 2026-02-20

#### Breaking
- Removed state: verify (code entry flow eliminated)
- Removed error: CODE_EXPIRED (replaced by TOKEN_INVALID)
- Removed vocabulary: verification_code (replaced by reset_token)
- Changed error: TOKEN_INVALID replaces CODE_EXPIRED with different code

#### Fixed
- Clarified INVALID_EMAIL message: "Email not recognized"
```

---

## Example 3: Edge case — semantic meaning change

**Input:**

Base version:
```yaml
vocabulary:
  workspace: A container for a user's files and projects
```

Head version:
```yaml
vocabulary:
  workspace: A shared container for team collaboration on files and projects
```

**Output:**

```md
# Context Pack Diff Report

**Pack:** [name]
**Base version:** 1.0.0
**Head version:** 2.0.0
**Recommended version:** 2.0.0

## Summary
- Breaking changes: 1
- Additions: 0
- Corrections: 0
- Version increment: MAJOR

## Breaking Changes

### [BREAK-001] Vocabulary definition changed: workspace
- **Section:** vocabulary.workspace
- **Was:** "A container for a user's files and projects"
- **Now:** "A shared container for team collaboration on files and projects"
- **Impact:** Scope changed from individual ("a user's") to collective ("team collaboration"); content implying single-user ownership now incorrect
- **Migration:** Audit all content using "workspace"; update copy implying personal ownership to reflect shared nature; review possessive pronouns ("your workspace" → "the workspace" or "your team's workspace")

## Classification rationale
This is a BREAKING change, not a correction, because:
1. Key noun changed: "user's" → "team"
2. Scope expanded: individual → collaborative
3. Implicit ownership model changed: personal → shared
4. Existing content ("your workspace" meaning "your personal space") becomes misleading
```

---

## Example 4: Patch version (corrections only)

**Input:**

Base version:
```yaml
states:
  uploading:
    entry: Upload satarts
    exit: Upload completes or fails
    content_guidance: Show progerss bar with percentage
```

Head version:
```yaml
states:
  uploading:
    entry: Upload starts
    exit: Upload completes or fails
    content_guidance: Show progress bar with percentage
```

**Output:**

```md
# Context Pack Diff Report

**Pack:** [name]
**Base version:** 1.0.0
**Head version:** 1.0.1
**Recommended version:** 1.0.1

## Summary
- Breaking changes: 0
- Additions: 0
- Corrections: 2
- Version increment: PATCH

## Corrections

### [CORR-001] Typo fixed: entry condition
- **Section:** states.uploading.entry
- **Was:** "Upload satarts"
- **Now:** "Upload starts"
- **Reason:** Spelling correction

### [CORR-002] Typo fixed: content guidance
- **Section:** states.uploading.content_guidance
- **Was:** "Show progerss bar with percentage"
- **Now:** "Show progress bar with percentage"
- **Reason:** Spelling correction

## Changelog Entry

### 1.0.1 - 2026-02-20

#### Fixed
- Typo in uploading state entry: "satarts" → "starts"
- Typo in uploading state guidance: "progerss" → "progress"
```
