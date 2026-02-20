# Code Sample Conventions

## Comment types and usage

| Comment prefix | When to use | Example |
|----------------|-------------|---------|
| `// REQUIRED:` | Parameter or step that cannot be skipped | `// REQUIRED: API key from dashboard` |
| `// OPTIONAL:` | Parameter with default behavior | `// OPTIONAL: Defaults to 'us-east-1'` |
| `// NOTE:` | Context that affects behavior | `// NOTE: This operation is idempotent` |
| `// WARNING:` | Potential issue or destructive behavior | `// WARNING: This deletes all data` |
| `// TODO:` | Placeholder for user customization | `// TODO: Replace with your bucket name` |

## What to comment

### Always comment
- Non-obvious parameter values (e.g., why `2500` instead of `25.00`)
- Environment-specific values that need replacement
- Security-sensitive operations
- Operations with side effects
- Return values that aren't self-explanatory

### Never comment
- Self-explanatory operations: `// Create client` before `client = new Client()`
- Language syntax: `// Import the module` before `import`
- Obvious variable assignments: `// Set name to John` before `name = "John"`

## Sample structure pattern

```
1. Purpose comment (one line)
2. Prerequisites comment (if any beyond SDK installation)
3. Blank line
4. Imports (grouped: standard library, third-party, SDK)
5. Blank line
6. Configuration/setup (with inline comments on non-obvious values)
7. Blank line
8. Main operation (with inline comments on key steps)
9. Blank line
10. Cleanup (if applicable)
11. Blank line
12. Expected output comment
```

## Variable naming

### Placeholder conventions
| Placeholder | Use for |
|-------------|---------|
| `YOUR_API_KEY` | API keys and secrets |
| `your-bucket-name` | Resource names user must provide |
| `user@example.com` | Email addresses |
| `tok_visa` | Test/sandbox tokens |
| `sk_test_xxx` | Test API keys |
| `acct_123` | Account IDs |

### Realistic values
Use realistic but obviously fake values:
- ✅ `"order_12345"` — clearly an example
- ❌ `"test"` — too generic, unclear if placeholder
- ✅ `2500` with comment `// $25.00 in cents`
- ❌ `1` — unclear if example or magic number

## Error handling samples

### Required elements
1. Show specific error types (not generic catch-all only)
2. Show appropriate response for each error type
3. Include at least one recoverable error with retry logic
4. Include at least one user-facing error with friendly message

### Pattern
```
try {
  // Main operation
} catch (SpecificError1) {
  // Handle with recovery action
} catch (SpecificError2) {
  // Handle with user message
} catch (GenericError) {
  // Log and re-throw or return generic message
}
```

## Completeness checklist

Before including a code sample, verify:

- [ ] Runs without modification (except credential placeholders)
- [ ] Includes all required imports
- [ ] Uses realistic variable names
- [ ] Comments explain non-obvious values
- [ ] Error handling is shown or explicitly noted as omitted
- [ ] Expected output is documented
- [ ] Follows target language conventions
