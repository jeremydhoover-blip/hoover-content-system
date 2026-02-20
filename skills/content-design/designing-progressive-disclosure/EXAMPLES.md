# Examples

## Example 1: Form with progressive disclosure

**Input**: Design progressive disclosure for a user registration form.

**Output**:
```md
## Progressive disclosure map: User registration

**User task**: Create account
**User context**: First-time user, low expertise assumed, medium urgency

### Layer 1: Essential (always visible)

| Content | Why essential | Visibility |
|---------|---------------|------------|
| Email field | Required for account creation | Always visible |
| Password field | Required for account creation | Always visible |
| Create account button | Primary action | Always visible |
| Terms link | Legal requirement | Always visible |

### Layer 2: Supplementary (on-demand)

| Content | Trigger | Reveal mechanism | Discoverability signal |
|---------|---------|------------------|------------------------|
| Password requirements | Focus password field | Inline expand below field | Auto-reveal on focus |
| Terms full text | Click "Terms" link | Modal | Underlined link text |
| Why we need email | Click (?) icon | Tooltip | (?) icon next to label |

### Layer 3: Edge-case (conditional)

| Content | Trigger condition | Reveal mechanism | Who needs this |
|---------|-------------------|------------------|----------------|
| SSO options | Enterprise domain detected | Section appears | Enterprise users |
| Accessibility mode | User preference | Persistent toggle | Screen reader users |

### Implementation details

**Password requirements reveal**:
- Trigger: Password field receives focus
- Mechanism: Inline expansion below field
- Content: "At least 8 characters, including a number"
- Reverse: Collapse when field loses focus (unless errors present)

**Terms modal**:
- Trigger: Click "Terms of Service" link
- Mechanism: Modal dialog
- Content: Full legal text
- Reverse: Close button or click outside

### Hidden content discoverability audit
- [x] Password requirements appear automatically on focus
- [x] Terms link is visible and styled as interactive
- [x] Help icons are visible next to fields
- [x] Essential fields never hidden
```

---

## Example 2: Settings with layered complexity

**Input**: Design progressive disclosure for notification settings.

**Output**:
```md
## Progressive disclosure map: Notification settings

**User task**: Control notification preferences
**User context**: Mixed expertise, occasional use, low stress

### Layer 1: Essential (always visible)

| Content | Why essential |
|---------|---------------|
| Master notification toggle | Core control |
| Email notifications toggle | Primary channel |
| Push notifications toggle | Primary channel |

### Layer 2: Supplementary (on-demand)

| Content | Trigger | Reveal mechanism | Discoverability |
|---------|---------|------------------|-----------------|
| Email frequency options | Expand email section | Accordion | "▼" icon + "Customize" |
| Push notification types | Expand push section | Accordion | "▼" icon + "Customize" |
| Quiet hours | Click "Set quiet hours" | Inline form expand | Text link below toggles |

### Layer 3: Edge-case (conditional)

| Content | Trigger condition | Reveal mechanism |
|---------|-------------------|------------------|
| Notification sound picker | Push enabled + device supports | Nested in push section |
| Per-project settings | User has 3+ projects | Link to sub-screen |
| API webhook settings | Developer role | Advanced section at bottom |

### Reveal specification: Email frequency

**Trigger**: Click "Customize" or expand icon
**Mechanism**: Accordion expand in place

**Content revealed**:
```
Email frequency
○ Real-time
○ Daily digest
○ Weekly digest

Email types
☑ Security alerts
☑ Product updates
☐ Marketing
```

**Discoverability**: "Customize ▼" text visible in collapsed state
**Reverse action**: Click header or "▲" to collapse
**State persistence**: Collapse state persists in session, resets on next visit
```

---

## Example 3: Error message with technical details

**Input**: Design progressive disclosure for a payment error.

**Output**:
```md
## Progressive disclosure map: Payment error state

**User task**: Recover from failed payment
**User context**: Variable expertise, rare occurrence, HIGH stress

### Layer 1: Essential (always visible)

| Content | Why essential |
|---------|---------------|
| "Payment didn't go through" | Acknowledge problem |
| "Your card wasn't charged" | Reduce anxiety |
| "Try again" button | Recovery action |
| "Use different card" link | Alternative action |

### Layer 2: Supplementary (on-demand)

| Content | Trigger | Reveal mechanism | Who benefits |
|---------|---------|------------------|--------------|
| Why it might have failed | Click "Why did this happen?" | Accordion expand | Users who want to understand |
| Technical error details | Click "Show details" | Accordion expand | Support, developers |

### Layer 3: Edge-case (conditional)

| Content | Trigger condition | Reveal mechanism |
|---------|-------------------|------------------|
| Contact support with pre-filled info | 2nd failure in session | Prominent link appears |
| Transaction ID | Always available in details | In technical details section |

### Reveal specification: Technical details

**Trigger**: Click "Show technical details"
**Mechanism**: Accordion expand at bottom of error card

**Content revealed**:
```
Error code: PAYMENT_DECLINED_DO_NOT_HONOR
Transaction ID: txn_abc123xyz
Timestamp: 2026-02-20T14:32:01Z

Copy details for support ↗
```

**Discoverability**: "Show technical details" link in muted text
**Reverse action**: Click to collapse
**State persistence**: None—collapses on page change

### High-stress design note
In high-stress contexts, Layer 1 must be ultra-scannable. Technical details are noise during stress—always Layer 2+.
```

---

## Example 4: Edge case — Over-disclosure diagnosis

**Input**: Current design shows all settings at once. Users report overwhelm.

**Output**:
```md
## Diagnosis: Over-disclosure in settings

**Problem**: All content at Layer 1 (always visible). No progressive disclosure applied.

**Current state**: 24 settings visible on single screen
**User feedback**: "Overwhelming", "Can't find what I need", "Too many options"

### Recommended layering

**Move to Layer 1 (keep visible)**: 6 items
- Settings users access >50% of visits
- Settings with security implications

**Move to Layer 2 (on-demand)**: 12 items
- Settings users access <20% of visits
- Settings with reasonable defaults

**Move to Layer 3 (edge-case)**: 6 items
- Settings only power users change
- Settings requiring expertise

### Disclosure strategy

| Current | Recommended layer | Trigger | Rationale |
|---------|-------------------|---------|-----------|
| Account name | L1 | — | Frequently edited |
| Password | L1 | — | Security critical |
| Two-factor | L1 | — | Security critical |
| Notification email | L1 | — | Common support issue |
| Theme | L2 | "Appearance" section | Preference, not task-critical |
| Font size | L2 | "Appearance" section | Accessibility |
| API keys | L3 | "Developer" section | <5% of users |
| Webhook URLs | L3 | "Developer" section | <5% of users |

### Result
- Visible items: 24 → 6
- Sections: 0 → 4 (Account, Notifications, Appearance, Developer)
- Access to all settings preserved via progressive disclosure
```

---

## Example 5: Edge case — Missing input

**Input**: "Use progressive disclosure here."

**Output**:
```md
To design progressive disclosure, I need:

1. **Full content inventory**
   List everything that could appear on this screen (even if currently hidden)

2. **User task**
   What is the primary goal users have when they reach this screen?

3. **User context**
   - Expertise: [Novice / Intermediate / Expert]
   - Frequency: [First-time / Occasional / Daily]
   - Stress level: [Low / Medium / High]

4. **Current state**
   - Is everything visible now? (over-disclosure)
   - Is too much hidden? (under-disclosure)
   - What user feedback exists?

5. **Platform constraints**
   - Can you use tooltips? Modals? Accordions?
   - Are there accessibility requirements?

Share the screen content or a screenshot to proceed.
```
