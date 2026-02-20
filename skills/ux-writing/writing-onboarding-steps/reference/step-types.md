# Step Types

Taxonomy of onboarding step types and their appropriate treatments.

---

## Table of contents
- [Step type definitions](#step-type-definitions)
- [Step patterns by type](#step-patterns-by-type)
- [Progress indication](#progress-indication)
- [Skip and escape patterns](#skip-and-escape-patterns)

---

## Step type definitions

| Type | Purpose | User action | Skippable? |
|------|---------|-------------|------------|
| **welcome** | Greet, set expectations | Read, proceed | No |
| **setup-required** | Configure essential settings | Complete form/action | No |
| **setup-optional** | Configure nice-to-have settings | Complete or skip | Yes |
| **education** | Teach feature/concept | Read, proceed | Yes |
| **activation** | Encourage first meaningful action | Take action | Yes |
| **completion** | Confirm setup done, celebrate | Proceed to app | No |

---

## Step patterns by type

### Welcome step
```yaml
step:
  type: "welcome"
  headline: "Welcome to [Product]"
  body: "Quick overview or value prop. Time estimate for full flow."
  action:
    primary: "Get started"
    secondary: null
```

### Setup-required step
```yaml
step:
  type: "setup-required"
  headline: "[Action verb] your [thing]"
  body: "Why this matters."
  action:
    primary: "Continue"
    secondary: null
  input_required: true
```

### Setup-optional step
```yaml
step:
  type: "setup-optional"
  headline: "[Action verb] your [thing]"
  body: "Why this helps (optional framing)."
  action:
    primary: "Continue"
    secondary: "Skip for now"
```

### Education step
```yaml
step:
  type: "education"
  headline: "This is your [feature]"
  body: "What it does and why it's useful."
  action:
    primary: "Next"
    secondary: "Skip tour"
```

### Activation step
```yaml
step:
  type: "activation"
  headline: "[Create/Start] your first [thing]"
  body: "Encouragement to take first action."
  action:
    primary: "[Create/Start] [thing]"
    secondary: "I'll do this later"
```

### Completion step
```yaml
step:
  type: "completion"
  headline: "You're all set!"
  body: "Summary or what to do next."
  action:
    primary: "Go to [destination]"
    secondary: null
```

---

## Progress indication

### When to show progress
| Flow length | Show progress? | Format |
|-------------|----------------|--------|
| 1-2 steps | No | — |
| 3-5 steps | Yes | "Step X of Y" or dots |
| 6-7 steps | Yes | Progress bar |
| 8+ steps | Reconsider flow | Break into sections |

### Progress formats
```
Numbered:     Step 2 of 5
Dots:         ● ● ○ ○ ○
Bar:          [████░░░░░░] 40%
Sectioned:    Account > Team > Preferences
```

---

## Skip and escape patterns

### Skip link placement
- Below primary action
- Subtle visual treatment (text link, not button)
- Clear but not prominent

### Skip copy patterns
| Context | Skip label |
|---------|------------|
| Optional step | "Skip for now" |
| Feature tour | "Skip tour" |
| Deferrable action | "I'll do this later" |
| Multiple steps | "Skip all" (use sparingly) |

### When skip should NOT be offered
- Required setup (account name, essential config)
- Legal agreements
- Security setup (if mandatory)

---

## Sequencing guidelines

### Recommended order
1. Welcome (set expectations)
2. Required setup (essential config)
3. Optional setup (if any)
4. Education (feature tour)
5. Activation (first action)
6. Completion (celebrate)

### Avoid
- Education before user understands context
- Activation before required setup
- Optional steps mixed with required (confusing)
- More than 7 total steps

---

## Anti-patterns

| Pattern | Problem | Fix |
|---------|---------|-----|
| No progress indicator | User doesn't know how long | Add progress |
| Required step with skip | Confusing, may break setup | Remove skip or make optional |
| "Tutorial" as welcome | Promises too much time | Focus on quick setup |
| 10+ steps | Abandonment risk | Reduce or section |
| No completion step | Setup feels incomplete | Add brief confirmation |
