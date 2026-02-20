# Examples

## Example 1: Feature naming with evaluation

**Input**: Name a feature that automatically saves document changes in real-time.

**Output**:
```md
## Naming brief: Auto-save feature

**What it does**: Automatically saves document changes without manual save action.
**User benefit**: Never lose work; no need to remember to save.
**User mental model**: Users expect "save" to mean preserving work. "Auto" prefix is widely understood.

**Constraints**:
- Character limit: 20 (settings panel)
- Must work in: Settings toggle, status indicator, docs
- Localization: Must translate to DE, FR, JA, ES
- Trademark: None known

**Existing patterns**: Product uses "Auto-[action]" for automatic features (Auto-correct, Auto-fill)
**Competitor terms**: Google Docs: implicit (no name). Word: AutoSave. Notion: "Saved"

## Candidate evaluation

| Candidate | Descriptive | Memorable | Consistent | Localization-safe | Conflicts | Score |
|-----------|-------------|-----------|------------|-------------------|-----------|-------|
| Autosave | 5 | 5 | 5 | 5 | None | 20/20 |
| Auto-save | 5 | 5 | 4 | 5 | Style conflict | 19/20 |
| Real-time save | 4 | 3 | 3 | 4 | None | 14/20 |
| Continuous backup | 3 | 3 | 2 | 4 | Implies copies | 12/20 |
| Smart save | 3 | 4 | 3 | 5 | Vague | 15/20 |

### Evaluation notes
- **Autosave**: Matches existing "Auto-" pattern, universally understood, clean translation.
- **Auto-save**: Hyphen inconsistent with product style (Autocorrect, not Auto-correct).
- **Real-time save**: Accurate but technical; "real-time" less familiar to non-technical users.
- **Continuous backup**: Implies separate copies exist; could create confusion about version history.
- **Smart save**: "Smart" is vague; doesn't explain trigger or behavior.

## Recommendation: Autosave

**Rationale**: Follows established "Auto-" naming pattern, universally recognized term, translates cleanly.

**Usage guidance**:
- In UI: "Autosave" (settings toggle)
- In status: "Autosaved" or "Autosaved at [time]"
- In docs: "Autosave automatically saves your changes as you work."

**Rejected alternatives**:
| Name | Rejection reason |
|------|------------------|
| Auto-save | Hyphenation inconsistent with product style |
| Real-time save | Too technical for general audience |
| Continuous backup | Misleading—implies copies, not in-place save |
| Smart save | Vague; doesn't communicate automatic behavior |

**Validation checklist**:
- [x] Trademark search completed — generic term, no issues
- [x] Localization review completed — direct equivalents exist in target languages
- [x] No conflicts with existing features
- [x] Fits character constraints (8 chars)
```

---

## Example 2: Settings naming pattern

**Input**: Establish naming patterns for notification settings.

**Output**:
```md
## Settings naming pattern: Notifications

**Pattern**: [Notification type] + [optional: channel]

| Setting | Name | Pattern applied |
|---------|------|-----------------|
| Toggle all notifications | Notifications | Category name as toggle |
| Email notifications | Email notifications | Type + channel |
| Push notifications | Push notifications | Type + channel |
| Marketing emails | Marketing emails | Content type + channel |
| Activity alerts | Activity alerts | Trigger + format |
| Sound | Notification sound | Category + attribute |

**Conventions**:
- Use plural nouns for categories (Notifications, not Notification)
- Channel comes after type (Email notifications, not Notification emails)
- On/off toggles use the feature name directly, no verb ("Notifications" not "Enable notifications")
- Avoid: "Alert" and "Notification" as synonyms—pick one per product

**When in doubt**: Match the user's language. If users say "turn off email alerts," use "Email alerts" not "Email notifications."
```

---

## Example 3: Edge case — Invented feature concept

**Input**: Name a feature that predicts what users will type next and offers suggestions.

**Output**:
```md
## Naming brief: Predictive text suggestions

**What it does**: Analyzes typing patterns to predict and suggest completions.
**User benefit**: Faster typing, fewer keystrokes, reduced errors.
**User mental model**: Users familiar with phone keyboards ("autocomplete"), search ("suggestions").

**Constraints**:
- Character limit: 25 (settings panel)
- Must work in: Settings, tooltip, marketing
- Localization: Global product, 12 languages
- Trademark: Avoid "Autocomplete" (generic but heavily associated with Google)

**Existing patterns**: Product doesn't have similar features yet. Establishing new pattern.
**Competitor terms**: iOS: "Predictive", SwiftKey: "Predictions", Gmail: "Smart Compose"

## Candidate evaluation

| Candidate | Descriptive | Memorable | Consistent | Localization-safe | Conflicts | Score |
|-----------|-------------|-----------|------------|-------------------|-----------|-------|
| Text predictions | 5 | 4 | N/A | 5 | None | 18/20 |
| Smart suggestions | 3 | 4 | N/A | 4 | "Smart" overused | 14/20 |
| Type-ahead | 4 | 3 | N/A | 3 | Technical | 13/20 |
| Writing assist | 3 | 3 | N/A | 5 | Too broad | 13/20 |
| Predictive text | 5 | 4 | N/A | 5 | iOS association | 17/20 |

## Recommendation: Text predictions

**Rationale**: Descriptive, neutral (no strong competitor association), localizes cleanly. "Predictions" is more specific than "suggestions" (implies intelligence).

**Usage guidance**:
- In UI: "Text predictions" (settings)
- In tooltip: "Suggestions based on what you're typing"
- In marketing: "Text predictions help you write faster"

**Rejected alternatives**:
| Name | Rejection reason |
|------|------------------|
| Smart suggestions | "Smart" is vague and overused in tech products |
| Type-ahead | Technical jargon, unclear to non-developers |
| Predictive text | Strong iOS association; could cause platform confusion |
```

---

## Example 4: Edge case — Incomplete input

**Input**: "Name this new feature."

**Output**:
```md
To generate effective name candidates, I need:

1. **What does the feature do?**
   [One sentence describing core functionality]

2. **Who uses it?**
   - [ ] All users
   - [ ] Specific role (describe)
   - [ ] Admin/power users only

3. **Where will the name appear?**
   - [ ] Navigation
   - [ ] Settings
   - [ ] Marketing
   - [ ] All of the above

4. **Constraints?**
   - Character limit: [number or "flexible"]
   - Localization requirements: [languages or "English only"]

5. **Existing naming patterns?**
   - Does the product have naming conventions? (e.g., "Smart [X]", "Auto-[X]")

I can proceed with a generic feature naming approach if you share just the feature description.
```

---

## Example 5: Conflict identification

**Input**: Name a feature that groups related emails together. Product already has "Collections" for file grouping.

**Output**:
```md
## Naming brief: Email grouping feature

**What it does**: Groups related emails into collapsible threads or bundles.
**User benefit**: Cleaner inbox, related context in one place.
**User mental model**: Gmail "Conversations", Outlook "Threads"

**Constraints**:
- Must differentiate from existing "Collections" (file grouping)
- Users should not confuse email groups with file collections

## Candidate evaluation

| Candidate | Descriptive | Memorable | Consistent | Localization-safe | Conflicts | Score |
|-----------|-------------|-----------|------------|-------------------|-----------|-------|
| Conversations | 5 | 5 | 4 | 5 | Gmail association | 18/20 |
| Threads | 5 | 4 | 4 | 4 | None | 17/20 |
| Email bundles | 4 | 3 | 3 | 4 | None | 14/20 |
| Collections | 5 | 4 | 5 | 5 | **CONFLICT** | — |

### Conflict analysis
- **Collections**: Cannot use. Already means file grouping in this product. Using for email would create confusion.
- **Conversations**: Strong Gmail association but accurately describes feature. Low conflict risk.

## Recommendation: Conversations

**Rationale**: Industry-standard term, accurate description, differentiates clearly from "Collections" (which implies intentional user curation, not automatic grouping).

**Differentiation guidance**:
| Term | Use for | Mental model |
|------|---------|--------------|
| Collections | User-created file groups | "I organized these" |
| Conversations | System-grouped email threads | "These belong together" |
```
