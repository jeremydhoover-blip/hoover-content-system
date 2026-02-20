# Examples

## Example 1: API endpoint reference

**Input:**
- Component: REST API endpoint for user creation
- Method: POST
- Path: /users
- Auth: Bearer token

**Output:**

```md
# Create user

Create a new user account in the system.

## Endpoint

`POST /users`

## Authentication

Requires `Bearer` token with `users:write` scope.

## Parameters

### Request body

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `email` | string | Yes | User's email address. Must be unique. Max length: 255. |
| `name` | string | Yes | Display name. Max length: 100. |
| `role` | string | No | User role. Default: `"member"`. Valid values: `member`, `admin`. |
| `metadata` | object | No | Custom key-value pairs. Max 10 keys. |

## Response

### Success response (201)

```json
{
  "id": "usr_abc123",
  "email": "user@example.com",
  "name": "Example User",
  "role": "member",
  "created_at": "2024-01-15T10:30:00Z"
}
```

### Response fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique user identifier. Prefixed with `usr_`. |
| `email` | string | User's email address. |
| `name` | string | User's display name. |
| `role` | string | User's assigned role. |
| `created_at` | string (ISO 8601) | Timestamp when user was created. |

## Errors

| Status | Code | Description |
|--------|------|-------------|
| 400 | `invalid_email` | Email format is invalid. |
| 400 | `invalid_role` | Role value not in allowed list. |
| 409 | `email_exists` | Email address already registered. |
| 422 | `validation_error` | Request body failed validation. |

## Example

```bash
curl -X POST \
  https://api.example.com/users \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"email": "new@example.com", "name": "New User"}'
```

## Related

- [Get user](./get-user.md)
- [Update user](./update-user.md)
- [Authentication guide](/guides/authentication)
```

---

## Example 2: Configuration reference

**Input:**
- Component: Logger configuration for Node.js app
- Format: JSON
- Location: config/logger.json

**Output:**

```md
# Logger configuration

Configure application logging behavior and output destinations.

## Location

`config/logger.json` or environment variables (see individual options).

## Format

JSON

## Options

### `level`

| Property | Value |
|----------|-------|
| Type | string |
| Default | `"info"` |
| Required | No |
| Environment variable | `LOG_LEVEL` |

Minimum severity level for log output.

**Valid values:**
- `debug` — All messages including debug information
- `info` — Informational messages and above
- `warn` — Warnings and errors only
- `error` — Errors only

### `format`

| Property | Value |
|----------|-------|
| Type | string |
| Default | `"json"` |
| Required | No |
| Environment variable | `LOG_FORMAT` |

Output format for log entries.

**Valid values:**
- `json` — Structured JSON, one object per line
- `text` — Human-readable plain text

### `destinations`

| Property | Value |
|----------|-------|
| Type | array of objects |
| Default | `[{"type": "stdout"}]` |
| Required | No |

Output destinations for log entries. Multiple destinations supported.

**Destination object properties:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | Yes | Destination type: `stdout`, `file`, `http`. |
| `path` | string | When type=file | File path for file destination. |
| `url` | string | When type=http | Endpoint URL for HTTP destination. |

### `redact`

| Property | Value |
|----------|-------|
| Type | array of strings |
| Default | `["password", "token", "secret"]` |
| Required | No |

Field names to redact from log output. Case-insensitive matching.

## Complete example

```json
{
  "level": "debug",
  "format": "json",
  "destinations": [
    { "type": "stdout" },
    { "type": "file", "path": "/var/log/app.log" }
  ],
  "redact": ["password", "apiKey", "authorization"]
}
```

## Related

- [How to configure logging](/guides/configure-logging)
- [Application configuration reference](./app-config.md)
```

---

## Example 3: Edge case — function with complex return type

**Input:**
- Component: Async function returning discriminated union
- Language: TypeScript

**Output:**

```md
# `fetchUser()`

Retrieve a user by ID with optional field expansion.

## Signature

```typescript
fetchUser(
  id: string,
  options?: FetchUserOptions
): Promise<FetchUserResult>
```

## Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `id` | `string` | Yes | — | User ID. Must match pattern `usr_[a-z0-9]+`. |
| `options` | `FetchUserOptions` | No | `{}` | Request options. |

### FetchUserOptions

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `expand` | `string[]` | `[]` | Related resources to include. Valid: `"profile"`, `"settings"`. |
| `cache` | `boolean` | `true` | Whether to use cached data. |

## Returns

`Promise<FetchUserResult>` — Resolves to a discriminated union:

### Success case

```typescript
{
  success: true;
  data: User;
}
```

### Error case

```typescript
{
  success: false;
  error: {
    code: string;
    message: string;
  };
}
```

**Note:** Function does not throw. Check `success` property to determine outcome.

## Example

```typescript
const result = await fetchUser("usr_abc123", { expand: ["profile"] });

if (result.success) {
  console.log(result.data.email);
} else {
  console.error(result.error.code);
}
```

## Related

- [`User` type reference](./types/user.md)
- [`createUser()`](./create-user.md)
```

---

## Anti-pattern example

**Bad output (do not produce):**

```md
# User API

The User API lets you manage users in your application. Users are a core concept...

## Creating users

To create a user, you'll want to first...

## Endpoint

POST /users

## Fields

- email - the user's email
- name - their name
- role - what role they have
```

**Why this fails:**
- Title too vague (should be "Create user" not "User API")
- Includes conceptual explanation
- Mixes task flow ("To create a user, you'll want to...") with reference
- Parameters missing types, requirements, constraints
- Inconsistent formatting (not using tables)
- No default values documented
