# Legal and Safety Standards

## Scope

Regulated content, prohibited claims, required disclosures, and safety-critical language for all content outputs.

## Hard Rules

### Prohibited Claims

1. Do not make guarantees about outcomes ("will always," "guaranteed to").
2. Do not make unsubstantiated performance claims ("fastest," "best," "most secure").
3. Do not make health, financial, or legal promises.
4. Do not claim compliance with regulations unless verified (HIPAA, GDPR, SOC 2).
5. Do not imply endorsement by third parties without documentation.

### Required Disclosures

1. Identify AI-generated content when required by product policy or regulation.
2. Disclose data collection at point of collection.
3. Disclose affiliate relationships in marketing content.
4. Disclose beta/experimental status of features.
5. Disclose limitations of automated systems.

### Liability Language

1. Do not use language that waives user rights.
2. Do not disclaim responsibility for system errors in user-facing copy.
3. Do not shift blame to the user for system-caused failures.
4. Use "may" not "will" for predicted outcomes.

### Safety-Critical Content

1. Destructive actions require explicit confirmation language.
2. Irreversible actions must state irreversibility.
3. Data deletion must specify what is deleted and that it cannot be recovered.
4. Security warnings must state the risk and the action to mitigate.
5. Do not use softening language for serious consequences ("just," "simply," "only").

### Regulated Domains

1. Financial content: Do not provide advice. State limitations.
2. Health content: Do not diagnose or prescribe. Direct to professionals.
3. Legal content: Do not provide legal advice. State limitations.
4. Children's content: Comply with COPPA and equivalent regulations.
5. Accessibility claims: Do not claim compliance without audit.

### User Consent

1. Consent requests must state what is being consented to.
2. Consent must be affirmative. No pre-checked boxes.
3. Consent language must match the action scope. No bundled consent.
4. Withdrawal of consent must be as easy as granting it.

## Prohibited Patterns

| Pattern | Issue | Alternative |
|---------|-------|-------------|
| `100% secure` | Unverifiable claim | `We use encryption to protect your data` |
| `Guaranteed results` | Outcome promise | `Designed to help you...` |
| `HIPAA compliant` (unverified) | False compliance claim | Remove or verify |
| `Just delete` | Softened destructive action | `Permanently delete` |
| `We're not responsible if...` | Liability disclaimer in UI | Move to legal terms |
| `By continuing you agree` | Passive consent | Explicit consent action |
| `This will fix the problem` | Outcome guarantee | `This may resolve the issue` |
| `Trust us` | Unsupported assurance | State the specific safeguard |

## Interaction with Skills

1. All outputs inherit these rules.
2. Skills in regulated domains must note applicable regulations in SKILL.md.
3. Skills producing consent flows must reference this file in RUBRIC.md.
4. Skills may not override safety-critical language requirements.