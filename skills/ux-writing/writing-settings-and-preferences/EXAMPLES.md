# Examples

## Example 1: Notification toggle
**Input:**
- Category: Notifications
- Setting: Control email notifications for project updates
- Default: On

**Output:**
```yaml
setting:
  category: "notifications"
  label: "Project update emails"
  description: "Get notified when someone updates a project you're in."
  type: "toggle"
  default: true
```

---

## Example 2: Theme selector
**Input:**
- Category: Appearance
- Setting: App color theme
- Options: Light, Dark, System default
- Default: System

**Output:**
```yaml
setting:
  category: "appearance"
  label: "Theme"
  description: "Choose light, dark, or match your system setting."
  type: "select"
  default: "System"
  options: ["Light", "Dark", "System"]
```

---

## Example 3: Privacy toggle
**Input:**
- Category: Privacy
- Setting: Profile visibility to non-team members
- Default: Off (private)

**Output:**
```yaml
setting:
  category: "privacy"
  label: "Public profile"
  description: "Allow people outside your team to see your profile."
  type: "toggle"
  default: false
```

---

## Example 4: Input setting
**Input:**
- Category: Account
- Setting: Display name shown to other users
- Default: Empty (from signup)

**Output:**
```yaml
setting:
  category: "account"
  label: "Display name"
  description: "How your name appears to teammates."
  type: "input"
  default: null
  placeholder: "Your name"
```

---

## Example 5: Destructive action
**Input:**
- Category: Account
- Setting: Delete account permanently
- Reversibility: Irreversible

**Output:**
```yaml
setting:
  category: "account"
  label: "Delete account"
  description: "Permanently delete your account and all your data. This can't be undone."
  type: "action"
  action_label: "Delete account"
  style: "destructive"
  requires_confirmation: true
```

---

## Edge case: Double negative to avoid
**Input (bad):**
- Label: "Disable email notifications"
- Type: Toggle

**Why it fails:**
- When toggle is ON, notifications are OFF — confusing
- Double mental model: "Turn on to turn off"

**Fixed output:**
```yaml
setting:
  category: "notifications"
  label: "Email notifications"
  description: "Receive emails about activity."
  type: "toggle"
  default: true
```
Rule: Toggle labels describe the ON state. "Email notifications" ON = you get emails.

---

## Edge case: Complex setting with learn more
**Input:**
- Category: Advanced
- Setting: API rate limiting
- Needs documentation link

**Output:**
```yaml
setting:
  category: "advanced"
  label: "API rate limit"
  description: "Maximum API requests per minute. Learn more"
  type: "input"
  default: "1000"
  helper_text: "Enter a number between 100 and 10000"
  learn_more_url: "/docs/api-rate-limits"
```
