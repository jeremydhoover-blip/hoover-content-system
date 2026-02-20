# Document Structure Patterns

## Table of contents
- [Step structure hierarchy](#step-structure-hierarchy)
- [Heading level rules](#heading-level-rules)
- [Callout types](#callout-types)
- [Code block conventions](#code-block-conventions)

---

## Step structure hierarchy

| Level | Use | Example |
|-------|-----|---------|
| Primary step | Main action in sequence | `### Step 1: Install dependencies` |
| Sub-step | Nested action within primary | Lettered list (a, b, c) |
| Inline instruction | Minor clarification | Prose within step |

**Maximum depth:** 2 levels (primary + one sub-level). Beyond this, split into separate guide.

---

## Heading level rules

```
# Title (H1) — One per document
## Major section (H2) — Prerequisites, Steps, Verify, Troubleshooting
### Step or subsection (H3) — Individual steps or troubleshooting items
#### Sub-step grouping (H4) — Rarely needed; consider restructuring
```

**Prohibited:**
- Skipping heading levels (H1 → H3)
- Multiple H1 headings
- H5 or deeper

---

## Callout types

Use blockquotes with bold labels:

| Type | Format | Use when |
|------|--------|----------|
| Note | `> **Note:**` | Helpful context, not critical |
| Important | `> **Important:**` | Must-read before proceeding |
| Warning | `> **Warning:**` | Risk of data loss or system impact |
| Tip | `> **Tip:**` | Optional optimization or shortcut |

**Placement rules:**
- Place callouts after the relevant step, not before
- Maximum one callout per step
- Never stack callouts

---

## Code block conventions

### Language identifiers (required)

| Language | Identifier |
|----------|------------|
| Bash/Shell | `bash` or `shell` |
| JavaScript | `javascript` or `js` |
| TypeScript | `typescript` or `ts` |
| Python | `python` |
| JSON | `json` |
| YAML | `yaml` |
| Environment files | `env` |
| Plain text/output | `text` |

### Command vs output

Show command and expected output separately:

```bash
npm --version
```

```text
10.2.0
```

### Placeholder conventions

| Format | Meaning |
|--------|---------|
| `[your-value]` | User must replace with their value |
| `<required>` | Required parameter |
| `{variable}` | Variable interpolation |

---

## Section order

Standard how-to guide sections must appear in this order:

1. Title (H1)
2. Introduction (1-2 sentences, no heading)
3. Prerequisites (H2)
4. Steps (H2, with H3 for each step)
5. Verify your setup (H2)
6. Next steps (H2, optional)
7. Troubleshooting (H2, optional)

**Do not add:** Table of contents for how-to guides (too short), changelog, author information.
