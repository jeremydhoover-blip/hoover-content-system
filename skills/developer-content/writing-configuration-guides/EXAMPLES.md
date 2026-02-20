# Examples

## Example 1: API client configuration

Input:
- Product: REST API client library
- Config methods: JSON file, environment variables
- Parameters: base URL, API key, timeout, retry count, debug mode

Output:
```md
# Configuration Reference

## Quick start

Minimal configuration to get started:

```json
{
  "baseUrl": "https://api.example.com/v1",
  "apiKey": "${API_KEY}"
}
```

## Configuration methods

This client accepts configuration via:
- [x] Configuration file (`client.config.json`)
- [x] Environment variables
- [ ] CLI flags
- [x] Programmatic API

Priority order (highest to lowest): Programmatic API > Environment variables > Config file

---

## Required parameters

### `baseUrl`
- **Type**: string
- **Format**: Valid HTTPS URL
- **Description**: Base URL for all API requests
- **Example**: `"https://api.example.com/v1"`

### `apiKey`
- **Type**: string
- **Format**: 32-character alphanumeric
- **Description**: Authentication key for API access
- **Example**: See [Security-sensitive parameters](#security-sensitive-parameters)

---

## Optional parameters

### `timeout`
- **Type**: number
- **Default**: `30`
- **Description**: Request timeout in seconds
- **Constraints**: 1-300
- **Example**: `60`

### `retryCount`
- **Type**: number
- **Default**: `3`
- **Description**: Number of retry attempts for failed requests
- **Constraints**: 0-10
- **Example**: `5`

### `debug`
- **Type**: boolean
- **Default**: `false`
- **Description**: Enable verbose logging for troubleshooting
- **Example**: `true`

---

## Environment variables

| Variable | Maps to | Example |
|----------|---------|---------|
| `CLIENT_BASE_URL` | `baseUrl` | `https://api.example.com/v1` |
| `CLIENT_API_KEY` | `apiKey` | (use secret manager) |
| `CLIENT_TIMEOUT` | `timeout` | `60` |
| `CLIENT_RETRY_COUNT` | `retryCount` | `5` |
| `CLIENT_DEBUG` | `debug` | `true` |

---

## Security-sensitive parameters

> ⚠️ These parameters contain secrets. Never commit to version control.

### `apiKey`
- **Type**: string
- **Description**: API authentication credential
- **Secure handling**: Set via `CLIENT_API_KEY` environment variable or inject from secret manager at runtime. Never store in config files committed to source control.

---

## Full configuration example

```json
{
  "baseUrl": "https://api.example.com/v1",
  "apiKey": "${CLIENT_API_KEY}",
  "timeout": 60,
  "retryCount": 5,
  "debug": false
}
```
```

---

## Example 2: Database connection configuration (multiple environments)

Input:
- Product: Database ORM
- Config methods: YAML file with environment overrides
- Environments: development, staging, production

Output:
```md
# Database Configuration

## Quick start

```yaml
database:
  host: localhost
  port: 5432
  name: myapp_dev
  user: dev_user
```

## Configuration methods

Priority order: Environment variables > YAML config > Defaults

---

## Required parameters

### `database.host`
- **Type**: string
- **Format**: Hostname or IP address
- **Description**: Database server hostname
- **Example**: `"db.internal.example.com"`

### `database.name`
- **Type**: string
- **Description**: Database name to connect to
- **Example**: `"myapp_production"`

---

## Optional parameters

### `database.port`
- **Type**: number
- **Default**: `5432`
- **Description**: Database server port
- **Constraints**: 1-65535
- **Example**: `5432`

### `database.pool.min`
- **Type**: number
- **Default**: `2`
- **Description**: Minimum connections in pool
- **Constraints**: 1-100
- **Example**: `5`

### `database.pool.max`
- **Type**: number
- **Default**: `10`
- **Description**: Maximum connections in pool
- **Constraints**: 1-500
- **Example**: `50`

### `database.ssl`
- **Type**: boolean
- **Default**: `false` (dev), `true` (production)
- **Description**: Require SSL for connections
- **Example**: `true`

---

## Environment-specific configuration

### Development
```yaml
database:
  host: localhost
  port: 5432
  name: myapp_dev
  user: dev_user
  password: dev_password  # OK for local dev only
  ssl: false
  pool:
    min: 2
    max: 10
```

### Production
```yaml
database:
  host: ${DB_HOST}
  port: 5432
  name: myapp_production
  user: ${DB_USER}
  password: ${DB_PASSWORD}  # Injected from secret manager
  ssl: true
  pool:
    min: 10
    max: 100
```

---

## Security-sensitive parameters

> ⚠️ Never commit production credentials to version control.

### `database.password`
- **Type**: string
- **Secure handling**: Use `DB_PASSWORD` environment variable. In production, inject from AWS Secrets Manager, HashiCorp Vault, or similar.

---

## Validation

Test your configuration:
```bash
myapp db:check-connection
```
```

---

## Example 3: Edge case — Feature flags with dependencies

Input:
- Product: Feature flag system
- Complexity: Flags have dependencies on other flags
- Risk: Enabling flags in wrong order causes failures

Output:
```md
# Feature Flags

## Flag reference

### `new_dashboard`
- **Type**: boolean
- **Default**: `false`
- **Stage**: beta
- **Description**: Enables redesigned dashboard UI
- **Dependencies**: None

### `dashboard_analytics`
- **Type**: boolean
- **Default**: `false`
- **Stage**: experimental
- **Description**: Adds analytics widgets to dashboard
- **Dependencies**: Requires `new_dashboard: true`

> ⚠️ Enabling `dashboard_analytics` without `new_dashboard` will cause render errors.

### `real_time_analytics`
- **Type**: boolean
- **Default**: `false`
- **Stage**: experimental
- **Description**: Streams live data to analytics widgets
- **Dependencies**: Requires `dashboard_analytics: true` AND `websocket_support: true`

---

## Dependency graph

```
new_dashboard
└── dashboard_analytics
    └── real_time_analytics (also requires websocket_support)
```

---

## Safe enablement order

1. Enable `new_dashboard`
2. Verify dashboard loads correctly
3. Enable `dashboard_analytics`
4. Verify widgets render
5. Enable `websocket_support` (separate system)
6. Enable `real_time_analytics`

---

## Rollback procedure

Disable in reverse order:
1. `real_time_analytics: false`
2. `dashboard_analytics: false`
3. `new_dashboard: false`

---

## Configuration example

```yaml
features:
  new_dashboard: true
  dashboard_analytics: true
  websocket_support: true
  real_time_analytics: false  # Enable after stability confirmed
```
```
