# Rubric

Pass if all are true:
- Tool name is a verb phrase or action noun (e.g., `search_files`, `create_document`)
- Description explicitly states when to use the tool (trigger condition)
- Description states what the tool does (core function)
- Each parameter has type, description, and example value
- Required parameters are distinguished from optional
- Complex types (arrays, objects) have nested schema definitions
- Constraints (min, max, enum, pattern) are documented where applicable
- Side effects are mentioned if the tool modifies state (files, databases, external services)
- Default values are documented for optional parameters
- Tool has a single, focused purpose (not a multi-function Swiss Army knife)

Fail if any are true:
- Tool name is a generic noun (e.g., `helper`, `data`, `util`)
- Description only says what the tool does, not when to use it
- Parameter has no description or has placeholder like "The X parameter"
- Required parameter not listed in `required` array
- Array or object parameter without items/properties schema
- Tool performs multiple unrelated actions
- Side effects undocumented (e.g., writes to disk, sends network requests)
- Enum values listed without explanation of what each means
