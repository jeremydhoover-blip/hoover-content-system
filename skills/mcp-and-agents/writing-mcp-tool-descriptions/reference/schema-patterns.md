# Schema Patterns Reference

## Table of contents
1. [JSON Schema basics for MCP](#json-schema-basics-for-mcp)
2. [Type patterns](#type-patterns)
3. [Constraint patterns](#constraint-patterns)
4. [Complex parameter patterns](#complex-parameter-patterns)
5. [Anti-patterns to avoid](#anti-patterns-to-avoid)

---

## JSON Schema basics for MCP

MCP tool schemas use JSON Schema for input validation. LLMs read these schemas to understand how to invoke tools correctly.

### Minimum viable schema
```json
{
  "type": "object",
  "properties": {},
  "required": []
}
```

### Standard schema structure
```json
{
  "type": "object",
  "properties": {
    "<param_name>": {
      "type": "<type>",
      "description": "<description with example>"
    }
  },
  "required": ["<required_params>"]
}
```

---

## Type patterns

### String
```json
{
  "type": "string",
  "description": "User's email address. Format: valid email. Example: 'user@example.com'"
}
```

With constraints:
```json
{
  "type": "string",
  "minLength": 1,
  "maxLength": 500,
  "pattern": "^[a-z0-9-]+$"
}
```

### Number/Integer
```json
{
  "type": "integer",
  "description": "Page number for pagination. Range: 1-1000. Example: 1",
  "minimum": 1,
  "maximum": 1000
}
```

```json
{
  "type": "number",
  "description": "Confidence threshold. Range: 0.0-1.0. Example: 0.8",
  "minimum": 0,
  "maximum": 1
}
```

### Boolean
```json
{
  "type": "boolean",
  "description": "If true, include archived items. Default: false."
}
```

### Enum (fixed choices)
```json
{
  "type": "string",
  "enum": ["low", "medium", "high"],
  "description": "Priority level. 'low': background task. 'medium': normal priority. 'high': urgent, process first."
}
```

### Array
```json
{
  "type": "array",
  "items": {
    "type": "string"
  },
  "description": "List of file paths to process. Example: ['/path/a.txt', '/path/b.txt']",
  "minItems": 1,
  "maxItems": 100
}
```

### Object
```json
{
  "type": "object",
  "properties": {
    "key": {"type": "string"},
    "value": {"type": "string"}
  },
  "required": ["key", "value"],
  "description": "Key-value pair to set. Example: {\"key\": \"theme\", \"value\": \"dark\"}"
}
```

---

## Constraint patterns

### Required vs optional

Required parameters:
```json
{
  "required": ["path", "content"]
}
```

Optional with default (document in description):
```json
{
  "encoding": {
    "type": "string",
    "description": "File encoding. Default: 'utf-8'. Options: utf-8, ascii, base64."
  }
}
```

### Value ranges
```json
{
  "timeout": {
    "type": "integer",
    "minimum": 1,
    "maximum": 60,
    "description": "Timeout in seconds. Range: 1-60. Default: 30."
  }
}
```

### String patterns
```json
{
  "email": {
    "type": "string",
    "pattern": "^[^@]+@[^@]+\\.[^@]+$",
    "description": "Email address in standard format."
  }
}
```

### String formats
```json
{
  "date": {
    "type": "string",
    "format": "date",
    "description": "Date in ISO 8601 format. Example: '2024-01-15'"
  }
}
```

---

## Complex parameter patterns

### Array of objects
```json
{
  "items": {
    "type": "array",
    "items": {
      "type": "object",
      "properties": {
        "id": {"type": "string"},
        "quantity": {"type": "integer", "minimum": 1}
      },
      "required": ["id", "quantity"]
    },
    "description": "List of items. Example: [{\"id\": \"SKU123\", \"quantity\": 2}]"
  }
}
```

### Nested objects
```json
{
  "config": {
    "type": "object",
    "properties": {
      "output": {
        "type": "object",
        "properties": {
          "format": {"type": "string", "enum": ["json", "csv"]},
          "path": {"type": "string"}
        },
        "required": ["format"]
      }
    },
    "description": "Configuration object. Example: {\"output\": {\"format\": \"json\", \"path\": \"/tmp/out\"}}"
  }
}
```

### Dynamic keys (additionalProperties)
```json
{
  "metadata": {
    "type": "object",
    "additionalProperties": {
      "type": "string"
    },
    "description": "Arbitrary key-value metadata. Example: {\"author\": \"Jane\", \"version\": \"1.0\"}"
  }
}
```

---

## Anti-patterns to avoid

### ❌ Vague parameter names
```json
{
  "data": {"type": "string"},
  "input": {"type": "object"},
  "value": {"type": "any"}
}
```

### ✅ Specific parameter names
```json
{
  "searchQuery": {"type": "string"},
  "fileMetadata": {"type": "object"},
  "temperatureCelsius": {"type": "number"}
}
```

### ❌ Missing descriptions
```json
{
  "limit": {"type": "integer"}
}
```

### ✅ Complete descriptions
```json
{
  "limit": {
    "type": "integer",
    "description": "Maximum results to return. Range: 1-100. Default: 20.",
    "minimum": 1,
    "maximum": 100
  }
}
```

### ❌ Undocumented enum values
```json
{
  "mode": {
    "type": "string",
    "enum": ["a", "b", "c"]
  }
}
```

### ✅ Explained enum values
```json
{
  "mode": {
    "type": "string",
    "enum": ["fast", "balanced", "accurate"],
    "description": "'fast': quick but may miss results. 'balanced': default, good for most cases. 'accurate': thorough but slower."
  }
}
```

### ❌ Implicit dependencies
```json
{
  "query": {"type": "string"},
  "isRegex": {"type": "boolean"}
}
```
(What happens to query interpretation when isRegex changes?)

### ✅ Explicit dependencies
```json
{
  "query": {
    "type": "string",
    "description": "Search pattern. Treated as regex if isRegex is true, otherwise literal match."
  },
  "isRegex": {
    "type": "boolean",
    "description": "If true, query is interpreted as regex pattern. Default: false."
  }
}
```
