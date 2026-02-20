# Templates: Writing Accessible UI Copy

Structured templates for creating accessible content across common UI patterns.

---

## Table of contents
- [Alt text template](#alt-text-template)
- [Button label template](#button-label-template)
- [Link text template](#link-text-template)
- [Form field template](#form-field-template)
- [Heading structure template](#heading-structure-template)
- [Status announcement template](#status-announcement-template)
- [Error message template](#error-message-template)
- [Data visualization template](#data-visualization-template)

---

## Alt text template

```yaml
alt_text:
  image_type: "[informative|decorative|functional|complex]"
  
  # For informative images
  informative:
    content: "[What the image shows]"
    context: "[Why it matters in this context]"
    alt: "[Concise description: what + why, max 125 chars]"
  
  # For decorative images
  decorative:
    alt: ""
    aria_hidden: true
  
  # For functional images (icons, buttons)
  functional:
    action: "[What clicking/activating does]"
    alt: "[Action verb + object]"
  
  # For complex images (charts, diagrams)
  complex:
    summary_alt: "[Brief summary, max 125 chars]"
    long_description: "[Full description via aria-describedby or link]"
```

### Alt text decision tree
```
Is the image purely decorative?
├── Yes → alt=""
└── No → Does it convey information?
    ├── Yes → Is it complex (chart/diagram)?
    │   ├── Yes → Short alt + long description
    │   └── No → Concise descriptive alt
    └── No → Is it functional (button/link)?
        ├── Yes → Describe the action
        └── No → Evaluate if truly needed
```

---

## Button label template

```yaml
button:
  context: "[Screen/feature context]"
  action: "[What happens when clicked]"
  object: "[What is being acted upon]"
  
  label:
    pattern: "[Verb] + [object]"
    examples:
      - "Save draft"
      - "Delete account"
      - "Add to cart"
    
  constraints:
    max_chars: 25
    starts_with_verb: true
    unique_on_page: true  # Avoid multiple "Submit" buttons
    
  accessibility:
    aria_label: "[Only if visible text insufficient]"
    aria_describedby: "[ID of element with additional context]"
```

---

## Link text template

```yaml
link:
  destination: "[Where the link goes]"
  context: "[Surrounding content]"
  
  label:
    pattern: "[Descriptive of destination]"
    
    # Good patterns
    good:
      - "View pricing plans"
      - "Read the accessibility guide"
      - "Download the report (PDF, 2.3 MB)"
    
    # Avoid these
    avoid:
      - "Click here"
      - "Learn more"
      - "Read more"
      - "Here"
    
  constraints:
    meaningful_alone: true  # Must make sense out of context
    indicates_format: "[If non-HTML: PDF, DOC, external]"
    indicates_behavior: "[If opens new window, downloads, etc.]"
    
  accessibility:
    # Only use aria-label if visible text cannot be made descriptive
    aria_label: "[Full description if link text is constrained]"
```

---

## Form field template

```yaml
form_field:
  field_name: "[Internal identifier]"
  field_type: "[text|email|password|select|checkbox|radio|textarea]"
  
  label:
    text: "[Visible label text]"
    position: "[above|beside]"  # Above preferred for accessibility
    required_indicator: "[*|'(required)'|'(optional)']"
    
  help_text:
    text: "[Additional guidance]"
    position: "below_field"
    association: "aria-describedby"
    
  placeholder:
    text: "[Example or format hint]"
    # Never use as replacement for label
    
  error:
    text: "[What's wrong] + [How to fix]"
    association: "aria-describedby"
    aria_invalid: true
    
  constraints:
    label_always_visible: true
    help_not_in_placeholder: true
    error_near_field: true
```

---

## Heading structure template

```yaml
page_headings:
  page_title: "[h1 - One per page, describes page purpose]"
  
  sections:
    - level: "h2"
      text: "[Major section name]"
      subsections:
        - level: "h3"
          text: "[Subsection name]"
          
  rules:
    one_h1_per_page: true
    no_skipping_levels: true  # h1 → h2 → h3, never h1 → h3
    descriptive_text: true    # Not "Section 1"
    logical_hierarchy: true   # Reflects content structure
    
  validation:
    - "Does h1 describe the page purpose?"
    - "Do h2s represent major sections?"
    - "Could someone navigate by headings alone?"
    - "Are heading levels sequential?"
```

---

## Status announcement template

```yaml
status_announcement:
  trigger: "[What caused this status]"
  
  message:
    text: "[What happened or changed]"
    max_chars: 80
    
  aria_live:
    region: "[polite|assertive]"
    # polite: Waits for pause in speech
    # assertive: Interrupts immediately (use sparingly)
    
  patterns:
    success:
      aria_live: "polite"
      example: "Settings saved"
    error:
      aria_live: "assertive"
      example: "Connection lost. Changes not saved."
    progress:
      aria_live: "polite"
      example: "Uploading: 50% complete"
    count_change:
      aria_live: "polite"
      example: "3 results found"
      
  constraints:
    concise: true
    no_redundant_words: true  # Not "Status: Success"
    action_focused: true      # What happened, not just state
```

---

## Error message template

```yaml
accessible_error:
  field: "[Associated form field]"
  
  message:
    what_wrong: "[Specific problem]"
    how_fix: "[Clear action to resolve]"
    
    pattern: "[What's wrong]. [How to fix]."
    max_chars: 80
    
  accessibility:
    aria_invalid: true
    aria_describedby: "[error-message-id]"
    role: "alert"  # For critical errors
    
  examples:
    required:
      message: "Email is required. Enter your email address."
    format:
      message: "Enter a valid email address (e.g., name@company.com)."
    constraint:
      message: "Password must be at least 8 characters."
```

---

## Data visualization template

```yaml
data_visualization:
  type: "[chart|graph|diagram|infographic]"
  
  accessibility:
    alt_text:
      summary: "[Key takeaway in 125 chars]"
      example: "Line chart showing revenue growth of 25% from Q1 to Q4 2025"
      
    long_description:
      method: "[aria-describedby|details element|linked page]"
      content: |
        [Full description including:]
        - Chart type and what it represents
        - Key data points
        - Trends or patterns
        - Source and date
        
    data_table:
      provide: true  # Alternative for screen readers
      location: "[below chart|linked|expandable]"
      
  design_requirements:
    not_color_alone: true  # Use patterns, labels
    sufficient_contrast: true
    clear_labels: true
```

---

## Accessibility checklist template

```yaml
accessibility_review:
  component: "[Component being reviewed]"
  
  checklist:
    perceivable:
      - alt_text_complete: "[yes|no|na]"
      - contrast_sufficient: "[yes|no]"
      - not_color_alone: "[yes|no]"
      
    understandable:
      - plain_language: "[yes|no]"
      - consistent_terms: "[yes|no]"
      - clear_instructions: "[yes|no]"
      
    operable:
      - keyboard_accessible: "[yes|no]"
      - focus_visible: "[yes|no]"
      - no_time_limits: "[yes|no|justified]"
      
    robust:
      - valid_markup: "[yes|no]"
      - aria_correct: "[yes|no]"
      - tested_with_at: "[screen reader used]"
      
  notes: "[Additional observations]"
```
