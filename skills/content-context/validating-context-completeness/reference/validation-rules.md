# Validation Rules Reference

## Table of Contents
1. [Structural validation](#structural-validation)
2. [Semantic validation](#semantic-validation)
3. [Coverage validation](#coverage-validation)
4. [Consistency validation](#consistency-validation)

---

## Structural validation

Check that required elements exist.

### Rule S1: Required sections present
```
FOR each section IN required_sections:
  IF section NOT IN context_pack:
    EMIT blocking_error("Missing required section: {section}")
```

### Rule S2: Required fields present
```
FOR each section IN context_pack:
  FOR each required_field IN section.required_fields:
    IF required_field NOT IN section:
      EMIT blocking_error("Missing required field: {section}.{field}")
```

### Rule S3: Minimum counts met
```
IF count(user_goals) < 1:
  EMIT blocking_error("At least one user_goal required")

IF count(states) < 1:
  EMIT blocking_error("At least one state required")

IF count(core_actions) < 1:
  EMIT blocking_error("At least one core_action required")
```

### Rule S4: Naming conventions
```
IF feature.name NOT MATCH /^[a-z][a-z0-9-]*$/:
  EMIT blocking_error("Feature name must be lowercase-hyphenated")

FOR each state_name IN states:
  IF state_name NOT MATCH /^[a-z][a-z0-9_]*$/:
    EMIT warning("State name should be snake_case: {state_name}")

FOR each action IN core_actions:
  IF action NOT MATCH /^[a-z][a-z0-9_]*$/:
    EMIT warning("Action should be snake_case: {action}")
```

---

## Semantic validation

Check that references resolve and definitions are consistent.

### Rule M1: Transition targets exist
```
FOR each transition IN transitions:
  IF transition.from NOT IN states AND transition.from != "any":
    EMIT blocking_error("Transition from undefined state: {from}")
  IF transition.to NOT IN states:
    EMIT blocking_error("Transition to undefined state: {to}")
```

### Rule M2: All states reachable
```
reachable = compute_reachable_states(transitions, initial_state)
FOR each state IN states:
  IF state NOT IN reachable:
    EMIT blocking_error("Unreachable state: {state}")
```

### Rule M3: No trapped states
```
FOR each state IN states:
  exits = get_transitions_from(state)
  IF count(exits) == 0 AND state NOT IN terminal_states:
    EMIT blocking_error("Trapped state with no exits: {state}")
```

### Rule M4: Vocabulary terms resolve
```
used_terms = extract_terms_from_content(context_pack)
FOR each term IN used_terms:
  IF term NOT IN vocabulary:
    EMIT blocking_error("Term used but not defined: {term}")
```

### Rule M5: No circular vocabulary
```
FOR each term IN vocabulary:
  definition = vocabulary[term]
  referenced_terms = extract_terms(definition)
  FOR each ref IN referenced_terms:
    IF ref IN vocabulary:
      IF term IN expand_definition(ref):
        EMIT blocking_error("Circular definition: {term} <-> {ref}")
```

### Rule M6: No conflicting definitions
```
FOR each term_a, term_b IN vocabulary:
  IF term_a != term_b:
    IF definitions_conflict(term_a, term_b):
      EMIT blocking_error("Conflicting definitions: {term_a} vs {term_b}")
```

Conflict detection heuristics:
- Same definition for different terms (synonyms not distinguished)
- One term defined using another as equivalent
- Overlapping scope without distinction

---

## Coverage validation

Check that all scenarios have guidance.

### Rule C1: States have error handling where needed
```
FOR each state IN states:
  IF state_can_fail(state):
    IF state.error_handling NOT DEFINED:
      EMIT warning("State can fail but has no error_handling: {state}")
```

State can fail if:
- Involves user input (forms)
- Involves network/API calls
- Has transitions triggered by failure conditions

### Rule C2: Error taxonomy covers failure modes
```
failure_modes = collect_failure_modes(states, transitions)
FOR each mode IN failure_modes:
  IF mode NOT IN error_taxonomy:
    EMIT warning("Failure mode not in error_taxonomy: {mode}")
```

### Rule C3: Transitions have content guidance
```
FOR each transition IN transitions:
  IF transition.content_guidance NOT DEFINED:
    EMIT suggestion("Transition has no content guidance: {from} -> {to}")
```

### Rule C4: Entry and exit completeness
```
FOR each state IN states:
  IF state.entry NOT DEFINED:
    EMIT blocking_error("State missing entry condition: {state}")
  IF state.exit NOT DEFINED:
    EMIT blocking_error("State missing exit condition: {state}")
```

---

## Consistency validation

Check for internal consistency.

### Rule K1: Actions referenced in transitions exist
```
FOR each transition IN transitions:
  IF transition.trigger IN action_format:
    IF transition.trigger NOT IN core_actions:
      EMIT warning("Transition trigger not in core_actions: {trigger}")
```

### Rule K2: Vocabulary used consistently
```
FOR each term IN vocabulary:
  usages = find_usages(term, context_pack)
  FOR each usage IN usages:
    IF usage.context != term.definition.context:
      EMIT warning("Term used inconsistently: {term} at {usage.location}")
```

### Rule K3: State names used consistently
```
state_references = collect_state_references(context_pack)
FOR each ref IN state_references:
  IF ref NOT IN states:
    EMIT blocking_error("Reference to undefined state: {ref}")
```

---

## Validation order

Execute in this order:
1. Structural validation (S1-S4)
2. Semantic validation (M1-M6)
3. Coverage validation (C1-C4)
4. Consistency validation (K1-K3)

Stop and report after each phase if blocking errors exist.
