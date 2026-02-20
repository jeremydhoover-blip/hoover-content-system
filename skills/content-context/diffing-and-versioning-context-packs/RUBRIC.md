# Rubric

## Pass criteria
Pass if all are true:

- [ ] Diff report identifies all structural changes (added, removed, modified sections)
- [ ] Each breaking change includes migration guidance
- [ ] Version increment recommendation follows semantic versioning rules
- [ ] Breaking changes force major version bump
- [ ] Additions force at least minor version bump
- [ ] Corrections force at least patch version bump
- [ ] Changelog entry is human-readable and complete
- [ ] No change is miscategorized (breaking listed as correction, etc.)
- [ ] Diff format clearly shows before/after values
- [ ] Impact of each breaking change is explicitly stated

## Fail criteria
Fail if any are true:

- [ ] Breaking change not flagged (false negative)
- [ ] Non-breaking change flagged as breaking (false positive)
- [ ] Version recommendation violates semver (e.g., minor bump for removal)
- [ ] Migration guidance missing for breaking changes
- [ ] Diff shows only structural changes without semantic classification
- [ ] Changelog entry omits changes from the diff
- [ ] Identical packs produce non-empty diff
- [ ] Different packs produce empty diff

## Change classification rules

| Change | Classification | Version impact |
|--------|----------------|----------------|
| State removed | Breaking | Major |
| State added | Additive | Minor |
| State renamed | Breaking | Major |
| State.entry changed | Corrective or Breaking* | Patch or Major |
| State.exit changed | Corrective or Breaking* | Patch or Major |
| State.content_guidance changed | Corrective | Patch |
| Transition removed | Breaking | Major |
| Transition added | Additive | Minor |
| Transition.trigger changed | Breaking | Major |
| Error code removed | Breaking | Major |
| Error code added | Additive | Minor |
| Error code value changed | Breaking | Major |
| Error message_pattern changed | Corrective | Patch |
| Vocabulary term removed | Breaking | Major |
| Vocabulary term added | Additive | Minor |
| Vocabulary definition changed (meaning) | Breaking | Major |
| Vocabulary definition changed (wording) | Corrective | Patch |
| Feature.purpose changed | Corrective | Patch |
| User goal removed | Breaking | Major |
| User goal added | Additive | Minor |

*State entry/exit changes are breaking if they change the semantic meaning; corrective if they clarify without changing meaning.

## Meaning change heuristics
A definition change is breaking if:
- Key nouns or verbs are replaced
- Scope is narrowed or expanded
- Preconditions or postconditions change
- Examples or constraints are contradicted

A definition change is corrective if:
- Grammar or spelling is fixed
- Synonyms are used without changing meaning
- Clarifying phrases are added without contradiction
