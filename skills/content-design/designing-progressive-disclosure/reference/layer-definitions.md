# Progressive Disclosure Layer Definitions Reference

Framework for organizing information into disclosure layers.

---

## Layer model

Progressive disclosure organizes content into layers by user need:

```
┌─────────────────────────────────────────┐
│  L1: Essential (Always visible)         │
├─────────────────────────────────────────┤
│  L2: Expected (One click/tap away)      │
├─────────────────────────────────────────┤
│  L3: Optional (On-demand)               │
├─────────────────────────────────────────┤
│  L4: Specialized (Deep/expert)          │
└─────────────────────────────────────────┘
```

---

## Layer definitions

### L1: Essential layer

**Definition**: Information required to complete the primary task or understand the current state.

**Visibility**: Always visible, no interaction required.

**Criteria for L1**:
- User cannot proceed without it
- User expects to see it immediately
- Removing it causes confusion or errors
- Critical for safety or legal compliance

**Examples**:
| Context | L1 content |
|---------|------------|
| Form | Field labels, required field indicators |
| Dashboard | Current status, critical alerts |
| List | Item identifiers, primary attributes |
| Error | Problem statement, primary recovery action |
| Modal | Title, primary action, cancel |

**Content constraints**:
- Maximum 3-5 distinct elements
- Must fit above the fold
- Highest visual priority

---

### L2: Expected layer

**Definition**: Information most users need but doesn't require immediate attention.

**Visibility**: One click/tap away or visible with minimal scrolling.

**Criteria for L2**:
- Most users (>50%) will need this
- Supports primary task but doesn't block it
- Common follow-up questions answered here
- Non-critical but valuable context

**Access mechanisms**:
- Scrolling (below fold)
- Single click expand (accordion)
- Tab navigation (sibling content)
- Inline links ("Learn more")

**Examples**:
| Context | L2 content |
|---------|------------|
| Form | Helper text, format examples |
| Dashboard | Trend data, secondary metrics |
| List | Additional item attributes, quick actions |
| Settings | Setting descriptions, recommendations |
| Profile | Additional details, activity history |

**Content constraints**:
- Maximum 10-15 elements per view
- Group related items
- Clear visual hierarchy below L1

---

### L3: Optional layer

**Definition**: Information some users need in specific situations.

**Visibility**: On-demand, requires intentional action to access.

**Criteria for L3**:
- Minority of users (<50%) will need this
- Specific use cases or edge cases
- Reference information (not action-blocking)
- Power user features

**Access mechanisms**:
- Tooltips and info icons
- Expandable sections (collapsed by default)
- Secondary tabs
- Links to separate pages/modals
- "Advanced" or "More options" sections

**Examples**:
| Context | L3 content |
|---------|------------|
| Form | Advanced options, optional fields |
| Dashboard | Historical data, export options |
| Settings | Advanced configuration, developer settings |
| Error | Technical details, error codes |
| Profile | Privacy settings, account management |

**Content constraints**:
- Clearly labeled access points
- Don't interrupt primary flow
- Reversible access (can collapse again)

---

### L4: Specialized layer

**Definition**: Information for expert users or rare situations.

**Visibility**: Deep access, multiple steps or specific triggers required.

**Criteria for L4**:
- Small minority (<10%) will ever need this
- Expert/technical content
- Regulatory/compliance documentation
- Audit trails and logs
- Developer-facing information

**Access mechanisms**:
- Separate pages/sections
- Documentation links
- Support channels
- Developer tools/consoles
- Admin-only interfaces

**Examples**:
| Context | L4 content |
|---------|------------|
| Settings | API credentials, webhook configuration |
| Error | Debug logs, stack traces |
| Account | Data export, account deletion |
| Compliance | Terms of service, privacy policy details |
| Admin | User management, system configuration |

**Content constraints**:
- Clearly marked as advanced/technical
- Warning labels where appropriate
- Documentation available

---

## Layer assignment framework

### Decision tree

```
Is the information required to complete the current task?
├── Yes → L1 (Essential)
└── No → Will most users (>50%) need this information?
    ├── Yes → L2 (Expected)
    └── No → Is this a common question or use case?
        ├── Yes → L3 (Optional)
        └── No → L4 (Specialized)
```

### Assignment by content type

| Content type | Typical layer | Rationale |
|--------------|---------------|-----------|
| Primary action | L1 | Required to proceed |
| Current status | L1 | Orientation |
| Field labels | L1 | Required for input |
| Error messages | L1 | Blocks progress |
| Helper text | L2 | Supports but doesn't block |
| Descriptions | L2 | Provides context |
| Secondary actions | L2-L3 | Depends on frequency |
| Advanced options | L3 | Minority need |
| Technical details | L3-L4 | Specialist audience |
| Legal text | L3-L4 | Reference only |
| Developer info | L4 | Expert audience |

### Assignment by user expertise

| User type | L1 tolerance | L2-L4 access pattern |
|-----------|--------------|----------------------|
| New user | Low (essentials only) | Guided access to L2, L3-L4 hidden |
| Regular user | Medium | Quick L2 access, L3 available |
| Expert user | High | Minimal L1, direct L3-L4 access |

---

## Layer transition patterns

### L1 → L2 transitions

| Pattern | Mechanism | Example |
|---------|-----------|---------|
| Scroll reveal | Content below fold | Settings page scroll |
| Click expand | Accordion | "Show more details" |
| Tab switch | Tab bar | Overview → Details tab |

### L2 → L3 transitions

| Pattern | Mechanism | Example |
|---------|-----------|---------|
| Tooltip | Hover/focus | Info icon → explanation |
| Section expand | Collapsed section | "Advanced options" |
| Link navigation | New page/modal | "View all settings" |

### L3 → L4 transitions

| Pattern | Mechanism | Example |
|---------|-----------|---------|
| Documentation link | External page | "Developer documentation" |
| Admin access | Restricted section | "Admin settings" |
| Support escalation | Contact flow | "Contact support" |

---

## Layer balance guidelines

### Per-screen limits

| Layer | Max elements | Rationale |
|-------|--------------|-----------|
| L1 | 5-7 elements | Cognitive limit for immediate processing |
| L2 | 10-15 elements | Manageable with scrolling/tabs |
| L3 | No hard limit | Behind interaction gate |
| L4 | No hard limit | Separate context |

### Load distribution

Healthy distribution for consumer products:
- L1: 20-30% of content
- L2: 40-50% of content
- L3: 20-30% of content
- L4: 5-10% of content

Signs of poor distribution:
- L1 overload: Too much competing for attention
- L2 underload: L1 contains non-essential content
- L3 underload: Users can't self-serve common questions
- L4 overload: Expert content hidden too deep

---

## Validation checklist

### L1 validation
- [ ] User cannot proceed without any L1 element?
- [ ] All L1 elements fit above the fold?
- [ ] No more than 5-7 distinct L1 elements?
- [ ] Clear visual hierarchy among L1 elements?

### L2 validation
- [ ] Access requires only one action (scroll/click)?
- [ ] Most users (>50%) will use this content?
- [ ] Clearly grouped with related L1 content?
- [ ] Doesn't distract from L1 content?

### L3 validation
- [ ] Clear access point visible from L1/L2?
- [ ] Access point indicates what will be revealed?
- [ ] Can be collapsed/dismissed after viewing?
- [ ] Doesn't block primary workflow?

### L4 validation
- [ ] Appropriate for the small audience that needs it?
- [ ] Doesn't clutter L1-L3 navigation?
- [ ] Clearly marked as advanced/specialized?
- [ ] Has appropriate access controls (if sensitive)?
