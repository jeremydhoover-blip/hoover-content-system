# Context Pack Schema Reference

## Purpose

This document defines the standard schema for feature content context packs. Consistent structure enables:
- AI systems to reliably parse and use context
- Content teams to create context efficiently
- Quality validation through automated checks

---

## Schema overview

```yaml
context_pack:
  version: "1.0"
  feature:
    name: string (required)
    purpose: string (required)
    boundaries:
      included: array[string]
      excluded: array[string]
  
  users:
    primary:
      description: string
      goals: array[{goal: string, priority: enum[primary, secondary, tertiary]}]
      knowledge:
        assumed: array[string]
        new_concepts: array[string]
      emotional_context: string
    secondary: (optional, same structure)
  
  states:
    happy_path: array[state_object]
    error_states: array[error_state_object]
    edge_cases: array[state_object]
  
  components: array[component_object]
  
  business_rules:
    constraints: array[{rule: string, content_implication: string}]
    compliance: array[string]
  
  terminology:
    vocabulary: array[{term: string, definition: string, usage_notes: string}]
    avoid: array[{term: string, alternative: string, reason: string}]
  
  metadata:
    last_updated: date
    updated_by: string
    change_summary: string
    related_context: array[string]
```

---

## Object definitions

### state_object
```yaml
state:
  name: string (required)
  when: string (required) # Condition that triggers this state
  user_need: string (required) # What user needs in this moment
  content_requirements: array[string] # Copy elements needed
```

### error_state_object
```yaml
error_state:
  name: string (required)
  when: string (required)
  cause: string (required) # Technical or user cause
  recovery: string (required) # How user can resolve
  content_requirements: array[string]
```

### component_object
```yaml
component:
  name: string (required)
  location: string (required)
  purpose: string (required)
  states: array[string] # Different states this component can have
  content_needs: array[string] # What copy is needed
  character_limits:
    headline: integer (optional)
    body: integer (optional)
    cta: integer (optional)
  current_copy: string (optional) # Existing copy if updating
```

---

## Required vs. optional fields

### Always required
- feature.name
- feature.purpose
- users.primary.description
- users.primary.goals (at least one)
- states.happy_path (at least one)
- states.error_states (at least one)
- components (at least one)
- terminology.vocabulary (at least one term)
- metadata.last_updated

### Required for AI consumption
- terminology.avoid (helps prevent bad outputs)
- user_need in all states (guides tone)
- character_limits in components (prevents overflow)

### Optional
- users.secondary
- states.edge_cases (but recommended)
- business_rules.compliance (if not applicable)
- component.current_copy (for new features)

---

## Validation rules

### Completeness checks
- [ ] Every state has user_need defined
- [ ] Every state has content_requirements defined
- [ ] Every component has character_limits OR explicit "no limit"
- [ ] At least one error state documented
- [ ] Terminology includes at least one "avoid" term

### Consistency checks
- [ ] Terms in vocabulary are used consistently in examples
- [ ] State names are unique within their category
- [ ] Component names match actual UI elements

### Quality checks
- [ ] User needs are written from user perspective
- [ ] Content requirements are specific enough to act on
- [ ] Terminology definitions are clear to someone new

---

## Version history

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01 | Initial schema |

---

## Example: Minimal valid context pack

```yaml
context_pack:
  version: "1.0"
  feature:
    name: "password-reset"
    purpose: "Allow users to reset forgotten password"
    boundaries:
      included: ["email entry", "reset link", "new password form"]
      excluded: ["account recovery questions", "2FA reset"]
  
  users:
    primary:
      description: "User who forgot their password"
      goals:
        - goal: "Regain account access"
          priority: "primary"
      knowledge:
        assumed: ["Has email access", "Created account previously"]
        new_concepts: ["Reset link expiration"]
      emotional_context: "Frustrated, locked out, wants quick resolution"
  
  states:
    happy_path:
      - name: "email_entry"
        when: "User lands on forgot password page"
        user_need: "Enter email to receive reset link"
        content_requirements: ["Email field label", "Submit button", "Instructions"]
      - name: "email_sent"
        when: "User submits valid email"
        user_need: "Confirmation that email was sent"
        content_requirements: ["Confirmation message", "Next steps", "Spam folder note"]
    error_states:
      - name: "email_not_found"
        when: "Email not in system"
        cause: "Typo or unregistered email"
        recovery: "Check email or create account"
        content_requirements: ["Error message", "Suggestions"]
  
  components:
    - name: "email_field"
      location: "Forgot password form"
      purpose: "Collect user email for reset"
      states: ["empty", "filled", "error"]
      content_needs: ["Label", "Placeholder", "Error message"]
      character_limits:
        label: 30
        error: 100
  
  terminology:
    vocabulary:
      - term: "reset link"
        definition: "Temporary URL sent via email to reset password"
        usage_notes: "Prefer over 'reset email' or 'password link'"
    avoid:
      - term: "click here"
        alternative: "select the link"
        reason: "Accessibility"
  
  metadata:
    last_updated: "2026-02-01"
    updated_by: "Content Team"
    change_summary: "Initial context pack"
```
