# Breaking Change Types

## Table of contents
- [Breaking change categories](#breaking-change-categories)
- [Impact assessment](#impact-assessment)
- [Communication timeline](#communication-timeline)
- [Migration complexity levels](#migration-complexity-levels)

---

## Breaking change categories

### API changes

| Change type | Example | Severity |
|-------------|---------|----------|
| Endpoint removal | `DELETE /v1/users` removed | High |
| Endpoint rename | `/users` → `/accounts` | Medium |
| Method change | `GET` → `POST` for same endpoint | High |
| Required parameter added | New required field in request | High |
| Response structure change | Field renamed or moved | Medium |
| Response type change | `string` → `object` | High |
| Status code change | `200` → `201` for create | Low |
| Default value change | `limit` default 100 → 20 | Medium |

### Authentication changes

| Change type | Example | Severity |
|-------------|---------|----------|
| Auth method removed | Basic auth → OAuth only | High |
| Token format change | JWT structure changed | High |
| Scope requirements | New required scopes | Medium |
| Header format | `Token` → `Bearer` prefix | Medium |

### Configuration changes

| Change type | Example | Severity |
|-------------|---------|----------|
| File format change | JSON → YAML | Medium |
| File location change | New config path | Medium |
| Key renamed | `db_host` → `database.host` | Medium |
| Key removed | Config option no longer supported | Medium |
| Default value change | Feature default on → off | Low |

### Behavioral changes

| Change type | Example | Severity |
|-------------|---------|----------|
| Error handling | Silent fail → throw exception | High |
| Ordering | Results default sort changed | Medium |
| Timing | Sync → async operation | High |
| Validation | Stricter input validation | Medium |
| Side effects | Additional actions on write | Medium |

---

## Impact assessment

### Severity matrix

| Factor | Low | Medium | High |
|--------|-----|--------|------|
| Users affected | <10% | 10-50% | >50% |
| Migration time | <1 hour | 1-8 hours | >1 day |
| Risk of breakage | Cosmetic | Degraded function | Total failure |
| Rollback difficulty | Easy | Moderate | Complex |

### Assessment questions

1. **Who is affected?**
   - All users or subset?
   - How to identify affected users?

2. **What breaks?**
   - Complete failure or degraded experience?
   - Error message or silent failure?

3. **How hard to fix?**
   - Code change required?
   - Configuration only?
   - No user action needed?

4. **What's the timeline?**
   - Immediate or phased?
   - Grace period available?

---

## Communication timeline

### Standard timeline (non-urgent)

| Week | Action |
|------|--------|
| -12 | Announce deprecation |
| -8 | Add deprecation warnings in product |
| -4 | Direct outreach to high-impact users |
| -2 | Final reminder |
| 0 | Breaking change takes effect |
| +4 | End of support for workarounds |

### Accelerated timeline (security)

| Day | Action |
|-----|--------|
| 0 | Security fix released |
| 0 | Announcement with migration guide |
| +7 | Old behavior disabled |

### Minimum notice periods

| Change severity | Minimum notice |
|-----------------|----------------|
| Low | 2 weeks |
| Medium | 4 weeks |
| High | 8 weeks |
| Critical (security) | Immediate with expedited support |

---

## Migration complexity levels

### Simple (< 1 hour)

**Characteristics:**
- Single code change
- No dependencies
- Clear before/after
- Automated migration available

**Documentation needs:**
- Brief announcement
- Before/after example
- Verification step

### Moderate (1-8 hours)

**Characteristics:**
- Multiple code changes
- Testing required
- May affect multiple systems
- Clear migration path

**Documentation needs:**
- Detailed migration guide
- Step-by-step instructions
- Rollback procedure
- FAQ section

### Complex (> 1 day)

**Characteristics:**
- Architectural changes
- Multiple team coordination
- Data migration involved
- Downtime may be required

**Documentation needs:**
- Comprehensive migration guide
- Migration tooling
- Dedicated support channel
- Migration workshop/webinar
- Extended timeline
- Possible extension policy

---

## Breaking change communication checklist

### Before announcement

- [ ] Change technically documented
- [ ] Migration path validated
- [ ] Timeline approved
- [ ] Support team briefed
- [ ] Migration tooling ready (if needed)

### Announcement includes

- [ ] Specific change description
- [ ] Who is affected (with self-check)
- [ ] Timeline with dates
- [ ] Migration instructions
- [ ] Before/after examples
- [ ] Support resources

### After announcement

- [ ] Monitor support channels
- [ ] Track migration progress
- [ ] Send reminders before deadline
- [ ] Document common issues
- [ ] Post-mortem after completion
