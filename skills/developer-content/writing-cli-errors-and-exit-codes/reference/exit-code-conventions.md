# Exit Code Conventions

## Standard ranges

| Range | Category | Description |
|-------|----------|-------------|
| 0 | Success | Operation completed successfully |
| 1 | General error | Unspecified or catch-all error |
| 2-10 | Application errors | Tool-specific error categories |
| 64-78 | BSD sysexits | Standardized meanings (see below) |
| 126-128 | Shell reserved | Command execution issues |
| 130 | Signal | Interrupted by Ctrl+C (128 + SIGINT) |
| 128+N | Signal | Terminated by signal N |

## BSD sysexits.h standard codes

These codes are widely recognized and should be used when applicable:

| Code | Name | Meaning |
|------|------|---------|
| 64 | EX_USAGE | Command line usage error |
| 65 | EX_DATAERR | Data format error (input) |
| 66 | EX_NOINPUT | Cannot open input |
| 67 | EX_NOUSER | Addressee unknown |
| 68 | EX_NOHOST | Host name unknown |
| 69 | EX_UNAVAILABLE | Service unavailable |
| 70 | EX_SOFTWARE | Internal software error |
| 71 | EX_OSERR | System error (OS-level) |
| 72 | EX_OSFILE | Critical OS file missing |
| 73 | EX_CANTCREAT | Can't create output file |
| 74 | EX_IOERR | Input/output error |
| 75 | EX_TEMPFAIL | Temporary failure, retry |
| 76 | EX_PROTOCOL | Remote protocol error |
| 77 | EX_NOPERM | Permission denied |
| 78 | EX_CONFIG | Configuration error |

## Recommended application exit codes (2-10)

For tool-specific errors not covered by sysexits:

| Code | Suggested meaning |
|------|-------------------|
| 2 | Invalid arguments or usage (alternative to 64) |
| 3 | Authentication or authorization failed |
| 4 | Resource not found |
| 5 | Resource conflict (already exists, version mismatch) |
| 6 | Network or connectivity error |
| 7 | Rate limit or quota exceeded |
| 8 | Timeout exceeded |
| 9 | Validation failed |
| 10 | Partial success (some operations failed) |

## Exit code selection guidelines

### Use code 0 only for complete success
- All requested operations completed
- No warnings that affect correctness
- Safe to continue pipeline

### Use code 1 for general/unhandled errors
- Unexpected exceptions
- Errors not fitting other categories
- Legacy compatibility

### Use specific codes for actionable errors
Map exit codes to user actions:

| If user should... | Use code |
|-------------------|----------|
| Fix command syntax | 2 or 64 |
| Fix input data | 65 |
| Log in or refresh credentials | 3 |
| Check resource name/path | 4 |
| Resolve conflict (rename, force, update) | 5 |
| Check network/retry later | 6 or 75 |
| Wait and retry | 7 (rate limit) or 75 (temporary) |
| Contact administrator | 77 |
| Fix configuration file | 78 |
| Report bug | 70 |

## Exit code documentation requirements

Every CLI should document exit codes in:
1. `--help` output (EXIT CODES section)
2. Man page (if applicable)
3. README or documentation site

Minimum documentation format:
```
EXIT CODES
    0     Success
    1     General error
    {n}   {Specific meaning}
```

## Scripting considerations

### Pipeline-safe exit codes
When tool is used in pipelines (`set -e`, `&&`, `||`):
- Non-zero exits stop pipeline execution
- Consider `--ignore-errors` flag for intentional continuation
- Document which errors are recoverable

### Partial success handling
When processing multiple items:
- Exit 0 if all succeeded
- Exit 10 (or custom code) if some failed
- Provide summary of failures
- Consider `--fail-fast` vs. `--continue-on-error` flags

### Signal handling
- Ctrl+C should exit with 130 (128 + 2)
- Clean up resources before exit
- Don't suppress signals in long-running operations
