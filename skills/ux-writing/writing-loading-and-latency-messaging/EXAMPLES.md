# Examples

## Example 1: Page load (medium)
**Input:**
- Loading type: initial page load
- Expected duration: 2-5 seconds
- Content: Dashboard with multiple data widgets

**Output:**
```yaml
loading_state:
  tier: "medium"
  message: null
  indicator: "skeleton"
  skeleton_areas: ["header", "stats-cards", "chart", "activity-feed"]
  interruptible: true
  timeout:
    duration_seconds: 15
    fallback: "Couldn't load dashboard. Try refreshing."
```

---

## Example 2: Action response (short)
**Input:**
- Loading type: button action
- Expected duration: 500ms-1s
- Action: Save document

**Output:**
```yaml
loading_state:
  tier: "short"
  message: null
  indicator: "spinner"
  button_state: "disabled"
  interruptible: false
  timeout:
    duration_seconds: 10
    fallback: "Couldn't save. Please try again."
```

---

## Example 3: File upload (long, determinate)
**Input:**
- Loading type: file upload
- Expected duration: 30 seconds
- File size: 50MB

**Output:**
```yaml
loading_state:
  tier: "long"
  message: "Uploading..."
  detail: "23 MB of 50 MB"
  indicator: "progress-bar"
  progress_percent: 46
  interruptible: true
  cancel_label: "Cancel"
  timeout:
    duration_seconds: 120
    fallback: "Upload timed out. Check your connection and try again."
```

---

## Example 4: Report generation (very long)
**Input:**
- Loading type: background processing
- Expected duration: 2-5 minutes
- User can leave: Yes

**Output:**
```yaml
loading_state:
  tier: "long"
  message: "Generating your report..."
  detail: "This usually takes 2-5 minutes. We'll email you when it's ready."
  indicator: "spinner"
  interruptible: true
  allow_close: true
  notification_on_complete: true
  timeout:
    duration_seconds: 600
    fallback: "Report generation timed out. Please try again or contact support."
```

---

## Example 5: Search (instant to short)
**Input:**
- Loading type: search results
- Expected duration: 100-500ms
- Interaction: Typing in search field

**Output:**
```yaml
loading_state:
  tier: "short"
  message: null
  indicator: "spinner"
  placement: "inline-search-field"
  debounce_ms: 300
  timeout:
    duration_seconds: 5
    fallback: "Search failed. Try again."
```

---

## Edge case: Unknown duration
**Input:**
- Loading type: third-party API call
- Expected duration: Unknown (depends on external service)
- Action: Importing data from integration

**Output:**
```yaml
loading_state:
  tier: "unknown"
  message: "Importing from Salesforce..."
  detail: "This may take a few moments depending on your data size."
  indicator: "spinner"
  interruptible: true
  cancel_label: "Cancel import"
  timeout:
    duration_seconds: 180
    fallback: "Import is taking longer than expected. Check back later or try again."
```

---

## Edge case: Background refresh (invisible)
**Input:**
- Loading type: background data refresh
- Expected duration: 1-2 seconds
- User sees: Existing stale content

**Output:**
```yaml
loading_state:
  tier: "short"
  message: null
  indicator: "none"
  show_stale_data: true
  update_on_complete: true
  silent_failure: true
```
Note: Background refreshes should be invisible unless they fail persistently.
