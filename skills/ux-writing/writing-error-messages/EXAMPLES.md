# Examples

## Example 1: Validation error
**Input:**
- Error type: validation
- Context: User submitted email field with invalid format
- Field: Email address

**Output:**
```yaml
error:
  title: "Enter a valid email address"
  body: null
  action:
    label: null
    type: null
```
Inline display: "Enter a valid email address" (below field, no action button)

---

## Example 2: Network error
**Input:**
- Error type: network
- Context: API call failed due to connectivity
- User action: Saving a document

**Output:**
```yaml
error:
  title: "Couldn't save your changes"
  body: "Check your internet connection and try again."
  action:
    label: "Retry"
    type: "retry"
```

---

## Example 3: Permission error
**Input:**
- Error type: permission
- Context: User tried to access admin settings without admin role
- User action: Clicking "Admin Settings" link

**Output:**
```yaml
error:
  title: "You don't have access to admin settings"
  body: "Contact your workspace admin to request access."
  action:
    label: "Request access"
    type: "navigate"
```

---

## Example 4: System error (unknown cause)
**Input:**
- Error type: system
- Context: Unexpected server error, cause unknown
- User action: Loading dashboard

**Output:**
```yaml
error:
  title: "Something went wrong"
  body: "We're working on it. Please try again in a few minutes."
  action:
    label: "Try again"
    type: "retry"
```

---

## Example 5: Not found error
**Input:**
- Error type: not-found
- Context: User navigated to a deleted project via old link
- Item: Project

**Output:**
```yaml
error:
  title: "Project not found"
  body: "This project may have been deleted or moved."
  action:
    label: "Go to projects"
    type: "navigate"
```

---

## Edge case: Error with no recovery action
**Input:**
- Error type: system
- Context: Account suspended by admin
- User action: Logging in

**Output:**
```yaml
error:
  title: "Your account has been suspended"
  body: "Contact your organization's admin for help."
  action:
    label: "Dismiss"
    type: "dismiss"
```
Note: When no in-app recovery exists, direct to human support.
