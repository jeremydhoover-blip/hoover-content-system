# Examples

## Example 1: Standard finding entry

**Input**: Audit the settings screen. Found button labeled "Do it" next to a toggle for notifications.

**Output**:
```md
### F-001: Vague action button label

**Location**: Settings > Notifications section
**Copy**: "Do it"
**Severity**: Major
**Issue type**: Clarity

**Problem**: Button label does not describe the action it performs.
**Impact**: Users cannot predict outcome; may hesitate or avoid the action.

**Recommendation**:
- Before: "Do it"
- After: "Save notification preferences"

**Rationale**: Action buttons must describe their outcome. Users scanning the screen should understand what happens without reading surrounding context.
```

---

## Example 2: Pattern analysis section

**Input**: Audit found 12 different phrasings for cancel actions across 8 screens.

**Output**:
```md
## Pattern analysis

### Inconsistent cancel terminology
Found 12 variations for cancel/dismiss actions:
- "Cancel" (3 instances)
- "Never mind" (2 instances)
- "Go back" (2 instances)
- "Dismiss" (2 instances)
- "Close" (1 instance)
- "Not now" (1 instance)
- "Skip" (1 instance)

**Impact**: Users must relearn interaction patterns on each screen. Increases cognitive load and reduces confidence.

**Recommendation**: Standardize on "Cancel" for reversible actions within a flow, "Close" for dialogs/modals, and "Skip" only when content can be accessed later.
```

---

## Example 3: Edge case — Incomplete input

**Input**: "Audit the app for copy issues."

**Output**:
```md
To proceed with the audit, I need:

1. **Which screens or flows?**
   - [ ] Onboarding
   - [ ] Settings
   - [ ] Core task flow (specify)
   - [ ] Error states
   - [ ] All screens

2. **Do existing voice/tone guidelines exist?**
   - [ ] Yes (provide or describe)
   - [ ] No (I'll note inconsistencies without a baseline)

3. **Known problem areas?**
   - [ ] User complaints about specific screens
   - [ ] Recent redesign areas
   - [ ] No known issues

I can proceed with reasonable defaults (audit visible screens, flag obvious inconsistencies) if you prefer speed. Label: [Assumptions will be documented in report]
```

---

## Example 4: Accessibility finding

**Input**: Audit found icon-only button with no label or aria-label.

**Output**:
```md
### F-007: Icon button lacks accessible label

**Location**: Toolbar > Share action
**Copy**: [No visible text; icon only]
**Severity**: Critical
**Issue type**: Accessibility

**Problem**: Screen reader users cannot identify button purpose. Icon conveys meaning visually but provides no programmatic label.
**Impact**: Feature is unusable for assistive technology users. May violate WCAG 2.1 SC 1.1.1.

**Recommendation**:
- Before: `<button><ShareIcon /></button>`
- After: `<button aria-label="Share this item"><ShareIcon /></button>`

**Rationale**: Every interactive element must have a programmatically determinable name. Icon-only buttons require aria-label or visually hidden text.
```

---

## Example 5: Audit summary excerpt

**Input**: Completed audit of checkout flow (5 screens, 47 copy elements).

**Output**:
```md
# UI Copy Audit Report

## Audit scope
- **Screens reviewed**: 5
- **Copy elements evaluated**: 47
- **Date**: 2026-02-20
- **Auditor**: AI-assisted

## Executive summary
Checkout flow has strong primary-path copy but inconsistent error handling. 3 critical issues block task completion for edge cases. Cancel terminology varies across screens.

## Findings by severity

### Critical (3)
- F-001: Payment error shows generic "Something went wrong" with no recovery path
- F-002: Shipping form validation fires before user finishes typing
- F-007: Confirmation button disabled with no explanation

### Major (8)
- F-003: Inconsistent cancel button labels (4 variations)
- F-004: Order summary uses jargon ("SKU", "line items")
- [...]

### Minor (12)
- F-010: "Proceed to checkout" could be "Continue to payment"
- [...]

## Pattern analysis
1. Error messages lack specificity and recovery guidance (5 instances)
2. Cancel/back terminology inconsistent (4 variations across 5 screens)
3. Form validation timing aggressive, interrupts user flow (3 forms)

## Recommendations
1. Rewrite all error messages to include: what happened, why, and how to fix
2. Standardize cancel terminology per content pattern library
3. Delay form validation until field blur or submission
```
