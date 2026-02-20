---
name: writing-release-notes
description: Create clear, scannable release notes that communicate changes, impact, and required actions. Use when shipping software updates, API changes, or product releases.
---

# Writing Release Notes

## Quick start
Collect or infer:
- Release version and date
- All changes (features, fixes, improvements, deprecations)
- Breaking changes requiring user action
- Migration steps if needed
- Affected user segments

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Categorize all changes by type (breaking, feature, fix, improvement, deprecation).
2. Lead with breaking changes and required actions.
3. Write user-facing benefit for each feature.
4. Describe fix outcomes, not implementation details.
5. Include migration instructions for breaking changes.
6. Link to detailed documentation for complex changes.
7. Run the rubric check. Revise until it passes.

## Degrees of freedom
- **Medium**: Categorization and grouping strategy can vary.
- Allowed variation: Level of technical detail, internal vs external audience tone, as long as rubric passes.

## State awareness
- If release has breaking changes, lead with them and include migration section.
- If release is security-focused, follow security disclosure format.
- If audience is developers, include technical details; if end users, focus on benefits.
- If release is patch-only, use condensed format.

## Failure modes to avoid
- Burying breaking changes below features
- Describing what changed without explaining impact
- Missing migration instructions for breaking changes
- Using internal ticket references as primary content
- Listing implementation details instead of user benefits

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
- Changelog patterns: [reference/changelog-patterns.md](reference/changelog-patterns.md)
