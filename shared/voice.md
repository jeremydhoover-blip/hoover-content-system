# Voice Constraints

## Scope

Rules for maintaining consistent voice across all content outputs. Applies to any content produced using skills in this repo.

## Hard Rules

### Voice Definition

1. Voice is the consistent personality of the product. It does not change.
2. A voice definition must include exactly four attributes.
3. Each attribute requires:
   - One-sentence definition
   - One "this, not that" contrast
4. All content outputs must align with the defined voice attributes.

### Tone Boundaries

1. Tone adapts to context. Voice does not.
2. Tone shifts are constrained to:
   - **Errors**: Empathetic, solution-focused
   - **Success**: Brief, confirming
   - **Onboarding**: Patient, guiding
   - **Destructive actions**: Serious, precise
3. Tone must never be:
   - Playful during errors
   - Celebratory during destructive confirmations
   - Apologetic for routine system behavior

### Person and Address

1. Use "you" for the user.
2. Use "we" only when the product acts on the user's behalf.
3. Do not use "I" unless content is for a named persona or agent.
4. Do not use "one" as a substitute for "you."

### Formality

1. Use contractions in UI copy.
2. Do not use contractions in legal or compliance content.
3. Prohibited: exclamation points (except one per success state), emoji in product UI, slang, idioms.
4. Prohibited: passive voice (unless actor is unknown), nominalization, undefined jargon.

## Prohibited Patterns

| Pattern | Why prohibited | Use instead |
|---------|----------------|-------------|
| `Oops!` | Playful during failure | State what happened |
| `We're so sorry` | Over-apologetic | State what to do next |
| `Awesome!` | Casual | `Done` or `Saved` |
| `One must configure` | Formal distance | `Configure your...` |
| `The system has determined` | Robotic | `We found` |
| `Please be advised` | Bureaucratic | State fact directly |
| `Don't worry` | Dismissive | Explain next step |

## Interaction with Skills

1. Skills reference this file; they do not redefine voice rules.
2. Skills may specify tone shifts for their domain.
3. Skill RUBRIC.md files grade outputs against these constraints.