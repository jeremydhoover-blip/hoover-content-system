# Term Conflict Patterns

## What is a term conflict?

A term conflict occurs when:
1. **Same term, different meanings:** The same word means different things in different contexts
2. **Same concept, different terms:** Multiple words are used for the same thing
3. **Overlapping scope:** Terms have ambiguous boundaries

## Conflict detection checklist

Before finalizing vocabulary, check for conflicts:

### Within the feature
- [ ] Does any term appear with different meanings in different screens?
- [ ] Are there multiple terms that could refer to the same concept?
- [ ] Do any terms have overlapping definitions?

### Across features
- [ ] Does any term conflict with vocabulary in adjacent features?
- [ ] Does any term have a different meaning elsewhere in the product?
- [ ] Are there shared concepts with inconsistent terminology?

### Against external standards
- [ ] Does any term conflict with platform conventions (iOS, Android, Windows, macOS)?
- [ ] Does any term have a specific meaning in the industry that differs from our usage?
- [ ] Does any term have a common meaning that differs from our usage?

## Common conflict types

### Type 1: Polysemy (one term, multiple meanings)

**Pattern:** Same term used for different concepts in different contexts.

**Example:**
- "Archive" in email: Move to archive folder (retrievable)
- "Archive" in project management: Mark as complete and hide (retrievable)
- "Archive" in data storage: Compress for long-term storage (requires extraction)

**Detection signals:**
- User asks "What happens if I archive this?"
- Support tickets about unexpected behavior after action
- Different teams describe the same action differently

**Resolution strategies:**
1. Choose one meaning and rename the others
2. Add qualifiers: "Archive project" vs. "Archive to storage"
3. Use completely different terms for different actions

---

### Type 2: Synonymy (different terms, same meaning)

**Pattern:** Multiple terms used interchangeably for the same concept.

**Example:**
- Settings page says "Delete account"
- Confirmation dialog says "Remove account"
- Email says "Account cancellation"

**Detection signals:**
- Different screens use different terms for same action
- Documentation inconsistent with UI
- User searches for term A but feature uses term B

**Resolution strategies:**
1. Audit all instances and unify to one term
2. Add prohibited alternatives to vocabulary doc
3. Create find-and-replace list for content review

---

### Type 3: Scope ambiguity (overlapping definitions)

**Pattern:** Terms have unclear boundaries, creating uncertainty about which applies.

**Example:**
- "Team" = group of people working together
- "Group" = collection of users with shared permissions
- Unclear: Is a team a type of group? Can groups be teams?

**Detection signals:**
- Users ask which category something belongs to
- Internal debates about which term to use
- Feature requests that reveal conceptual confusion

**Resolution strategies:**
1. Create explicit scope definitions with boundaries
2. Document the relationship (subset, superset, orthogonal)
3. Rename one term to eliminate overlap

---

### Type 4: Platform convention conflict

**Pattern:** Product term differs from established platform convention.

**Example:**
- iOS uses "Trash" for deleted items
- Our product uses "Deleted" folder
- User expects "Trash" behavior but gets different functionality

**Detection signals:**
- Users look for feature using platform term
- Support tickets referencing platform conventions
- Usability test participants use platform vocabulary

**Resolution strategies:**
1. Align with platform convention when possible
2. If must differ, document rationale and make difference clear
3. Consider platform-specific terminology (iOS: Trash, Windows: Recycle Bin)

---

### Type 5: User mental model mismatch

**Pattern:** Internal term doesn't match how users think about the concept.

**Example:**
- Product uses "Deactivate" for temporary account suspension
- Users interpret "Deactivate" as permanent deletion
- Support tickets: "I deactivated but my data is gone"

**Detection signals:**
- User research shows comprehension failure
- High support ticket volume about specific feature
- Users express surprise at action outcomes

**Resolution strategies:**
1. User research to identify natural language
2. Test term comprehension with target users
3. Replace internal term with user-validated term

## Conflict resolution process

### Step 1: Identify
- Review vocabulary for conflict patterns above
- Check support tickets for terminology confusion
- Audit UI strings for inconsistencies

### Step 2: Document
```md
## Conflict: <description>

**Type:** <polysemy / synonymy / scope ambiguity / platform conflict / mental model mismatch>

**Terms involved:** <list>

**Where it appears:**
- <location 1>
- <location 2>

**User impact:** <what goes wrong>

**Source of conflict:** <why this happened>
```

### Step 3: Resolve
- Propose canonical term
- Get stakeholder alignment
- Document prohibited alternatives
- Create migration plan

### Step 4: Prevent
- Add to vocabulary document
- Update content review checklist
- Add to onboarding for new team members

## Conflict log format

Track resolved conflicts for institutional knowledge:

| Date | Conflict | Type | Resolution | Impact |
|------|----------|------|------------|--------|
| 2026-02-20 | "mute" vs "block" confusion | Mental model | Changed to "pause notifications" | 4 UI strings, 2 help articles |
| 2026-02-15 | "workspace" vs "org" vs "team space" | Synonymy | Unified to "workspace" | 12 UI strings, design specs |
