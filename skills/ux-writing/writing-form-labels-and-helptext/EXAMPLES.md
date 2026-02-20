# Examples

## Example 1: Simple text field
**Input:**
- Purpose: Collect user's full name
- Required: Yes
- Constraints: None

**Output:**
```yaml
form_field:
  label: "Full name"
  required: true
  input_type: "text"
  placeholder: null
  help_text: null
  validation:
    - rule: "required"
      error: "Enter your name"
```

---

## Example 2: Email with validation
**Input:**
- Purpose: Account email address
- Required: Yes
- Constraints: Must be valid email format

**Output:**
```yaml
form_field:
  label: "Email address"
  required: true
  input_type: "email"
  placeholder: "you@example.com"
  help_text: null
  validation:
    - rule: "required"
      error: "Enter your email address"
    - rule: "valid_email"
      error: "Enter a valid email address"
```

---

## Example 3: Password with requirements
**Input:**
- Purpose: Set account password
- Required: Yes
- Constraints: Min 8 chars, must include number

**Output:**
```yaml
form_field:
  label: "Password"
  required: true
  input_type: "password"
  placeholder: null
  help_text: "At least 8 characters with one number"
  validation:
    - rule: "required"
      error: "Enter a password"
    - rule: "min_length_8"
      error: "Use at least 8 characters"
    - rule: "has_number"
      error: "Include at least one number"
```

---

## Example 4: Optional phone number
**Input:**
- Purpose: Phone for account recovery
- Required: No
- Constraints: None, but format hint helpful

**Output:**
```yaml
form_field:
  label: "Phone number"
  required: false
  input_type: "tel"
  placeholder: "(555) 555-5555"
  help_text: "For account recovery only"
  optional_indicator: "(optional)"
  validation: null
```

---

## Example 5: Dropdown select
**Input:**
- Purpose: Select user's country
- Required: Yes
- Options: List of countries

**Output:**
```yaml
form_field:
  label: "Country"
  required: true
  input_type: "select"
  placeholder: "Select a country"
  help_text: null
  options: ["United States", "Canada", "United Kingdom", "..."]
  validation:
    - rule: "required"
      error: "Select your country"
```

---

## Edge case: Credit card number
**Input:**
- Purpose: Payment card number
- Required: Yes
- Constraints: 16 digits, formatted

**Output:**
```yaml
form_field:
  label: "Card number"
  required: true
  input_type: "text"
  placeholder: "1234 5678 9012 3456"
  help_text: null
  inputmode: "numeric"
  validation:
    - rule: "required"
      error: "Enter your card number"
    - rule: "valid_card"
      error: "Enter a valid card number"
```

---

## Edge case: Textarea with character limit
**Input:**
- Purpose: Bio or description
- Required: No
- Constraints: Max 280 characters

**Output:**
```yaml
form_field:
  label: "Bio"
  required: false
  input_type: "textarea"
  placeholder: "Tell us about yourself"
  help_text: "Max 280 characters"
  optional_indicator: "(optional)"
  max_length: 280
  show_character_count: true
  validation:
    - rule: "max_length_280"
      error: "Bio must be 280 characters or fewer"
```
