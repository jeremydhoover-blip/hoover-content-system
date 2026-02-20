# Rubric

## Pass if all are true:
- Primary task is explicitly identified and all content supports it
- Primary action is visible without scrolling on standard viewports
- Content elements are prioritized with explicit rationale (not just "important")
- Related content is grouped; unrelated content is visually separated
- Reading order matches logical task sequence
- DOM order matches visual order (or deviation is justified for accessibility)
- Help text appears at point of need, not in separate location
- Error states have defined content placement
- Secondary actions are visually subordinate to primary action
- Content structure accounts for empty, loading, and error states

## Fail if any are true:
- Primary action is below fold or visually equal to secondary actions
- Reading order requires users to jump around the screen to complete task
- Related content is scattered across the screen without grouping logic
- Content hierarchy relies solely on visual styling without structural organization
- Help text is front-loaded before users need it (violates progressive disclosure)
- Error messages appear in fixed location away from error source
- Screen structure changes between states without user orientation
- No consideration of mobile/responsive behavior
- DOM order diverges from visual order without ARIA landmarks or skip links
