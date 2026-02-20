# Examples

## Example 1: File reading tool

Input:
- Function: Read contents of a file
- Parameters: file path, optional line range
- Returns: File content as string

Output:
```json
{
  "name": "read_file",
  "description": "Use when you need to examine file contents. Reads and returns the content of a file at the specified path. Use line range parameters for large files to avoid token limits. Returns error if file does not exist.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "path": {
        "type": "string",
        "description": "Absolute path to the file to read. Example: '/workspace/src/index.ts'"
      },
      "startLine": {
        "type": "integer",
        "description": "First line to read (1-indexed). Omit to start from beginning. Example: 1",
        "minimum": 1
      },
      "endLine": {
        "type": "integer",
        "description": "Last line to read (1-indexed, inclusive). Omit to read to end. Example: 100",
        "minimum": 1
      }
    },
    "required": ["path"]
  }
}
```

---

## Example 2: Database query tool

Input:
- Function: Execute read-only SQL queries
- Parameters: query string, optional limit, database name
- Returns: Query results as array of objects
- Constraints: Read-only, timeout after 30 seconds

Output:
```json
{
  "name": "query_database",
  "description": "Use when the user needs data from the database. Executes read-only SQL SELECT queries. Cannot modify data (INSERT, UPDATE, DELETE are rejected). Queries timeout after 30 seconds. For large result sets, use LIMIT clause.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string",
        "description": "SQL SELECT query to execute. Must be read-only. Example: 'SELECT id, name FROM users WHERE active = true LIMIT 10'"
      },
      "database": {
        "type": "string",
        "enum": ["production", "analytics", "staging"],
        "description": "Target database. 'production': live user data. 'analytics': aggregated metrics. 'staging': test data. Default: production."
      },
      "timeout": {
        "type": "integer",
        "description": "Query timeout in seconds. Range: 1-30. Default: 30. Example: 10",
        "minimum": 1,
        "maximum": 30
      }
    },
    "required": ["query"]
  }
}
```

---

## Example 3: API integration tool

Input:
- Function: Send HTTP requests to external APIs
- Parameters: URL, method, headers, body
- Side effects: Makes network request, may modify external state
- Returns: Response status, headers, body

Output:
```json
{
  "name": "http_request",
  "description": "Use when the user needs to call an external API. Sends HTTP requests to specified URLs. WARNING: This tool makes real network requests—POST/PUT/DELETE operations may modify external systems. Verify URL and payload before use.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "url": {
        "type": "string",
        "description": "Full URL to request. Must be HTTPS for non-localhost. Example: 'https://api.example.com/v1/users'",
        "pattern": "^https?://"
      },
      "method": {
        "type": "string",
        "enum": ["GET", "POST", "PUT", "PATCH", "DELETE", "HEAD"],
        "description": "HTTP method. GET: read data. POST: create. PUT/PATCH: update. DELETE: remove. HEAD: check existence. Default: GET."
      },
      "headers": {
        "type": "object",
        "additionalProperties": {
          "type": "string"
        },
        "description": "HTTP headers as key-value pairs. Example: {\"Authorization\": \"Bearer token123\", \"Content-Type\": \"application/json\"}"
      },
      "body": {
        "type": "string",
        "description": "Request body for POST/PUT/PATCH. Should match Content-Type header. Omit for GET/DELETE/HEAD."
      },
      "timeout": {
        "type": "integer",
        "description": "Request timeout in seconds. Range: 1-60. Default: 30.",
        "minimum": 1,
        "maximum": 60
      }
    },
    "required": ["url"]
  }
}
```

---

## Example 4: Edge case — Tool with mutually exclusive parameters

Input:
- Function: Search for content
- Complexity: Can search by text or by semantic similarity, but not both

Output:
```json
{
  "name": "search_content",
  "description": "Use when the user wants to find content in the knowledge base. Supports two modes: text search (exact/regex match) OR semantic search (meaning-based). Provide either 'textQuery' or 'semanticQuery', not both.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "textQuery": {
        "type": "string",
        "description": "Literal text or regex pattern to find exact matches. Use this for known strings, code, or identifiers. Example: 'function handleError'. Cannot be used with semanticQuery."
      },
      "semanticQuery": {
        "type": "string",
        "description": "Natural language description of what you're looking for. Use this when you don't know exact wording. Example: 'code that handles authentication failures'. Cannot be used with textQuery."
      },
      "scope": {
        "type": "string",
        "enum": ["all", "code", "docs", "comments"],
        "description": "Where to search. 'all': everything. 'code': source files only. 'docs': markdown/text. 'comments': inline comments. Default: all."
      },
      "maxResults": {
        "type": "integer",
        "description": "Maximum results to return. Range: 1-100. Default: 20.",
        "minimum": 1,
        "maximum": 100
      }
    },
    "required": []
  }
}
```

**Note**: The description explicitly states the mutual exclusivity constraint since JSON Schema oneOf can be complex for LLMs to interpret.

---

## Example 5: Edge case — Tool with no parameters

Input:
- Function: Get current system status
- Parameters: None
- Returns: System health information

Output:
```json
{
  "name": "get_system_status",
  "description": "Use when the user asks about system health, uptime, or current state. Returns current system status including uptime, resource usage, and service health. No parameters required—always returns current snapshot.",
  "inputSchema": {
    "type": "object",
    "properties": {},
    "required": []
  }
}
```
