# Templates

## Default output: MCP tool definition

Use this as the default structure:

```json
{
  "name": "<tool_name>",
  "description": "<When to use>. <What it does>. <Key constraints or requirements>.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "<param_name>": {
        "type": "<type>",
        "description": "<What this parameter controls>. <Constraints>. Example: <example_value>"
      }
    },
    "required": ["<required_param>"]
  }
}
```

## Description formula

Structure tool descriptions as:

```
<Trigger condition>. <Core function>. <Important constraint or note>.
```

Examples:
- "Use when the user asks to search files by content. Performs regex or literal search across the workspace. Returns matching file paths and line numbers."
- "Use to read file contents. Requires an absolute file path. Returns the file content as a string, or an error if file not found."

## Parameter description formula

```
<What it is>. <Constraints or format>. Example: <concrete_value>
```

Examples:
- "The search pattern to match. Supports regex when isRegex is true. Example: 'function\\s+\\w+'"
- "Maximum number of results to return. Range: 1-1000. Default: 100. Example: 50"

## Variant: Tool with complex parameters

```json
{
  "name": "create_file",
  "description": "Use when the user wants to create a new file. Creates a file at the specified path with the given content. Will overwrite existing files. Parent directories are created automatically.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "path": {
        "type": "string",
        "description": "Absolute path where the file should be created. Example: '/workspace/src/utils.js'"
      },
      "content": {
        "type": "string",
        "description": "The content to write to the file. Can be empty string for blank file."
      },
      "encoding": {
        "type": "string",
        "enum": ["utf-8", "ascii", "base64"],
        "description": "File encoding. Default: utf-8. Use base64 for binary content."
      }
    },
    "required": ["path", "content"]
  }
}
```

## Variant: Tool with array/object parameters

```json
{
  "name": "batch_rename",
  "description": "Use when the user wants to rename multiple files at once. Applies rename operations atomically—all succeed or all fail. Use for refactoring or bulk organization.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "operations": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "from": {
              "type": "string",
              "description": "Current file path (absolute)"
            },
            "to": {
              "type": "string",
              "description": "New file path (absolute)"
            }
          },
          "required": ["from", "to"]
        },
        "description": "List of rename operations. Each operation specifies source and destination paths."
      },
      "dryRun": {
        "type": "boolean",
        "description": "If true, validate operations without executing. Default: false."
      }
    },
    "required": ["operations"]
  }
}
```

## Variant: Tool with conditional parameters

```json
{
  "name": "search_code",
  "description": "Use when the user wants to find code in the workspace. Supports literal text or regex search. For simple word searches, use literal mode; for patterns, enable regex.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string",
        "description": "The search pattern. Interpretation depends on isRegex flag."
      },
      "isRegex": {
        "type": "boolean",
        "description": "If true, query is treated as regex. If false, literal match. Default: false."
      },
      "caseSensitive": {
        "type": "boolean",
        "description": "If true, match case exactly. Default: false."
      },
      "includePattern": {
        "type": "string",
        "description": "Glob pattern to filter files. Only files matching this pattern are searched. Example: '**/*.ts'"
      },
      "excludePattern": {
        "type": "string",
        "description": "Glob pattern to exclude files. Example: '**/node_modules/**'"
      }
    },
    "required": ["query"]
  }
}
```
