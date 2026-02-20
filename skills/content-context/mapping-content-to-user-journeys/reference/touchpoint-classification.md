# Touchpoint Classification

## Touchpoint definition

A **touchpoint** is any moment where content is delivered to the user. Each touchpoint should be classified by:

1. **Channel** — Where the content appears
2. **Content type** — What kind of content it is
3. **Purpose** — Why the content exists
4. **Timing** — When relative to user action

## Channel classification

| Channel | Description | Characteristics | Examples |
|---------|-------------|-----------------|----------|
| **In-app** | Content within the product interface | Immediate context, high attention | Modals, tooltips, empty states, forms |
| **Email** | Content delivered to inbox | Asynchronous, can be missed, permanent | Transactional, marketing, lifecycle |
| **Push** | Mobile or desktop notifications | Interruptive, brief, actionable | Alerts, reminders, updates |
| **SMS** | Text messages | Urgent, personal, high open rate | Verification, critical alerts |
| **Web** | Marketing or documentation sites | Discovery-focused, SEO-relevant | Landing pages, help articles |
| **In-person** | Human-delivered content | High-touch, personalized | Sales calls, support chats |
| **Physical** | Printed or mailed content | Tangible, lasting | Packaging, direct mail |

## Content type classification

### Navigational content
| Type | Purpose | Examples |
|------|---------|----------|
| **Menu/nav labels** | Orient and direct | "Settings", "Dashboard", "Help" |
| **Breadcrumbs** | Show location in hierarchy | "Home > Projects > Settings" |
| **CTAs** | Prompt specific action | "Get started", "Learn more", "Upgrade" |
| **Links** | Connect to related content | Inline text links, "See also" |

### Informational content
| Type | Purpose | Examples |
|------|---------|----------|
| **Headlines** | Summarize and attract attention | Page titles, section headers |
| **Body copy** | Explain and inform | Paragraphs, descriptions |
| **Labels** | Identify elements | Form fields, data labels |
| **Tooltips** | Provide contextual detail | Hover explanations |
| **Help text** | Guide correct usage | Field hints, instructions |

### Feedback content
| Type | Purpose | Examples |
|------|---------|----------|
| **Success messages** | Confirm completed action | "Changes saved", "Email sent" |
| **Error messages** | Explain problems and recovery | Validation errors, system errors |
| **Progress indicators** | Show status of operation | Loading states, step counters |
| **Empty states** | Explain absence and prompt action | "No results", "Get started" |

### Persuasive content
| Type | Purpose | Examples |
|------|---------|----------|
| **Value propositions** | Communicate benefit | "Save 10 hours per week" |
| **Social proof** | Build trust through others | Testimonials, user counts |
| **Urgency messaging** | Motivate immediate action | "Offer ends Friday", "3 left" |
| **Objection handling** | Address concerns | FAQ, guarantee statements |

## Purpose classification

Each touchpoint serves one primary purpose:

| Purpose | Intent | Tone characteristics | Example |
|---------|--------|---------------------|---------|
| **Inform** | Transfer knowledge | Neutral, clear, concise | "Your subscription renews on March 1" |
| **Instruct** | Guide action | Direct, imperative, specific | "Enter your email address" |
| **Persuade** | Influence decision | Confident, benefit-focused | "Join 10,000+ teams who ship faster" |
| **Reassure** | Reduce anxiety | Calm, empathetic, supportive | "Your data is encrypted and secure" |
| **Celebrate** | Acknowledge achievement | Warm, congratulatory | "You've completed your first project!" |
| **Warn** | Prevent negative outcome | Clear, serious, not alarming | "This action cannot be undone" |
| **Recover** | Help after error | Helpful, solution-focused | "Check your connection and try again" |

## Timing classification

| Timing | When | Content characteristics |
|--------|------|------------------------|
| **Pre-action** | Before user takes action | Preparation, expectation-setting |
| **During action** | While action is in progress | Progress, reassurance |
| **Post-action** | After action completes | Confirmation, next steps |
| **Proactive** | System-initiated, not user-triggered | Re-engagement, alerts |
| **Reactive** | Response to user query | Support, help content |

## Touchpoint documentation format

When documenting a touchpoint in a journey map:

```yaml
touchpoint:
  name: <descriptive identifier>
  channel: <in-app | email | push | sms | web | in-person | physical>
  type: <content type from classification>
  purpose: <inform | instruct | persuade | reassure | celebrate | warn | recover>
  timing: <pre-action | during | post-action | proactive | reactive>
  owner: <responsible team>
  content_elements:
    - headline: <if applicable>
    - body: <if applicable>
    - cta: <if applicable>
  constraints:
    - <character limits, legal requirements, etc.>
```

## Touchpoint audit questions

When reviewing existing touchpoints:

1. Is the channel appropriate for the urgency and content type?
2. Does the content type match the user's information need at this stage?
3. Is the purpose clear and singular (not trying to do too many things)?
4. Is the timing right relative to user action?
5. Are there gaps where a touchpoint should exist but doesn't?
6. Are there redundant touchpoints that could be consolidated?
