# CLI Error Taxonomy

## Error categories by source

### 1. User input errors
Errors caused by incorrect command invocation.

| Error type | Characteristics | User action |
|------------|-----------------|-------------|
| Invalid argument | Wrong type, out of range, malformed | Correct the value |
| Missing required argument | Argument not provided | Add the argument |
| Unknown flag | Flag doesn't exist | Check spelling, use --help |
| Mutually exclusive options | Conflicting flags used | Remove one option |
| Too many arguments | Unexpected positional args | Remove extra arguments |

**Message pattern:** State what's wrong, show what's expected, suggest fix.

### 2. Configuration errors
Errors in config files or environment.

| Error type | Characteristics | User action |
|------------|-----------------|-------------|
| Config file not found | Expected file missing | Create or specify path |
| Config parse error | Syntax error in file | Fix syntax at line/column |
| Config validation error | Invalid values in config | Correct values per schema |
| Missing required setting | Required field absent | Add the setting |
| Environment variable missing | Required env var not set | Export the variable |

**Message pattern:** State which config, show error location, explain valid options.

### 3. Authentication/authorization errors
Errors related to identity and permissions.

| Error type | Characteristics | User action |
|------------|-----------------|-------------|
| Not authenticated | No credentials found | Log in |
| Invalid credentials | Credentials rejected | Re-enter or refresh |
| Expired credentials | Token/session expired | Refresh or re-login |
| Insufficient permissions | Authorized but not allowed | Request access |
| Account disabled | Account exists but blocked | Contact admin |

**Message pattern:** State auth state, explain what's needed, show how to authenticate.

### 4. Resource errors
Errors accessing or manipulating resources.

| Error type | Characteristics | User action |
|------------|-----------------|-------------|
| Not found | Resource doesn't exist | Check name, create first |
| Already exists | Conflict on create | Use different name or update |
| Version conflict | Stale data | Refresh and retry |
| Locked | Resource in use | Wait or force unlock |
| Quota exceeded | Limit reached | Delete resources or request increase |

**Message pattern:** State resource and operation, explain conflict, show resolution options.

### 5. Network errors
Errors in remote communication.

| Error type | Characteristics | User action |
|------------|-----------------|-------------|
| Connection refused | Server not accepting | Check server status |
| Connection timeout | No response in time | Retry with longer timeout |
| DNS failure | Can't resolve host | Check address spelling |
| SSL/TLS error | Certificate issue | Verify cert or use --insecure |
| Protocol error | Unexpected response | Check API version compatibility |

**Message pattern:** State connection target, explain failure mode, suggest retry or check.

### 6. Processing errors
Errors during operation execution.

| Error type | Characteristics | User action |
|------------|-----------------|-------------|
| Invalid input data | Data doesn't meet requirements | Fix data format |
| Processing failure | Operation couldn't complete | Check input, retry |
| Timeout | Operation took too long | Increase timeout or simplify |
| Partial failure | Some items failed | Review failures, retry failed |
| Dependency error | Required tool/service missing | Install dependency |

**Message pattern:** State what failed, show progress if partial, explain recovery.

### 7. System errors
Errors from OS or runtime environment.

| Error type | Characteristics | User action |
|------------|-----------------|-------------|
| Permission denied | OS blocked access | Check file/process permissions |
| Disk full | No space for write | Free disk space |
| Memory exhausted | OOM condition | Reduce workload or add memory |
| Process limit | Too many processes | Close other processes |
| File handle limit | Too many open files | Increase ulimit |

**Message pattern:** State system limitation, explain OS context, suggest system fix.

### 8. Internal errors
Errors indicating bugs or unexpected states.

| Error type | Characteristics | User action |
|------------|-----------------|-------------|
| Assertion failed | Invariant violated | Report bug |
| Unhandled exception | Unexpected error path | Report with trace |
| Corrupted state | Data inconsistency | Reset and report |
| Dependency failure | Library error | Check versions, report |

**Message pattern:** Apologize briefly, provide diagnostic info, show how to report.

## Recoverability matrix

| Category | Typically recoverable | Typical exit code |
|----------|----------------------|-------------------|
| User input | Yes | 2 or 64 |
| Configuration | Yes | 78 |
| Authentication | Yes | 3 |
| Authorization | Sometimes | 77 |
| Resource not found | Sometimes | 4 |
| Resource conflict | Yes | 5 |
| Network (transient) | Yes | 75 |
| Network (permanent) | No | 6 or 69 |
| Processing (data) | Yes | 65 |
| Processing (timeout) | Sometimes | 8 |
| System | Depends | 71-74 |
| Internal | No | 70 |

## Severity levels

### Error (stops execution)
- Operation cannot continue
- Must exit with non-zero code
- Requires user intervention

### Warning (execution continues)
- Non-critical issue detected
- Execution continues with degradation
- Should log but not exit

### Info (diagnostic only)
- Helpful context for debugging
- Only shown in verbose mode
- No impact on execution
