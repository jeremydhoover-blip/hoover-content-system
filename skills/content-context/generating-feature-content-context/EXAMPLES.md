# Examples

## Example 1: File upload feature

**Input:**
- Feature: File upload in document management system
- Users: Business users uploading contracts and documents
- Constraints: 25MB limit, specific file types only

**Output:**

```md
# Feature Content Context: File Upload

## Feature overview

### Purpose
Allows users to upload documents to their workspace for storage, sharing, and processing.

### User goals
| Goal | Priority |
|------|----------|
| Upload a document quickly | Primary |
| Understand upload status | Secondary |
| Recover from upload failures | Secondary |

### Feature boundaries
- **Included:** File selection, upload progress, success/error handling, file type validation
- **Excluded:** File organization (separate feature), file preview, sharing settings

---

## User context

### Who uses this
Business users managing contracts and documents; varying technical comfort levels.

### When they use it
- Onboarding: Adding existing documents to new workspace
- Daily work: Uploading new contracts as they're signed
- Batch work: End of month document uploads

### What they know
- **Assumed:** Familiar with file upload from other apps
- **New:** Our specific file type restrictions and size limits

### Emotional state
- **Normal upload:** Routine task, want it to be fast
- **Large batch:** May be tedious, want progress visibility
- **Failed upload:** Frustrated, need clear path to resolution

---

## Feature states

### Happy path states

#### Empty (no file selected)
**When:** User opens upload dialog with no file selected
**User need:** Understand how to start, what's supported
**Content requirements:**
- Primary instruction (what to do)
- Supported file types
- Size limit information
- Drag-drop affordance

#### Uploading (in progress)
**When:** File is being uploaded to server
**User need:** Know it's working, estimate wait time
**Content requirements:**
- Progress indicator context
- File name confirmation
- Cancel option label

#### Success
**When:** Upload completes successfully
**User need:** Confirmation, next step options
**Content requirements:**
- Success confirmation
- File name
- Next action options (view, upload another)

### Error states

#### File too large
**When:** User selects file >25MB
**Cause:** User error (selected wrong file or file exceeds limit)
**Recovery:** Select smaller file or compress
**Content requirements:**
- Error message stating limit
- Current file size
- Suggested action

#### Invalid file type
**When:** User selects unsupported format
**Cause:** User error
**Recovery:** Convert file or select different file
**Content requirements:**
- Error message stating invalid type
- List of supported types
- Suggestion to convert

#### Network failure
**When:** Connection lost during upload
**Cause:** Technical (user's network)
**Recovery:** Check connection, retry
**Content requirements:**
- Error message (not blaming user)
- Retry option
- Auto-retry indication if applicable

#### Server error
**When:** Our servers fail to process
**Cause:** Technical (our fault)
**Recovery:** Automatic retry or manual retry
**Content requirements:**
- Apologetic error message
- Assurance file is not lost
- Retry guidance

### Edge case states

#### Duplicate file name
**When:** User uploads file with name that exists in workspace
**Handling:** Prompt user to rename or replace
**Content requirements:**
- Clear explanation of conflict
- Options (rename, replace, cancel)
- Consequences of each option

#### Upload while offline
**When:** User attempts upload with no connection
**Handling:** Queue for later or show error
**Content requirements:**
- Offline status indication
- Queued confirmation OR connection required message

---

## UI component inventory

### Upload button
**Location:** Workspace toolbar, document list header
**Purpose:** Initiate upload flow
**States:** Default, hover, disabled
**Character limit:** 15 characters
**Current copy:** "Upload"

### Drag-drop zone
**Location:** Upload dialog center
**Purpose:** Provide drag-drop target and instructions
**Content needs:**
- Primary instruction headline
- Supported formats subtext
- Size limit note
**Character limits:** Headline 40, subtext 80

### Progress indicator
**Location:** Upload dialog during upload
**Purpose:** Show upload progress
**Content needs:**
- Status text (uploading, processing)
- Percentage or file size progress
- Cancel option
**Character limit:** Status text 30 characters

### Error message
**Location:** Upload dialog, replacing progress
**Purpose:** Explain error and recovery
**Content needs:**
- Error headline
- Explanation
- Recovery action
**Character limits:** Headline 50, explanation 150, action 25

---

## Business rules affecting content

### Constraints
| Rule | Implication for content |
|------|------------------------|
| 25MB file size limit | Must communicate limit clearly before and during errors |
| PDF, DOCX, PNG, JPG only | Must list supported types; suggest conversion for others |
| Virus scan required | May need processing state messaging |

### Compliance requirements
- Files may contain PII; no file content in error logs
- GDPR: User must be able to delete uploaded files

---

## Terminology

### Feature vocabulary
| Term | Definition | Usage notes |
|------|------------|-------------|
| Upload | Transfer file to workspace | Preferred term |
| Document | Any uploaded file | Use for all file types |
| Workspace | User's file storage area | Not "folder" or "drive" |

### Terms to avoid
| Avoid | Use instead | Why |
|-------|-------------|-----|
| Folder | Workspace | Product terminology |
| Disk space | Storage | More approachable |
| Server | System | Less technical |

---

## Related context
- File management feature context: [link]
- Error message patterns: [link]
- Progress indicator patterns: [link]
```

---

## Example 2: Payment method feature

**Input:**
- Feature: Adding/managing payment methods
- Users: Subscription customers
- Constraints: PCI compliance, multiple card types, international

**Output:**

```md
# Feature Content Context: Payment Methods

## Feature overview

### Purpose
Allows users to add, update, and manage payment methods for their subscription.

### User goals
| Goal | Priority |
|------|----------|
| Add a payment method to start/continue subscription | Primary |
| Update expiring or declined card | Primary |
| Remove old payment methods | Secondary |

### Feature boundaries
- **Included:** Add card, update card, remove card, set default
- **Excluded:** Billing history (separate), invoice management, subscription changes

---

## User context

### Who uses this
Billing administrators and individual users managing their own subscription.

### When they use it
- **Onboarding:** Adding first payment method to start subscription
- **Maintenance:** Card expiring, need to update
- **Recovery:** Card declined, need to fix to restore access

### Emotional state
- **Onboarding:** Ready to commit, may have payment hesitation
- **Expiring card:** Routine, low stress
- **Declined card:** Stressed, may lose access, want fast resolution

---

## Feature states

### Happy path states

#### No payment method (new user)
**When:** User has no payment method on file
**User need:** Understand what's needed and why
**Content requirements:**
- Clear prompt to add payment method
- What payment types accepted
- Security reassurance

#### Payment method on file
**When:** User has active payment method
**User need:** Verify it's correct, manage if needed
**Content requirements:**
- Masked card number display
- Expiration date
- Card type indicator
- Edit/remove options

#### Adding card (form)
**When:** User is entering card details
**User need:** Enter information correctly, feel secure
**Content requirements:**
- Field labels
- Format guidance
- Validation messages
- Security indicators

#### Card added successfully
**When:** Card is validated and saved
**User need:** Confirmation, next steps
**Content requirements:**
- Success message
- What card was added (masked)
- Next action options

### Error states

#### Card declined
**When:** Card fails validation with processor
**Cause:** Various (insufficient funds, expired, blocked)
**Recovery:** Try again or use different card
**Content requirements:**
- Non-specific error (we don't know exact cause)
- Suggestion to check details or try another card
- Contact bank suggestion

#### Invalid card number
**When:** Card number doesn't pass Luhn check
**Cause:** Typo or invalid card
**Recovery:** Re-enter correctly
**Content requirements:**
- Inline validation message
- Request to check and re-enter

#### Expired card
**When:** User enters already-expired card
**Cause:** User error
**Recovery:** Enter valid card
**Content requirements:**
- Clear expiration date error
- Suggest checking card

#### Unsupported card type
**When:** User enters card type we don't accept
**Cause:** User has unsupported card
**Recovery:** Use different card
**Content requirements:**
- List of supported card types
- Apology for limitation

### Edge case states

#### Only payment method (can't delete)
**When:** User tries to delete only payment method while on active subscription
**Handling:** Prevent deletion, explain why
**Content requirements:**
- Explanation that payment method required
- Option to add new card first then delete

#### Card expiring soon
**When:** Card on file expires within 30 days
**Handling:** Proactive warning
**Content requirements:**
- Warning about upcoming expiration
- Easy path to update

---

## UI component inventory

### Card display
**Location:** Payment methods section
**Purpose:** Show saved card info
**Content needs:**
- Card type (Visa, Mastercard)
- Last 4 digits
- Expiration
- Default indicator
**Character limit:** N/A (structured display)

### Add card button
**Location:** Payment methods section
**Purpose:** Open add card flow
**Character limit:** 20 characters
**Current copy:** "Add payment method"

### Card number field
**Label:** "Card number"
**Placeholder:** "1234 5678 9012 3456"
**Validation message:** "Enter a valid card number"
**Character limit:** N/A (structured input)

### Security message
**Location:** Below card form
**Purpose:** Reassure user about security
**Content needs:** Brief security statement
**Character limit:** 100 characters

---

## Business rules affecting content

### Constraints
| Rule | Implication for content |
|------|------------------------|
| PCI compliance | Cannot show full card numbers; must mask |
| Cannot store CVV | Must re-collect for each transaction if needed |
| Supported cards: Visa, MC, Amex | Must list explicitly |

### Compliance requirements
- PCI DSS: Specific masking requirements
- GDPR: Right to delete payment data
- Regional: Some countries have specific disclosure requirements

---

## Terminology

### Feature vocabulary
| Term | Definition | Usage notes |
|------|------------|-------------|
| Payment method | Card or other payment source | Generic term |
| Card | Credit or debit card | When specifically about cards |
| Default | Primary payment method used | For charging |

### Terms to avoid
| Avoid | Use instead | Why |
|-------|-------------|-----|
| Credit card | Card / Payment method | May be debit |
| Billing info | Payment method | More specific |
| CVV | Security code | More accessible |
```

---

## Example 3: Edge case — Feature with AI/automation

**Input:**
- Feature: AI-powered writing suggestions
- Users: Content creators using editor
- Challenge: Must explain AI behavior, limitations, and data usage

**Output:**

```md
# Feature Content Context: Writing Suggestions

## Feature overview

### Purpose
Provides AI-powered writing suggestions to help users improve their content.

### User goals
| Goal | Priority |
|------|----------|
| Get helpful suggestions to improve writing | Primary |
| Understand why suggestions are made | Secondary |
| Control when suggestions appear | Secondary |

### Feature boundaries
- **Included:** Real-time suggestions, accept/dismiss, settings
- **Excluded:** Full AI rewriting, content generation, grammar checking (separate feature)

---

## AI-specific context

### How the AI works (for content purposes)
- Analyzes text as user writes
- Suggests improvements based on clarity, concision, tone
- Does not store content permanently
- Suggestions are optional—user decides

### Transparency requirements
Users must understand:
- When AI is being used
- What data AI can see
- How to disable AI features

---

## Feature states

### Happy path states

#### AI analyzing
**When:** User is writing, AI is processing
**User need:** Know AI is working without distraction
**Content requirements:**
- Subtle indicator (not interruptive)

#### Suggestion available
**When:** AI has a suggestion to offer
**User need:** Decide whether to accept
**Content requirements:**
- Suggestion display
- Accept/dismiss controls
- Brief explanation option

#### Suggestion accepted
**When:** User accepts a suggestion
**User need:** Confirmation change was made
**Content requirements:**
- Subtle confirmation
- Undo option

#### Suggestion dismissed
**When:** User dismisses suggestion
**User need:** Confirmation, know it won't reappear
**Content requirements:**
- Dismissal acknowledged
- Feedback option (wrong suggestion?)

### Error states

#### AI unavailable
**When:** AI service is down or unreachable
**Cause:** Technical (our servers)
**Recovery:** Automatic retry; user can continue without AI
**Content requirements:**
- Non-alarming notice
- Assurance work is not affected
- Auto-enable when available

#### Rate limited
**When:** User has made too many requests
**Cause:** Fair use limits
**Recovery:** Wait or upgrade
**Content requirements:**
- Clear limit message
- When limit resets
- Upgrade option if applicable

### Edge case states

#### Sensitive content detected
**When:** AI detects content it shouldn't process (PII, etc.)
**Handling:** Pauses suggestions for that section
**Content requirements:**
- Explanation that suggestions paused
- Privacy protection framing
- How to continue

---

## UI component inventory

### Suggestion popover
**Location:** Inline with text
**Purpose:** Display suggestion and controls
**Content needs:**
- Suggested text
- Accept button
- Dismiss button
- "Why?" expandable
**Character limits:** Suggested text limited to 200 chars

### Settings toggle
**Location:** Editor settings
**Purpose:** Enable/disable AI suggestions
**Content needs:**
- Toggle label
- Description of what it controls
**Character limits:** Label 30, description 100

### AI indicator
**Location:** Editor toolbar
**Purpose:** Show AI is active
**Content needs:**
- Icon + text indicator
- Tooltip explaining what AI can see
**Character limit:** Tooltip 150

---

## AI-specific messaging guidelines

### Transparency patterns
| Situation | Message pattern |
|-----------|-----------------|
| AI is analyzing | [Subtle indicator, no text] |
| What AI can see | "Suggestions are based on your current document" |
| Data usage | "Your content is not stored or used to train our AI" |
| Disabling AI | "You can turn off suggestions in Settings" |

### Avoid
- Implying AI is "reading" or "understanding" (anthropomorphization)
- Guaranteeing suggestions are always good
- Hiding that AI is involved

---

## Terminology

### Feature vocabulary
| Term | Definition | Usage notes |
|------|------------|-------------|
| Suggestion | AI-generated improvement | Not "recommendation" |
| Accept | Apply the suggestion | Not "use" |
| Dismiss | Ignore the suggestion | Not "reject" (softer) |
| Writing assistant | The AI feature overall | Marketing term |

### Terms to avoid
| Avoid | Use instead | Why |
|-------|-------------|-----|
| AI thinks | AI suggests | Less anthropomorphic |
| The AI | Writing assistant | More approachable |
| Smart | AI-powered | "Smart" is vague |
```
