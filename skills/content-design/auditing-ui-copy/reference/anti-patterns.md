# UI Copy Anti-Patterns

Common copy failures to identify during audits. Each anti-pattern includes detection criteria and remediation guidance.

---

## AP-01: The Vague Error

**Pattern**: Error message provides no useful information.

**Detection signals**:
- "Something went wrong"
- "An error occurred"
- "Invalid input"
- "Please try again"
- Generic error codes without explanation

**Why it fails**: Users cannot recover without understanding what happened.

**Remediation**: 
```
Before: "An error occurred"
After: "Couldn't save your changes. Check your connection and try again."
```

**Severity**: Critical

---

## AP-02: The Blame Shift

**Pattern**: Error message implies user fault when system is responsible.

**Detection signals**:
- "You entered invalid data"
- "Your request could not be processed"
- "You don't have permission"
- Accusatory "you" when system caused issue

**Why it fails**: Damages trust, feels hostile, may be factually wrong.

**Remediation**:
```
Before: "You entered an invalid email"
After: "Enter a valid email address. Example: name@company.com"
```

**Severity**: Major

---

## AP-03: The Jargon Dump

**Pattern**: Copy uses technical terms unfamiliar to users.

**Detection signals**:
- Technical terms (API, endpoint, payload, schema)
- Product-internal terminology
- Acronyms without expansion
- Developer-facing language in user-facing UI

**Why it fails**: Users cannot understand or act on information.

**Remediation**:
```
Before: "API rate limit exceeded. Retry after TTL expires."
After: "You've made too many requests. Wait a few minutes and try again."
```

**Severity**: Major

---

## AP-04: The Mystery Meat Button

**Pattern**: Action button doesn't describe what it does.

**Detection signals**:
- "Submit"
- "OK"
- "Go"
- "Click here"
- "Continue" (without context)
- Icon-only without label

**Why it fails**: Users cannot predict outcome, reduces confidence.

**Remediation**:
```
Before: "Submit"
After: "Create account"
```

**Severity**: Major

---

## AP-05: The Wall of Text

**Pattern**: Too much copy for the UI context.

**Detection signals**:
- Paragraphs in tooltips
- Multiple sentences in error messages
- Instructions longer than the form
- Help text that requires scrolling

**Why it fails**: Users don't read; key information gets buried.

**Remediation**:
```
Before: "Please note that when you change your password, you will be required to 
        use the new password on all devices where you are currently signed in, 
        and you may be asked to sign in again on some devices."
After: "You'll need to sign in again on all devices."
```

**Severity**: Minor (unless hides critical info, then Major)

---

## AP-06: The Synonym Shuffle

**Pattern**: Same concept called different things across product.

**Detection signals**:
- "Delete" / "Remove" / "Trash" for same action
- "Project" / "Workspace" / "Space" for same concept
- "Team" / "Organization" / "Group" interchangeably
- Different button labels for same action on different screens

**Why it fails**: Users unsure if these are same or different things.

**Remediation**:
```
Document canonical terms. Search-replace all variants.
Single source of truth: terminology.md
```

**Severity**: Major (compounds over time)

---

## AP-07: The Premature Detail

**Pattern**: Information provided before user needs it.

**Detection signals**:
- Full instructions before user starts task
- Edge case warnings on happy path
- All validation rules shown upfront
- Password requirements before field focus

**Why it fails**: Increases cognitive load; information forgotten by time it's needed.

**Remediation**:
```
Before: [Page load shows all 8 password rules]
After: [Rules appear when password field is focused]
```

**Severity**: Minor

---

## AP-08: The Orphan Error

**Pattern**: Error message appears far from error source.

**Detection signals**:
- Error banner at page top when field is below fold
- Toast notification for form validation
- Error message doesn't reference which field
- Modal error for inline issue

**Why it fails**: Users don't connect error to cause; can't find problem.

**Remediation**:
```
Before: Page banner: "Some fields have errors"
After: Inline under field: "Email is required"
```

**Severity**: Major

---

## AP-09: The Fake Question

**Pattern**: Confirmation uses question format but doesn't enable informed decision.

**Detection signals**:
- "Are you sure?"
- "Do you want to continue?"
- Questions without stating consequences
- Yes/No buttons without context

**Why it fails**: User cannot make informed decision; just adds friction.

**Remediation**:
```
Before: "Are you sure?" [Yes] [No]
After: "Delete 'Project Alpha'? This can't be undone." [Delete] [Cancel]
```

**Severity**: Major (for destructive actions), Minor (for low-risk)

---

## AP-10: The Crying Wolf

**Pattern**: Overuse of warnings, urgency, or confirmations.

**Detection signals**:
- Warning styling for non-warning content
- "Important!" on routine information
- Confirmation dialogs for reversible actions
- Exclamation marks on neutral messages

**Why it fails**: Users learn to ignore warnings; miss real ones.

**Remediation**:
```
Before: "Important! Your preferences have been saved!"
After: "Preferences saved"
```

**Severity**: Minor (but degrades over time)

---

## AP-11: The Abandoned User

**Pattern**: Empty or error state provides no forward path.

**Detection signals**:
- Empty state with no CTA
- Error without recovery action
- Dead ends with only "OK" button
- Success message without next step

**Why it fails**: User stuck; doesn't know what to do next.

**Remediation**:
```
Before: "No results found"
After: "No results found. Try different keywords or browse all items."
```

**Severity**: Major

---

## AP-12: The Apologetic Error

**Pattern**: Error message over-apologizes or uses cutesy language.

**Detection signals**:
- "Oops!"
- "Sorry, something went wrong"
- "Uh oh!"
- "We're sorry but..."
- Excessive apologetic framing

**Why it fails**: Unprofessional; doesn't help user recover; wastes space.

**Remediation**:
```
Before: "Oops! We're so sorry, but something went wrong on our end."
After: "Something went wrong. Try again in a few minutes."
```

**Severity**: Minor

---

## Anti-pattern audit matrix

| Anti-pattern | Quick check | Severity |
|--------------|-------------|----------|
| AP-01 Vague Error | Does error explain problem? | Critical |
| AP-02 Blame Shift | Does error accuse user? | Major |
| AP-03 Jargon Dump | Would a new user understand? | Major |
| AP-04 Mystery Meat | Does button describe outcome? | Major |
| AP-05 Wall of Text | Is copy > 2 sentences? | Minor |
| AP-06 Synonym Shuffle | Is term used consistently? | Major |
| AP-07 Premature Detail | Is info needed right now? | Minor |
| AP-08 Orphan Error | Is error near the problem? | Major |
| AP-09 Fake Question | Does question enable decision? | Major |
| AP-10 Crying Wolf | Is warning/urgency justified? | Minor |
| AP-11 Abandoned User | Is there a next step? | Major |
| AP-12 Apologetic Error | Is tone professional? | Minor |
