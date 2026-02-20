# Reference Documentation Patterns

## Table of contents
- [Document type selection](#document-type-selection)
- [Parameter table conventions](#parameter-table-conventions)
- [Completeness checklist by type](#completeness-checklist-by-type)
- [Cross-referencing rules](#cross-referencing-rules)

---

## Document type selection

| Component type | Template to use | Key sections |
|----------------|-----------------|--------------|
| REST API endpoint | API endpoint reference | Endpoint, Parameters, Response, Errors |
| GraphQL query/mutation | API endpoint reference (adapted) | Query, Variables, Response, Errors |
| Configuration file | Configuration reference | Location, Format, Options |
| Environment variable | Configuration reference | Variable name, Type, Default |
| Function/method | Function reference | Signature, Parameters, Returns, Throws |
| CLI command | CLI reference | Usage, Options, Arguments, Examples |
| Event/webhook | Event reference | Trigger, Payload, Headers |
| Data type/schema | Type reference | Properties, Constraints, Examples |

---

## Parameter table conventions

### Column order (strict)

**For API/function parameters:**
```
| Parameter | Type | Required | Default | Description |
```

**For configuration options:**
```
| Option | Type | Default | Description |
```

**For response fields:**
```
| Field | Type | Description |
```

### Type notation

| Type | Notation | Example |
|------|----------|---------|
| Primitive | Lowercase | `string`, `integer`, `boolean` |
| Array | Type with brackets | `string[]`, `integer[]` |
| Object | Camel case | `UserOptions`, `RequestConfig` |
| Union | Pipe-separated | `string \| null` |
| Literal | Quoted | `"active"`, `"pending"` |

### Constraint documentation

Always include:

| Constraint type | Format | Example |
|-----------------|--------|---------|
| String length | "Max length: N." | Max length: 255. |
| Number range | "Valid range: N-M." | Valid range: 1-100. |
| Enum values | "Valid values: a, b, c." | Valid values: `asc`, `desc`. |
| Pattern | "Must match pattern: X." | Must match pattern: `^[a-z]+$`. |
| Uniqueness | "Must be unique." | Must be unique. |

---

## Completeness checklist by type

### API endpoint

- [ ] HTTP method and path
- [ ] Authentication requirements
- [ ] All path parameters with types
- [ ] All query parameters with types and defaults
- [ ] All request body fields with types and requirements
- [ ] Success response code and body structure
- [ ] All response fields with types
- [ ] All error codes with conditions
- [ ] Minimal curl example

### Configuration option

- [ ] Option name/path
- [ ] Type
- [ ] Default value (explicit, not "none")
- [ ] Required/optional status
- [ ] Environment variable equivalent (if applicable)
- [ ] Valid values or constraints
- [ ] Behavioral description

### Function/method

- [ ] Full signature with types
- [ ] All parameters with types and defaults
- [ ] Return type and description
- [ ] Exception/error types with conditions
- [ ] Minimal usage example

---

## Cross-referencing rules

### When to link

| Scenario | Action |
|----------|--------|
| Related endpoint/function | Link in "Related" section |
| Complex nested type | Link to type definition |
| Prerequisite concept | Link inline at first mention |
| How-to guide for common tasks | Link in "Related" section |

### Link format

- Same directory: `[Display text](./filename.md)`
- Parent directory: `[Display text](../section/filename.md)`
- External docs: `[Display text](/docs/path/to/page)`

### Do not link

- Basic programming concepts
- Standard library functions
- External specifications (link to official source instead)

---

## Ordering conventions

### Multiple parameters

Order by:
1. Path parameters (URL order)
2. Required parameters (alphabetical)
3. Optional parameters (alphabetical)

### Multiple options

Order by:
1. Required options first
2. Most commonly used
3. Alphabetical for remainder

### Response fields

Order by:
1. Identifier fields (`id`, `uuid`)
2. Core data fields
3. Metadata fields (`created_at`, `updated_at`)
4. Nested objects last
