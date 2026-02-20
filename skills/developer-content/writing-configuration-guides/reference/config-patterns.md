# Configuration Patterns Reference

## Table of contents
1. [Configuration methods](#configuration-methods)
2. [Parameter grouping patterns](#parameter-grouping-patterns)
3. [Environment override patterns](#environment-override-patterns)
4. [Secret management patterns](#secret-management-patterns)

---

## Configuration methods

### File-based configuration

| Format | Best for | Limitations |
|--------|----------|-------------|
| JSON | Programmatic generation, strict schema | No comments, verbose |
| YAML | Human-edited configs, nested structures | Whitespace-sensitive |
| TOML | Simple flat configs, INI replacement | Less common tooling |
| .env | Environment variables only | No nesting, strings only |

### Environment variables

**Naming convention**: `<APP>_<SECTION>_<PARAM>` in SCREAMING_SNAKE_CASE

```bash
MYAPP_DATABASE_HOST=localhost
MYAPP_DATABASE_PORT=5432
MYAPP_CACHE_TTL=3600
```

### Priority order (typical)

1. CLI flags (highest)
2. Environment variables
3. User config file
4. System config file
5. Defaults (lowest)

---

## Parameter grouping patterns

### Group by function
```yaml
database:
  host: localhost
  port: 5432
cache:
  host: localhost
  ttl: 3600
logging:
  level: info
  format: json
```

### Group by lifecycle
```yaml
startup:
  timeout: 30
  retries: 3
runtime:
  max_connections: 100
shutdown:
  grace_period: 10
```

### Group by sensitivity
```yaml
public:
  app_name: "MyApp"
  version: "1.0.0"
private:
  api_key: ${API_KEY}
  db_password: ${DB_PASSWORD}
```

---

## Environment override patterns

### Layered files
```
config/
  default.yaml      # Base defaults
  development.yaml  # Dev overrides
  production.yaml   # Prod overrides
```

Load order: default → environment-specific (merge/override)

### Environment variable override
```yaml
# config.yaml
database:
  host: localhost  # Default
  
# Override at runtime
DATABASE_HOST=prod.db.example.com ./myapp
```

### Profile-based selection
```bash
# Select config profile
MYAPP_PROFILE=production ./myapp

# Loads config/production.yaml
```

---

## Secret management patterns

### Pattern 1: Environment variable reference
```yaml
database:
  password: ${DB_PASSWORD}
```
Resolved at runtime from environment.

### Pattern 2: File-based secrets
```yaml
database:
  password_file: /run/secrets/db_password
```
Application reads file contents.

### Pattern 3: Secret manager integration
```yaml
database:
  password: vault://secret/data/myapp/db#password
```
Application fetches from secret manager.

### Anti-patterns to avoid

| Anti-pattern | Problem | Alternative |
|--------------|---------|-------------|
| Secrets in config files | Committed to VCS | Use env vars or secret manager |
| Secrets in CLI flags | Visible in process list | Use env vars |
| Base64 "encoding" | Not encryption | Use actual encryption or secret manager |
| Shared secrets across envs | Blast radius | Per-environment secrets |
