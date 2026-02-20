# Setting Categories

Taxonomy for organizing and labeling settings and preferences.

---

## Table of contents
- [Category definitions](#category-definitions)
- [Setting types](#setting-types)
- [Label patterns](#label-patterns)
- [Description guidelines](#description-guidelines)

---

## Category definitions

### Standard setting categories

| Category | Contains | Example labels |
|----------|----------|----------------|
| **Account** | Identity, profile, authentication | Profile, Password, Email |
| **Notifications** | Alerts, emails, push messages | Email notifications, Push alerts |
| **Privacy** | Data sharing, visibility | Who can see, Data sharing |
| **Appearance** | Visual customization | Theme, Display, Language |
| **Accessibility** | Assistive features | Motion, Contrast, Screen reader |
| **Security** | Protection features | Two-factor, Login alerts |
| **Data** | Storage, exports, imports | Download data, Clear cache |
| **Integrations** | Connected services | Connected apps, API keys |
| **Billing** | Payment, subscriptions | Payment method, Plan |

### Category naming rules
- Use nouns (not verbs)
- Singular preferred: "Notification" not "Notifications"
- Max 2 words
- Plain language (no jargon)

---

## Setting types

### Toggle settings
```yaml
setting:
  type: "toggle"
  label: "[Noun phrase]"
  description: "What happens when ON"
  default: on|off
```
**Examples:**
- "Email notifications" / "Receive email updates for new messages"
- "Auto-save" / "Automatically save changes as you work"

### Selection settings
```yaml
setting:
  type: "selection"
  label: "[Noun phrase]"
  description: "What this controls"
  options:
    - value: "option_1"
      label: "[Readable label]"
```
**Examples:**
- "Theme" with options: Light, Dark, System

### Input settings
```yaml
setting:
  type: "input"
  label: "[Noun phrase]"
  placeholder: "[Example value]"
  description: "What this is used for"
```
**Examples:**
- "Display name" / "Jane Doe" / "How others see you"

---

## Label patterns

### Do
| Pattern | Example |
|---------|---------|
| Noun phrase | "Email notifications" |
| Describe the thing controlled | "Auto-play videos" |
| Be specific | "Marketing emails" vs "Emails" |

### Don't
| Pattern | Example | Fix |
|---------|---------|-----|
| Questions | "Do you want emails?" | "Email notifications" |
| Commands | "Turn on dark mode" | "Dark mode" |
| Negatives | "Don't show tips" | "Show tips" (toggle off) |
| Full sentences | "Enable email notifications" | "Email notifications" |

---

## Description guidelines

### When descriptions are needed
- Setting effect isn't obvious from label
- Setting has consequences user should know
- Setting requires context to understand

### When to omit descriptions
- Label is self-explanatory: "Language: English"
- Selection options are clear: "Theme: Light / Dark / System"

### Description patterns
| Type | Pattern | Example |
|------|---------|---------|
| What it does | "Receive [X] when [trigger]" | "Receive email when someone mentions you" |
| What changes | "[Thing] will [change]" | "Videos will play automatically" |
| Consequence | "This [enables/prevents] [outcome]" | "This prevents notifications at night" |

### Description constraints
- Max 80 characters
- One sentence
- No marketing language
- State facts, not benefits

---

## Complex setting patterns

### Grouped settings
```yaml
group:
  label: "Email notifications"
  description: "Choose which emails you receive"
  settings:
    - label: "Product updates"
      type: toggle
    - label: "Marketing"
      type: toggle
    - label: "Security alerts"
      type: toggle
      locked: true
      locked_reason: "Required for account security"
```

### Dependent settings
```yaml
setting:
  label: "Do not disturb"
  type: toggle
  children:
    - label: "Schedule"
      type: time-range
      depends_on: "do_not_disturb == true"
```

### Settings with consequences
```yaml
setting:
  label: "Delete account"
  type: action
  consequence: "destructive"
  confirmation_required: true
  description: "Permanently delete your account and all data"
```

---

## Anti-patterns

| Pattern | Problem | Fix |
|---------|---------|-----|
| Double negative | "Disable hiding" | "Show [thing]" |
| Jargon | "Enable SSO" | "Single sign-on" or expand |
| Vague labels | "Advanced" | Specific category name |
| Marketing speak | "Supercharge your workflow" | Describe actual function |
| Too many levels | 4+ nested groups | Flatten or redesign |
