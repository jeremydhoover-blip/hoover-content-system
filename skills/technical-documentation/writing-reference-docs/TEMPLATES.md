# Templates

## API endpoint reference

```md
# [Endpoint name]

[One-sentence description of what this endpoint does.]

## Endpoint

`[METHOD] /path/to/endpoint`

## Authentication

[Required authentication method.]

## Parameters

### Path parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | [Description] |

### Query parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `limit` | integer | `20` | [Description]. Valid range: 1-100. |
| `offset` | integer | `0` | [Description] |

### Request body

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | Yes | [Description]. Max length: 255. |
| `options` | object | No | [Description]. See [Options object](#options-object). |

## Response

### Success response (200)

```json
{
  "id": "abc123",
  "name": "Example",
  "created_at": "2024-01-15T10:30:00Z"
}
```

### Response fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | [Description] |
| `created_at` | string (ISO 8601) | [Description] |

## Errors

| Status | Code | Description |
|--------|------|-------------|
| 400 | `invalid_parameter` | [When this occurs] |
| 404 | `not_found` | [When this occurs] |

## Example

```bash
curl -X [METHOD] \
  https://api.example.com/path \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"name": "Example"}'
```

## Related

- [Related endpoint 1]
- [Related endpoint 2]
```

---

## Configuration reference

```md
# [Configuration file/option name]

[One-sentence description of this configuration.]

## Location

`[path/to/config.file]` or environment variable `[VAR_NAME]`

## Format

[File format: JSON, YAML, TOML, etc.]

## Options

### `option_name`

| Property | Value |
|----------|-------|
| Type | string |
| Default | `"default_value"` |
| Required | No |
| Environment variable | `OPTION_NAME` |

[Description of what this option controls.]

**Valid values:**
- `value1` — [Effect]
- `value2` — [Effect]

**Example:**
```yaml
option_name: value1
```

### `nested.option`

| Property | Value |
|----------|-------|
| Type | integer |
| Default | `100` |
| Valid range | 1-1000 |

[Description.]

## Complete example

```yaml
option_name: value1
nested:
  option: 500
```

## Related

- [Related configuration]
- [Related how-to guide]
```

---

## Function/method reference

```md
# `functionName()`

[One-sentence description.]

## Signature

```typescript
functionName(param1: Type1, param2?: Type2): ReturnType
```

## Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `param1` | `Type1` | Yes | — | [Description] |
| `param2` | `Type2` | No | `defaultValue` | [Description] |

## Returns

`ReturnType` — [Description of return value.]

Returns `null` when [condition].

## Throws

| Error | Condition |
|-------|-----------|
| `ErrorType1` | [When this is thrown] |
| `ErrorType2` | [When this is thrown] |

## Example

```typescript
const result = functionName("value", { option: true });
```

## Related

- [`relatedFunction()`](./related-function.md)
```

---

## Variation rules
- All parameters must include type information.
- All optional parameters must show default values.
- Tables must use consistent column order within document.
- Examples must be minimal—demonstrate usage, not solve problems.
- Cross-references must use relative links.
