# Accessibility Standards

## Scope

Inclusive language, screen reader compatibility, and cognitive accessibility rules for all content outputs.

## Hard Rules

### Inclusive Language

1. Do not use ability-based metaphors or idioms.
2. Do not reference sensory actions as requirements (see, hear, watch).
3. Use person-first or identity-first language based on community preference.
4. Do not use gendered terms when gender is unknown or irrelevant.

### Screen Reader Compatibility

1. Link text must describe the destination. Never use "click here" or "learn more" alone.
2. Alt text required for all images. Decorative images use empty alt (`alt=""`).
3. Alt text must not start with "Image of" or "Picture of."
4. Form labels must be explicit. Do not rely on placeholder text as the label.
5. Error messages must identify the field and the problem.
6. Icon-only buttons require accessible names.

### Reading Level

1. Target 8th grade reading level for general UI content.
2. Target 10th grade reading level for technical documentation.
3. Measure using Flesch-Kincaid or equivalent.
4. Specialized terminology permitted if defined on first use or in glossary.

### Cognitive Load

1. One action per sentence in instructions.
2. Front-load important information. Do not bury key terms.
3. Use consistent terminology. Do not alternate synonyms for the same concept.
4. Chunk content into scannable sections with clear headings.

### Motion and Timing

1. Do not describe content as requiring specific timing ("quickly," "before it disappears").
2. Do not write instructions that assume animation will be seen.
3. Provide text alternatives for any content conveyed through motion.

## Prohibited Patterns

| Pattern | Issue | Alternative |
|---------|-------|-------------|
| `See the results` | Vision-dependent | `View the results` or `Check the results` |
| `Click here` | No destination context | `View your account settings` |
| `Simply do X` | Dismissive of difficulty | `Do X` |
| `Crazy fast` | Ableist idiom | `Very fast` |
| `Blind to the issue` | Ableist metaphor | `Unaware of the issue` |
| `Sanity check` | Ableist term | `Validation check` |
| `Crippled feature` | Ableist term | `Limited feature` |
| `Grandfathered in` | Exclusionary origin | `Legacy access` |
| `Dummy data` | Ableist term | `Placeholder data` or `Sample data` |
| `Master/slave` | Exclusionary term | `Primary/replica` or `Main/secondary` |
| `Blacklist/whitelist` | Exclusionary term | `Blocklist/allowlist` |

## Interaction with Skills

1. All outputs inherit these rules.
2. Skills targeting developer audiences may use higher reading levels with justification.
3. Skills may add domain-specific accessibility requirements.
4. Skills may not exempt outputs from inclusive language rules.