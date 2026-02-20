# Common Style Conflicts

## Table of contents
- [AP vs. Chicago differences](#ap-vs-chicago-differences)
- [Tech industry conventions](#tech-industry-conventions)
- [House style override patterns](#house-style-override-patterns)
- [Conflict resolution hierarchy](#conflict-resolution-hierarchy)

---

## AP vs. Chicago differences

| Element | AP Style | Chicago Style |
|---------|----------|---------------|
| Oxford comma | No (except for clarity) | Yes |
| Numbers | Spell out one-nine, numerals 10+ | Spell out one-hundred, numerals 101+ |
| Percent | Use % symbol | Spell out "percent" |
| Titles | Capitalize principal words | Capitalize principal words (same) |
| Time | 8 a.m., 3 p.m. | 8:00 AM, 3:00 PM |
| Dates | March 15, 2024 | 15 March 2024 (flexible) |
| Abbreviations | Use periods (U.S., U.N.) | No periods (US, UN) in some cases |
| Em dash | space—space | no space—no space |
| Ellipsis | three dots ... | three spaced dots . . . |
| "Toward" | toward (no s) | toward or towards |
| "Website" | website (lowercase) | Website or website (flexible) |

---

## Tech industry conventions

These conventions often override traditional style guides in tech contexts:

### Product and feature names
- Follow the company's official capitalization regardless of style guide
- Examples: "GitHub" not "Github," "macOS" not "MacOS," "iOS" not "IOS"

### Code-adjacent text
- Use code formatting for: commands, file names, variables, parameters
- Keep technical terms lowercase when they're code references: `true`, `null`, `string`
- Capitalize when using as concepts: "Boolean values," "Null state"

### UI terminology
- Button labels: Match exact UI text, including capitalization
- Menu paths: Use > for navigation: Settings > Account > Privacy

### Version numbers
- No "version" or "v" unless part of official name
- Correct: "iOS 17," "Python 3.12"
- Incorrect: "iOS version 17," "Python v3.12"

---

## House style override patterns

Common areas where house styles override standard guides:

### Terminology standardization

| Category | Decision | Example |
|----------|----------|---------|
| Product users | "customer" vs. "user" | Pick one, document in terminology guide |
| The company | "we" vs. company name | Define when each is appropriate |
| Actions | "click" vs. "select" vs. "tap" | Define by platform |
| Interface elements | "dialog" vs. "modal" vs. "popup" | Pick canonical term |

### Brand voice markers

| Element | Possible house rule |
|---------|---------------------|
| Contractions | Always/never/situational |
| Exclamation marks | Never/sparingly/allowed in X context |
| Questions in headings | Allowed/discouraged |
| Starting with "And" or "But" | Allowed/formal contexts only |
| Emoji | Never/marketing only/specific set |

### Structural preferences

| Element | Options to standardize |
|---------|----------------------|
| Heading case | Sentence case vs. Title Case |
| List punctuation | Periods on all items / only full sentences / never |
| Callout formatting | Note: / **Note:** / > Note: |

---

## Conflict resolution hierarchy

When styles conflict, resolve in this order:

1. **Explicit house style rule** — Always wins if documented
2. **Author intent** — If author made a deliberate choice, preserve or flag
3. **Channel conventions** — Blog vs. docs vs. UI may have different standards
4. **Primary style guide** — AP, Chicago, or designated guide
5. **Consistency within document** — Match existing patterns if no rule applies
6. **Editor judgment** — Document reasoning in change log

### Documenting deviations

When you deviate from the primary style guide, log it:

```md
## Style deviations

| Deviation | Style guide rule | Reason |
|-----------|------------------|--------|
| "eCommerce" | Lowercase per AP | Client brand standard |
| No Oxford comma | Chicago requires it | House style override |
| "10" not "ten" | Chicago spells out | Tech convention for versions |
```

### Escalation triggers

Flag for style guide owner when:
- Same conflict appears 3+ times
- Rule would improve consistency but doesn't exist
- Existing rule creates confusion or is frequently overridden
- External requirements conflict with house style (legal, partner, regulatory)
