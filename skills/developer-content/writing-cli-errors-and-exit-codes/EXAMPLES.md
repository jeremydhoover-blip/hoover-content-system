# Examples

## Example 1: File operation errors

**Input:**
- Command: `configctl validate`
- Operation: Validate configuration file
- Error types: file not found, parse error, schema violation

**Output:**

### File not found
```
configctl: error: file not found: /etc/myapp/config.yaml
The specified configuration file does not exist.

Check:
  - The file path is correct
  - The file has not been moved or deleted
  - You have read permissions on the directory

To use the default config:
  configctl validate --default
```
Exit code: `4` (resource not found)

### Parse error
```
configctl: error: invalid YAML syntax in /etc/myapp/config.yaml
Parse error at line 23, column 4: unexpected key

  22 | database:
  23 |    host: localhost
       ^--- expected indentation of 2 spaces, found 3

Fix the indentation and run:
  configctl validate /etc/myapp/config.yaml
```
Exit code: `65` (data format error)

### Schema violation
```
configctl: error: configuration validation failed: /etc/myapp/config.yaml
Found 2 errors:

  1. database.port: expected integer, got string "5432"
     Fix: Remove quotes around the port number

  2. database.ssl: required field missing
     Fix: Add 'ssl: true' or 'ssl: false' under database section

After fixing, validate again:
  configctl validate /etc/myapp/config.yaml
```
Exit code: `65` (data format error)

---

## Example 2: Authentication and authorization errors

**Input:**
- Command: `cloud-cli deploy`
- Context: Cloud deployment requiring authentication
- Error types: not logged in, token expired, insufficient permissions

**Output:**

### Not authenticated
```
cloud-cli: error: not authenticated
No credentials found. You must log in before deploying.

To authenticate:
  cloud-cli login

Or set credentials via environment:
  export CLOUD_TOKEN=your-api-token
```
Exit code: `3` (authentication failed)

### Token expired
```
cloud-cli: error: authentication token expired
Your session token expired at 2024-01-15 10:30:00 UTC.

To refresh your session:
  cloud-cli login --refresh

Or log in again:
  cloud-cli login
```
Exit code: `3` (authentication failed)

### Insufficient permissions
```
cloud-cli: error: permission denied for project 'production'
You don't have the required role to deploy to this project.

Required role: deployer or admin
Your role: viewer

To request access:
  1. Contact your project administrator
  2. Or request access at: https://console.cloud.example/access-request

To deploy to a project you have access to:
  cloud-cli deploy --project staging
```
Exit code: `77` (permission denied)

---

## Example 3: Edge case—network errors with retry guidance

**Input:**
- Command: `sync-tool push`
- Context: File sync tool with unreliable network
- Challenge: Different network errors need different retry strategies

**Output:**

### Connection refused
```
sync-tool: error: connection refused by sync.example.com:443
The server is not accepting connections.

Possible causes:
  - The server is down for maintenance
  - The port is blocked by a firewall
  - The address is incorrect

Check server status: https://status.example.com

If the address is wrong, update your config:
  sync-tool config set server https://correct-address.example.com
```
Exit code: `6` (network error)

### DNS resolution failed
```
sync-tool: error: could not resolve host: sync.example.com
DNS lookup failed for the server address.

Check:
  - Your internet connection
  - The server address is spelled correctly
  - Your DNS settings are configured

To use an IP address directly:
  sync-tool push --server 203.0.113.50
```
Exit code: `68` (host name unknown)

### Connection timeout
```
sync-tool: error: connection timed out after 30s
The server did not respond in time.

This may be temporary. Retry options:

  Retry immediately:
    sync-tool push --retry 3

  Retry with longer timeout:
    sync-tool push --timeout 120

  Retry with exponential backoff (for scripts):
    sync-tool push --retry 5 --retry-delay exponential
```
Exit code: `75` (temporary failure, retry)

### SSL certificate error
```
sync-tool: error: SSL certificate verification failed
The server's certificate could not be verified.

Certificate issue: expired on 2024-01-10

This is a security risk. Do NOT proceed unless you understand the implications.

If this is expected (e.g., self-signed cert in development):
  sync-tool push --insecure

To specify a custom CA bundle:
  sync-tool push --ca-bundle /path/to/ca-certificates.crt
```
Exit code: `6` (network error)

---

## Example 4: Machine-readable error output

**Input:**
- Command: `api-client request`
- Context: CLI used in CI/CD pipelines
- Format: JSON output for script parsing

**Output:**

### Standard error (human-readable, stderr)
```
api-client: error: rate limit exceeded
You have made too many requests. Limit: 100 per minute.

Retry after: 45 seconds
```

### JSON error (with --output json, stdout)
```json
{
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Rate limit exceeded",
    "details": "You have made too many requests. Limit: 100 requests per minute.",
    "recoverable": true,
    "retry_after_seconds": 45,
    "suggestion": "Wait 45 seconds before retrying, or use --batch for bulk operations",
    "documentation": "https://docs.example.com/api/rate-limits"
  }
}
```
Exit code: `7` (rate limit exceeded)

### Script usage example
```bash
#!/bin/bash
output=$(api-client request --output json 2>&1)
exit_code=$?

if [ $exit_code -eq 7 ]; then
  retry_after=$(echo "$output" | jq -r '.error.retry_after_seconds')
  echo "Rate limited. Waiting ${retry_after}s..."
  sleep "$retry_after"
  api-client request --output json
fi
```
