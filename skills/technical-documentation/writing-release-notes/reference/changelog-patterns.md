# Changelog Patterns

## Table of contents
- [Change categorization](#change-categorization)
- [Audience adaptation](#audience-adaptation)
- [Breaking change documentation](#breaking-change-documentation)
- [Security disclosure format](#security-disclosure-format)
- [Version numbering conventions](#version-numbering-conventions)

---

## Change categorization

### Standard categories (in order)

| Category | Use when | Lead with |
|----------|----------|-----------|
| Breaking | Requires user action to maintain functionality | Impact and migration |
| Security | Addresses vulnerability | Severity and fix |
| Added/New | New functionality | User benefit |
| Changed | Modified existing behavior (backward compatible) | What's different |
| Improved | Better performance, UX, or quality | What got better |
| Fixed | Resolved defect | Problem that was fixed |
| Deprecated | Still works but will be removed | Replacement and timeline |
| Removed | Previously deprecated, now gone | What to use instead |

### Category signals

| Signal in source | Category |
|------------------|----------|
| Requires migration | Breaking |
| CVE or security advisory | Security |
| New endpoint, feature flag | Added |
| Parameter default changed | Changed |
| Performance optimization | Improved |
| Bug fix, issue resolved | Fixed |
| Marked for removal | Deprecated |
| Deleted code | Removed |

---

## Audience adaptation

### Developer audience

Include:
- Technical details (endpoints, parameters, types)
- Code examples for migration
- API version information
- Links to technical documentation

Example tone:
> `POST /users` now requires the `workspace_id` field. Requests without this field return `422 Unprocessable Entity`.

### End user audience

Include:
- Benefit-focused descriptions
- Visual changes (screenshots if applicable)
- Impact on daily workflows
- Link to help articles

Example tone:
> You can now organize your projects into team workspaces. Invite colleagues and collaborate in shared spaces.

### Internal/operations audience

Include:
- Risk assessment
- Rollback procedures
- Monitoring guidance
- Owner and timeline

---

## Breaking change documentation

### Required elements

| Element | Purpose |
|---------|---------|
| What changed | Technical description |
| Impact | Who is affected |
| Migration | How to update |
| Deadline | When old behavior ends |
| Support | Where to get help |

### Migration instruction format

```md
**Migration:**
1. [Identify if you're affected]
2. [Make code/config changes]
3. [Test in non-production]
4. [Deploy before deadline]

**Example:**
```before
// Old approach
```

```after
// New approach
```
```

### Deadline communication

| Deadline type | Format |
|---------------|--------|
| Immediate (patch) | "Effective immediately" |
| Grace period | "Old behavior supported until [date]" |
| Deprecation cycle | "Deprecated in [version], removed in [version]" |

---

## Security disclosure format

### Standard structure

```md
### [CVE-ID or internal ID]

**Severity:** Critical / High / Medium / Low
**CVSS Score:** [if applicable]
**Impact:** [What could happen if exploited]
**Affected versions:** [Version range]
**Fixed in:** [This version]
**Workaround:** [If any, before upgrading]
**Credit:** [Reporter, if publicly disclosed]
```

### Severity definitions

| Level | Criteria |
|-------|----------|
| Critical | Remote code execution, full system compromise |
| High | Data breach, authentication bypass |
| Medium | Information disclosure, limited impact |
| Low | Minor information leak, requires unlikely conditions |

### Timing considerations

- Security fixes may be released with minimal detail initially
- Full disclosure after users have had time to upgrade
- Coordinate with responsible disclosure timelines

---

## Version numbering conventions

### Semantic versioning (SemVer)

```
MAJOR.MINOR.PATCH

MAJOR — Breaking changes
MINOR — New features, backward compatible
PATCH — Bug fixes, backward compatible
```

### Date-based versioning

```
YYYY-MM-DD

Used for APIs with continuous deployment
Each version represents API contract at that date
```

### Choosing version format

| Scenario | Recommended format |
|----------|--------------------|
| Installable software | Semantic versioning |
| API service | Date-based versioning |
| Libraries | Semantic versioning |
| SaaS products | Date or semantic |

### Pre-release identifiers

```
2.0.0-alpha.1 — Early preview, unstable
2.0.0-beta.1 — Feature complete, may have bugs
2.0.0-rc.1 — Release candidate, final testing
2.0.0 — Stable release
```
