# Examples

## Example 1: B2B SaaS product

**Input:**
- Product: Project management tool for distributed teams
- Problems: Content is inconsistent across features; too much jargon; help content doesn't match UI
- Audience: Project managers, team leads, non-technical users
- Values: Clarity, efficiency, inclusivity

**Output:**

```md
# Content Principles: TeamSync

## How to use this document
These principles guide all content decisions. When unsure, consult this document. When principles conflict, see the prioritization rules below.

---

## Principles

### 1. Clarity over cleverness
**Statement:** Choose the clearest option, even if it's less interesting.

**What this means:**
- Use common words over jargon
- Write for scanning, not deep reading
- One idea per sentence

**Decision test:** Would a new user understand this immediately?

**Example application:**
> Situation: Naming a feature that auto-assigns tasks based on workload
> Decision: Named it "Auto-assign" not "Smart Load Balancer" or "WorkGenius"

---

### 2. Action-first
**Statement:** Lead with what the user can do, not what the system does.

**What this means:**
- Start with verbs
- Frame features as user capabilities
- Put the action before the explanation

**Decision test:** Does this tell users what they can do in the first 5 words?

**Example application:**
> Situation: Explaining the calendar integration
> Decision: "Sync your calendar to see deadlines" not "TeamSync's calendar integration enables bi-directional synchronization"

---

### 3. Consistent everywhere
**Statement:** Use the same term for the same thing, always.

**What this means:**
- One name per concept (not "tasks" and "to-dos" interchangeably)
- Same capitalization rules everywhere
- UI text matches help content exactly

**Decision test:** If I search for this term, will I find all relevant content?

**Example application:**
> Situation: Help article used "workspace" but UI said "project space"
> Decision: Updated UI to "workspace" to match documentation

---

### 4. Inclusive by default
**Statement:** Write for the widest possible audience.

**What this means:**
- Avoid idioms that don't translate
- Don't assume technical knowledge
- Use inclusive pronouns and examples

**Decision test:** Would this work in translation? For a non-native speaker?

**Example application:**
> Situation: Error message said "Looks like you dropped the ball"
> Decision: Changed to "This task wasn't completed on time"

---

### 5. Honest about complexity
**Statement:** Don't hide complexity; explain it simply.

**What this means:**
- Acknowledge when things are complicated
- Provide progressive disclosure for advanced users
- Don't oversimplify to the point of inaccuracy

**Decision test:** Is this accurate? Would an expert agree?

**Example application:**
> Situation: Permissions system is genuinely complex
> Decision: Created "Quick setup" for common cases + "Advanced permissions" for edge cases

---

## Prioritization rules

When principles conflict, use this hierarchy:

1. **Clarity** always wins when user safety or data is at risk
2. **Consistency** takes precedence in navigation and naming
3. **Inclusive by default** overrides cleverness in global-facing content
4. Default to **Action-first** when stakes are unclear

### Common conflicts and resolutions

| Conflict | Resolution |
|----------|------------|
| Clarity vs Consistency | If existing term is unclear, fix the term everywhere (one-time consistency break) |
| Action-first vs Honest about complexity | Use action-first as hook, then disclose complexity |
| Inclusive vs Consistency | Inclusive wins; update terminology if old terms are exclusionary |

---

## Anti-patterns
These violate our principles:
- Using synonyms to avoid repetition (breaks consistency)
- Leading with system architecture ("Our microservices...") instead of user value
- Hiding important complexity behind "just" or "simply"
- Using sports metaphors without explanation
```

---

## Example 2: Healthcare patient portal

**Input:**
- Product: Patient-facing health records and appointment system
- Problems: Medical jargon confuses patients; anxious users need reassurance; legal requirements add complexity
- Audience: Patients of all ages and literacy levels
- Values: Trust, accessibility, patient empowerment

**Output:**

```md
# Content Principles: HealthConnect

## Principles

### 1. Respect the reader's anxiety
**Statement:** Health information is stressful; write to reduce fear, not add to it.

**What this means:**
- Lead with reassurance when appropriate
- Provide clear next steps
- Avoid alarming language when facts are neutral

**Decision test:** Would a worried patient feel calmer or more anxious after reading this?

**Example application:**
> Situation: Displaying lab results that are outside normal range
> Decision: "Your result is outside the typical range. Your care team will review this and contact you." Not: "ABNORMAL RESULT DETECTED"

---

### 2. Plain language first, medical terms second
**Statement:** Explain in everyday words; add clinical terms for reference.

**What this means:**
- Define medical terms on first use
- Pair technical terms with plain equivalents
- Never assume medical literacy

**Decision test:** Would someone without medical training understand this?

**Example application:**
> Situation: Explaining a diagnosis
> Decision: "High blood sugar (hyperglycemia)" not just "Hyperglycemia"

---

### 3. Transparency over simplification
**Statement:** Be honest about what we know and don't know.

**What this means:**
- Don't hide uncertainty
- Be clear about what requires doctor input vs. self-service
- Explain why we ask for information

**Decision test:** Are we being fully honest, even if it's complicated?

**Example application:**
> Situation: Patient asks AI chatbot about symptoms
> Decision: "I can share general information, but only your doctor can diagnose. Would you like to schedule a visit?"

---

### 4. Accessible to all bodies and abilities
**Statement:** Every patient can use this, regardless of disability or device.

**What this means:**
- Screen reader compatible
- No instructions that assume physical ability ("click and drag")
- Works on slow connections and old devices

**Decision test:** Could a patient using assistive technology complete this task?

**Example application:**
> Situation: Selecting appointment time
> Decision: "Select a time" with list navigation, not a visual calendar-only picker

---

### 5. Patient in control
**Statement:** Patients own their data and decisions.

**What this means:**
- Explain how data is used
- Provide choices, not mandates
- Never use guilt or pressure

**Decision test:** Does the patient feel in control of this interaction?

**Example application:**
> Situation: Requesting prescription refill
> Decision: Clear opt-in for auto-refill, not auto-enrolled with hidden opt-out

---

### 6. Legal clarity, not legal speak
**Statement:** Meet legal requirements in plain language.

**What this means:**
- Required disclosures in simple terms
- Summaries before full legal text
- Explain what legal terms mean for the patient

**Decision test:** Could a patient explain their rights based on this?

**Example application:**
> Situation: HIPAA consent
> Decision: "This protects who can see your health records" summary + full legal text expandable

---

## Prioritization rules

1. **Respect anxiety** always wins in clinical result communication
2. **Accessible to all** overrides design preferences
3. **Transparency** beats simplification when health outcomes are at stake
4. **Legal clarity** is non-negotiable but style is flexible

### Common conflicts and resolutions

| Conflict | Resolution |
|----------|------------|
| Plain language vs Legal requirements | Plain summary first, legal language in expandable section |
| Respect anxiety vs Transparency | Be transparent but frame information with care; lead with next steps |
| Patient control vs Medical urgency | Provide urgent recommendations clearly, but preserve patient choice |
```

---

## Example 3: Edge case — Startup without established brand

**Input:**
- Product: New productivity app, brand not yet defined
- Problems: No existing content to audit; team has different ideas about tone
- Audience: Knowledge workers (broad)
- Values: Not yet articulated

**Output:**

```md
# Content Principles: [ProductName] — v0.1 Draft

> Note: This is a starter set. Revisit after 3 months of content production to refine based on what's working.

## Principles

### 1. Ship clarity
**Statement:** Clear beats perfect.

**What this means:**
- Release simple, clear content fast
- Iterate based on user feedback
- Don't block launches on copy perfection

**Decision test:** Is this clear enough to ship?

---

### 2. Match user effort
**Statement:** Small tasks get small explanations; big decisions get full context.

**What this means:**
- Tooltip for a button, not a paragraph
- Full disclosure for account deletion
- Match content depth to task weight

**Decision test:** Is the explanation proportional to what the user is deciding?

---

### 3. One name, one thing
**Statement:** Pick a term and stick with it.

**What this means:**
- Create a glossary early
- Don't invent synonyms
- When in doubt, use the simpler word

**Decision test:** Would a user searching for this find what they need?

---

### 4. Write for the tired user
**Statement:** Assume users are distracted and in a hurry.

**What this means:**
- Scannable over readable
- Front-load key information
- Reduce clicks and cognitive load

**Decision test:** Could a user get the point in 3 seconds?

---

### 5. Be honest about beta
**Statement:** If it's rough, say so.

**What this means:**
- Label experimental features clearly
- Set expectations about what might change
- Don't overpromise

**Decision test:** Will users feel surprised or misled later?

---

## Prioritization

1. **Clarity** always wins (we can't iterate without user understanding)
2. **One name, one thing** next (consistency saves support costs)
3. Others are flexible during beta

## Review schedule
- Week 4: Check if principles match actual content decisions
- Week 12: Full revision based on patterns learned
```
