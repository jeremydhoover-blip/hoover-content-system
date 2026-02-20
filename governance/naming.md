# Naming Conventions

## Scope

Rules for naming skills, folders, files, and identifiers throughout the repository.

## Hard Rules

### Skill Names

1. Use lowercase letters, numbers, and hyphens only.
2. Use gerund form (verb ending in -ing) as the first word.
3. Maximum 5 words, 40 characters.
4. Folder name must exactly match the `name` field in SKILL.md frontmatter.

**Valid:**
- `writing-error-messages`
- `designing-agent-instructions`
- `auditing-ui-copy`

**Invalid:**
- `error-messages` (no gerund)
- `write-error-messages` (not gerund form)
- `Writing-Error-Messages` (uppercase)
- `writing_error_messages` (underscores)

### Category Folder Names

1. Use lowercase letters and hyphens only.
2. Use plural nouns or compound descriptors.
3. Must describe a content domain, not a format.

**Valid:**
- `ux-writing`
- `content-strategy`
- `mcp-and-agents`

**Invalid:**
- `ux` (too vague)
- `writing` (too broad)
- `miscellaneous` (catch-all)

### File Names

| File | Name | Case |
|------|------|------|
| Skill overview | `SKILL.md` | UPPER |
| Templates | `TEMPLATES.md` | UPPER |
| Rubric | `RUBRIC.md` | UPPER |
| Examples | `EXAMPLES.md` | UPPER |
| Checklist | `CHECKLIST.md` | UPPER |
| Reference files | `{descriptor}.md` | lowercase-hyphen |
| Scripts | `{descriptor}.py` | lowercase_underscore |
| Eval files | `{skill-name}.eval.json` | lowercase-hyphen |

### Identifiers in Files

1. YAML frontmatter `name`: lowercase-hyphen, matches folder.
2. Rubric criterion `id`: lowercase-hyphen, prefixed with skill name.
3. Eval case `id`: lowercase-hyphen, descriptive of scenario.
4. Glossary term keys: lowercase-hyphen.

**Example rubric ID:**
```
writing-error-messages-has-recovery-action
```

**Example eval case ID:**
```
missing-context-prompts-for-input
```

### Prohibited Names

| Name | Reason |
|------|--------|
| `helper`, `utils`, `tools` | Too vague |
| `content`, `writing`, `text` | Too broad |
| `misc`, `other`, `general` | Catch-all |
| `new`, `old`, `v2` | Time-relative |
| `test`, `temp`, `draft` | Non-permanent |
| Product names as skill names | Couples to external dependency |

## Validation

1. Folder names must pass regex: `^[a-z0-9]+(-[a-z0-9]+)*$`
2. Skill names must start with gerund: `^(writing|designing|creating|building|defining|auditing|mapping|planning|measuring|generating|updating|validating|structuring|reducing|improving|editing|documenting)-`
3. File names in `reference/` must pass: `^[a-z0-9]+(-[a-z0-9]+)*\.md$`
4. Script names must pass: `^[a-z0-9]+(_[a-z0-9]+)*\.py$`

## Renaming Rules

1. Renaming a skill requires updating:
   - Folder name
   - SKILL.md frontmatter `name`
   - Eval file name
   - All references in `skill-catalog.md`
2. Do not create aliases or redirects.
3. Old names must not be reused for 2 release cycles.
