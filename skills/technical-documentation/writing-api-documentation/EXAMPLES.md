# Examples

## Example 1: REST API endpoint

**Input:**
- API: User management API
- Endpoint: Create a new user
- Auth: Bearer token with users:write scope

**Output:**

```md
# Create user

Create a new user account.

## Endpoint

`POST /users`

## Authentication

Requires bearer token with `users:write` scope.

## Parameters

### Request body

```json
{
  "email": "user@example.com",
  "name": "Jane Smith",
  "role": "member"
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `email` | string | Yes | User's email address. Must be valid email format. Max: 255 chars. Must be unique. |
| `name` | string | Yes | Display name. Max: 100 chars. |
| `role` | string | No | User role. Default: `"member"`. Allowed: `member`, `admin`, `viewer`. |
| `metadata` | object | No | Custom key-value pairs. Max 20 keys, 1KB total size. |

## Response

### `201 Created`

```json
{
  "id": "usr_abc123xyz",
  "email": "user@example.com",
  "name": "Jane Smith",
  "role": "member",
  "metadata": {},
  "created_at": "2024-01-15T10:30:00Z",
  "updated_at": "2024-01-15T10:30:00Z"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique user identifier. Format: `usr_[a-z0-9]{11}`. |
| `email` | string | User's email address. |
| `name` | string | User's display name. |
| `role` | string | User's assigned role. |
| `metadata` | object | Custom metadata. Empty object if not set. |
| `created_at` | string | ISO 8601 timestamp of creation. |
| `updated_at` | string | ISO 8601 timestamp of last update. |

## Errors

| Status | Code | Description |
|--------|------|-------------|
| `400` | `invalid_email` | Email format is invalid. |
| `400` | `invalid_role` | Role not in allowed values. |
| `400` | `metadata_too_large` | Metadata exceeds 1KB limit. |
| `409` | `email_already_exists` | Email address already registered. |
| `422` | `validation_failed` | Multiple validation errors. Check `details.errors` array. |

## Example

```bash
curl -X POST "https://api.example.com/v1/users" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "jane@example.com",
    "name": "Jane Smith",
    "role": "member"
  }'
```

Response:

```json
{
  "id": "usr_abc123xyz",
  "email": "jane@example.com",
  "name": "Jane Smith",
  "role": "member",
  "metadata": {},
  "created_at": "2024-01-15T10:30:00Z",
  "updated_at": "2024-01-15T10:30:00Z"
}
```

## Related

- [Get user](./get-user.md)
- [Update user](./update-user.md)
- [Delete user](./delete-user.md)
```

---

## Example 2: List endpoint with pagination

**Input:**
- Endpoint: List all users with filtering and pagination
- Supports: role filter, pagination, sorting

**Output:**

```md
# List users

Retrieve a paginated list of users.

## Endpoint

`GET /users`

## Authentication

Requires bearer token with `users:read` scope.

## Parameters

### Query parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `limit` | integer | `20` | Number of results per page. Range: 1-100. |
| `offset` | integer | `0` | Number of results to skip for pagination. |
| `role` | string | — | Filter by role. Allowed: `member`, `admin`, `viewer`. |
| `sort` | string | `created_at` | Sort field. Allowed: `created_at`, `name`, `email`. |
| `order` | string | `desc` | Sort order. Allowed: `asc`, `desc`. |
| `search` | string | — | Search by name or email. Min: 2 chars. |

## Response

### `200 OK`

```json
{
  "data": [
    {
      "id": "usr_abc123xyz",
      "email": "user@example.com",
      "name": "Jane Smith",
      "role": "member",
      "created_at": "2024-01-15T10:30:00Z"
    }
  ],
  "pagination": {
    "total": 150,
    "limit": 20,
    "offset": 0,
    "has_more": true
  }
}
```

| Field | Type | Description |
|-------|------|-------------|
| `data` | array | Array of user objects. |
| `pagination.total` | integer | Total number of users matching filters. |
| `pagination.limit` | integer | Current page size. |
| `pagination.offset` | integer | Current offset. |
| `pagination.has_more` | boolean | Whether more results exist. |

## Errors

| Status | Code | Description |
|--------|------|-------------|
| `400` | `invalid_limit` | Limit outside 1-100 range. |
| `400` | `invalid_sort` | Sort field not allowed. |

## Example

```bash
# Get first page of admin users
curl "https://api.example.com/v1/users?role=admin&limit=10" \
  -H "Authorization: Bearer $TOKEN"

# Get second page
curl "https://api.example.com/v1/users?role=admin&limit=10&offset=10" \
  -H "Authorization: Bearer $TOKEN"

# Search users
curl "https://api.example.com/v1/users?search=jane" \
  -H "Authorization: Bearer $TOKEN"
```
```

---

## Example 3: Edge case — webhook/event documentation

**Input:**
- Component: Webhook event for user creation
- Delivery: HTTP POST to registered URL

**Output:**

```md
# user.created event

Triggered when a new user account is created.

## Event type

`user.created`

## Delivery

HTTP POST to your registered webhook URL.

### Headers

| Header | Description |
|--------|-------------|
| `Content-Type` | `application/json` |
| `X-Webhook-Signature` | HMAC-SHA256 signature for verification |
| `X-Event-Type` | `user.created` |
| `X-Event-Id` | Unique event identifier for idempotency |

## Payload

```json
{
  "event": "user.created",
  "event_id": "evt_xyz789",
  "created_at": "2024-01-15T10:30:00Z",
  "data": {
    "user": {
      "id": "usr_abc123xyz",
      "email": "user@example.com",
      "name": "Jane Smith",
      "role": "member",
      "created_at": "2024-01-15T10:30:00Z"
    }
  }
}
```

| Field | Type | Description |
|-------|------|-------------|
| `event` | string | Event type identifier. |
| `event_id` | string | Unique ID. Use for idempotency. |
| `created_at` | string | When event was created. |
| `data.user` | object | Full user object at time of creation. |

## Signature verification

Verify the `X-Webhook-Signature` header to ensure the request came from our servers:

```python
import hmac
import hashlib

def verify_signature(payload: bytes, signature: str, secret: str) -> bool:
    expected = hmac.new(
        secret.encode(),
        payload,
        hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(f"sha256={expected}", signature)
```

## Response

Return `200 OK` to acknowledge receipt. Any other status triggers retry.

## Retry policy

| Attempt | Delay |
|---------|-------|
| 1 | Immediate |
| 2 | 1 minute |
| 3 | 5 minutes |
| 4 | 30 minutes |
| 5 | 2 hours |

After 5 failed attempts, webhook is disabled. Check webhook logs in dashboard.

## Related

- [user.updated event](./user-updated.md)
- [user.deleted event](./user-deleted.md)
- [Webhook configuration guide](/docs/webhooks)
```

---

## Anti-pattern example

**Bad output (do not produce):**

```md
# Users API

## Create User

You can create users by sending a POST request to /users.

**Request:**
- email (required)
- name (required)
- role (optional)

**Response:**
Returns the created user object.

**Example:**
```
POST /users
{email: "test@test.com"}
```
```

**Why this fails:**
- No full endpoint path
- Parameters missing types and constraints
- Response not documented
- Example missing auth header
- Example JSON invalid (unquoted keys)
- No error documentation
- No content-type header
