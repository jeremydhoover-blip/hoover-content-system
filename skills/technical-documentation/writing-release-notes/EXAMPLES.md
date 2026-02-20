# Examples

## Example 1: Major release with breaking changes

**Input:**
- Version: 3.0.0
- Breaking: Auth header format changed
- New: Team workspaces feature
- Fix: File upload timeout issue
- Deprecation: v2 API endpoints

**Output:**

```md
# Release 3.0.0 — January 15, 2024

Major release introducing team workspaces and updated authentication.

## Breaking changes

> **Action required:** These changes may require updates to your integration.

### Authentication header format changed

**What changed:** The `Authorization` header now requires the `Bearer` prefix.

**Impact:** All API integrations using API keys directly in the Authorization header.

**Before:**
```
Authorization: sk_live_abc123
```

**After:**
```
Authorization: Bearer sk_live_abc123
```

**Migration:**
1. Update your HTTP client to prepend `Bearer ` to your API key.
2. Test authentication with a non-production key.
3. Deploy the update before March 1, 2024.

**Deadline:** Old format accepted until March 1, 2024.

**Migration guide:** [Updating to v3 authentication](/docs/migration/auth-v3)

## New features

### Team workspaces

Collaborate with your team in shared workspaces. Create separate environments for different projects, control member access, and manage billing per workspace.

- Create unlimited workspaces per organization
- Invite members with role-based permissions (Admin, Editor, Viewer)
- Transfer projects between workspaces

**Learn more:** [Team workspaces documentation](/docs/workspaces)

### Bulk operations API

Perform batch operations on up to 1,000 resources in a single request. Reduces API calls and improves performance for large-scale operations.

**Learn more:** [Bulk operations guide](/docs/api/bulk)

## Improvements

- **Dashboard:** Redesigned project list with filtering and sorting options
- **API:** Response times improved by 40% for list endpoints
- **Webhooks:** Added retry status visibility in webhook logs

## Bug fixes

- Fixed file uploads failing after 60 seconds on slow connections — uploads now respect configured timeout
- Fixed search returning duplicate results when using pagination
- Fixed incorrect timezone display for users in UTC+ timezones

## Deprecations

### v2 API endpoints

**Deprecated:** All `/v2/*` API endpoints
**Replacement:** `/v3/*` endpoints with equivalent functionality
**Removal date:** June 1, 2024

**Migration guide:** [v2 to v3 migration](/docs/migration/v2-to-v3)

---

**Full changelog:** [GitHub releases](https://github.com/example/repo/releases/tag/v3.0.0)
**Upgrade guide:** [v3 upgrade guide](/docs/upgrade/v3)
```

---

## Example 2: Patch release

**Input:**
- Version: 2.5.3
- Fixes only, no features
- One security fix

**Output:**

```md
# Release 2.5.3 — January 20, 2024

Patch release with bug fixes and a security update.

## Security

### Dependency update for CVE-2024-1234

**Severity:** Medium
**Impact:** Potential information disclosure in error messages
**Fixed in:** This release

Updated internal logging library to version 2.1.0 which addresses the vulnerability.

## Bug fixes

- Fixed session expiration not being enforced correctly after password change
- Fixed CSV export including deleted records in some edge cases
- Fixed notification emails sent with incorrect sender address

---

**Full changelog:** [v2.5.2...v2.5.3](https://github.com/example/repo/compare/v2.5.2...v2.5.3)
```

---

## Example 3: Edge case — API versioning release

**Input:**
- API version: 2024-01-15
- Multiple endpoint changes
- Date-based versioning

**Output:**

```md
# API Version 2024-01-15

Released January 15, 2024. Request this version with header `X-API-Version: 2024-01-15`.

## Breaking

### `POST /users` — Email verification required by default

New user accounts now require email verification before becoming active. Previously, accounts were active immediately.

**Migration:** If your integration relies on immediate account activation:
1. Set `skip_email_verification: true` in the request body, OR
2. Update your flow to handle the `pending_verification` status

**Details:** [Email verification changes](/docs/api/changelog/email-verification)

### `GET /projects` — Response pagination changed

Default page size reduced from 100 to 20. Maximum page size now 100 (was 1000).

**Migration:** Update pagination logic if you relied on larger page sizes.

## Added

- `POST /teams` — Create team workspaces
- `GET /users/{id}/workspaces` — List user's workspace memberships
- New field `workspace_id` on project responses

## Changed

- `GET /users` — Now includes `last_active_at` timestamp (backward compatible)
- `POST /files` — Maximum file size increased to 100MB

## Deprecated

- `GET /projects?include_deleted=true` — Use `GET /projects/deleted` instead
- `user.team_id` response field — Use `user.workspace_ids` array instead

**Removal:** API version 2024-07-01

## Fixed

- `POST /webhooks` — Fixed incorrect error code when URL validation fails (was 500, now 422)
- `GET /files/{id}` — Fixed timeout on large file metadata retrieval

---

**Version changelog:** [API versions](/docs/api/versions)
**Previous version:** [2023-10-01](/docs/api/changelog/2023-10-01)
```

---

## Anti-pattern example

**Bad output (do not produce):**

```md
# v3.0.0

## Changes

- PROJ-1234: Updated auth
- PROJ-1245: Added workspaces feature
- PROJ-1256: Fixed bug
- PROJ-1267: Performance improvements
- Breaking: Changed some API stuff, see docs

## Notes

This release has some breaking changes so please update your code.
```

**Why this fails:**
- No date
- Breaking changes not first and not explained
- Uses ticket numbers instead of descriptions
- "Fixed bug" doesn't describe what was fixed
- No migration instructions
- Vague language ("some API stuff", "please update your code")
- No categorization
- No links to documentation
