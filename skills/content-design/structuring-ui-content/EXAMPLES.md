# Examples

## Example 1: Form screen structure

**Input**: Structure content for a user profile edit screen.

**Output**:
```md
## Screen: Edit profile

**Primary task**: Update user profile information
**Entry point**: Settings > Profile > Edit button
**Exit point**: Save changes | Cancel

### Content hierarchy

| Priority | Element | Purpose | Position |
|----------|---------|---------|----------|
| 1 | Save button | Complete task | Top-right (sticky on scroll) |
| 2 | Form fields | Input collection | Main content area |
| 3 | Cancel link | Abandon without saving | Near Save button |
| 4 | Delete account | Destructive action | Bottom, separated |

### Content groups

**Group 1: Identity**
- Display name field
- Username field
- Profile photo
- Relationship: Public-facing identity elements

**Group 2: Contact**
- Email field
- Phone field (optional)
- Relationship: How others/system can reach user

**Group 3: Preferences**
- Language dropdown
- Timezone dropdown
- Relationship: Localization settings

**Group 4: Danger zone**
- Delete account button
- Relationship: Destructive, irreversible action (isolate from other actions)

### Reading order
1. Page title: "Edit profile"
2. Identity fields (most commonly edited)
3. Contact fields
4. Preferences
5. Save / Cancel actions
6. Delete account (intentionally last, requires deliberate scroll)

**Accessibility note**: DOM order matches visual order. Delete section uses `aria-label="Danger zone"` landmark.
```

---

## Example 2: Confirmation screen structure

**Input**: Structure content for a successful payment confirmation.

**Output**:
```md
## Screen: Payment confirmation

**Primary task**: Confirm transaction completed, provide next steps
**Entry point**: Redirect from payment processor
**Exit point**: View order | Return to shopping

### Content hierarchy

| Priority | Element | Purpose | Position |
|----------|---------|---------|----------|
| 1 | Success indicator | Confirm completion | Top, prominent |
| 2 | Order number | Reference for support | Immediately after headline |
| 3 | Order summary | Verification | Main content |
| 4 | Next action | Continue journey | Below summary |
| 5 | Secondary actions | Alternative paths | Bottom |

### Content groups

**Group 1: Confirmation**
- Success icon
- "Payment complete" headline
- Order number
- Relationship: Immediate reassurance

**Group 2: Details**
- Items purchased
- Total charged
- Payment method (last 4 digits)
- Relationship: Verifiable transaction details

**Group 3: Next steps**
- "View order" button (primary)
- "Continue shopping" link (secondary)
- Estimated delivery info
- Relationship: Forward momentum

### Reading order
1. Success icon + headline (immediate reassurance)
2. Order number (reference capture)
3. Summary (verification)
4. Delivery estimate (expectation setting)
5. Primary action (view order)
6. Secondary action (continue shopping)

**Accessibility note**: Success state announced via `aria-live="polite"` region.
```

---

## Example 3: Complex flow content mapping

**Input**: Structure content for a 3-step checkout flow.

**Output**:
```md
## Flow: Checkout

### Step sequence

```
[Cart review] → [Shipping info] → [Payment] → [Confirmation]
      ↓               ↓              ↓
  [Empty cart]   [Address error]  [Payment error]
```

### Content per step

| Step | Screen | Primary content | Primary action | Exit options |
|------|--------|-----------------|----------------|--------------|
| 1 | Cart review | Items, quantities, totals | "Continue to shipping" | Edit cart, Remove items |
| 2 | Shipping | Address form, shipping options | "Continue to payment" | Back to cart |
| 3 | Payment | Payment form, order summary | "Place order" | Back to shipping |
| 4 | Confirmation | Success message, order number | "View order" | Continue shopping |

### Progress indication
- Show step indicator: "Step 2 of 3: Shipping"
- Completed steps are clickable for editing
- Future steps are visible but inactive

### State handling
- **Empty cart**: Redirect to cart with empty state message
- **Address error**: Inline validation, block progression until fixed
- **Payment error**: Show specific error, retain form data, allow retry
- **Session timeout**: Save cart to account, prompt re-authentication

### Content persistence across steps
- Order summary visible on all steps (collapsible on mobile)
- Shipping address summary shown on payment step
- Edit links return to relevant step without losing other data
```

---

## Example 4: Edge case — Incomplete input

**Input**: "Structure this screen better."

**Output**:
```md
To structure screen content, I need:

1. **What is the primary task?**
   [What should users accomplish on this screen?]

2. **What content elements exist?**
   - [ ] Headings/titles
   - [ ] Body text
   - [ ] Form fields
   - [ ] Buttons/actions
   - [ ] Images/media
   - [ ] Help text
   - [ ] Error messages

3. **Screen context:**
   - How do users arrive? (nav, link, redirect)
   - What do they do next? (submit, navigate away, close)

4. **Constraints:**
   - Viewport: Mobile / Desktop / Both
   - Scrolling: Allowed / Avoid

Share a screenshot, wireframe, or list of elements to proceed.
```

---

## Example 5: Mobile vs desktop structure adaptation

**Input**: Adapt a settings screen structure for mobile.

**Output**:
```md
## Screen: Notification settings (Mobile adaptation)

### Desktop structure
- Two-column layout: categories left, settings right
- All settings visible, grouped by category
- Save button in header

### Mobile adaptation

**Structure changes**:
| Desktop | Mobile | Rationale |
|---------|--------|-----------|
| Two columns | Single column | Viewport constraint |
| All settings visible | Category navigation → Detail view | Reduce scroll depth |
| Save in header | Save as sticky footer button | Thumb reachability |
| Inline help text | Help icon → expandable | Conserve vertical space |

**Mobile reading order**:
1. Screen title
2. Category list (tap to drill down)
3. [On category tap] Settings list for category
4. [On setting tap] Toggle/control with expanded help
5. Save button (sticky footer)

**Mobile-specific rules**:
- Max 7 items per category list (reduce cognitive load)
- Tappable areas min 44x44px
- Back navigation via system gesture, not in-app button
- Auto-save preferred over explicit save action

**Accessibility note**: Focus management returns to category list after setting change.
```
