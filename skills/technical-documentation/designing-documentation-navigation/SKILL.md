---
name: designing-documentation-navigation
description: Design navigation systems, menus, and wayfinding elements for documentation sites. Use when creating or improving how users find and move through documentation.
---

# Designing Documentation Navigation

## Quick start
Collect or infer:
- Site structure and content inventory
- Primary user tasks and entry points
- Navigation constraints (platform, viewport)
- Search capabilities and patterns
- Breadcrumb and contextual navigation needs

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Map user entry points and common paths.
2. Design primary navigation (top-level menu).
3. Design section navigation (sidebar/submenu).
4. Configure breadcrumbs and location indicators.
5. Add contextual navigation (related, previous/next).
6. Integrate search placement and behavior.
7. Test navigation paths for common tasks.
8. Run the rubric check. Revise until it passes.

## Degrees of freedom
- **Medium**: Navigation patterns can vary by site type.
- Allowed variation: Sidebar position, menu style, mobile behavior may vary as long as rubric passes.

## State awareness
- If content is versioned, integrate version selector prominently.
- If site is large, prioritize search over deep navigation.
- If users come from search engines, ensure breadcrumbs provide context.
- If documentation spans products, provide clear product switching.

## Failure modes to avoid
- Navigation deeper than 3 clicks to any content
- Missing breadcrumbs on content pages
- No "on this page" navigation for long pages
- Inconsistent navigation behavior across sections
- Search hidden or hard to access

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
- Navigation patterns: [reference/nav-patterns.md](reference/nav-patterns.md)
