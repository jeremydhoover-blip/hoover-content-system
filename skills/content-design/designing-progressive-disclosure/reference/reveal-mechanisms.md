# Reveal Mechanisms Reference

Catalog of UI mechanisms for progressive disclosure, with usage guidelines.

---

## Mechanism taxonomy

### Click/tap reveal

#### Accordion
**Behavior**: Header click expands/collapses content panel.

| Attribute | Specification |
|-----------|---------------|
| Trigger | Click header row |
| Animation | Expand/collapse, 200-300ms |
| State indicator | Chevron rotation or +/- |
| Multi-open | Designer choice (default: one at a time) |

**Best for**:
- Long lists of items with details
- FAQ patterns
- Settings categories
- Grouped form sections

**Copy requirements**:
| Element | Pattern | Example |
|---------|---------|---------|
| Header | Noun phrase (category) | Billing information |
| Expanded content | Full detail | Address fields, payment history |
| State (optional) | Summary when collapsed | "3 addresses saved" |

---

#### Expandable row
**Behavior**: Row click reveals inline detail panel.

| Attribute | Specification |
|-----------|---------------|
| Trigger | Click row or expand icon |
| Animation | Row expansion, 200ms |
| State indicator | Caret/chevron |
| Context | Maintains position in list |

**Best for**:
- Tables with supplementary detail
- List items needing preview
- Order/transaction history

**Copy requirements**:
| Element | Pattern | Example |
|---------|---------|---------|
| Row content | Key identifiers | Order #1234 - $45.00 |
| Expanded content | Full details | Line items, timestamps, actions |

---

#### Disclosure triangle
**Behavior**: Small control reveals nested content.

| Attribute | Specification |
|-----------|---------------|
| Trigger | Click triangle/arrow icon |
| Animation | Instant or 150ms |
| State indicator | Triangle rotation (▶ → ▼) |
| Nesting | Supports multiple levels |

**Best for**:
- File trees
- Nested navigation
- Hierarchical data

**Copy requirements**:
| Element | Pattern | Example |
|---------|---------|---------|
| Node label | Item name | Documents |
| Children | Nested items | File1.pdf, File2.doc |

---

### Hover reveal

#### Tooltip
**Behavior**: Hover displays floating text panel.

| Attribute | Specification |
|-----------|---------------|
| Trigger | Hover (desktop), long-press (mobile) |
| Delay | 300-500ms before appear |
| Duration | Disappear on mouse leave |
| Position | Above element, auto-reposition |

**Best for**:
- Icon-only buttons
- Truncated text
- Supplementary definitions
- Keyboard shortcut hints

**Copy requirements**:
| Element | Max chars | Example |
|---------|-----------|---------|
| Content | 100 chars | "Share this document with others via link or email" |

**Constraints**:
- No interactive content (links, buttons)
- Not for critical information (accessibility)
- Single paragraph maximum

---

#### Hover card
**Behavior**: Hover displays rich content panel.

| Attribute | Specification |
|-----------|---------------|
| Trigger | Hover with 500ms delay |
| Duration | Persistent while hovering card |
| Position | Near trigger, auto-reposition |
| Content | Rich: images, links, actions |

**Best for**:
- User profile previews
- Link previews
- Product previews in lists

**Copy requirements**:
| Element | Pattern | Example |
|---------|---------|---------|
| Title | Primary identifier | John Smith |
| Summary | Key attributes | Product Designer · San Francisco |
| Action (optional) | Verb | View profile |

---

### Navigation reveal

#### Tabs
**Behavior**: Tab click switches visible panel.

| Attribute | Specification |
|-----------|---------------|
| Trigger | Click tab label |
| Animation | Instant switch or slide |
| State indicator | Active tab styling |
| URL update | Optional (deep linking) |

**Best for**:
- Parallel content categories
- Different views of same data
- Related but separate sections

**Copy requirements**:
| Element | Max chars | Example |
|---------|-----------|---------|
| Tab label | 15 chars | Overview, Activity, Settings |

**Constraints**:
- 2-6 tabs maximum
- Labels must differentiate clearly
- All tabs should be equally weighted

---

#### Segmented control
**Behavior**: Toggle between 2-4 mutually exclusive options.

| Attribute | Specification |
|-----------|---------------|
| Trigger | Click segment |
| Animation | Instant with indicator slide |
| State indicator | Filled/highlighted segment |

**Best for**:
- View mode toggles (list/grid)
- Time range selection (day/week/month)
- Filter toggles (all/active/completed)

**Copy requirements**:
| Element | Max chars | Example |
|---------|-----------|---------|
| Segment label | 10 chars | All, Active, Done |

---

#### Stepper/wizard
**Behavior**: Sequential step navigation with content reveal.

| Attribute | Specification |
|-----------|---------------|
| Trigger | Next/previous buttons or step click |
| Animation | Slide or fade transition |
| State indicator | Step progress (numbers, checkmarks) |
| Back navigation | Always enabled for completed steps |

**Best for**:
- Multi-step forms
- Onboarding flows
- Complex task workflows

**Copy requirements**:
| Element | Pattern | Example |
|---------|---------|---------|
| Step label | Noun or verb phrase | Account details / Create account |
| Progress | Step X of Y | Step 2 of 4 |
| Next action | Verb or "Next" | Continue, Next |
| Back action | "Back" | Back |

---

### Modal reveal

#### Dialog/modal
**Behavior**: Overlay displays focused content, blocking background.

| Attribute | Specification |
|-----------|---------------|
| Trigger | Button click, action initiation |
| Animation | Fade in with backdrop, 200ms |
| Dismissal | X button, backdrop click, Escape key |
| Focus trap | Yes (accessibility) |

**Best for**:
- Confirmations
- Focused data entry
- Critical alerts
- Preview/detail views

**Copy requirements**:
| Element | Pattern | Example |
|---------|---------|---------|
| Title | Action or question | Delete file? / Add team member |
| Body | Context, consequence | This will permanently delete... |
| Primary action | Verb matching title | Delete / Add |
| Secondary action | Cancel or alternative | Cancel / Skip |

---

#### Drawer/panel
**Behavior**: Panel slides in from edge, partial overlay.

| Attribute | Specification |
|-----------|---------------|
| Trigger | Button click, item selection |
| Animation | Slide from edge, 250ms |
| Position | Right (detail), Left (nav), Bottom (mobile) |
| Dismissal | X button, outside click, gesture |

**Best for**:
- Item detail panels
- Filters and settings
- Secondary navigation
- Quick actions

**Copy requirements**:
| Element | Pattern | Example |
|---------|---------|---------|
| Header | Item/section name | Project details |
| Content | Full detail or form | All project fields |
| Actions | Context-specific | Edit, Delete |

---

#### Popover
**Behavior**: Small floating panel anchored to trigger.

| Attribute | Specification |
|-----------|---------------|
| Trigger | Click (not hover) |
| Animation | Fade/scale, 150ms |
| Position | Near trigger, auto-reposition |
| Dismissal | Outside click, action completion |

**Best for**:
- Menus and dropdowns
- Quick settings
- Color pickers
- Date pickers

**Copy requirements**:
| Element | Pattern | Example |
|---------|---------|---------|
| Options | Action verbs or choices | Edit, Duplicate, Delete |

---

## Selection guide

### By content size

| Content size | Mechanism |
|--------------|-----------|
| 1 line | Tooltip |
| 2-5 lines | Popover, hover card |
| Paragraph | Accordion, expandable row |
| Section | Drawer, tab |
| Full screen | Modal, new page |

### By interaction frequency

| Frequency | Mechanism |
|-----------|-----------|
| Frequent reference | Tooltip, always-visible |
| Occasional need | Accordion, expandable |
| One-time setup | Stepper, modal |
| On-demand detail | Drawer, hover card |

### By task criticality

| Criticality | Mechanism |
|-------------|-----------|
| Low (nice to know) | Tooltip |
| Medium (helpful) | Accordion, drawer |
| High (required) | Modal (blocking) |
| Critical (must see) | Inline (no reveal) |

---

## Accessibility requirements

### All mechanisms
- Keyboard accessible (Tab, Enter, Escape)
- Focus management (focus moves to revealed content)
- Screen reader announcements (aria-expanded, aria-controls)

### Hover mechanisms
- Must have keyboard/focus alternative
- Touch alternative for mobile
- Not for critical information

### Modal mechanisms
- Focus trap within modal
- Return focus on close
- Escape key closes
- Background scroll prevention
