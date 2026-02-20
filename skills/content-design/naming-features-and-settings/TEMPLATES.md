# Templates

## Naming brief
Use this structure to define the naming problem:

```md
## Naming brief: [Feature/setting]

**What it does**: [One sentence describing functionality]
**User benefit**: [What problem it solves for users]
**User mental model**: [How users think about this concept, existing vocabulary]

**Constraints**:
- Character limit: [max chars or N/A]
- Must work in: [contexts—nav, settings, marketing, etc.]
- Localization: [languages, concerns]
- Trademark: [any known conflicts to avoid]

**Existing patterns**: [How similar things are named in this product]
**Competitor terms**: [What others call similar features]
```

## Candidate evaluation matrix
Use this to evaluate naming options:

```md
## Candidate evaluation

| Candidate | Descriptive | Memorable | Consistent | Localization-safe | Conflicts | Score |
|-----------|-------------|-----------|------------|-------------------|-----------|-------|
| [Name 1] | [1-5] | [1-5] | [1-5] | [1-5] | [None/Risk] | [/20] |
| [Name 2] | [1-5] | [1-5] | [1-5] | [1-5] | [None/Risk] | [/20] |

### Scoring key
- **Descriptive** (1-5): Does it explain what the feature does?
- **Memorable** (1-5): Is it easy to recall and reference?
- **Consistent** (1-5): Does it match product naming patterns?
- **Localization-safe** (1-5): Does it translate cleanly, avoid idioms/puns?

### Evaluation notes
[Per-candidate rationale for scores]
```

## Naming recommendation
Use this for the final output:

```md
## Recommendation: [Selected name]

**Rationale**: [Why this name wins]

**Usage guidance**:
- In UI: "[exact usage]"
- In docs: "[how to reference]"
- In marketing: "[if different from UI]"

**Rejected alternatives**:
| Name | Rejection reason |
|------|------------------|
| [Name] | [Why not] |

**Validation checklist**:
- [ ] Trademark search completed
- [ ] Localization review completed
- [ ] No conflicts with existing features
- [ ] Fits character constraints
- [ ] User comprehension tested (if applicable)
```

## Settings naming pattern
Use for systematic settings naming:

```md
## Settings naming pattern: [Category]

**Pattern**: [Structure, e.g., "Noun + modifier" or "Action + scope"]

| Setting | Name | Pattern applied |
|---------|------|-----------------|
| [What it controls] | [Name] | [How pattern was applied] |

**Conventions**:
- Use [nouns/verbs] for [type of setting]
- Avoid: [patterns to avoid]
- When in doubt: [tiebreaker rule]
```
