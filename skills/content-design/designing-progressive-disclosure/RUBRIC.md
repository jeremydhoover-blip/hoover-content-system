# Rubric

## Pass if all are true:
- All content is categorized into explicit layers (essential, supplementary, edge-case)
- Essential content is never hidden behind interaction requirements
- Each hidden layer has a defined trigger and reveal mechanism
- Discoverability signals exist for all hidden content (users know more exists)
- Reveal mechanisms are appropriate for content type (tooltip for brief, drawer for complex)
- Reverse action is defined (how to collapse/dismiss revealed content)
- Progressive disclosure serves user task, not just visual cleanliness
- Advanced/power-user content is accessible but not blocking primary path
- Accessibility is preserved (revealed content is reachable via keyboard, announced to screen readers)
- Layer categorization is justified by user research or behavioral logic, not assumption

## Fail if any are true:
- Essential task-completion content is hidden behind clicks
- Hidden content has no discoverability signal (users must guess it exists)
- Reveal mechanism is inappropriate (complex content in tooltip, brief content requiring new screen)
- All content is treated as essential (no layering applied—just "show everything")
- All content is treated as supplementary (over-hidden—essential content buried)
- Hover-triggered reveals with no click alternative (accessibility failure)
- Progressive disclosure is used to hide problems instead of solving them
- No reverse action defined (revealed content cannot be collapsed)
- Layer categorization is arbitrary ("feels like too much" without task analysis)
