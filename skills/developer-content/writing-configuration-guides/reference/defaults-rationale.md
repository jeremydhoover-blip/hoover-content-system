# Defaults Rationale Reference

## Table of contents
1. [Why document default rationale](#why-document-default-rationale)
2. [Common default patterns](#common-default-patterns)
3. [Defaults by parameter type](#defaults-by-parameter-type)
4. [Anti-patterns](#anti-patterns)

---

## Why document default rationale

Defaults communicate intent. When developers understand why a default exists, they can:
- Decide whether to change it for their use case
- Avoid unintended consequences
- Trust the default or know when to override

### Good default documentation
```md
### `timeout`
- **Default**: `30`
- **Rationale**: Balances responsiveness with tolerance for slow networks. Increase for high-latency environments; decrease for fast internal networks.
```

### Insufficient default documentation
```md
### `timeout`
- **Default**: `30`
```
(No guidance on when to change)

---

## Common default patterns

### Development-friendly defaults
Optimize for local development, require explicit production config.

| Parameter | Dev default | Why |
|-----------|-------------|-----|
| `debug` | `true` | Verbose logging helps troubleshooting |
| `ssl` | `false` | No cert setup for local |
| `host` | `localhost` | Works without network config |

### Production-safe defaults
Optimize for security and stability.

| Parameter | Prod default | Why |
|-----------|--------------|-----|
| `debug` | `false` | No sensitive data in logs |
| `ssl` | `true` | Encrypted by default |
| `pool_max` | Conservative (10) | Prevent resource exhaustion |

### Fail-safe defaults
When in doubt, choose the safer option.

| Parameter | Safe default | Why |
|-----------|--------------|-----|
| `auto_migrate` | `false` | No accidental schema changes |
| `delete_on_error` | `false` | No data loss |
| `allow_insecure` | `false` | Security first |

---

## Defaults by parameter type

### Timeouts
| Context | Typical default | Rationale |
|---------|-----------------|-----------|
| API request | 30s | Balances UX and network variance |
| Database query | 60s | Complex queries may be legitimate |
| Health check | 5s | Fast failure detection |
| Shutdown grace | 30s | Allow in-flight requests to complete |

### Retry counts
| Context | Typical default | Rationale |
|---------|-----------------|-----------|
| API call | 3 | Handles transient failures |
| Database connect | 5 | Startup race conditions |
| Queue message | 3 | Then dead-letter |

### Pool sizes
| Context | Typical min | Typical max | Rationale |
|---------|-------------|-------------|-----------|
| DB connections | 2 | 10 | Prevents connection churn |
| Thread pool | CPU count | CPU × 2 | Balances parallelism and overhead |
| HTTP client | 5 | 20 | Limits downstream pressure |

### Buffer sizes
| Context | Typical default | Rationale |
|---------|-----------------|-----------|
| Log buffer | 4KB | Balances memory and I/O |
| Read buffer | 8KB | Matches typical page size |
| Batch size | 100 | Balances throughput and latency |

---

## Anti-patterns

### Magic numbers without rationale
```yaml
timeout: 37  # Why 37? No one knows.
```
Fix: Document the reasoning or use a standard value.

### Inherited defaults
```yaml
timeout: 30  # "That's what the old system used"
```
Fix: Validate the default still makes sense.

### Copy-paste defaults
```yaml
# Every service uses these regardless of actual needs
pool_min: 5
pool_max: 50
```
Fix: Size pools based on actual usage patterns.

### Optimistic defaults
```yaml
max_file_size: 10GB  # "Why limit it?"
```
Fix: Set reasonable limits that protect the system.
