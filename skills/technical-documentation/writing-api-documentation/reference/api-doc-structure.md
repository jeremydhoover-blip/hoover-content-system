# API Documentation Structure

## Table of contents
- [Documentation hierarchy](#documentation-hierarchy)
- [Endpoint documentation order](#endpoint-documentation-order)
- [Parameter table standards](#parameter-table-standards)
- [Code example requirements](#code-example-requirements)
- [Cross-referencing patterns](#cross-referencing-patterns)

---

## Documentation hierarchy

```
API Documentation/
├── Overview
│   ├── Introduction
│   ├── Authentication
│   ├── Base URL & Versioning
│   ├── Rate Limits
│   ├── Pagination
│   └── Error Handling
│
├── Resources (by domain)
│   ├── Users
│   │   ├── Create user
│   │   ├── Get user
│   │   ├── List users
│   │   ├── Update user
│   │   └── Delete user
│   ├── Projects
│   │   └── [CRUD endpoints]
│   └── [Additional resources]
│
├── Events/Webhooks
│   ├── Event overview
│   └── Event reference
│
└── Reference
    ├── Error codes
    ├── Rate limits detail
    └── Changelog
```

---

## Endpoint documentation order

Standard sections in order:

| Section | Required | Purpose |
|---------|----------|---------|
| Title | Yes | "[Verb] [resource]" format |
| Description | Yes | One sentence |
| Endpoint | Yes | Method + path |
| Authentication | Yes | Required scopes/permissions |
| Path parameters | If any | URL parameters |
| Query parameters | If any | Filter/pagination |
| Request body | If POST/PUT/PATCH | Input schema |
| Response | Yes | Success response |
| Errors | Yes | Possible error responses |
| Example | Yes | Working curl example |
| Related | Optional | Links to related endpoints |

---

## Parameter table standards

### Column order

**Path/query parameters:**
```
| Parameter | Type | Required/Default | Description |
```

**Request body fields:**
```
| Field | Type | Required | Description |
```

**Response fields:**
```
| Field | Type | Description |
```

### Type notation

| Type | Format | Example value |
|------|--------|---------------|
| String | `string` | `"example"` |
| Integer | `integer` | `42` |
| Number | `number` | `3.14` |
| Boolean | `boolean` | `true` |
| Array | `type[]` | `["a", "b"]` |
| Object | `object` or named type | `{}` |
| Timestamp | `string (ISO 8601)` | `"2024-01-15T10:00:00Z"` |
| Enum | `string` with allowed values | `"active"` |

### Constraint documentation

Include in Description column:

| Constraint | Format |
|------------|--------|
| Max length | "Max: 255 chars." |
| Range | "Range: 1-100." |
| Pattern | "Format: `[pattern]`." |
| Allowed values | "Allowed: `a`, `b`, `c`." |
| Uniqueness | "Must be unique." |

---

## Code example requirements

### Minimum requirements

Every endpoint needs at least one complete, executable example:

1. Full URL (or clear indication that base URL is prepended)
2. HTTP method
3. Required headers (auth, content-type)
4. Request body for POST/PUT/PATCH
5. Expected response

### curl format standard

```bash
curl -X METHOD "https://api.example.com/v1/path" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "field": "value"
  }'
```

### Variable conventions

| Variable | Format | Example |
|----------|--------|---------|
| Auth token | Environment variable | `$TOKEN` |
| Path parameter | Descriptive placeholder | `USER_ID` |
| Request value | Literal example | `"jane@example.com"` |

---

## Cross-referencing patterns

### When to link

| Scenario | Link to |
|----------|---------|
| Related CRUD endpoints | Same resource's other operations |
| Nested object type | Type definition or parent resource |
| Common pattern | Pagination, authentication docs |
| Error handling | Error reference page |
| Setup requirement | Authentication guide |

### Link format

Same section:
```md
[Update user](./update-user.md)
```

Different section:
```md
[Authentication guide](/docs/authentication)
```

Anchor:
```md
[Rate limits](#rate-limits)
```

### Link placement

- **Related section**: Links to related endpoints (end of document)
- **Inline**: First mention of referenced concept
- **Parameter description**: When type is complex object

---

## Versioning documentation

### URL versioning (recommended)

```
Base URL: https://api.example.com/v1
```

### Header versioning

```
Header: X-API-Version: 2024-01-15
```

### Documentation requirements for versioning

- State current version prominently
- Document breaking changes between versions
- Provide migration guides for version upgrades
- Note deprecation timelines for old versions
