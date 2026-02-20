# Templates

## API overview page

```md
# [API Name] API

[One-sentence description of what this API does.]

## Base URL

```
https://api.example.com/v1
```

## Authentication

[Description of authentication method]

```bash
curl -H "Authorization: Bearer YOUR_TOKEN" https://api.example.com/v1/resource
```

See [Authentication guide](/docs/authentication) for setup instructions.

## Common headers

| Header | Required | Description |
|--------|----------|-------------|
| `Authorization` | Yes | Bearer token |
| `Content-Type` | For POST/PUT | `application/json` |
| `Accept` | No | `application/json` (default) |

## Rate limits

| Tier | Requests per minute | Burst |
|------|---------------------|-------|
| Free | 60 | 10 |
| Pro | 600 | 100 |

Rate limit headers returned with each response:
- `X-RateLimit-Limit`: Your limit
- `X-RateLimit-Remaining`: Requests remaining
- `X-RateLimit-Reset`: Unix timestamp when limit resets

## Pagination

List endpoints return paginated results:

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `limit` | integer | 20 | Items per page (max 100) |
| `offset` | integer | 0 | Number of items to skip |

Response includes pagination metadata:

```json
{
  "data": [...],
  "pagination": {
    "total": 150,
    "limit": 20,
    "offset": 0,
    "has_more": true
  }
}
```

## Errors

All errors return JSON with consistent structure:

```json
{
  "error": {
    "code": "error_code",
    "message": "Human-readable message",
    "details": {}
  }
}
```

See [Error reference](/docs/errors) for all error codes.

## Resources

- [Users](/docs/api/users)
- [Projects](/docs/api/projects)
- [Files](/docs/api/files)
```

---

## REST endpoint documentation

```md
# [Action] [Resource]

[One-sentence description.]

## Endpoint

`[METHOD] /path/to/resource`

## Authentication

Requires `scope:permission` scope.

## Parameters

### Path parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `id` | string | [Description] |

### Query parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `include` | string | — | Comma-separated related resources to include |

### Request body

```json
{
  "field": "value"
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `field` | string | Yes | [Description]. Max: 255 chars. |

## Response

### `200 OK`

```json
{
  "id": "res_123",
  "field": "value",
  "created_at": "2024-01-15T10:00:00Z"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Resource identifier |

## Errors

| Status | Code | Description |
|--------|------|-------------|
| `400` | `invalid_field` | Field validation failed |
| `404` | `not_found` | Resource does not exist |

## Example

```bash
curl -X [METHOD] \
  "https://api.example.com/v1/resource" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"field": "value"}'
```

Response:

```json
{
  "id": "res_123",
  "field": "value"
}
```
```

---

## GraphQL operation documentation

```md
# [Operation name]

[One-sentence description.]

## Operation

```graphql
[query|mutation] [OperationName]($var: Type!) {
  fieldName(arg: $var) {
    field1
    field2
  }
}
```

## Variables

| Variable | Type | Required | Description |
|----------|------|----------|-------------|
| `var` | `Type!` | Yes | [Description] |

## Response

```json
{
  "data": {
    "fieldName": {
      "field1": "value",
      "field2": 123
    }
  }
}
```

## Errors

| Error code | Description |
|------------|-------------|
| `NOT_FOUND` | [When this occurs] |

## Example

```bash
curl -X POST \
  "https://api.example.com/graphql" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"query": "...", "variables": {"var": "value"}}'
```
```

---

## Error reference page

```md
# Error reference

## Error response format

```json
{
  "error": {
    "code": "error_code",
    "message": "Human-readable description",
    "details": {
      "field": "Additional context"
    }
  }
}
```

## HTTP status codes

| Status | Meaning | Action |
|--------|---------|--------|
| `400` | Bad request | Check request parameters |
| `401` | Unauthorized | Check authentication |
| `403` | Forbidden | Check permissions/scopes |
| `404` | Not found | Verify resource exists |
| `429` | Rate limited | Wait and retry |
| `500` | Server error | Retry or contact support |

## Error codes

### `invalid_parameter`

Parameter validation failed.

**Cause:** Request parameter does not meet requirements.

**Resolution:** Check `details.field` for the invalid parameter and `details.reason` for why.

### `authentication_required`

Request missing authentication.

**Cause:** No `Authorization` header provided.

**Resolution:** Include valid bearer token in header.

[Continue for each error code...]
```

---

## Variation rules
- Every endpoint must have at least one complete curl example.
- All parameters must include type information.
- Response examples must match documented schema.
- Error section required for all endpoints with non-trivial validation.
