# Alt Text Patterns

Reference for writing effective alt text by image type and context.

---

## Table of contents
- [Decision tree](#decision-tree)
- [Patterns by image type](#patterns-by-image-type)
- [Context-dependent examples](#context-dependent-examples)
- [Common mistakes](#common-mistakes)

---

## Decision tree

```
Is the image purely decorative (adds no information)?
├── Yes → alt="" (empty)
└── No → Does it contain text?
    ├── Yes → Is the text also in surrounding content?
    │   ├── Yes → alt="" (avoid repetition)
    │   └── No → Include the text in alt
    └── No → Is it a functional image (link/button)?
        ├── Yes → Describe the action/destination
        └── No → Is it complex (chart/diagram)?
            ├── Yes → Short alt + long description
            └── No → Describe what matters in context
```

---

## Patterns by image type

### Informative photos
**Pattern:** Describe what's shown and why it matters in this context.

```yaml
# Product photo
alt: "ProBook 15 laptop, silver, open showing 15-inch display"

# Team photo
alt: "Customer support team of five people at help desk"

# Screenshot
alt: "Dashboard showing monthly revenue chart and key metrics"
```

### Decorative images
**Pattern:** Empty alt attribute, optionally aria-hidden.

```yaml
# Background pattern
alt: ""
aria_hidden: true

# Divider graphic
alt: ""

# Mood image that repeats text content
alt: ""
```

### Functional images (icons, buttons)
**Pattern:** Describe what happens when activated.

```yaml
# Search icon button
alt: "Search"

# Close button (X icon)
alt: "Close"

# External link icon
alt: "Opens in new window"

# Download icon
alt: "Download"
```

### Image links
**Pattern:** Describe destination, not the image.

```yaml
# Logo linking to home
alt: "Acme Corp home"

# Social media icon
alt: "Follow us on Twitter"

# Product thumbnail linking to detail
alt: "View ProBook 15 details"
```

### Charts and graphs
**Pattern:** Summarize key insight in alt, provide full data separately.

```yaml
# Bar chart
alt: "Bar chart: Q4 sales highest in Northeast at $2.4M"
aria_describedby: "chart-data-table"

# Line graph
alt: "Line graph showing 25% revenue growth from January to December"

# Pie chart
alt: "Pie chart: Mobile users 60%, Desktop 35%, Tablet 5%"
```

### Diagrams and infographics
**Pattern:** Short summary + extended description.

```yaml
# Process diagram
alt: "Four-step onboarding flow from signup to first project"
longdesc: "#onboarding-steps-detail"

# Infographic
alt: "2025 industry trends: AI adoption, remote work, sustainability"
aria_describedby: "infographic-full-text"
```

### Icons with text
**Pattern:** Usually decorative when text provides meaning.

```yaml
# Icon + "Settings" label
icon_alt: ""  # Text provides meaning

# Icon + "Email: contact@example.com"
icon_alt: ""  # Text provides meaning

# Icon alone conveying status
icon_alt: "Error"  # Icon is only indicator
```

---

## Context-dependent examples

The same image may need different alt text in different contexts.

### Example: Photo of person at laptop

**On "About Us" page:**
```yaml
alt: "Sarah Chen, VP of Engineering, working at her desk"
# Identity matters
```

**On "Remote Work" blog post:**
```yaml
alt: "Employee working from home office with dual monitors"
# Situation matters
```

**On "Laptop Stands" product page:**
```yaml
alt: "Laptop on adjustable stand at eye level"
# Product placement matters
```

**As decorative header image:**
```yaml
alt: ""
# No information added to page content
```

### Example: Company logo

**On home page header:**
```yaml
alt: "Acme Corp"
# Just the name
```

**On partner page listing multiple logos:**
```yaml
alt: "Acme Corp logo"
# Distinguish from other content
```

**Linking to home from another page:**
```yaml
alt: "Acme Corp home"
# Indicates destination
```

---

## Common mistakes

### Using filename
```yaml
# Wrong
alt: "IMG_2847.jpg"
alt: "hero-banner-v2-final.png"

# Right
alt: "Customer using mobile app at coffee shop"
```

### Starting with "image of" or "photo of"
```yaml
# Wrong
alt: "Image of a laptop"
alt: "Photo of the team"

# Right
alt: "Laptop displaying code editor"
alt: "Engineering team at quarterly planning meeting"
```

### Too vague
```yaml
# Wrong
alt: "Person"
alt: "Graph"
alt: "Screenshot"

# Right
alt: "Customer support representative wearing headset"
alt: "Line graph showing 40% increase in signups"
alt: "Account settings page with profile form"
```

### Too verbose
```yaml
# Wrong (85 words)
alt: "This image shows a beautiful photograph of our modern 
office space located in downtown San Francisco, featuring 
an open floor plan with standing desks, collaborative 
meeting areas, a fully stocked kitchen, and floor-to-ceiling 
windows with views of the Bay Bridge, taken during the 
golden hour of sunset which creates a warm and inviting 
atmosphere for our dedicated team members."

# Right (12 words)
alt: "Open-plan office with standing desks and Bay Bridge view"
```

### Describing decorative images
```yaml
# Wrong (for decorative divider)
alt: "Blue gradient horizontal line divider element"

# Right
alt: ""
```

### Missing alt attribute entirely
```yaml
# Wrong
<img src="product.jpg">

# Right (informative)
<img src="product.jpg" alt="ProBook 15 in silver">

# Right (decorative)
<img src="divider.png" alt="">
```

---

## Character limits

| Context | Recommended max | Notes |
|---------|-----------------|-------|
| Simple images | 125 characters | Fits most screen reader buffers |
| Complex images | 150 characters | Summary only; use long description |
| Functional images | 50 characters | Action words are short |
| Decorative | 0 characters | Empty alt="" |

---

## Testing alt text

### Screen reader test
1. Navigate to image with screen reader
2. Listen to announcement
3. Ask: Does this give equivalent information?

### Image-off test
1. Disable images in browser
2. Read alt text displayed
3. Ask: Can I understand the page content?

### Context test
1. Read alt text in isolation
2. Ask: Does it make sense without seeing the image?
3. Ask: Is it appropriate for this specific context?
