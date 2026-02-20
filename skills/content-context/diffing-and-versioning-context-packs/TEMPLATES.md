# Templates

## Default output: Context Pack Diff Report

Use this as the default structure:

```md
# Context Pack Diff Report

**Pack:** [context pack name]
**Base version:** [X.Y.Z]
**Head version:** [A.B.C]
**Generated:** [date]
**Recommended version:** [computed version]

## Summary
- Breaking changes: [count]
- Additions: [count]
- Corrections: [count]
- Version increment: [MAJOR | MINOR | PATCH | NONE]

## Breaking Changes
[If none: "No breaking changes."]

### [BREAK-001] [Change description]
- **Section:** [affected section]
- **Was:** [previous value/structure]
- **Now:** [new value/structure or "removed"]
- **Impact:** [what this breaks for consumers]
- **Migration:** [how to update dependent content]

## Additions
[If none: "No additions."]

### [ADD-001] [Change description]
- **Section:** [affected section]
- **Added:** [new value/structure]
- **Purpose:** [why this was added]

## Corrections
[If none: "No corrections."]

### [CORR-001] [Change description]
- **Section:** [affected section]
- **Was:** [previous value]
- **Now:** [corrected value]
- **Reason:** [why this was corrected]

## Detailed Diff

### feature
[No changes | Changes listed]

### user_goals
| Status | Goal |
|--------|------|
| [+/-/~] | [goal text] |

### states
| State | Status | Changes |
|-------|--------|---------|
| [name] | [added/removed/modified/unchanged] | [summary of changes] |

### transitions
| Status | From | To | Trigger |
|--------|------|-----|---------|
| [+/-/~] | [state] | [state] | [trigger] |

### error_taxonomy
| Status | Code | Change |
|--------|------|--------|
| [+/-/~] | [ERROR_CODE] | [what changed] |

### vocabulary
| Status | Term | Change |
|--------|------|--------|
| [+/-/~] | [term] | [definition change] |

## Changelog Entry

### [computed version] - [date]

#### Breaking
- [breaking change 1]
- [breaking change 2]

#### Added
- [addition 1]
- [addition 2]

#### Fixed
- [correction 1]
- [correction 2]
```

## Compact diff output (for CI/automation)

```json
{
  "pack": "[name]",
  "base_version": "[X.Y.Z]",
  "head_version": "[A.B.C]",
  "recommended_version": "[computed]",
  "increment_type": "MAJOR | MINOR | PATCH | NONE",
  "breaking": [
    {
      "code": "BREAK-001",
      "section": "[path]",
      "description": "[change]",
      "migration": "[steps]"
    }
  ],
  "additions": [
    {
      "code": "ADD-001",
      "section": "[path]",
      "description": "[change]"
    }
  ],
  "corrections": [
    {
      "code": "CORR-001",
      "section": "[path]",
      "description": "[change]"
    }
  ]
}
```

## Inline diff format (for visual review)

```diff
# Context Pack: [name]
# Comparing: [base_version] → [head_version]

## states

  idle:
    entry: Page load
-   exit: User clicks button
+   exit: User selects action
    content_guidance: Show welcome message

+ new_state:
+   entry: User completes action
+   exit: Timeout or dismiss
+   content_guidance: Show confirmation

- removed_state:
-   entry: Legacy trigger
-   exit: Deprecated flow

## vocabulary

- old_term: Previous definition
+ new_term: New definition
~ changed_term:
-   Old definition text
+   Updated definition text
```

## Version history template

```md
# Context Pack Version History

**Pack:** [name]
**Current version:** [X.Y.Z]

## Versions

### X.Y.Z - [date]
[Changelog for this version]

### X.Y.W - [date]
[Changelog for previous version]

...
```
