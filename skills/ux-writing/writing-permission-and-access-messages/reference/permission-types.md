# Permission Types

Taxonomy of permission and access message types.

---

## Table of contents
- [Permission categories](#permission-categories)
- [Access states](#access-states)
- [Request patterns](#request-patterns)
- [Denial patterns](#denial-patterns)

---

## Permission categories

### System permissions (device/OS level)
| Permission | Data accessed | Sensitivity |
|------------|---------------|-------------|
| Camera | Photos, video | High |
| Microphone | Audio | High |
| Location | GPS coordinates | High |
| Contacts | Address book | High |
| Calendar | Events | Medium |
| Photos/Files | Storage | Medium |
| Notifications | Alert capability | Low |
| Bluetooth | Nearby devices | Medium |

### App permissions (feature access)
| Permission | Access granted | Typical roles |
|------------|----------------|---------------|
| Admin | Full control | Owners |
| Editor | Create, modify | Team members |
| Viewer | Read only | Guests, stakeholders |
| Commenter | Read + comment | Reviewers |
| None | No access | Default/removed |

### Data permissions
| Permission | Scope | Example |
|------------|-------|---------|
| Public | Anyone | Profile visible to all |
| Organization | Company members | Internal docs |
| Team | Specific group | Project files |
| Private | Owner only | Drafts |
| Specific people | Named individuals | Shared file |

---

## Access states

| State | Meaning | User can... |
|-------|---------|-------------|
| **granted** | Has permission | Use feature |
| **denied** | Explicitly refused | Request again (some) |
| **not_requested** | Never asked | Be prompted |
| **restricted** | System-level block | Go to settings |
| **expired** | Was granted, now revoked | Re-request |
| **pending** | Requested, awaiting approval | Wait, check status |

---

## Request patterns

### Pre-prompt (before system dialog)
```yaml
pre_prompt:
  purpose: "Explain why before asking"
  structure:
    headline: "[App] wants to access your [permission]"
    body: "[Why we need it] + [What you get]"
    actions:
      primary: "Continue"
      secondary: "Not now"
```

### System prompt enhancement
| OS | Customizable | Location |
|----|--------------|----------|
| iOS | Usage description string | Info.plist |
| Android | Permission rationale | Before dialog |
| Web | Prompt timing only | — |

### Request copy patterns
```yaml
# Camera
headline: "Take and share photos"
body: "Camera access lets you [specific use case]."

# Location  
headline: "Find [things] near you"
body: "Location access lets you [specific benefit]."

# Notifications
headline: "Stay updated on [relevant thing]"
body: "Get notified when [specific trigger]."
```

### What to include
- **Why**: Specific reason for this permission
- **What**: What user can do with it
- **When**: If relevant (e.g., "only when using the app")

### What NOT to include
- Vague justifications ("to improve your experience")
- Multiple permissions at once
- Technical language

---

## Denial patterns

### First denial
```yaml
denial_response:
  type: "first_denial"
  show_immediately: false
  offer_alternative: true
  tone: "Understanding, not pushy"
```

### Persistent denial
```yaml
denial_response:
  type: "persistent"
  action: "Offer manual path"
  copy: "To use [feature], enable [permission] in Settings."
  cta: "Open Settings"
```

### Hard block (feature requires permission)
```yaml
denial_response:
  type: "blocking"
  headline: "[Feature] needs [permission]"
  body: "To [user goal], allow [permission] access."
  actions:
    primary: "Go to Settings"
    secondary: "Cancel"
```

### Soft block (degraded experience)
```yaml
denial_response:
  type: "degraded"
  inline_notice: "[Feature] works better with [permission]."
  action: "Enable"
```

---

## Role-based access patterns

### Insufficient permissions
```yaml
access_denied:
  headline: "You don't have access to [thing]"
  body: "Contact [owner/admin] to request access."
  action:
    primary: "Request access"
    secondary: "Go back"
```

### Upgrade required
```yaml
access_denied:
  headline: "[Feature] is available on [plan]"
  body: "Upgrade to [plan] to [benefit]."
  action:
    primary: "See plans"
    secondary: "Maybe later"
```

### Ownership transfer
```yaml
access_change:
  headline: "Transfer ownership"
  body: "[Current owner] will lose owner permissions."
  warning: "This can't be undone."
  confirmation: "Transfer to [new owner]"
```

---

## Message timing

| Scenario | When to request |
|----------|-----------------|
| Onboarding | Only if essential to core value |
| Feature trigger | When user tries to use feature |
| Contextual | When benefit is clear |
| Never | Immediately on app launch |

---

## Anti-patterns

| Pattern | Problem | Fix |
|---------|---------|-----|
| Request all at once | Overwhelming, low grant rate | Request contextually |
| No explanation | User doesn't understand why | Explain benefit |
| "We need access" | Company-focused | User-focused: "You can..." |
| Request on launch | No context | Wait for feature use |
| Repeated asking | Annoying | Respect "no", offer settings |
| Vague denials | User confused | Be specific about what's blocked |
