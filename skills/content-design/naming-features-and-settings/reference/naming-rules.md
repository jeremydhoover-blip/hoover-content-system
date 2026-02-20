# Naming Rules Reference

Naming conventions and requirements for features, settings, and UI elements.

---

## Core naming principles

### Rule N-01: Clarity over brevity
Names must be unambiguous even at cost of length.

| ❌ Avoid | ✅ Prefer | Reason |
|----------|-----------|--------|
| Sync | Auto-sync | Clarifies automatic nature |
| Mode | Edit mode | Specifies which mode |
| Share | Share link | Distinguishes from invite |

---

### Rule N-02: User-centric vocabulary
Name based on user benefit, not technical implementation.

| ❌ Technical | ✅ User-centric |
|--------------|-----------------|
| Cache invalidation | Refresh content |
| Token expiry | Session timeout |
| Webhook | Automated notification |
| Regex filter | Pattern matching |

---

### Rule N-03: Parallel construction
Related features use parallel grammatical structure.

| ❌ Inconsistent | ✅ Parallel |
|----------------|-------------|
| Copy, Duplicate item, Clone this | Copy, Duplicate, Clone |
| Auto-save / Saving automatically | Auto-save / Auto-backup |
| Dark mode / Enable light theme | Dark mode / Light mode |

---

### Rule N-04: Action verbs for features
Active features use verb + noun construction.

**Pattern**: `[Verb] + [Object]` or `[Verb] + [Modifier] + [Object]`

| Feature type | Pattern | Examples |
|--------------|---------|----------|
| Creation | Create + object | Create folder, Create template |
| Modification | Edit/Update + object | Edit profile, Update settings |
| Deletion | Delete/Remove + object | Delete file, Remove member |
| Toggle | Enable/Disable + feature | Enable notifications, Disable tracking |

---

### Rule N-05: Noun phrases for settings
Settings use noun or noun phrase (not verbs).

| ❌ Verb phrase | ✅ Noun phrase |
|----------------|----------------|
| Show timestamps | Timestamps |
| Enable auto-save | Auto-save |
| Allow notifications | Notifications |

Settings with on/off states implied by toggle UI.

---

### Rule N-06: Specificity hierarchy
More specific names for deeper navigation levels.

| Level | Name style | Example |
|-------|-----------|---------|
| Top nav | Broad category | Settings |
| Section | Category subset | Notifications |
| Individual setting | Specific feature | Email notifications |
| Setting option | Precise variant | Daily digest |

---

## Grammatical requirements

### Capitalization
| Element type | Style | Example |
|--------------|-------|---------|
| Feature name | Sentence case | Auto-save |
| Setting name | Sentence case | Push notifications |
| Menu item | Sentence case | Export data |
| Button label | Sentence case | Save changes |
| Navigation | Sentence case | Account settings |

**Exception**: Proper nouns retain original capitalization (e.g., "Google Drive", "Microsoft Word").

---

### Word count limits
| Element | Max words | Example |
|---------|-----------|---------|
| Feature name | 3 | Two-factor authentication |
| Setting name | 4 | Automatic session timeout |
| Menu item | 3 | Export to CSV |
| Tab label | 2 | Account |

---

### Character limits
| Element | Max chars | Reason |
|---------|-----------|--------|
| Feature name | 30 | UI space constraints |
| Setting name | 40 | List view alignment |
| Menu item | 25 | Dropdown width |
| Tab label | 15 | Tab bar space |
| Navigation item | 20 | Sidebar width |

---

## Naming patterns by category

### Toggle settings
Pattern: `[Feature noun]` (state implied by toggle)

| ✅ Good | ❌ Avoid |
|---------|----------|
| Notifications | Enable notifications |
| Dark mode | Turn on dark mode |
| Auto-save | Automatically save |

---

### Choice settings (radio/select)
Pattern: `[Category]: [Options list]`

Setting name: `Theme`
Options: `Light`, `Dark`, `System default`

Setting name: `Language`
Options: `English`, `Spanish`, `French`...

---

### Numeric settings
Pattern: `[Property] + [Unit context]`

| ✅ Clear | ❌ Ambiguous |
|----------|--------------|
| Session timeout (minutes) | Timeout |
| Max file size (MB) | File limit |
| Auto-lock (minutes) | Lock timer |

---

### Feature actions
Pattern: `[Verb] + [Object]` for primary, `[Object]` for secondary

| Context | Primary action | Secondary actions |
|---------|----------------|-------------------|
| Document | Create document | Duplicate, Archive, Delete |
| User | Invite user | Edit role, Remove |
| Report | Generate report | Schedule, Export |

---

## Compound naming rules

### With modifiers
When modifier needed, place before noun:

| Pattern | Example |
|---------|---------|
| `[Modifier] + [Feature]` | Advanced search |
| `[Frequency] + [Action]` | Daily backup |
| `[Scope] + [Setting]` | Global permissions |

---

### With qualifiers
When scope/target needed, place after noun:

| Pattern | Example |
|---------|---------|
| `[Feature] + [Scope]` | Notifications for @mentions |
| `[Setting] + [Context]` | Theme for dark environments |
| `[Action] + [Target]` | Export to PDF |

---

## Consistency requirements

### Same feature, same name
A feature must have identical name everywhere it appears:
- Navigation
- Page title
- Settings reference
- Help documentation
- Error messages

**Violation example**:
- Nav: "Preferences"
- Page title: "Settings"
- Help: "Options"

---

### Version naming
When features have tiers/versions:

| Pattern | Examples |
|---------|----------|
| `[Base] + [Modifier]` | Search, Advanced search |
| `[Base] + [Tier]` | Plan, Pro plan, Enterprise plan |
| `[Base] + [Version]` | Editor, New editor, Classic editor |

Avoid: Search v2, Search (beta), New search 2.0

---

## Internationalization considerations

### Avoid idioms
Names must translate directly:

| ❌ Idiomatic | ✅ Translatable |
|--------------|-----------------|
| Inbox zero | Empty inbox |
| Deep dive | Detailed analysis |
| Heads up | Alert |

### Avoid culture-specific references
| ❌ Cultural | ✅ Universal |
|-------------|--------------|
| Home run | Success |
| Quarterback | Lead |
| Hat trick | Triple achievement |

### Allow space expansion
Reserve 30-40% extra space for translation (German, Finnish expand significantly).
