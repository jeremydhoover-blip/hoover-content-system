# Templates

## Default permission request structure

```md
## [Headline - what access]
[Explanation - why needed and benefit]

[Deny action] | [Allow action]
```

## Structured output format

```yaml
permission_message:
  type: "<system|data|role|feature>"
  state: "<requesting|denied|expired|insufficient>"
  headline: "<what access - max 60 chars>"
  explanation: "<why and benefit - max 150 chars>"
  allow:
    label: "<grant action - max 20 chars>"
  deny:
    label: "<decline action - max 20 chars>"
```

## Variations by message state

### Permission request (before system prompt)
```yaml
permission_message:
  type: "system"
  state: "requesting"
  headline: "Allow location access?"
  explanation: "We use your location to show nearby stores and calculate delivery times."
  allow:
    label: "Allow"
  deny:
    label: "Not now"
```

### Permission denied (user previously declined)
```yaml
permission_message:
  type: "system"
  state: "denied"
  headline: "Location access needed"
  explanation: "To use this feature, allow location access in your device settings."
  allow:
    label: "Open settings"
  deny:
    label: "Cancel"
```

### Insufficient role access
```yaml
permission_message:
  type: "role"
  state: "insufficient"
  headline: "Admin access required"
  explanation: "Only workspace admins can change billing settings."
  allow:
    label: "Request access"
  deny:
    label: "Cancel"
```

### Feature access (paywall or plan limit)
```yaml
permission_message:
  type: "feature"
  state: "insufficient"
  headline: "Upgrade to use this feature"
  explanation: "Advanced analytics is available on Pro and Enterprise plans."
  allow:
    label: "View plans"
  deny:
    label: "Maybe later"
```

## Pre-request pattern (recommended for sensitive permissions)
Show a custom prompt before triggering the system permission dialog:
```yaml
pre_request:
  headline: "See stores near you"
  explanation: "Allow location access to find stores and get accurate delivery times."
  allow:
    label: "Continue"
  deny:
    label: "Not now"
```

## Allowed variations
- Use "Not now" instead of "Don't allow" for softer decline
- Include illustration showing feature that needs permission
- Link to privacy policy for data-sensitive permissions
