# Vocabulary Reconciliation Reference

Framework for mapping user vocabulary to system terminology and resolving conflicts.

---

## Vocabulary layer model

User interfaces bridge three vocabulary domains:

```
┌─────────────────────────────────────┐
│     USER VOCABULARY                 │
│  (Natural language, mental models)  │
└──────────────────┬──────────────────┘
                   │
                   ▼ Mapping
┌─────────────────────────────────────┐
│     UI VOCABULARY                   │
│  (Labels, copy, terminology)        │
└──────────────────┬──────────────────┘
                   │
                   ▼ Mapping  
┌─────────────────────────────────────┐
│     SYSTEM VOCABULARY               │
│  (Technical terms, data models)     │
└─────────────────────────────────────┘
```

---

## User vocabulary research

### Collection methods

| Method | Captures | Example output |
|--------|----------|----------------|
| **Search query analysis** | Task vocabulary | "how to share file", "send to team" |
| **Support ticket mining** | Problem vocabulary | "can't login", "password not working" |
| **User interview** | Mental model vocabulary | "I think of these as folders..." |
| **Usability testing** | Action vocabulary | "I would click here to..." |
| **Survey/card sort** | Category vocabulary | Groupings and labels users create |

### Documentation template

| Field | Description | Example |
|-------|-------------|---------|
| User term | What users say | "share" |
| Context | Where/when used | Trying to give access |
| Frequency | How common | High (80% of sessions) |
| Variations | Synonyms observed | "share", "send", "give access" |
| Associated tasks | What they're trying to do | Collaborate with teammate |

---

## System vocabulary inventory

### Documentation template

| Field | Description | Example |
|-------|-------------|---------|
| System term | Technical name | `sharing_permission_grant` |
| Data entity | Where stored | `permission_grants` table |
| Scope | What it affects | Document access level |
| Behavior | What happens | Creates read/write access |
| Constraints | Limitations | Requires owner permission |

---

## Mapping process

### Step 1: Term inventory
List all terms from both domains:

| User terms | System terms |
|------------|--------------|
| share | sharing_permission_grant |
| send | notification_dispatch |
| give access | permission_add |
| invite | user_invitation |
| add to team | team_membership_add |

### Step 2: Intent clustering
Group user terms by underlying intent:

| Intent cluster | User terms | Notes |
|----------------|------------|-------|
| Grant access | share, give access, add | Same outcome desired |
| Notify | send, message, alert | Communication intent |
| Add user | invite, add person | New user creation |

### Step 3: System behavior mapping
Map intents to system capabilities:

| Intent | System capability | UI term decision |
|--------|-------------------|------------------|
| Grant access | permission_grant | "Share" |
| Notify | notification_send | "Send notification" |
| Add user | user_invite | "Invite" |

### Step 4: Conflict resolution
Identify and resolve vocabulary conflicts:

| Conflict type | Example | Resolution |
|---------------|---------|------------|
| One-to-many | "Share" → grant OR send | Separate: "Share" vs "Send" |
| Many-to-one | "Delete"/"Remove" → delete | Standardize: "Delete" |
| Ambiguous | "Add" → add user OR add item | Context-specific labels |

---

## Conflict types and resolutions

### Type 1: Synonyms
Multiple user terms for same system action.

| Scenario | User terms | System action | Resolution |
|----------|------------|---------------|------------|
| File operations | trash, delete, remove | file_delete | Pick one: "Delete" |
| Login | sign in, log in, login | authenticate | Pick one: "Sign in" |
| Settings | preferences, options, settings | config | Pick one: "Settings" |

**Resolution principle**: Choose most common user term; use others as search synonyms.

---

### Type 2: Homonyms
Same user term for different system actions.

| User term | Possible meanings | Context signal | Resolution |
|-----------|-------------------|----------------|------------|
| "Add" | Add user, add item, add to list | Screen context | "Add member" / "Add item" |
| "Share" | Grant access, send copy | Action context | "Share access" / "Send copy" |
| "Remove" | Revoke access, delete item | Object type | "Remove access" / "Delete" |

**Resolution principle**: Add object or qualifier to disambiguate.

---

### Type 3: Conceptual mismatches
User mental model differs from system model.

| User expectation | System reality | Gap | Resolution |
|------------------|----------------|-----|------------|
| "Delete" = gone forever | Soft delete (recoverable) | Permanence | "Move to trash" + recovery option |
| "Save" = single action | Auto-save enabled | Control | Show "Saved" status |
| "Copy" = duplicate | Creates reference | Behavior | "Create copy" vs "Add to" |

**Resolution principle**: Align UI copy with system behavior, not user assumption.

---

### Type 4: Vocabulary evolution
Terms change meaning over time or vary by user segment.

| Term | Legacy meaning | Current meaning | Resolution |
|------|----------------|-----------------|------------|
| "Post" | Publish | May just mean "save" | Context-aware labeling |
| "Friend" | Social connection | May mean "contact" | Use product-specific term |
| "Cloud" | Remote storage | May be assumed default | De-emphasize as default |

**Resolution principle**: Use research to track vocabulary drift; update periodically.

---

## Mapping documentation format

### Vocabulary map entry

```yaml
term:
  ui_label: "Share"
  user_vocabulary:
    - "share"
    - "give access"
    - "let them see"
  system_vocabulary:
    - "permission_grant"
    - "access_share"
  definition: "Grant another user read or edit access to an item"
  context: 
    - location: "Item context menu"
    - location: "Collaboration panel"
  disambiguation:
    - if: "Sending a copy (not access)"
      use: "Send copy"
    - if: "Adding to team (not item)"
      use: "Add to team"
  search_synonyms:
    - "collaborate"
    - "access"
    - "permission"
```

---

## Reconciliation checklist

### For new features
- [ ] What user vocabulary exists for this concept?
- [ ] What system terminology is being used?
- [ ] Does UI term match user mental model?
- [ ] Does UI term accurately describe system behavior?
- [ ] Are there conflicts with existing UI vocabulary?
- [ ] Have search synonyms been added?

### For existing vocabulary
- [ ] Is term used consistently across product?
- [ ] Do support queries suggest terminology confusion?
- [ ] Has user vocabulary shifted since launch?
- [ ] Are there localization challenges with current term?

---

## Cross-reference requirements

### Vocabulary should align across:

| Touchpoint | Must match | Example |
|------------|------------|---------|
| Navigation label | Page title | "Settings" → "Settings" |
| Button label | Success message | "Save" → "Saved" |
| Menu item | Dialog title | "Delete" → "Delete this item?" |
| Help article | UI label | "How to share" → "Share button" |
| Error message | Field label | "Email is invalid" → "Email" field |

### Consistency validation

When adding new term:
1. Search codebase for related terms
2. Check help documentation vocabulary
3. Verify marketing/website alignment
4. Confirm translation compatibility
