# Audit Heuristics

Systematic evaluation criteria for UI copy quality assessment.

## Clarity heuristics

### H1: Action-outcome alignment
**Check**: Does the copy accurately describe what will happen?
- Button labels must match the resulting action
- Links must indicate destination or outcome
- Settings labels must reflect what they control

**Pass**: "Delete project" → deletes the project
**Fail**: "Submit" → unclear what is being submitted

### H2: Scannability
**Check**: Can users extract meaning without reading every word?
- Key information front-loaded
- One idea per UI element
- Hierarchy visually reinforced

**Pass**: "3 items selected" immediately scannable
**Fail**: "You have currently selected a total of 3 items from the list"

### H3: Jargon absence
**Check**: Does copy use user vocabulary, not system vocabulary?
- No technical terms without explanation
- No internal product codenames
- No acronyms without context

**Pass**: "Your file is ready"
**Fail**: "Asset pipeline processing complete"

## Consistency heuristics

### H4: Terminology consistency
**Check**: Is the same concept always called the same thing?
- One term per concept across all screens
- No synonyms for same action
- Matches marketing and documentation

**Pass**: "Delete" used everywhere for removal
**Fail**: "Delete", "Remove", "Trash", "Clear" for same action

### H5: Pattern consistency
**Check**: Do similar UI elements follow the same copy pattern?
- All error messages follow same structure
- All confirmation dialogs use same format
- All empty states have consistent elements

**Pass**: All errors: "[Problem]. [How to fix]."
**Fail**: Mixed error formats across screens

### H6: Tone consistency
**Check**: Does tone stay within defined range?
- No jarring shifts between screens
- Matches product voice guidelines
- Appropriate for context (error vs. success)

**Pass**: Consistently professional across flow
**Fail**: Casual onboarding, formal errors, cute empty states

## Behavioral heuristics

### H7: Action clarity
**Check**: Do users know what to do next?
- Primary action is obvious
- Secondary actions are visible but subordinate
- No dead ends without guidance

**Pass**: Clear CTA with supporting context
**Fail**: Information without action path

### H8: Error recovery
**Check**: Do error states enable recovery?
- Problem is explained
- Fix path is provided
- No blame language

**Pass**: "Email format invalid. Check for typos."
**Fail**: "Invalid input"

### H9: Confirmation appropriateness
**Check**: Are confirmations used correctly?
- Destructive actions require confirmation
- Reversible actions don't over-confirm
- Confirmation copy matches risk level

**Pass**: "Delete project?" for irreversible action
**Fail**: "Are you sure?" for saving a draft

## Accessibility heuristics

### H10: Screen reader compatibility
**Check**: Does copy work without visual context?
- Icon-only buttons have labels
- Images have alt text
- Link text is descriptive (not "click here")

**Pass**: `<button aria-label="Close dialog">`
**Fail**: `<button><XIcon /></button>`

### H11: Cognitive accessibility
**Check**: Is copy accessible to users with cognitive differences?
- Short sentences
- Simple vocabulary
- No idioms or metaphors without explanation

**Pass**: "Save your changes"
**Fail**: "Lock it in before it's too late!"

### H12: Reading level
**Check**: Is copy readable at appropriate grade level?
- Target: 8th grade reading level for consumer products
- Target: 10th grade for professional tools
- Measure with Flesch-Kincaid or similar

**Pass**: Flesch-Kincaid grade 7.2
**Fail**: Flesch-Kincaid grade 14.8

## Scoring guide

| Score | Meaning | Action |
|-------|---------|--------|
| Pass | Meets heuristic fully | No change needed |
| Partial | Meets heuristic with minor gaps | Minor revision |
| Fail | Does not meet heuristic | Requires fix |
| N/A | Heuristic doesn't apply | Skip |

## Severity mapping

| Heuristic failures | Severity |
|-------------------|----------|
| H7, H8, H10 fail | Critical — blocks task or excludes users |
| H1, H3, H4 fail | Major — causes confusion |
| H2, H5, H6, H9, H11, H12 fail | Minor — polish issues |
