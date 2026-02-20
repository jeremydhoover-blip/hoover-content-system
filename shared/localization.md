# Localization Standards

## Scope

Translation-ready writing and locale-neutral patterns for all content outputs.

## Hard Rules

### String Structure

1. Do not concatenate strings to form sentences. Use complete translatable units.
2. Do not embed variables mid-sentence where word order may change.
3. Use placeholders with descriptive names (`{userName}` not `{0}`).
4. Keep one complete thought per string. Do not split sentences across strings.

### Text Expansion

1. Allow 30–40% expansion for English-to-other-language translation.
2. Do not design for exact character counts.
3. Avoid fixed-width containers for text that will be localized.
4. Button and label text must tolerate expansion without truncation.

### Cultural Neutrality

1. Do not use idioms, slang, or culturally specific references.
2. Do not reference holidays, seasons, or events specific to one region.
3. Do not assume left-to-right reading order in content structure.
4. Do not use humor that depends on wordplay.

### Date, Time, and Numbers

1. Do not hardcode date formats. Use locale-aware formatting.
2. Do not hardcode time formats. Support 12-hour and 24-hour.
3. Do not hardcode currency symbols or positions.
4. Do not hardcode decimal or thousands separators.
5. Write dates in ISO 8601 when locale is unknown (2026-02-20).

### Units and Measurement

1. Support both metric and imperial where applicable.
2. Do not assume a default unit system.
3. Label units explicitly. Do not rely on context.

### Names and Address

1. Do not assume first name / last name structure.
2. Use "Full name" as a single field unless separation is required.
3. Do not hardcode address field order or requirements.
4. Do not assume phone number formats.

## Prohibited Patterns

| Pattern | Issue | Alternative |
|---------|-------|-------------|
| `"Hello " + name + "!"` | Concatenation | `"Hello {name}!"` |
| `{0} of {1}` | Positional placeholders | `{current} of {total}` |
| `Fall sale` | Season-specific | `Seasonal sale` or specific dates |
| `Like hitting a home run` | Cultural idiom | State meaning directly |
| `02/20/2026` | Ambiguous date format | `2026-02-20` or locale-formatted |
| `First name` + `Last name` | Name structure assumption | `Full name` or locale-appropriate fields |
| `$100` hardcoded | Currency assumption | `{amount}` with locale formatting |
| `5 miles` hardcoded | Unit assumption | Offer unit selection or show both |

## Interaction with Skills

1. All outputs inherit these rules.
2. Skills may specify character limits but must note expansion requirements.
3. Skills producing UI strings must follow placeholder naming conventions.
4. Skills may not use idioms regardless of target audience.