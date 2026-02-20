# System Rules

## Scope

Rules for how skills behave, interact with each other, and resolve conflicts. Applies to skill structure and execution, not content outputs.

## Hard Rules

### Skill Structure

1. Every skill folder must contain: `SKILL.md`, `TEMPLATES.md`, `RUBRIC.md`, `EXAMPLES.md`.
2. Every skill must have a corresponding eval file in `/evals`.
3. `SKILL.md` must include YAML frontmatter with `name` and `description`.
4. `SKILL.md` must not exceed 150 lines.
5. Optional files: `CHECKLIST.md`, `reference/`, `scripts/`.
6. No other file types permitted in skill folders.

### Inheritance

1. All skills inherit rules from `/shared` automatically.
2. Skills may extend shared rules with domain-specific constraints.
3. Skills may not override, contradict, or exempt themselves from shared rules.
4. If a skill needs an exception, the exception must be added to the shared file.

### References

1. `SKILL.md` may reference files in the same skill folder only.
2. `SKILL.md` may reference files in `/shared` and `/governance`.
3. Referenced files may not reference other files (one level deep only).
4. Use relative paths for same-folder references: `[TEMPLATES.md]`.
5. Use folder paths for shared references: `[shared/style.md]`.

### Conflict Resolution

1. `/governance` rules override all other rules.
2. `/shared` rules override skill-level rules.
3. Skill rules override defaults only within skill scope.
4. When two skills apply, the more specific skill takes precedence.
5. If specificity is equal, user must specify which skill to use.

### Triggers

1. Every skill must define triggers in `SKILL.md` description.
2. Triggers must be concrete nouns or verbs, not abstract concepts.
3. No two skills may share identical trigger sets.
4. Overlapping triggers require documented differentiation.

### Inputs and Outputs

1. `SKILL.md` must list required inputs.
2. `SKILL.md` must list optional inputs with defaults.
3. If required inputs are missing, skill must prompt for them.
4. Output format must be defined in `TEMPLATES.md`.
5. Output must be gradable against `RUBRIC.md` criteria.

### Versioning

1. Skills are versioned via git history, not inline version numbers.
2. Breaking changes require updating all dependent evals.
3. Deprecated patterns move to a `## Deprecated` section, not deleted.
4. Deprecated sections are removed after two release cycles.

## Prohibited Patterns

| Pattern | Violation |
|---------|-----------|
| `SKILL.md` over 150 lines | Too much content in navigational file |
| Referencing `reference/foo.md` from `reference/bar.md` | Nested references |
| Overriding shared rule in skill | Inheritance violation |
| Trigger like "content" or "writing" | Too vague |
| Missing eval file | Incomplete skill package |
| Hardcoded version number in SKILL.md | Use git history |

## Interaction with Other Files

1. `naming.md` defines how to name skills and files.
2. `glossary.json` defines canonical terms skills must use.
3. `skill-catalog.md` is the source of truth for which skills exist.
4. `eval-spec.md` defines how to write eval files for skills.