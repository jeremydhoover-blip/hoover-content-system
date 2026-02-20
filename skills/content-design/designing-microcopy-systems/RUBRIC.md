# Rubric

## Pass if all are true:
- Every component type has explicit copy slots defined
- Each slot specifies: required/optional, max characters, structural pattern
- Patterns use testable language ("Verb + object" not "make it clear")
- Variation rules distinguish allowed flexibility from required consistency
- At least one correct and one incorrect example per component type
- Incorrect examples explain why they fail
- Global constraints address localization expansion (typically 30-40% for English-to-German)
- Accessibility slot requirements are explicit (e.g., button labels must be self-describing)
- Error patterns include both "what happened" and "how to fix" structure
- System documentation includes a component inventory with coverage status

## Fail if any are true:
- Patterns use subjective language ("sounds natural", "feels right")
- Character limits are missing for constrained UI elements
- Components have undefined copy slots (placeholder exists but no guidance)
- Variation rules are absent (everything is "use your judgment")
- Examples only show correct usage without failure cases
- System covers primary states but ignores error, empty, loading states
- Localization requirements are ignored
- Patterns contradict each other across components
- Helper text patterns duplicate label patterns (redundant slots)
