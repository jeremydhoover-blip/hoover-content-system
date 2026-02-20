# Completeness Checklist

## Pre-creation checklist

Before creating a context pack, verify you have:

### Source materials
- [ ] Feature specification or PRD
- [ ] State map or user flow diagram
- [ ] Vocabulary document (if exists)
- [ ] Brand/voice guidelines
- [ ] Character limit specifications from design
- [ ] Examples of existing content (good and bad)
- [ ] Regulatory requirements (if applicable)

### AI system requirements
- [ ] Target AI system identified
- [ ] Token limit known
- [ ] Output format requirements understood
- [ ] Integration context (how AI will receive context pack)

## Context pack completeness checklist

After creating a context pack, validate:

### Metadata (required)
- [ ] Feature name is accurate and matches product nomenclature
- [ ] Version follows semver (x.y.z)
- [ ] Last updated date is current
- [ ] Target AI system specified
- [ ] Token budget specified and within limit
- [ ] Owner team identified

### Feature overview (required)
- [ ] Description explains what feature does in 2-3 sentences
- [ ] Non-expert reader could understand the feature purpose
- [ ] No assumptions about prior knowledge

### Content scope (required)
- [ ] Explicit list of what AI should generate
- [ ] Explicit list of what AI should NOT generate
- [ ] Scope matches actual AI use case

### Vocabulary (required)
- [ ] All domain-specific terms defined
- [ ] Canonical terms specified (exact form to use)
- [ ] Prohibited alternatives listed for each term
- [ ] Definitions are precise and unambiguous
- [ ] No circular definitions

### States (required for stateful content)
- [ ] All relevant states documented
- [ ] Each state has user situation described
- [ ] Each state has tone guidance
- [ ] Each state has content focus
- [ ] Error states included
- [ ] Edge case states included

### Constraints (required)
- [ ] Hard constraints clearly labeled (non-negotiable)
- [ ] Soft constraints clearly labeled (preferred)
- [ ] Character limits specified for each content type
- [ ] Character limit rationale provided (why this number)
- [ ] Prohibited patterns explicitly listed

### Tone (required)
- [ ] Default tone described
- [ ] State-specific tone adjustments documented
- [ ] "Never sound like" boundaries set
- [ ] "Always sound like" guidance provided
- [ ] Tone guidance is specific, not generic

### Examples (minimum 3 required)
- [ ] At least 3 example scenarios
- [ ] Each example has state/context specified
- [ ] Each example has GOOD output with explanation
- [ ] Each example has BAD output with explanation
- [ ] Examples cover different states/content types
- [ ] At least one edge case example
- [ ] Explanations say WHY not just WHAT

### Edge cases (required)
- [ ] Common edge cases documented
- [ ] Each edge case has handling guidance
- [ ] Edge cases the AI might encounter are covered
- [ ] Recovery scenarios included

## Quality checklist

### Clarity
- [ ] No ambiguous language
- [ ] Instructions are actionable
- [ ] Constraints are testable (can verify compliance)
- [ ] Examples clearly illustrate the rules

### Completeness
- [ ] AI has enough context to generate content without asking questions
- [ ] No critical information missing that would lead to incorrect output
- [ ] All referenced items (states, terms) are defined

### Efficiency
- [ ] No redundant information
- [ ] Content is within token budget
- [ ] High-value information prioritized
- [ ] Filler removed

### Accuracy
- [ ] Terms match product vocabulary exactly
- [ ] Character limits match actual UI constraints
- [ ] Constraints reflect actual requirements (not aspirational)
- [ ] Examples are realistic (from actual product context)

## Testing checklist

Before shipping context pack:

- [ ] Tested with target AI system
- [ ] AI output meets quality bar
- [ ] AI respects all hard constraints
- [ ] AI handles edge cases appropriately
- [ ] AI doesn't hallucinate information not in context
- [ ] Output fits within character limits
- [ ] Output uses correct vocabulary
- [ ] Output maintains correct tone

## Maintenance checklist

After shipping:

- [ ] Context pack version tracked
- [ ] Update process documented
- [ ] Owner responsible for updates identified
- [ ] Feature changes trigger context pack review
- [ ] AI output quality monitored
- [ ] Feedback loop to improve context pack exists
