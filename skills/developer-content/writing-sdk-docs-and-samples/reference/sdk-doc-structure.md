# SDK Documentation Structure Reference

## Required sections (in order)

| Section | Purpose | Required for |
|---------|---------|--------------|
| Overview | One sentence explaining SDK purpose and service | All SDKs |
| Prerequisites | Runtime, dependencies, credentials | All SDKs |
| Installation | Package manager commands | All SDKs |
| Authentication | Credential setup and initialization | All SDKs |
| Quickstart | Single complete working example | All SDKs |
| Operations | Method-by-method documentation | All SDKs |
| Error handling | Common errors and handling patterns | All SDKs |
| Advanced usage | Patterns beyond basic CRUD | SDKs with pagination, streaming, retries |
| Troubleshooting | Symptom-cause-solution table | All SDKs |
| Migration guide | Version upgrade instructions | Major version releases only |

## Section depth guidelines

### Overview
- Maximum: 2 sentences
- Must answer: "What does this connect to?" and "What can I do with it?"
- Avoid: Feature lists, marketing language

### Prerequisites
- List runtime version with minimum requirement
- List external dependencies (not installed by package manager)
- State credential requirements without detailing how to obtain

### Installation
- Show primary package manager first
- Include version constraint syntax
- If multiple packages required, explain which are optional

### Authentication
- Show most common method first
- Show environment variable method (preferred for production)
- Include inline warning about credential security
- Show how to verify authentication succeeded

### Quickstart
- Must be runnable with only credential substitution
- Should complete in under 30 seconds
- Must include expected output comment
- Should demonstrate the SDK's primary use case

### Operations
- Group by resource type (e.g., Buckets, Blobs, Users)
- Within each group, order: Create, Read, Update, Delete, List
- Every method needs parameter table if >2 parameters
- Every method needs return type documentation

### Error handling
- Table of 3-5 most common errors
- Code sample showing try-catch with specific error types
- Include retry logic sample if SDK supports retries

### Advanced usage
Include sections for any of these if SDK supports them:
- Pagination (cursor-based and offset-based if both supported)
- Streaming (upload and download)
- Batch operations
- Retry configuration
- Connection pooling
- Async/concurrent operations

## Language-specific conventions

### Python
- Use `snake_case` for variables and functions
- Show type hints in samples
- Include `requirements.txt` or `pyproject.toml` format
- Prefer `with` statements for resource management

### JavaScript/TypeScript
- Use `camelCase` for variables and functions
- Show both CommonJS (`require`) and ESM (`import`) if SDK supports
- Include TypeScript types in parameter tables
- Show async/await patterns (not callbacks)

### Java
- Use `camelCase` for methods, `PascalCase` for classes
- Show Maven and Gradle installation
- Include `try-with-resources` for closeable resources
- Document checked exceptions

### Go
- Use `camelCase` for unexported, `PascalCase` for exported
- Show `go get` with version
- Always show error handling (no ignored errors in samples)
- Include context.Context in samples

### C#
- Use `PascalCase` for public members
- Show NuGet installation
- Include `using` statements for disposables
- Show async patterns with `ConfigureAwait(false)` where appropriate
