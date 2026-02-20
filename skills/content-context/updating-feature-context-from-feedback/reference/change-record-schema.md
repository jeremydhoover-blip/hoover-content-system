# Change Record Schema

## Required fields

Every context update record must include:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| context_pack | string | Yes | Name of the feature context pack |
| previous_version | semver | Yes | Version before changes |
| new_version | semver | Yes | Version after changes |
| update_date | date | Yes | ISO 8601 format (YYYY-MM-DD) |
| update_author | string | Yes | Name or role of person making changes |
| feedback_sources | array | Yes | At least one source required |
| changes | array | Yes | At least one change required |
| changelog_entry | string | Yes | Imperative mood summary |

## Feedback source object

```yaml
feedback_source:
  source_type: enum [user-research, support-ticket, analytics, pm-input, internal-review, social-feedback]
  reference: string # Link, ticket ID, or study reference
  date_received: date # ISO 8601
```

## Change object

```yaml
change:
  id: integer # Sequential within record
  description: string # Short summary (≤10 words)
  affected_section: enum [vocabulary, states, actions, constraints, error-taxonomy, tone-boundaries, success-metrics, regulatory, other]
  feedback_type: enum [gap, correction, expansion, deprecation, conflict]
  change_type: enum [additive, modifying, removing]
  before: string # Exact current content
  after: string # Exact proposed content
  rationale: string # Why change is warranted (must cite feedback)
  conflicts: string | null # Description or "none"
```

## Version increment rules

| Scenario | Version change | Example |
|----------|---------------|---------|
| Typo fix, clarification without meaning change | Patch (x.y.Z) | 1.2.0 → 1.2.1 |
| New state, term, or constraint added | Minor (x.Y.0) | 1.2.1 → 1.3.0 |
| Term renamed, state removed, breaking change | Major (X.0.0) | 1.3.0 → 2.0.0 |
| Experimental or beta change | Pre-release suffix | 1.3.0 → 1.3.1-beta |

## Changelog format

```md
## [version] - YYYY-MM-DD
- <imperative verb> <what changed> <why, if not obvious>
```

**Good:**
- Add link-expired-file-exists state to distinguish link expiration from file deletion
- Replace "mute" with "pause notifications" to resolve user confusion

**Bad:**
- Updated states (no specificity)
- Changed terminology based on feedback (no detail)
- The mute term was confusing so we changed it (past tense, no action clarity)
