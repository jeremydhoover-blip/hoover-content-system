# Examples

## Example 1: Location permission request
**Input:**
- Permission type: system (location)
- State: requesting
- Feature: Store finder
- User benefit: Find nearby stores

**Output:**
```yaml
permission_message:
  type: "system"
  state: "requesting"
  headline: "Allow location access?"
  explanation: "Find stores near you and get accurate delivery estimates."
  allow:
    label: "Allow"
  deny:
    label: "Not now"
```

---

## Example 2: Notification permission request
**Input:**
- Permission type: system (notifications)
- State: requesting
- Feature: Order updates
- User benefit: Know when order ships/arrives

**Output:**
```yaml
permission_message:
  type: "system"
  state: "requesting"
  headline: "Get notified about your orders?"
  explanation: "We'll let you know when your order ships and arrives."
  allow:
    label: "Allow"
  deny:
    label: "Not now"
```

---

## Example 3: Permission previously denied
**Input:**
- Permission type: system (camera)
- State: denied
- Feature: Scan QR code
- Context: User trying to use scanner after denying camera access

**Output:**
```yaml
permission_message:
  type: "system"
  state: "denied"
  headline: "Camera access needed"
  explanation: "To scan QR codes, allow camera access in your device settings."
  allow:
    label: "Open settings"
  deny:
    label: "Cancel"
```

---

## Example 4: Role-based access denied
**Input:**
- Permission type: role
- State: insufficient
- Feature: Team billing settings
- Required role: Admin
- User's role: Member

**Output:**
```yaml
permission_message:
  type: "role"
  state: "insufficient"
  headline: "Admin access required"
  explanation: "Contact your workspace admin to change billing settings."
  allow:
    label: "Request access"
  deny:
    label: "Go back"
```

---

## Example 5: Feature behind paywall
**Input:**
- Permission type: feature
- State: insufficient
- Feature: Export to PDF
- Current plan: Free
- Required plan: Pro

**Output:**
```yaml
permission_message:
  type: "feature"
  state: "insufficient"
  headline: "Upgrade to export as PDF"
  explanation: "PDF export is available on Pro plans. Start a free trial today."
  allow:
    label: "Start free trial"
  deny:
    label: "Maybe later"
```

---

## Edge case: Sensitive data permission
**Input:**
- Permission type: data
- State: requesting
- Feature: Contact sync
- Sensitivity: High (accessing user's contacts)

**Output:**
```yaml
pre_request:
  headline: "Import your contacts?"
  explanation: "We'll find people you know who are already on the app. Your contacts stay private."
  allow:
    label: "Continue"
  deny:
    label: "Skip"
  privacy_link: "/privacy"
```
Note: For sensitive permissions, use pre-request to explain before system prompt.

---

## Edge case: Session expired
**Input:**
- Permission type: data
- State: expired
- Context: OAuth token expired
- Action needed: Re-authenticate

**Output:**
```yaml
permission_message:
  type: "data"
  state: "expired"
  headline: "Sign in again to continue"
  explanation: "Your session expired. Sign in to reconnect your account."
  allow:
    label: "Sign in"
  deny:
    label: "Cancel"
```
