# Templates

## Default setting structure

```md
**[Label]**
[Description of what happens]
[Control: toggle/select/input]
```

## Structured output format

```yaml
setting:
  category: "<account|notifications|privacy|appearance|integrations|advanced>"
  label: "<what it controls - max 40 chars>"
  description: "<what happens - max 120 chars, optional>"
  type: "<toggle|select|input|action>"
  default: "<default value>"
  options: ["<option1>", "<option2>"]  # for select type only
```

## Variations by setting type

### Toggle (on/off)
```yaml
setting:
  label: "Email notifications"
  description: "Receive email updates about activity in your projects."
  type: "toggle"
  default: true
```

### Select (choose from options)
```yaml
setting:
  label: "Theme"
  description: "Choose how the app looks."
  type: "select"
  default: "System"
  options: ["Light", "Dark", "System"]
```

### Input (text entry)
```yaml
setting:
  label: "Display name"
  description: "This is how your name appears to others."
  type: "input"
  default: null
  placeholder: "Enter your name"
```

### Action (button that does something)
```yaml
setting:
  label: "Export data"
  description: "Download a copy of all your data."
  type: "action"
  action_label: "Export"
```

## Section header patterns
- "Account" — profile, email, password
- "Notifications" — email, push, in-app
- "Privacy" — visibility, data sharing
- "Appearance" — theme, density, language
- "Integrations" — connected apps, APIs
- "Advanced" — developer options, experimental

## Allowed variations
- Omit description if label is completely self-explanatory
- Add helper text below input fields for format requirements
- Use "Learn more" links for complex settings with documentation
