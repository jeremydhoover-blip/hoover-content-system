# Context Pack Schema

## Purpose

This schema defines the required and optional components of an AI context pack. Context packs provide structured information that enables AI systems to generate consistent, accurate, on-brand content.

## Schema overview

```yaml
context_pack:
  metadata:           # Required
  feature_overview:   # Required
  content_scope:      # Required
  vocabulary:         # Required
  states:             # Required for stateful content
  constraints:        # Required
  tone:               # Required
  examples:           # Required (minimum 3)
  edge_cases:         # Required
  validation:         # Optional but recommended
```

## Required sections

### Metadata
```yaml
metadata:
  feature: string           # Feature name
  version: semver           # Context pack version (x.y.z)
  last_updated: date        # ISO 8601 (YYYY-MM-DD)
  target_system: string     # AI system name or "general"
  token_budget: integer     # Approximate token count
  owner: string             # Responsible team
  regulatory_scope: string  # Optional: compliance requirements
```

### Feature overview
```yaml
feature_overview:
  description: string       # 2-3 sentences explaining the feature
  users: string             # Who uses this feature
  context: string           # When/why they use it
```

### Content scope
```yaml
content_scope:
  generates:                # What AI should generate
    - content_type: string
    - content_type: string
  excludes:                 # What AI should NOT generate
    - content_type: string
```

### Vocabulary
```yaml
vocabulary:
  terms:
    - concept: string       # What the term represents
      canonical: string     # Exact term to use
      prohibited: [string]  # Terms to never use
      definition: string    # Precise definition
```

### States (for stateful content)
```yaml
states:
  - name: string            # State identifier
    user_situation: string  # What user is experiencing
    tone: string            # Tone for this state
    content_focus: string   # What to emphasize
```

### Constraints
```yaml
constraints:
  hard:                     # Never violate
    - constraint: string
  soft:                     # Prefer but can flex
    - constraint: string
  limits:                   # Character/word limits
    - type: string
      limit: integer
      unit: chars | words
      rationale: string
  prohibited:               # Never do
    - pattern: string
```

### Tone
```yaml
tone:
  default: string           # Baseline tone description
  by_state:                 # State-specific adjustments
    - state: string
      adjustment: string
  boundaries:
    never: [string]         # What never to sound like
    always: [string]        # What always to sound like
```

### Examples
```yaml
examples:                   # Minimum 3 required
  - id: integer
    content_type: string
    state: string
    input: string           # Trigger or context
    good:
      output: string
      explanation: string   # Why it works
    bad:
      output: string
      explanation: string   # Why it fails
```

### Edge cases
```yaml
edge_cases:
  - scenario: string        # What unusual situation
    handling: string        # How to handle it
```

## Optional sections

### Validation
```yaml
validation:
  checklist:
    - item: string
      required: boolean
  test_cases:
    - input: string
      expected_output_contains: [string]
```

### Regulatory (for regulated content)
```yaml
regulatory:
  requirements:
    - disclosure: string    # What must be included
  approved_phrases:
    - concept: string
      exact_language: string
  prohibited_claims:
    - claim: string
```

## Token budget guidelines

| Content complexity | Recommended budget | Notes |
|--------------------|-------------------|-------|
| Simple (1-2 content types) | 500-800 tokens | Compact format |
| Medium (3-5 content types) | 1000-1500 tokens | Standard format |
| Complex (6+ content types or regulated) | 1500-2500 tokens | Full format with regulatory section |

## Version increment rules

| Change type | Version bump | Example |
|-------------|--------------|---------|
| Typo fix, clarification | Patch (x.y.Z) | 1.0.0 → 1.0.1 |
| New state, new content type | Minor (x.Y.0) | 1.0.1 → 1.1.0 |
| Breaking change, constraint change | Major (X.0.0) | 1.1.0 → 2.0.0 |
