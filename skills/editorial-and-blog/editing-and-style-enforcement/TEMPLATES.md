# Templates

## Default output: Edited content with change log

Use this structure when returning edited content:

```md
## Edited content

[Full edited text here]

---

## Change log

| Location | Original | Change | Rationale |
|----------|----------|--------|-----------|
| Para 1, line 2 | "utilize" | "use" | Simpler word per style guide |
| Heading 3 | "Getting Started With..." | "Getting started with..." | Sentence case per house style |
| Para 4 | [deleted sentence] | — | Redundant with para 2 |

## Flags for author review

- [ ] Para 6: Statistic "40% improvement" — source needed
- [ ] Para 8: "Recently" is vague — specify timeframe or remove
```

## Alternative: Inline edit markup

Use when author prefers to see changes in context:

```md
## Edited content (tracked changes)

The new feature ~~will allow~~ **lets** users ~~to be able to~~ export data directly.

~~We are excited to announce~~ **Announcing** the release of version 3.0.

## Summary

- **Structural changes**: 2
- **Line edits**: 8
- **Copy edits**: 14
- **Flags for review**: 3
```

## Style deviation log

Use when documenting intentional departures from the style guide:

```md
## Style deviations

| Deviation | Style guide rule | Reason for departure |
|-----------|------------------|---------------------|
| "eCommerce" | Lowercase "e-commerce" | Brand-specific capitalization |
| Oxford comma omitted | Use Oxford comma | Matches client house style |
```
