# Description Style Reference

## Table of contents
1. [Description anatomy](#description-anatomy)
2. [Trigger condition patterns](#trigger-condition-patterns)
3. [Constraint documentation](#constraint-documentation)
4. [Side effect warnings](#side-effect-warnings)
5. [Common mistakes](#common-mistakes)

---

## Description anatomy

Every tool description should have three components:

```
<When to use> + <What it does> + <Key constraint or warning>
```

### Component 1: When to use (trigger condition)
Tells the LLM when this tool is the right choice.

| Pattern | Example |
|---------|---------|
| "Use when..." | "Use when the user asks to search files by content." |
| "Use to..." | "Use to read file contents from the workspace." |
| "Call this when..." | "Call this when you need to execute a shell command." |

### Component 2: What it does (core function)
Explains the tool's primary action in one sentence.

| Good | Bad |
|------|-----|
| "Creates a new file at the specified path." | "Handles file operations." |
| "Executes a SQL query and returns results." | "Database tool." |
| "Sends an HTTP request to an external URL." | "Makes API calls." |

### Component 3: Key constraint or warning
Highlights the most important limitation or side effect.

| Type | Example |
|------|---------|
| Side effect | "WARNING: This modifies files on disk." |
| Limitation | "Only returns first 100 results." |
| Requirement | "Requires absolute file paths." |
| Scope | "Searches only the current workspace." |

---

## Trigger condition patterns

### Explicit user request
```
"Use when the user asks to [action]."
```
Example: "Use when the user asks to search for text in files."

### Implicit need
```
"Use when you need to [capability] to complete the task."
```
Example: "Use when you need to read a file's contents to understand the code."

### Situational trigger
```
"Use when [condition is true]."
```
Example: "Use when the user mentions a URL and wants to see its contents."

### Negative trigger (when NOT to use)
```
"Use for [scope]. Do not use for [out of scope]."
```
Example: "Use for reading text files. Do not use for binary files—use read_binary instead."

---

## Constraint documentation

### Format requirements
```
"Requires [format]. Example: [example]"
```
- "Requires absolute file path. Example: '/workspace/src/main.ts'"
- "Requires ISO 8601 date format. Example: '2024-01-15'"

### Value ranges
```
"[Parameter] must be between [min] and [max]."
```
- "Results limited to 1-100 items per request."
- "Timeout must be between 1 and 60 seconds."

### Mutually exclusive options
```
"Provide [A] or [B], not both."
```
- "Provide either textQuery for literal search or semanticQuery for meaning-based search, not both."

### Dependencies
```
"[A] is required when [B] is set."
```
- "Body is required when method is POST, PUT, or PATCH."

---

## Side effect warnings

### File system modifications
```
"WARNING: This [creates/modifies/deletes] files."
```
- "WARNING: This creates files on disk. Existing files at the same path will be overwritten."
- "WARNING: This deletes files permanently. Cannot be undone."

### Network requests
```
"WARNING: This makes real network requests to [target]."
```
- "WARNING: This makes real HTTP requests. POST/PUT/DELETE operations may modify external systems."

### State changes
```
"WARNING: This modifies [system state]."
```
- "WARNING: This modifies database records. Changes are immediate and permanent."
- "WARNING: This sends notifications to users."

### Irreversible actions
```
"WARNING: This action cannot be undone."
```
- "WARNING: Deletion is permanent. Confirm with user before calling."

---

## Common mistakes

### ❌ Too vague
```
"A tool for handling files."
```

### ✅ Specific trigger and function
```
"Use when the user wants to read a file. Returns the file content as a string. Requires an absolute path."
```

---

### ❌ Only describes what, not when
```
"Searches the codebase for matching text."
```

### ✅ Includes trigger condition
```
"Use when the user wants to find specific text or patterns in code. Searches the codebase and returns matching file paths with line numbers."
```

---

### ❌ Missing constraints
```
"Executes a command in the terminal."
```

### ✅ Constraints documented
```
"Use to run shell commands. Executes in the workspace root directory. Commands timeout after 30 seconds. Long-running commands should use background mode."
```

---

### ❌ Undocumented side effects
```
"Updates the configuration."
```

### ✅ Side effects explicit
```
"Updates the configuration file. WARNING: This modifies the config file on disk. Changes take effect immediately and persist across sessions."
```

---

### ❌ Jargon without explanation
```
"Performs CRUD operations on resources."
```

### ✅ Plain language
```
"Use to create, read, update, or delete items in the database. Specify the operation type and item data."
```
