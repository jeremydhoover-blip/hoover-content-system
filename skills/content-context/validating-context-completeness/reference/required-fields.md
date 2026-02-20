# Required Fields Reference

## Table of Contents
1. [Required sections](#required-sections)
2. [Required fields per section](#required-fields-per-section)
3. [Optional sections](#optional-sections)
4. [Validation severity matrix](#validation-severity-matrix)

---

## Required sections

Every context pack must include these sections:

| Section | Purpose | Blocking if missing |
|---------|---------|---------------------|
| `feature` | Identifies the feature | Yes |
| `feature.name` | Machine-readable identifier | Yes |
| `feature.purpose` | Human-readable goal statement | Yes |
| `user_goals` | What users want to accomplish | Yes |
| `core_actions` | Canonical action names | Yes |
| `states` | All possible feature states | Yes |
| `transitions` | How states connect | Yes |
| `error_taxonomy` | Error types and patterns | Yes |
| `vocabulary` | Term definitions | Yes |

---

## Required fields per section

### feature
```yaml
feature:
  name: required        # lowercase-hyphenated
  purpose: required     # one sentence, user-focused
  version: optional     # semver format
```

### user_goals
```yaml
user_goals:
  - required            # at least one goal
  - format: verb phrase # "Upload a file", "Reset password"
```

Minimum: 1 goal  
Recommended: 3-5 goals covering primary use cases

### core_actions
```yaml
core_actions:
  - required            # at least one action
  - format: snake_case  # select_file, submit_form
```

Minimum: 1 action  
Must match actions referenced in states and transitions

### states
```yaml
states:
  state_name:           # required: at least one state
    entry: required     # condition that activates this state
    exit: required      # condition that ends this state
    error_handling: conditional  # required if state can fail
    content_guidance: required   # what content to show
```

Every state must have:
- `entry`: How user arrives
- `exit`: How user leaves
- `content_guidance`: What to display

Conditional requirements:
- `error_handling`: Required if state involves user input, network calls, or can fail

### transitions
```yaml
transitions:
  - from: required      # source state name
    to: required        # target state name
    trigger: required   # what causes transition
```

Every transition must:
- Reference defined states (no orphans)
- Have explicit trigger
- Create reachable graph (no isolated states)

### error_taxonomy
```yaml
error_taxonomy:
  - code: required          # SCREAMING_SNAKE_CASE
    message_pattern: required   # template with [placeholders]
    recovery: required      # what user can do
    severity: optional      # blocking, warning, info
```

Minimum: Cover all failure modes in states with error_handling

### vocabulary
```yaml
vocabulary:
  term_name: required       # definition
```

Requirements:
- Every unique term used in the pack must be defined
- No circular definitions (A defined as B, B defined as A)
- No conflicting definitions

---

## Optional sections

| Section | Purpose | When to include |
|---------|---------|-----------------|
| `tone_boundaries` | Emotional guardrails | High-stakes or sensitive features |
| `constraints` | Technical/legal limits | Regulated features, char limits |
| `localization_notes` | Translation guidance | Multi-language products |
| `success_metrics` | How to measure | When content has KPIs |
| `related_features` | Cross-feature links | Complex systems |

---

## Validation severity matrix

| Missing element | Severity | Rationale |
|-----------------|----------|-----------|
| feature.name | Blocking | Cannot identify pack |
| feature.purpose | Blocking | Cannot understand intent |
| user_goals (all) | Blocking | No user context |
| core_actions (all) | Blocking | No action vocabulary |
| states (all) | Blocking | No state model |
| state.entry | Blocking | Unreachable state |
| state.exit | Blocking | Trapped state |
| state.content_guidance | Blocking | No content direction |
| state.error_handling (when applicable) | Warning | Incomplete error coverage |
| transitions (all) | Blocking | No flow definition |
| transition to undefined state | Blocking | Broken reference |
| error_taxonomy (all) | Blocking | No error patterns |
| vocabulary (all) | Blocking | No term definitions |
| vocabulary term used but undefined | Blocking | Broken reference |
| circular vocabulary | Blocking | Unresolvable definition |
| tone_boundaries | N/A | Optional |
| constraints | N/A | Optional |
