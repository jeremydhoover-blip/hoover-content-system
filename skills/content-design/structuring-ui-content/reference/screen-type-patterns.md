# Screen Type Patterns Reference

Content structure patterns by screen type. Use to determine optimal information hierarchy for different UI contexts.

---

## Screen type taxonomy

| Screen type | Primary purpose | User state | Content priority |
|-------------|-----------------|------------|------------------|
| **Dashboard** | Overview/monitoring | Scanning | Status → Actions → Details |
| **List/Browse** | Find & select | Searching | Filters → Items → Actions |
| **Detail** | Deep information | Focused | Context → Core → Related |
| **Form** | Data entry | Task-focused | Progress → Fields → Validation |
| **Settings** | Configuration | Configuring | Categories → Options → Help |
| **Onboarding** | Initial setup | Learning | Value → Steps → Progress |
| **Empty state** | First use / no data | Uncertain | Why → What → How |
| **Error** | Problem resolution | Frustrated | Problem → Cause → Fix |
| **Confirmation** | Decision point | Deciding | Consequence → Options → Exit |

---

## Pattern definitions

### Dashboard

**Purpose**: Provide at-a-glance status and quick access to actions.

**Content structure**:
```
1. Status summary (what's happening now)
2. Key metrics (numbers that matter)
3. Action shortcuts (frequent tasks)
4. Recent activity (what changed)
5. Alerts/notifications (what needs attention)
```

**Hierarchy rules**:
- Most important status at top-left (F-pattern reading)
- Group related metrics together
- Distinguish actionable vs. informational items
- Use visual hierarchy for severity (alerts > info)

**Copy patterns**:
| Element | Pattern | Example |
|---------|---------|---------|
| Metric label | Noun | Active users |
| Metric context | vs. comparison | vs. last week |
| Status | State + since | Healthy since 9:00 AM |
| Alert | Impact + action | 3 items need review |

---

### List / Browse

**Purpose**: Help users find, filter, and select items.

**Content structure**:
```
1. Page context (what you're looking at)
2. Search/filter controls (narrow down)
3. Results count (orientation)
4. List items (the content)
5. Pagination/load more (navigation)
6. Empty state (when no results)
```

**Hierarchy rules**:
- Filter controls above or beside list
- Item count visible before scrolling
- Each item: Primary identifier + key attributes + actions
- Consistent item structure across list

**Copy patterns**:
| Element | Pattern | Example |
|---------|---------|---------|
| Page title | Plural noun | Documents |
| Search placeholder | Verb + object | Search documents |
| Results count | Number + item type | 24 documents |
| Filter label | Attribute noun | Status |
| Empty search | No [items] + criteria | No documents match your search |

---

### Detail

**Purpose**: Provide comprehensive information about a single item.

**Content structure**:
```
1. Identity (what is this)
2. Status/state (current condition)
3. Primary content (main information)
4. Actions (what you can do)
5. Metadata (supporting details)
6. Related items (connections)
```

**Hierarchy rules**:
- Title identifies item immediately
- Status badges near title (visible without scrolling)
- Primary actions above the fold
- Secondary information in collapsible sections
- Related items at bottom

**Copy patterns**:
| Element | Pattern | Example |
|---------|---------|---------|
| Title | Item name/identifier | Project Alpha |
| Status | State adjective | Active |
| Section header | Content category | Activity |
| Action | Verb (+ object) | Edit, Share, Delete |
| Metadata label | Attribute | Created |

---

### Form

**Purpose**: Collect information through structured input.

**Content structure**:
```
1. Form purpose (what you're creating/editing)
2. Progress indicator (multi-step forms)
3. Section groupings (related fields)
4. Individual fields (labels, inputs, help)
5. Validation feedback (inline errors)
6. Form actions (submit, cancel)
```

**Hierarchy rules**:
- One question/concept per visible section
- Required fields marked consistently (asterisk or "optional" label)
- Help text beneath field, not inside
- Errors appear inline, near field
- Primary action visually dominant

**Copy patterns**:
| Element | Pattern | Example |
|---------|---------|---------|
| Form title | Verb + object | Create project |
| Section header | Category noun | Contact information |
| Field label | Attribute noun | Email address |
| Helper text | Explanation/constraint | We'll use this for notifications |
| Error | Problem + fix | Enter a valid email address |
| Submit | Verb (+ object) | Create project |

---

### Settings

**Purpose**: Allow users to configure preferences and options.

**Content structure**:
```
1. Settings navigation (categories)
2. Category header (what's in this group)
3. Individual settings (label + control)
4. Setting description (what it does)
5. Save/apply mechanism (explicit or auto-save)
```

**Hierarchy rules**:
- Group related settings in categories
- Most common settings first within category
- Toggle/choice controls aligned consistently
- Descriptions below setting, not beside
- Indicate auto-save or require explicit save

**Copy patterns**:
| Element | Pattern | Example |
|---------|---------|---------|
| Category | Noun (plural or mass) | Notifications |
| Setting label | Feature noun | Email notifications |
| Description | What happens when on/off | Receive email when someone mentions you |
| Choice option | Variant noun | Daily digest |

---

### Onboarding

**Purpose**: Guide new users through initial setup and value discovery.

**Content structure**:
```
1. Welcome/value proposition (why you're here)
2. Progress indicator (how far along)
3. Current step content (one task)
4. Next action (clear CTA)
5. Skip option (if applicable)
```

**Hierarchy rules**:
- One primary action per screen
- Progress visible throughout
- Skip/later always available for non-critical steps
- Celebrate completion (transition to regular experience)

**Copy patterns**:
| Element | Pattern | Example |
|---------|---------|---------|
| Welcome | Greeting + value | Welcome! Let's get you set up. |
| Step title | Verb + object | Add your first project |
| Step description | Benefit statement | Projects help you organize your work |
| Primary CTA | Verb + object | Create project |
| Skip | Skip + optional context | Skip for now |

---

### Empty state

**Purpose**: Guide users when no content exists.

**Content structure**:
```
1. Visual indicator (illustration/icon)
2. Headline (what's empty)
3. Explanation (why it matters)
4. Primary action (create first item)
5. Alternative action (learn more)
```

**Hierarchy rules**:
- Centered composition
- Illustration reinforces message (not decorative)
- Headline states the empty condition
- Description is forward-looking (not apologetic)
- Single primary CTA

**Copy patterns**:
| Element | Pattern | Example |
|---------|---------|---------|
| Headline | No [items] yet | No projects yet |
| Description | Benefit + prompt | Projects help you organize work. Create one to get started. |
| Primary CTA | Verb + first [item] | Create your first project |
| Secondary | Learn more about [feature] | Learn more about projects |

---

### Error screen

**Purpose**: Explain problems and provide recovery paths.

**Content structure**:
```
1. Error indication (clear signal)
2. What happened (problem statement)
3. Why it happened (if helpful)
4. How to fix (recovery action)
5. Alternative path (if primary fix unavailable)
```

**Hierarchy rules**:
- Don't blame user
- Technical details optional/collapsible
- Primary recovery action prominent
- Alternative path always available (go back, contact support)

**Copy patterns**:
| Element | Pattern | Example |
|---------|---------|---------|
| Headline | Problem statement | Page not found |
| Description | Context + next step | The page you're looking for doesn't exist or has moved. |
| Primary CTA | Recovery action | Go to home |
| Secondary | Alternative | Contact support |

---

### Confirmation dialog

**Purpose**: Ensure intentional action for consequential operations.

**Content structure**:
```
1. Title (action being confirmed)
2. Consequence explanation (what will happen)
3. Primary action (confirm)
4. Secondary action (cancel)
```

**Hierarchy rules**:
- Title matches action that triggered dialog
- Consequence is specific (what data affected)
- Destructive actions use warning color
- Cancel always available and safe

**Copy patterns**:
| Element | Pattern | Example |
|---------|---------|---------|
| Title | Verb + object? | Delete project? |
| Description | Consequence statement | This will permanently delete "Project Alpha" and all its contents. |
| Confirm | Verb (matching title) | Delete |
| Cancel | Cancel | Cancel |

---

## Cross-pattern rules

### Information hierarchy
All screens follow this hierarchy:
1. **Orientation**: Where am I? What's this?
2. **Status**: What's the current state?
3. **Action**: What can I do?
4. **Details**: What else do I need to know?

### Progressive disclosure by screen type
| Screen type | Immediate | On demand | On request |
|-------------|-----------|-----------|------------|
| Dashboard | Metrics, alerts | Trends, details | Historical data |
| List | Items, count | Filters, sorting | Bulk actions |
| Detail | Core info, status | Metadata, history | Related items |
| Form | Current fields | Help text | Advanced options |
| Settings | Common settings | Descriptions | Advanced settings |

### Density guidelines
| Screen type | Density | Rationale |
|-------------|---------|-----------|
| Dashboard | Medium | Balance overview with scannability |
| List | High | Maximize items visible |
| Detail | Low | Allow focused reading |
| Form | Low | Reduce input errors |
| Settings | Medium | Group related options |
