# Templates

## Default form field structure

```md
**[Label]** (optional indicator if applicable)
[Input field with placeholder]
[Help text below field]
```

## Structured output format

```yaml
form_field:
  label: "<what to enter - max 40 chars>"
  required: <true|false>
  input_type: "<text|email|password|tel|url|number|date|select|textarea>"
  placeholder: "<format hint - max 40 chars, optional>"
  help_text: "<constraints or context - max 100 chars, optional>"
  validation:
    - rule: "<validation rule>"
      error: "<error message - max 80 chars>"
```

## Variations by input type

### Text input
```yaml
form_field:
  label: "Full name"
  required: true
  input_type: "text"
  placeholder: null
  help_text: null
```

### Email input
```yaml
form_field:
  label: "Email address"
  required: true
  input_type: "email"
  placeholder: "name@company.com"
  help_text: null
  validation:
    - rule: "valid_email"
      error: "Enter a valid email address"
```

### Password input
```yaml
form_field:
  label: "Password"
  required: true
  input_type: "password"
  placeholder: null
  help_text: "At least 8 characters with a number and symbol"
  validation:
    - rule: "min_length_8"
      error: "Password must be at least 8 characters"
    - rule: "has_number"
      error: "Include at least one number"
    - rule: "has_symbol"
      error: "Include at least one symbol"
```

### Select/dropdown
```yaml
form_field:
  label: "Country"
  required: true
  input_type: "select"
  placeholder: "Select a country"
  help_text: null
  options: ["United States", "Canada", "..."]
```

### Optional field
```yaml
form_field:
  label: "Phone number"
  required: false
  input_type: "tel"
  placeholder: "(555) 555-5555"
  help_text: "Optional. We'll only use this for account recovery."
  optional_indicator: "(optional)"
```

## Allowed variations
- Show "(optional)" next to optional fields, or "(required)" if most fields are optional
- Use inline validation errors below the field
- Group related fields (e.g., first name + last name on same row)
