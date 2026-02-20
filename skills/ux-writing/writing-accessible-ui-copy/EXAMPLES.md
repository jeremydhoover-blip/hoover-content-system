# Examples: Writing Accessible UI Copy

Practical examples demonstrating accessible content patterns across common UI scenarios.

---

## Table of contents
- [Example 1: Image alt text](#example-1-image-alt-text)
- [Example 2: Button labels](#example-2-button-labels)
- [Example 3: Link text](#example-3-link-text)
- [Example 4: Form accessibility](#example-4-form-accessibility)
- [Example 5: Status announcements](#example-5-status-announcements)
- [Example 6: Data visualization](#example-6-data-visualization)
- [Anti-patterns](#anti-patterns)

---

## Example 1: Image alt text

### Scenario
Product page with hero image, decorative background, product photo, and chart.

### Before (inaccessible)
```yaml
hero_image:
  alt: "hero-banner-summer-2025.jpg"
  # Problem: Filename, not description

background:
  alt: "abstract blue pattern"
  # Problem: Describes decorative image unnecessarily

product_photo:
  alt: "laptop"
  # Problem: Too vague, no context

chart:
  alt: "chart showing data"
  # Problem: Doesn't convey the information
```

### After (accessible)
```yaml
hero_image:
  type: "informative"
  alt: "Person using laptop on outdoor patio, summer collection"
  # Describes what matters for this context

background:
  type: "decorative"
  alt: ""
  aria_hidden: true
  # Empty alt for decorative images

product_photo:
  type: "informative"
  alt: "ProBook 15 laptop, silver, shown open at 45-degree angle"
  # Specific product identification

chart:
  type: "complex"
  alt: "Bar chart: Customer satisfaction increased 23% year over year"
  aria_describedby: "chart-description"
  # Summary in alt, full data available separately
```

### Why it works
- Informative images describe what matters in context
- Decorative images don't distract screen reader users
- Product images identify the specific product
- Charts summarize the key insight, with data available

---

## Example 2: Button labels

### Scenario
Document editor with multiple save options and actions.

### Before (inaccessible)
```yaml
buttons:
  - label: "Save"
  - label: "Save"       # Duplicate!
  - label: "Submit"
  - label: "Click to delete"
  - label: "X"
```

### After (accessible)
```yaml
buttons:
  - label: "Save draft"
    action: "Saves current document as draft"
    
  - label: "Save and publish"
    action: "Saves and makes document public"
    
  - label: "Submit for review"
    action: "Sends to approver"
    
  - label: "Delete document"
    action: "Permanently removes document"
    aria_describedby: "delete-warning"
    
  - label: "Close"
    aria_label: "Close dialog"
    # Visual X icon, but needs text for screen readers
```

### Why it works
- Each button is unique and specific
- Action + object pattern makes purpose clear
- Icon-only buttons have accessible names
- Related context available via aria-describedby

---

## Example 3: Link text

### Scenario
Pricing page with multiple "Learn more" opportunities.

### Before (inaccessible)
```yaml
links:
  - text: "Click here"
    destination: "/pricing"
    
  - text: "Learn more"
    destination: "/features/analytics"
    
  - text: "Learn more"
    destination: "/features/reporting"
    
  - text: "here"
    context: "Download the PDF here"
```

### After (accessible)
```yaml
links:
  - text: "View pricing plans"
    destination: "/pricing"
    
  - text: "Explore analytics features"
    destination: "/features/analytics"
    
  - text: "See reporting capabilities"
    destination: "/features/reporting"
    
  - text: "Download the 2025 report (PDF, 2.4 MB)"
    destination: "/reports/2025-annual.pdf"
    # Indicates format and file size
```

### Screen reader links list test
When a screen reader user pulls up a list of all links on the page:

**Before:**
- Click here
- Learn more
- Learn more
- here

**After:**
- View pricing plans
- Explore analytics features
- See reporting capabilities
- Download the 2025 report (PDF, 2.4 MB)

### Why it works
- Each link is meaningful without surrounding context
- Destinations are clear
- File format and size indicated for downloads
- No duplicates that confuse navigation

---

## Example 4: Form accessibility

### Scenario
Contact form with name, email, and message fields.

### Before (inaccessible)
```html
<!-- Placeholder as label (disappears on focus) -->
<input type="text" placeholder="Your name">

<!-- Label not associated -->
<label>Email</label>
<input type="email" placeholder="Enter email">

<!-- Error not associated with field -->
<input type="text" id="phone">
<span class="error" style="color: red;">Invalid phone number</span>
```

### After (accessible)
```yaml
form:
  fields:
    - name: "full_name"
      label:
        text: "Full name"
        for: "full_name"
      input:
        id: "full_name"
        type: "text"
        required: true
        aria_required: true
        
    - name: "email"
      label:
        text: "Email address"
        for: "email"
      input:
        id: "email"
        type: "email"
        required: true
        aria_describedby: "email-help"
      help_text:
        id: "email-help"
        text: "We'll send confirmation to this address"
        
    - name: "phone"
      label:
        text: "Phone number (optional)"
        for: "phone"
      input:
        id: "phone"
        type: "tel"
        aria_describedby: "phone-error"
        aria_invalid: true
      error:
        id: "phone-error"
        role: "alert"
        text: "Enter a valid phone number (e.g., 555-123-4567)"
```

### Why it works
- Visible labels always present (not just placeholder)
- Labels programmatically associated with inputs
- Help text connected via aria-describedby
- Errors identify field and suggest format
- Required fields indicated accessibly

---

## Example 5: Status announcements

### Scenario
E-commerce cart with add/remove actions and checkout flow.

### Before (inaccessible)
```yaml
# Visual-only feedback
add_to_cart:
  animation: "Item flies into cart icon"
  # No announcement for screen readers

remove_item:
  visual: "Item fades out"
  # No confirmation

checkout_error:
  display: "Red banner at top of page"
  # User may not know it appeared
```

### After (accessible)
```yaml
add_to_cart:
  visual: "Item animation + cart badge update"
  announcement:
    text: "Wireless headphones added to cart. Cart total: 3 items."
    aria_live: "polite"
    
remove_item:
  visual: "Item removed from list"
  announcement:
    text: "Wireless headphones removed from cart."
    aria_live: "polite"
    
checkout_error:
  visual: "Red banner with error icon"
  announcement:
    text: "Payment failed. Please check your card details and try again."
    aria_live: "assertive"
    role: "alert"
    
form_submission:
  visual: "Success checkmark"
  announcement:
    text: "Order confirmed. Confirmation number: 12345."
    aria_live: "polite"
```

### Why it works
- Status changes announced to screen readers
- Polite announcements for routine updates
- Assertive announcements for critical errors
- Content is specific and actionable

---

## Example 6: Data visualization

### Scenario
Dashboard with sales performance chart.

### Before (inaccessible)
```yaml
chart:
  alt: "Sales chart"
  # No data accessible to screen readers
  # Color-coded without labels
```

### After (accessible)
```yaml
chart:
  alt: "Bar chart showing Q4 2025 sales by region. Northeast leads at $2.4M."
  aria_describedby: "chart-details"
  
  long_description:
    id: "chart-details"
    content: |
      Q4 2025 Regional Sales:
      - Northeast: $2.4 million (highest)
      - West: $1.9 million
      - Southeast: $1.7 million
      - Midwest: $1.2 million
      Total Q4 sales: $7.2 million, up 15% from Q3.
      
  data_table:
    caption: "Q4 2025 Sales by Region"
    available: true
    location: "Below chart, expandable"
    
  design:
    patterns: true  # Not color alone
    labels: "On each bar"
    legend: "Pattern + color key"
```

### Why it works
- Alt text gives key insight (not just "chart")
- Full data available in text form
- Data table as alternative for detailed exploration
- Visual design doesn't rely on color alone

---

## Anti-patterns

### Don't do this

| Pattern | Problem | Fix |
|---------|---------|-----|
| `alt="image"` | Meaningless | Describe what matters |
| `alt="IMG_2847.jpg"` | Filename, not content | Write description |
| Placeholder as label | Disappears, accessibility fail | Use visible label |
| "Click here" | Meaningless out of context | Describe destination |
| "Read more" x 5 | Indistinguishable | Make each unique |
| Color-only error | Invisible to colorblind | Add icon + text |
| `<div onclick>` | Not keyboard accessible | Use `<button>` |
| Heading for styling | Breaks navigation | Use CSS for styling |
| ALL CAPS | Harder to read | Sentence case |
| "See image above" | Assumes visual | Describe directly |

### Test questions
Before shipping, verify:

1. **Links list test**: Do all links make sense in a list without context?
2. **Headings test**: Does heading navigation tell the page story?
3. **Tab test**: Can you complete the task with keyboard only?
4. **Grayscale test**: Is all information still clear without color?
5. **Screen reader test**: Is the experience equivalent, not just compliant?
