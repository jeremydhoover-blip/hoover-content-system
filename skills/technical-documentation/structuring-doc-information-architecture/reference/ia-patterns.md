# Information Architecture Patterns

## Table of contents
- [Content organization models](#content-organization-models)
- [Navigation patterns](#navigation-patterns)
- [URL structure conventions](#url-structure-conventions)
- [Landing page patterns](#landing-page-patterns)
- [Cross-linking strategies](#cross-linking-strategies)

---

## Content organization models

### By user intent (Diátaxis framework)

| Quadrant | User mode | Content type | Example |
|----------|-----------|--------------|---------|
| Tutorials | Learning | Learning-oriented | "Build your first app" |
| How-to guides | Working | Task-oriented | "How to configure SSO" |
| Reference | Working | Information-oriented | "API endpoints" |
| Explanation | Studying | Understanding-oriented | "How auth works" |

### By user role

| Role | Primary navigation | Content focus |
|------|-------------------|---------------|
| New user | Getting Started | Onboarding, tutorials |
| Developer | API, SDKs | Reference, integration |
| Admin | Admin, Security | Configuration, management |
| Operator | Operations, Monitoring | Deployment, troubleshooting |

### By product area

| When to use | Structure |
|-------------|-----------|
| Multiple distinct products | Product selector + consistent sub-navigation |
| Single product, multiple features | Feature-based sections |
| Platform with services | Service catalog with shared concepts |

---

## Navigation patterns

### Primary navigation limits

| Items | Usability |
|-------|-----------|
| 3-5 | Excellent — easy scanning |
| 6-7 | Good — at cognitive limit |
| 8-9 | Acceptable — requires grouping |
| 10+ | Poor — needs restructuring |

### Hierarchy depth

| Depth | Example | Usability |
|-------|---------|-----------|
| 1 level | `/guides` | Excellent |
| 2 levels | `/guides/authentication` | Good |
| 3 levels | `/guides/authentication/oauth` | Acceptable limit |
| 4+ levels | `/guides/auth/oauth/providers/google` | Too deep |

### Navigation label patterns

| Pattern | Example | Use when |
|---------|---------|----------|
| Noun | "Authentication" | Reference sections |
| Gerund | "Getting Started" | Action-oriented sections |
| Task phrase | "Set up your account" | Tutorials, guides |

**Avoid:**
- Questions: "How do I authenticate?"
- Vague: "Resources", "More", "Misc"
- Internal: "Platform Services", "Core APIs"

---

## URL structure conventions

### Naming rules

| Rule | Example |
|------|---------|
| Lowercase | `/getting-started` |
| Hyphens for spaces | `/api-reference` |
| No special characters | `/oauth2` not `/oauth_2.0` |
| Match navigation label | Nav: "Getting Started" → `/getting-started` |

### Hierarchy in URLs

```
/                           # Home
/getting-started            # Section landing
/getting-started/install    # Page within section
/api/users                  # Reference section
/api/users/create           # Reference page
```

### Redirects policy

| Scenario | Action |
|----------|--------|
| Page moved | 301 redirect, keep for 1 year minimum |
| Section restructured | Redirect old section root to new |
| Page deleted | Redirect to parent or related page |
| Page renamed | Redirect old URL |

---

## Landing page patterns

### Section landing page requirements

| Element | Purpose |
|---------|---------|
| Section title | Clear identification |
| Description | Who this section is for |
| Content categories | Visual grouping |
| Popular pages | Quick access |
| Related sections | Cross-navigation |

### Layout patterns

**Card grid** (best for 6-12 items):
```
┌────────────┐ ┌────────────┐ ┌────────────┐
│ Category 1 │ │ Category 2 │ │ Category 3 │
│ - Item     │ │ - Item     │ │ - Item     │
│ - Item     │ │ - Item     │ │ - Item     │
└────────────┘ └────────────┘ └────────────┘
```

**List with descriptions** (best for 4-8 items):
```
## Section

**Item 1**: Description
**Item 2**: Description
**Item 3**: Description
```

---

## Cross-linking strategies

### When to cross-link

| Scenario | Link type |
|----------|-----------|
| Prerequisite content | "Before you begin" section |
| Related task | "See also" / "Related guides" |
| Deeper explanation | Inline link to concept |
| Next step | "Next: [Page]" at end |

### Link placement

| Location | Best for |
|----------|----------|
| Inline | First mention of related concept |
| Prerequisites section | Required reading before this page |
| Related section (bottom) | Related but not required content |
| Next/Previous navigation | Sequential content |

### Avoiding over-linking

| Guideline | Reason |
|-----------|--------|
| Max 3-5 inline links per section | Reduces cognitive load |
| Don't link common terms | "API" doesn't need linking every time |
| Link on first mention only | Subsequent mentions don't need links |
| Descriptive link text | "See the auth guide" not "click here" |
