# Examples

## Example 1: Developer documentation navigation

**Input:**
- Site: API platform documentation
- Sections: Getting Started, Guides, API Reference, SDKs
- Features: Versioned docs, code search

**Output:**

```
┌─────────────────────────────────────────────────────────────────────┐
│ [Logo] │ Getting Started  Guides  API  SDKs │ [🔍] [v2.0 ▼] [☾]  │
└─────────────────────────────────────────────────────────────────────┘
│                                                                     │
│ ┌──────────────┐  ┌─────────────────────────────────┐  ┌─────────┐ │
│ │ SIDEBAR      │  │ CONTENT                         │  │ ON THIS │ │
│ │              │  │                                 │  │ PAGE    │ │
│ │ ▼ Getting    │  │ Docs > Guides > Auth > OAuth    │  │         │ │
│ │   Started    │  │                                 │  │ • Intro │ │
│ │   • Overview │  │ # OAuth Setup                   │  │ • Setup │ │
│ │   • Install  │  │                                 │  │ • Config│ │
│ │   • Quick... │  │ [Content...]                    │  │ • Test  │ │
│ │              │  │                                 │  │         │ │
│ │ ▶ Guides     │  │                                 │  │         │ │
│ │ ▶ Reference  │  │                                 │  │         │ │
│ │              │  │ ← Previous  |  Next →           │  │         │ │
│ └──────────────┘  └─────────────────────────────────┘  └─────────┘ │
└─────────────────────────────────────────────────────────────────────┘
```

**Navigation specification:**

```yaml
# Primary navigation
header:
  logo:
    text: "Platform Docs"
    href: /
  nav:
    - label: Getting Started
      href: /getting-started
    - label: Guides
      href: /guides
    - label: API
      href: /api
    - label: SDKs
      href: /sdks
  utilities:
    - search:
        shortcut: "/"
        placeholder: "Search docs..."
    - version:
        current: "v2.0"
        options: ["v2.0", "v1.0"]
    - theme:
        options: ["light", "dark", "system"]

# Sidebar (Guides section)
sidebar:
  - category: Authentication
    items:
      - label: Overview
        href: /guides/auth
      - label: API Keys
        href: /guides/auth/api-keys
      - label: OAuth Setup
        href: /guides/auth/oauth
  - category: Webhooks
    items:
      - label: Setting Up
        href: /guides/webhooks/setup
      - label: Verification
        href: /guides/webhooks/verify

# In-page navigation
toc:
  levels: [2, 3]
  title: "On this page"
  
# Footer navigation  
pagination:
  previous: /guides/auth/api-keys
  next: /guides/auth/tokens
```

---

## Example 2: Product documentation navigation

**Input:**
- Site: SaaS product documentation
- Audiences: End users, admins, developers
- Challenge: Role-based content

**Output:**

```
┌─────────────────────────────────────────────────────────────────────┐
│ [Logo] │ User Guide  Admin  Developers │ [🔍 Search]              │
└─────────────────────────────────────────────────────────────────────┘

Homepage layout:

┌─────────────────────────────────────────────────────────────────────┐
│                         Welcome to Docs                            │
│                  Find guides, tutorials, and reference             │
│                                                                     │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐    │
│  │ 👤 User Guide   │  │ ⚙️ Admin        │  │ 💻 Developers   │    │
│  │                 │  │                 │  │                 │    │
│  │ Learn to use    │  │ Configure and   │  │ API reference   │    │
│  │ the product     │  │ manage settings │  │ and SDKs        │    │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘    │
│                                                                     │
│  Popular:  Getting started · Projects · Teams · API overview       │
└─────────────────────────────────────────────────────────────────────┘
```

**Navigation by role:**

```md
## User Guide navigation

Sidebar:
- Getting Started
  - Create account
  - First project
  - Invite team
- Projects
  - Creating projects
  - Project settings
  - Templates
- Tasks
  - Creating tasks
  - Assignments
  - Due dates
- Collaboration
  - Comments
  - Notifications

## Admin navigation

Sidebar:
- User Management
  - Inviting users
  - Roles
  - Removing users
- Settings
  - Workspace settings
  - Security
  - Integrations
- Billing
  - Plans
  - Invoices

## Developer navigation

Sidebar:
- Overview
- Authentication
- API Reference
  - Users
  - Projects
  - Tasks
- Webhooks
- SDKs
```

---

## Example 3: Edge case — mobile navigation

**Input:**
- Challenge: Complex navigation on mobile
- Requirement: All content accessible, no horizontal scroll

**Output:**

**Mobile navigation pattern:**

```
┌─────────────────────────────┐
│ [☰]  Platform Docs  [🔍]   │
└─────────────────────────────┘
        │
        ▼ (menu tap)
┌─────────────────────────────┐
│ ┌─────────────────────────┐ │
│ │ 🔍 Search docs...       │ │
│ └─────────────────────────┘ │
│                             │
│ Getting Started        →   │
│ Guides                 →   │
│ API Reference          →   │
│ SDKs                   →   │
│                             │
│ ─────────────────────────  │
│ Version: v2.0          ▼   │
│ Theme: System          ▼   │
└─────────────────────────────┘
```

**Specification:**

```yaml
mobile:
  breakpoint: 768px
  
  header:
    left: hamburger_menu
    center: site_title
    right: search_icon
    
  menu:
    type: full_screen_overlay
    animation: slide_from_left
    
    structure:
      - search_bar (sticky)
      - primary_nav (expandable)
      - utilities (version, theme)
      
  sidebar:
    behavior: hidden
    access: via_hamburger_menu
    
  toc:
    behavior: collapsed_dropdown
    trigger: "On this page ▼"
    position: below_title
    
  breadcrumbs:
    max_items: 3
    truncate: middle
```

**Mobile-specific patterns:**

| Element | Desktop | Mobile |
|---------|---------|--------|
| Primary nav | Horizontal header | Hamburger menu |
| Sidebar | Left, always visible | Hidden, via menu |
| TOC | Right sidebar | Dropdown below title |
| Search | Header | Icon → expand |
| Breadcrumbs | Full | Truncated |

---

## Anti-pattern example

**Bad output (do not produce):**

```
Navigation:
- Home
- Docs
  - Section 1
    - Subsection A
      - Topic 1
        - Subtopic a
          - Detail i
          - Detail ii
        - Subtopic b
    - Subsection B
  - Section 2
  - Section 3
  ...
  - Section 15
```

**Why this fails:**
- Navigation 5+ levels deep
- 15+ primary items
- No breadcrumbs planned
- No search consideration
- No mobile strategy
- No current location indicator
- Generic labels ("Section 1")
