# Cognitive Load Reduction Strategies Reference

Catalog of strategies for reducing cognitive load in UI content.

---

## Strategy categories

### S1: Chunking strategies
Break information into digestible units.

| Strategy | Implementation | Example |
|----------|----------------|---------|
| **Sentence chunking** | Max 20 words per sentence | Split compound sentences |
| **Paragraph chunking** | Max 3 sentences per paragraph | Add breaks at topic shifts |
| **List conversion** | Convert inline series to bullets | "A, B, and C" → bullet list |
| **Step sequencing** | Number sequential actions | "1. Click Save. 2. Confirm." |
| **Section grouping** | Cluster related items under headers | Group settings by category |

---

### S2: Simplification strategies
Reduce complexity of individual elements.

| Strategy | Implementation | Example |
|----------|----------------|---------|
| **Vocabulary simplification** | Replace complex words | "utilize" → "use" |
| **Sentence restructuring** | Active voice, simple structure | "The file was saved by the system" → "We saved your file" |
| **Jargon elimination** | Plain language alternatives | "authenticate" → "sign in" |
| **Abbreviation expansion** | Spell out on first use | "API (Application Programming Interface)" |
| **Concept reduction** | One idea per sentence | Split multi-concept sentences |

---

### S3: Visual hierarchy strategies
Use visual design to guide attention.

| Strategy | Implementation | Example |
|----------|----------------|---------|
| **Size differentiation** | Larger = more important | H1 > H2 > body text |
| **Color coding** | Consistent meaning per color | Red = error, green = success |
| **Whitespace separation** | Group related, separate unrelated | Margins between sections |
| **Proximity grouping** | Related items near each other | Label directly above field |
| **Emphasis restraint** | Limit bold/highlights | Max 1 emphasized phrase per paragraph |

---

### S4: Progressive disclosure strategies
Reveal information as needed.

| Strategy | Implementation | Example |
|----------|----------------|---------|
| **Default hiding** | Advanced options collapsed | "Advanced settings" expandable |
| **On-demand details** | Info icons with tooltips | ⓘ reveals explanation |
| **Step-by-step reveal** | Show next step after completing current | Wizard pattern |
| **Summary + detail** | Overview first, details on request | Dashboard → detail view |
| **Learn more links** | Deep content external to flow | "Learn more about permissions" |

---

### S5: Recognition over recall strategies
Show rather than require remembering.

| Strategy | Implementation | Example |
|----------|----------------|---------|
| **Option display** | Show all choices | Dropdown vs. free text |
| **Format examples** | Show expected format | "MM/DD/YYYY" in placeholder |
| **Recent items** | Display recent selections | "Recent files" list |
| **Inline help** | Context-specific guidance | Helper text below field |
| **Persistent context** | Keep relevant info visible | Breadcrumbs, current selection |

---

### S6: Consistency strategies
Reduce learning across contexts.

| Strategy | Implementation | Example |
|----------|----------------|---------|
| **Terminology consistency** | Same word for same concept | Always "Delete", never "Remove" |
| **Pattern consistency** | Same UI for same action | All confirmations use same modal |
| **Position consistency** | Elements in expected locations | Primary action always bottom-right |
| **Behavior consistency** | Same interaction = same result | All toggles work identically |
| **Visual consistency** | Same meaning for same style | All links are blue |

---

### S7: Error prevention strategies
Reduce cognitive load of error recovery.

| Strategy | Implementation | Example |
|----------|----------------|---------|
| **Constraint design** | Prevent invalid input | Disable submit until valid |
| **Inline validation** | Immediate feedback | Check email format on blur |
| **Confirmation dialogs** | Verify destructive actions | "Delete this file?" |
| **Undo availability** | Reduce decision anxiety | "Undo" for 10 seconds |
| **Smart defaults** | Pre-fill sensible values | Default country from IP |

---

## Strategy selection guide

### By load type

| Load type | Primary strategies |
|-----------|-------------------|
| **High vocabulary load** | S2: Simplification |
| **High visual density** | S1: Chunking, S3: Visual hierarchy |
| **High option count** | S4: Progressive disclosure |
| **High recall demand** | S5: Recognition over recall |
| **High learning curve** | S6: Consistency |
| **High error rate** | S7: Error prevention |

### By user state

| User state | Recommended strategies |
|------------|----------------------|
| **New user** | S4, S5, S6 (disclosure, recognition, consistency) |
| **Task-focused** | S1, S3 (chunking, hierarchy) |
| **Error recovery** | S2, S7 (simplification, prevention) |
| **Expert** | S4 (disclosure—hide basics, expose power features) |

### By content type

| Content type | Priority strategies |
|--------------|-------------------|
| **Instructions** | S1: Chunking (numbered steps) |
| **Error messages** | S2: Simplification + S7: Prevention |
| **Forms** | S5: Recognition + S4: Disclosure |
| **Settings** | S4: Disclosure + S6: Consistency |
| **Onboarding** | S4: Disclosure + S1: Chunking |

---

## Strategy combinations

### High-impact combinations

**Onboarding flow**:
- S4 (progressive disclosure) + S1 (step sequencing) + S5 (format examples)

**Complex form**:
- S1 (section grouping) + S4 (advanced options hidden) + S7 (inline validation)

**Error screen**:
- S2 (simple vocabulary) + S3 (visual hierarchy) + S7 (clear recovery action)

**Settings page**:
- S4 (categories collapsed) + S6 (consistent controls) + S5 (current values shown)

---

## Implementation checklist

### Before changes
- [ ] Identify current load type (intrinsic vs. extraneous)
- [ ] Measure baseline load score
- [ ] Identify user state and context

### Strategy selection
- [ ] Match strategies to identified load types
- [ ] Prioritize strategies by impact
- [ ] Check for strategy conflicts

### After changes
- [ ] Re-score cognitive load
- [ ] Verify no new load introduced
- [ ] Test with target user group

---

## Anti-patterns to avoid

| Anti-pattern | Problem | Alternative |
|--------------|---------|-------------|
| **Over-simplification** | Removes necessary information | Disclose progressively, don't delete |
| **Excessive chunking** | Too many clicks/steps | Balance chunks with efficiency |
| **Inconsistent disclosure** | Sometimes hidden, sometimes not | Establish disclosure rules |
| **Style-only hierarchy** | Visual changes without information hierarchy | Ensure hierarchy is semantic |
| **Help text overload** | Too much inline help | Move to on-demand (tooltips, links) |
