# Examples

## Example 1: Delete single item
**Input:**
- Action: Delete a document
- Item name: "Q4 Report.docx"
- Reversibility: Irreversible
- Impact: Single item, user's own content

**Output:**
```yaml
confirmation_dialog:
  headline: "Delete \"Q4 Report.docx\"?"
  body: "This can't be undone."
  confirm:
    label: "Delete"
    style: "destructive"
  cancel:
    label: "Cancel"
```

---

## Example 2: Remove team member
**Input:**
- Action: Remove person from team
- Person: "Alex Chen"
- Team: "Marketing"
- Reversibility: Reversible (can re-add)
- Impact: Affects another person's access

**Output:**
```yaml
confirmation_dialog:
  headline: "Remove Alex Chen from Marketing?"
  body: "They'll lose access to all team projects and files immediately."
  confirm:
    label: "Remove"
    style: "destructive"
  cancel:
    label: "Cancel"
```

---

## Example 3: Archive (reversible action)
**Input:**
- Action: Archive a project
- Item name: "Website Redesign"
- Reversibility: Fully reversible
- Impact: Removes from active view

**Output:**
```yaml
confirmation_dialog:
  headline: "Archive \"Website Redesign\"?"
  body: "You can restore it anytime from Settings > Archive."
  confirm:
    label: "Archive"
    style: "default"
  cancel:
    label: "Cancel"
```

---

## Example 4: Bulk delete
**Input:**
- Action: Delete multiple files
- Count: 23 files
- Reversibility: Irreversible
- Impact: Multiple items permanently removed

**Output:**
```yaml
confirmation_dialog:
  headline: "Delete 23 files?"
  body: "This will permanently delete all selected files. This can't be undone."
  confirm:
    label: "Delete 23 files"
    style: "destructive"
  cancel:
    label: "Cancel"
```

---

## Example 5: Leave organization
**Input:**
- Action: User leaving an organization
- Organization: "Acme Corp"
- Reversibility: Requires re-invitation
- Impact: Account-wide, affects access to all org resources

**Output:**
```yaml
confirmation_dialog:
  headline: "Leave Acme Corp?"
  body: "You'll lose access to all shared projects and files. You'll need a new invitation to rejoin."
  confirm:
    label: "Leave organization"
    style: "destructive"
  cancel:
    label: "Stay"
```
Note: "Stay" is clearer than "Cancel" here because it explicitly describes the safe outcome.

---

## Edge case: Discard unsaved changes
**Input:**
- Action: Navigate away with unsaved changes
- Context: User edited a form and clicked away
- Reversibility: Changes lost permanently
- Impact: User's work discarded

**Output:**
```yaml
confirmation_dialog:
  headline: "Discard unsaved changes?"
  body: "Your changes haven't been saved and will be lost."
  confirm:
    label: "Discard"
    style: "destructive"
  cancel:
    label: "Keep editing"
```
