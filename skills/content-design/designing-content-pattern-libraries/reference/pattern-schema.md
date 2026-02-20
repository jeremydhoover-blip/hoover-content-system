# Content Pattern Schema Reference

Canonical schema definition for content patterns. All patterns in the library must conform to this schema.

---

## Schema version

```
schema_version: 1.0.0
last_updated: 2024
```

---

## Pattern schema

```yaml
pattern:
  # Required fields
  id: string                    # Unique identifier (kebab-case)
  name: string                  # Human-readable name
  category: string              # Pattern category
  description: string           # What this pattern does
  
  # Structure definition
  structure:
    slots: array                # Content slots in pattern
      - name: string            # Slot identifier
        required: boolean       # Whether slot is mandatory
        type: string            # text | options | variable
        constraints:            # Slot-specific constraints
          max_chars: integer
          max_words: integer
          format: string
          allowed_values: array
    
    syntax: string              # How slots combine
    
  # Usage guidance
  usage:
    when_to_use: array          # Scenarios for this pattern
    when_not_to_use: array      # Anti-pattern scenarios
    platforms: array            # web | ios | android | all
    
  # Examples
  examples:
    minimal: string             # Simplest valid example
    typical: string             # Common usage example
    complex: string             # Full-featured example
    
  # Variants (optional)
  variants: array
    - id: string                # Variant identifier
      name: string              # Variant name
      modifies: object          # Slot overrides
      
  # Metadata
  metadata:
    created: date
    updated: date
    author: string
    status: string              # draft | active | deprecated
    related_patterns: array     # IDs of related patterns
```

---

## Field specifications

### Required fields

#### id
- Format: Kebab-case (`error-message-inline`)
- Unique across entire library
- Immutable once published
- 3-50 characters

#### name
- Format: Title case
- Human-readable, descriptive
- 3-60 characters

#### category
- Must match defined categories:
  - `feedback` (errors, success, status)
  - `guidance` (help, instructions, onboarding)
  - `action` (buttons, links, CTAs)
  - `navigation` (labels, menus, breadcrumbs)
  - `form` (labels, placeholders, validation)
  - `notification` (alerts, toasts, banners)
  - `empty-state` (no data, first use)
  - `confirmation` (dialogs, modals)

#### description
- Single sentence explaining pattern purpose
- 20-200 characters
- Starts with verb (describes what pattern does)

---

### Structure fields

#### slots
Array of content placeholders in the pattern.

**Slot properties**:

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Slot identifier (snake_case) |
| `required` | boolean | Yes | Is content mandatory |
| `type` | enum | Yes | `text`, `options`, `variable` |
| `constraints` | object | No | Validation rules |

**Slot types**:
- `text`: Free-form text content
- `options`: Choice from predefined values
- `variable`: Dynamic value insertion (names, numbers)

**Constraint options**:
```yaml
constraints:
  max_chars: 80           # Maximum character count
  max_words: 10           # Maximum word count
  min_chars: 1            # Minimum character count
  format: "sentence"      # sentence | fragment | question
  tone: "neutral"         # neutral | positive | urgent
  allowed_values:         # For 'options' type
    - "Save"
    - "Submit"
    - "Create"
  pattern: "^[A-Z]"       # Regex pattern
```

#### syntax
String showing how slots combine.

Format: Use `{slot_name}` for slot references.

Example:
```yaml
syntax: "{problem}. {solution}."
```

---

### Usage fields

#### when_to_use
Array of scenarios where pattern applies.

Example:
```yaml
when_to_use:
  - "User input fails validation"
  - "Form field has incorrect format"
  - "Required field is empty"
```

#### when_not_to_use
Array of scenarios where pattern is inappropriate.

Example:
```yaml
when_not_to_use:
  - "System-level errors (use error-message-banner)"
  - "Success feedback (use success-message)"
```

#### platforms
Array of platforms where pattern is valid.

Values: `web`, `ios`, `android`, `all`

---

### Example fields

All three example types required:

#### minimal
Simplest valid instance of the pattern.

#### typical
Most common usage in real applications.

#### complex
Full-featured usage with all optional slots.

---

### Variant fields (optional)

Variants modify the base pattern for specific contexts.

Example:
```yaml
variants:
  - id: "inline-with-icon"
    name: "With Icon"
    modifies:
      slots:
        icon:
          required: true
          type: options
          constraints:
            allowed_values: ["error", "warning", "info"]
```

---

### Metadata fields

#### status
- `draft`: In development, not for production
- `active`: Approved for production use
- `deprecated`: Being phased out, use alternative

#### related_patterns
Array of pattern IDs that complement or relate to this pattern.

---

## Full example

```yaml
pattern:
  id: error-message-inline
  name: Inline Error Message
  category: feedback
  description: Displays validation error adjacent to form field.
  
  structure:
    slots:
      - name: problem
        required: true
        type: text
        constraints:
          max_chars: 60
          format: fragment
      - name: solution
        required: false
        type: text
        constraints:
          max_chars: 40
          format: fragment
          
    syntax: "{problem}. {solution}."
    
  usage:
    when_to_use:
      - "Form field fails client-side validation"
      - "User input doesn't match expected format"
      - "Required field is left empty"
    when_not_to_use:
      - "Server-side errors after form submission"
      - "Multiple fields have errors (use summary)"
    platforms:
      - all
      
  examples:
    minimal: "Enter an email address"
    typical: "Enter a valid email address. Check for typos."
    complex: "This email is already registered. Try signing in or use a different email."
    
  variants:
    - id: error-message-inline-required
      name: Required Field Error
      modifies:
        slots:
          problem:
            constraints:
              allowed_values:
                - "This field is required"
                - "Please enter {field_name}"
                
  metadata:
    created: 2024-01-15
    updated: 2024-03-20
    author: content-design-team
    status: active
    related_patterns:
      - error-message-banner
      - error-message-toast
      - success-message-inline
```

---

## Validation rules

### Schema validation

1. All required fields present
2. Field types match specification
3. Enum values from allowed list
4. Cross-references resolve (related_patterns exist)

### Content validation

1. Examples satisfy slot constraints
2. Syntax uses all required slots
3. Each slot referenced in syntax
4. Examples match syntax structure

### Consistency validation

1. ID unique across library
2. Category from approved list
3. Related patterns are bidirectional
4. Deprecated patterns have replacement reference
