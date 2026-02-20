# Examples

## Example 1: Developer platform documentation IA

**Input:**
- Product: API platform with CLI and SDK
- Users: Developers (new and experienced), DevOps
- Content: Installation, API reference, guides, changelog

**Output:**

```
Primary Navigation:

┌─────────────────────────────────────────────────────┐
│ Home | Getting Started | Guides | API | CLI | SDKs │
└─────────────────────────────────────────────────────┘

Site Map:

Documentation/
├── Home
│   └── [Quick links to popular content]
│
├── Getting Started
│   ├── Overview (landing)
│   ├── Installation
│   ├── Quick start (5-minute tutorial)
│   └── First integration
│
├── Guides
│   ├── Overview (landing with categories)
│   ├── Authentication
│   │   ├── API keys
│   │   ├── OAuth setup
│   │   └── Token management
│   ├── Webhooks
│   │   ├── Setting up webhooks
│   │   ├── Verifying signatures
│   │   └── Troubleshooting webhooks
│   └── Best practices
│       ├── Rate limiting
│       ├── Error handling
│       └── Pagination
│
├── API Reference
│   ├── Overview (landing)
│   ├── Authentication
│   ├── Users
│   │   ├── Create user
│   │   ├── Get user
│   │   └── [etc.]
│   ├── Projects
│   └── [Other resources]
│
├── CLI Reference
│   ├── Overview (landing + installation)
│   ├── Commands
│   │   ├── auth
│   │   ├── projects
│   │   └── [etc.]
│   └── Configuration
│
├── SDKs
│   ├── Overview (landing)
│   ├── JavaScript
│   ├── Python
│   └── Go
│
└── Resources (footer/utility)
    ├── Changelog
    ├── Status
    └── Support
```

**Navigation specification:**

| Label | Purpose | Target user |
|-------|---------|-------------|
| Getting Started | First-time setup and orientation | New developers |
| Guides | Task-oriented learning | All developers |
| API | Endpoint reference and lookup | Experienced developers |
| CLI | Command-line tool reference | DevOps, power users |
| SDKs | Language-specific libraries | Developers by language |

---

## Example 2: Product documentation IA

**Input:**
- Product: SaaS project management tool
- Users: End users, admins, developers (API)
- Content: User guides, admin guides, API docs

**Output:**

```
Primary Navigation:

┌──────────────────────────────────────────────────────────┐
│ Home | Getting Started | Features | Admin | Developers  │
└──────────────────────────────────────────────────────────┘

Site Map:

Documentation/
├── Home
│   └── Role-based entry points
│
├── Getting Started
│   ├── Overview
│   ├── Create your account
│   ├── Create your first project
│   └── Invite your team
│
├── Features (user guides)
│   ├── Projects
│   │   ├── Creating projects
│   │   ├── Project templates
│   │   └── Archiving projects
│   ├── Tasks
│   │   ├── Creating tasks
│   │   ├── Assigning tasks
│   │   └── Task views
│   ├── Collaboration
│   │   ├── Comments
│   │   ├── Mentions
│   │   └── Notifications
│   └── Reporting
│
├── Admin
│   ├── Overview
│   ├── User management
│   │   ├── Inviting users
│   │   ├── Roles and permissions
│   │   └── Removing users
│   ├── Workspace settings
│   ├── Security
│   │   ├── SSO setup
│   │   └── Audit logs
│   └── Billing
│
└── Developers
    ├── Overview
    ├── API Reference
    ├── Webhooks
    └── Integrations
```

**Role-based entry points on home page:**

| Role | Entry point | First action |
|------|-------------|--------------|
| New user | Getting Started | Create account |
| Team member | Features | Learn daily tasks |
| Admin | Admin | Configure workspace |
| Developer | Developers | API reference |

---

## Example 3: Edge case — large documentation with multiple products

**Input:**
- Company: Cloud platform with 5+ products
- Challenge: Unified docs vs per-product docs
- Users: Different roles per product

**Output:**

```
Global Navigation:

┌───────────────────────────────────────────────────────────┐
│ [Product Selector ▼] | Docs | API | Pricing | Support    │
└───────────────────────────────────────────────────────────┘

Product Selector Dropdown:
├── Platform Overview
├── Compute
├── Storage
├── Database
├── Networking
└── Security

Per-Product Documentation (consistent structure):

[Product Name] Documentation/
├── Home (product-specific)
├── Getting Started
├── Guides
├── Reference
└── Troubleshooting

Cross-Product Elements:
├── Unified search across all products
├── Consistent navigation pattern
├── Shared concepts section
└── Cross-product tutorials
```

**IA design decisions:**

| Challenge | Solution |
|-----------|----------|
| Users work across products | Unified search, cross-linking |
| Products have different complexity | Consistent structure, variable depth |
| Shared concepts | Shared section with product links |
| User confusion | Clear product selector, breadcrumbs |

**Cross-product content strategy:**

```md
# Shared Concepts

These concepts apply across all [Platform] products.

## Authentication

All products use the same authentication system.
- [Authentication overview](/platform/auth)
- Product-specific: [Compute auth](/compute/auth) | [Storage auth](/storage/auth)

## Billing

- [Billing overview](/platform/billing)
- [Compute pricing](/compute/pricing)
- [Storage pricing](/storage/pricing)
```

---

## Anti-pattern example

**Bad output (do not produce):**

```
Navigation:

├── Products
│   ├── Platform Team
│   │   ├── Core API
│   │   ├── Auth Service
│   │   └── Billing Module
│   ├── Frontend Team
│   │   ├── Web App
│   │   ├── Mobile App
│   │   └── Components
│   └── Data Team
│       ├── ETL Pipeline
│       ├── Analytics
│       └── ML Models
├── Engineering
│   ├── Architecture
│   ├── RFC Process
│   └── Oncall
```

**Why this fails:**
- Organized by team structure, not user needs
- Uses internal terms ("Platform Team", "RFC Process")
- No Getting Started section
- No task-oriented organization
- Deep nesting (4+ levels implied)
- No clear entry point for external users
- Mixes internal and external content
