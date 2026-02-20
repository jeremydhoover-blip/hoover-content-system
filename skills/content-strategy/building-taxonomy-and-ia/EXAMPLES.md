# Examples

## Example 1: SaaS help center

**Input:**
- Product: Email marketing platform
- Content: Help articles, tutorials, troubleshooting, API docs
- Users: Marketers (non-technical), developers
- Problem: Current structure mirrors product features, users can't find what they need

**Output:**

```md
# Taxonomy: MailForge Help Center

## Taxonomy principles
- **Mutual exclusivity:** Each article lives in one category
- **Exhaustiveness:** All help content has a home
- **User-centric:** Categories based on user goals, not product architecture
- **Scalable:** New features fit existing categories

---

## Hierarchy

### Level 1: Primary categories

| Category | Description | Contains |
|----------|-------------|----------|
| Getting started | First-time setup and quick wins | Onboarding, account setup, first campaign |
| Creating campaigns | Building and sending emails | Editor, templates, scheduling, sending |
| Managing contacts | Lists, segments, and subscriber data | Import, segmentation, compliance |
| Analyzing results | Reports, metrics, optimization | Analytics, A/B tests, deliverability |
| Account & billing | Settings, team, payments | Account settings, billing, team management |
| Developers | API, integrations, webhooks | API docs, SDKs, integration guides |

### Level 2: Subcategories

#### Getting started
| Subcategory | Description |
|-------------|-------------|
| Account setup | Creating account, verification, settings |
| Quick start guides | First campaign, first automation, first segment |
| Concepts | Glossary, how MailForge works |

#### Creating campaigns
| Subcategory | Description |
|-------------|-------------|
| Email editor | Using the drag-drop editor |
| Templates | Choosing, customizing, saving templates |
| Sending | Scheduling, testing, sending |
| Automations | Triggered emails, drip campaigns |

#### Managing contacts
| Subcategory | Description |
|-------------|-------------|
| Importing | Uploading contacts, CSV, integrations |
| Segments | Creating and managing segments |
| Compliance | GDPR, unsubscribes, consent |

#### Analyzing results
| Subcategory | Description |
|-------------|-------------|
| Campaign reports | Opens, clicks, conversions |
| Deliverability | Bounce rates, spam, sender reputation |
| A/B testing | Setting up and analyzing tests |

#### Developers
| Subcategory | Description |
|-------------|-------------|
| API reference | Endpoints, authentication |
| SDKs | Official libraries |
| Integrations | Third-party connections |

---

## Content type mapping

| Content type | Primary location | Cross-link |
|--------------|------------------|------------|
| How-to article | Relevant task category | Related concepts |
| Troubleshooting | Within relevant category | Deliverability if email-related |
| API endpoint doc | Developers > API reference | — |
| Tutorial | Getting started or relevant category | — |

---

## Decision rules

### Where does troubleshooting content go?
1. If about sending → Creating campaigns > Sending
2. If about deliverability → Analyzing results > Deliverability
3. If about imports → Managing contacts > Importing
4. Default: Category of the feature involved

---

## Visual hierarchy

```
Help Center
├── Getting started
│   ├── Account setup
│   ├── Quick start guides
│   └── Concepts
├── Creating campaigns
│   ├── Email editor
│   ├── Templates
│   ├── Sending
│   └── Automations
├── Managing contacts
│   ├── Importing
│   ├── Segments
│   └── Compliance
├── Analyzing results
│   ├── Campaign reports
│   ├── Deliverability
│   └── A/B testing
├── Account & billing
└── Developers
    ├── API reference
    ├── SDKs
    └── Integrations
```
```

---

## Example 2: Documentation site for developer tool

**Input:**
- Product: CLI tool for cloud deployment
- Content: Tutorials, reference docs, conceptual guides, changelogs
- Users: Developers (beginner to advanced)
- Problem: Flat structure makes discovery difficult; users don't know where to start

**Output:**

```md
# Taxonomy: CloudDeploy Docs

## Hierarchy

### Level 1: Primary categories

| Category | Description | Audience |
|----------|-------------|----------|
| Getting started | Installation, first deployment | New users |
| Tutorials | Step-by-step guided walkthroughs | Learning |
| Concepts | How things work, architecture | Understanding |
| Reference | Commands, config, API | Lookup |
| Guides | Best practices, patterns | Intermediate+ |
| Releases | Changelogs, migration | All |

### Level 2: Subcategories

#### Getting started
| Subcategory | Description |
|-------------|-------------|
| Installation | Platform-specific install |
| Quickstart | Deploy in 5 minutes |
| Authentication | Setting up credentials |

#### Reference
| Subcategory | Description |
|-------------|-------------|
| CLI commands | All commands A-Z |
| Configuration | Config file options |
| Environment variables | Supported env vars |
| Exit codes | Error code reference |

#### Guides
| Subcategory | Description |
|-------------|-------------|
| CI/CD | Integration patterns |
| Multi-environment | Staging, production setups |
| Security | Secrets, permissions |

---

## Navigation labels

| Internal | User-facing | Why |
|----------|-------------|-----|
| CLI reference | Commands | Users say "commands" |
| Conceptual docs | Concepts | Matches mental model |

---

## Content placement rules

| Content type | Location | Rationale |
|--------------|----------|-----------|
| "How do I...?" | Tutorials or Guides | Task-oriented |
| "What is...?" | Concepts | Explanation-oriented |
| "What are the options for...?" | Reference | Lookup-oriented |
| "What's new?" | Releases | Temporal |

---

## Visual hierarchy

```
CloudDeploy Docs
├── Getting started
│   ├── Installation
│   ├── Quickstart
│   └── Authentication
├── Tutorials
├── Concepts
├── Reference
│   ├── CLI commands
│   ├── Configuration
│   ├── Environment variables
│   └── Exit codes
├── Guides
│   ├── CI/CD
│   ├── Multi-environment
│   └── Security
└── Releases
```
```

---

## Example 3: Edge case — Regulated industry with compliance requirements

**Input:**
- Product: Financial services knowledge base
- Content: Product info, compliance docs, procedures, FAQs
- Users: Internal staff, external customers
- Constraint: Some content must be access-controlled; audit trail required

**Output:**

```md
# Taxonomy: WealthFirst Knowledge Base

## Special considerations
- Access control: Some categories are internal-only
- Audit requirements: Compliance content requires version history
- Dual audience: Same topics need customer and staff versions

---

## Hierarchy

### Level 1: Primary categories

| Category | Access | Description |
|----------|--------|-------------|
| Customer resources | Public | Client-facing information |
| Products | Public | Product descriptions, features |
| Forms & applications | Public | Required paperwork |
| Procedures | Internal | Staff processes |
| Compliance | Internal | Regulatory requirements |
| Training | Internal | Staff education |

### Level 2: Customer resources
| Subcategory | Description |
|-------------|-------------|
| Account management | Opening, closing, changes |
| Statements & reports | Understanding documents |
| Fees & pricing | Cost information |
| Contact & support | How to get help |

### Level 2: Compliance (Internal)
| Subcategory | Description |
|-------------|-------------|
| Regulatory requirements | SEC, FINRA rules |
| Internal policies | Company procedures |
| Audit materials | Audit-ready documentation |

---

## Dual-audience content handling

| Topic | Customer version | Staff version |
|-------|------------------|---------------|
| Account opening | Products > [Product] > How to open | Procedures > Account opening |
| Fee disputes | Customer resources > Fees | Procedures > Fee adjustments |

---

## Governance

### Compliance content changes
1. Legal review required
2. Version must be preserved
3. Effective date must be documented

### Access control review
- Quarterly audit of category access
- Annual review of internal/external split
```
