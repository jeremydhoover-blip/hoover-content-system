# Templates

## Standard release notes

```md
# Release [version] — [date]

[One-sentence summary of this release's theme or highlight.]

## Breaking changes

> **Action required:** These changes may require updates to your code or configuration.

### [Change title]

**What changed:** [Description of the change]

**Impact:** [Who is affected and how]

**Migration:**
1. [Step 1]
2. [Step 2]

**Deadline:** [If deprecation, when old behavior ends]

## New features

### [Feature name]

[One to two sentences describing the feature and its benefit.]

[Optional: brief example or screenshot]

**Learn more:** [Link to documentation]

### [Feature name]

[Description and benefit.]

## Improvements

- **[Area]:** [What improved and why it matters]
- **[Area]:** [What improved and why it matters]

## Bug fixes

- Fixed [issue] that caused [user-observable problem]
- Resolved [issue] where [behavior description]

## Deprecations

### [Deprecated item]

**Deprecated:** [What is being deprecated]
**Replacement:** [What to use instead]
**Removal date:** [When it will be removed]

## Security

### [CVE-YYYY-XXXXX] (if applicable)

**Severity:** [Critical/High/Medium/Low]
**Impact:** [What could happen]
**Fixed in:** This release
**Credit:** [Reporter, if disclosed]

---

**Full changelog:** [Link]
**Upgrade guide:** [Link]
```

---

## Patch release (condensed)

```md
# Release [version] — [date]

Patch release with bug fixes and security updates.

## Bug fixes

- Fixed [issue] that caused [problem] ([#issue-number])
- Fixed [issue] affecting [area] ([#issue-number])

## Security

- Updated [dependency] to address [CVE-ID]

---

**Full changelog:** [Link]
```

---

## API changelog entry

```md
## [version] — [date]

### Breaking

- `[METHOD] /endpoint` — [Change description]. [Migration: link]

### Added

- `[METHOD] /new-endpoint` — [Description]
- New field `field_name` on [resource] response

### Changed

- `[METHOD] /endpoint` — [Change description, backward compatible]

### Deprecated

- `[METHOD] /old-endpoint` — Use `[METHOD] /new-endpoint` instead. Removal: [date]

### Fixed

- `[METHOD] /endpoint` — Fixed [issue description]
```

---

## Internal release notes

```md
# Release [version] — [date]

**Release manager:** [Name]
**Deploy time:** [Time and timezone]

## Summary

[Brief description of release scope and risk level]

## Changes

| Change | Type | Risk | Owner |
|--------|------|------|-------|
| [Description] | Feature | Low | @name |
| [Description] | Fix | Medium | @name |

## Breaking changes

[None / List with migration details]

## Rollback plan

[How to rollback if issues arise]

## Monitoring

Watch for:
- [Metric to monitor]
- [Error pattern to watch]

## Post-release verification

- [ ] [Check 1]
- [ ] [Check 2]
```

---

## Variation rules
- Breaking changes must always appear first when present.
- Every breaking change needs migration instructions.
- Bug fixes describe the problem fixed, not the code changed.
- Features describe user benefit, not implementation.
- Security issues follow responsible disclosure format.
