# Templates

## Standard error message structure

```
{command}: error: {what happened}
{why this happened or what was expected}

{how to fix}

For more information, run: {command} --help
```

## Error message by category

### Input validation error
```
{command}: error: invalid value for --{flag}: '{value}'
Expected: {constraint description}

Try: {command} --{flag} {valid_example}
```

### Missing required argument
```
{command}: error: missing required argument: {ARG}

Usage: {command} [OPTIONS] {ARG}
Run '{command} --help' for more information.
```

### File not found
```
{command}: error: file not found: {path}
The specified file does not exist or is not accessible.

Check:
  - The file path is correct
  - You have read permissions
  - The file has not been moved or deleted
```

### Authentication error
```
{command}: error: authentication failed
{specific reason: expired, invalid, missing}

To authenticate:
  {command} login
  
Or set credentials:
  export {CREDENTIAL_VAR}=your-token
```

### Network error
```
{command}: error: could not connect to {host}
{specific error: timeout, refused, DNS failure}

Check:
  - Your network connection
  - The server address is correct: {url}
  - Any proxy settings are configured correctly

Retry with: {command} {original_args} --retry
```

### Permission denied
```
{command}: error: permission denied: {resource}
You don't have access to perform this operation.

Required permission: {permission_name}
Your current role: {current_role}

Contact your administrator to request access.
```

### Resource conflict
```
{command}: error: {resource_type} already exists: {name}

To update the existing {resource_type}:
  {command} update {name} {args}

To replace it:
  {command} {action} --force {name} {args}
```

### Rate limit error
```
{command}: error: rate limit exceeded
You have made too many requests. Limit: {limit} per {period}.

Retry after: {retry_after}

To avoid rate limits:
  - Use --batch for bulk operations
  - Add delays between requests in scripts
```

### Internal error
```
{command}: error: internal error (code: {error_code})
An unexpected error occurred during {operation}.

Please report this issue:
  {issue_url}

Include this diagnostic information:
  Version: {version}
  OS: {os}
  Command: {full_command}
  Trace ID: {trace_id}
```

## Verbose error format (with --verbose)
```
{command}: error: {what happened}

Details:
  Operation: {operation_name}
  Input: {relevant_input}
  Expected: {expected_state}
  Actual: {actual_state}

Context:
  File: {file_path}
  Line: {line_number} (if applicable)
  
Stack trace:
  {stack_trace}

{how to fix}
```

## Machine-readable error format (with --output json)
```json
{
  "error": {
    "code": "{error_code}",
    "message": "{short message}",
    "details": "{extended explanation}",
    "recoverable": true|false,
    "suggestion": "{how to fix}",
    "documentation": "{help_url}"
  }
}
```

## Exit code documentation template
```
EXIT CODES
    0     Success
    1     General error (unspecified)
    2     Invalid usage or arguments
    3     Authentication or authorization failed
    4     Resource not found
    5     Resource conflict (already exists)
    6     Network or connectivity error
    7     Rate limit or quota exceeded
    64    Command line usage error (BSD convention)
    65    Data format error
    66    Cannot open input
    67    Addressee unknown
    68    Host name unknown
    69    Service unavailable
    70    Internal software error
    71    System error
    73    Can't create output file
    74    Input/output error
    75    Temporary failure, retry
    77    Permission denied
    126   Command found but not executable
    127   Command not found
    130   Script terminated by Ctrl+C
```
