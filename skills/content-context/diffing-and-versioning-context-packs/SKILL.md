---
name: diffing-and-versioning-context-packs
description: Compares context pack versions to identify changes, generates semantic diffs, and applies version control discipline. Use when updating context packs, reviewing changes before publish, auditing context drift, or maintaining context history.
---

# Diffing and Versioning Context Packs

## Quick start
Collect or infer:
- Base context pack (previous version)
- Head context pack (current/proposed version)
- Change type (major, minor, patch) or infer from diff

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Load base and head context packs.
2. Run structural diff: identify added, removed, modified sections.
3. Run semantic diff: classify changes by impact (breaking, additive, corrective).
4. Determine version increment based on change classification.
5. Generate changelog entry with human-readable summary.
6. Run the rubric check. Revise until it passes.

## Degrees of freedom
**Level: Low**

- Default: follow semantic versioning rules exactly
- Allowed variation: changelog prose style may vary; version scheme may follow organization conventions if documented

## Behavioral logic
Context packs evolve. Without version discipline, consumers cannot know:
- What changed between versions
- Whether changes break existing content
- When to update downstream assets

This skill enforces structured change tracking as a gate for context updates.

## Version increment rules

| Change type | Examples | Version impact |
|-------------|----------|----------------|
| Breaking | Remove state, rename action, change error code | Major (X.0.0) |
| Additive | Add new state, add vocabulary term, add error type | Minor (x.Y.0) |
| Corrective | Fix typo, clarify definition, improve content guidance | Patch (x.y.Z) |

## Decision framework

| Condition | Action |
|-----------|--------|
| State removed | Major version bump |
| State renamed | Major version bump |
| Transition removed | Major version bump |
| Error code changed | Major version bump |
| Vocabulary term definition changed substantively | Major version bump |
| New state added | Minor version bump |
| New transition added | Minor version bump |
| New error type added | Minor version bump |
| New vocabulary term added | Minor version bump |
| Content guidance improved | Patch version bump |
| Typo fixed | Patch version bump |
| No functional change | No version bump |

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
- Version schema: [reference/version-schema.md](reference/version-schema.md)
- Diff format: [reference/diff-format.md](reference/diff-format.md)
- Scripts: [scripts/](scripts/)
