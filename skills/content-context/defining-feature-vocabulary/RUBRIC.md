# Rubric

## Pass criteria
Pass if all are true:

- [ ] All core feature concepts have a defined canonical term
- [ ] Each term has a precise definition scoped to the feature context
- [ ] Each term lists prohibited alternatives (synonyms not to use)
- [ ] No term is used for multiple different concepts (no overloading)
- [ ] No concept has multiple canonical terms (no synonyms in the vocabulary)
- [ ] Usage context is specified for each term (where it appears)
- [ ] Terms are checked against platform conventions (OS, framework, ecosystem)
- [ ] Terms are checked against adjacent feature vocabularies
- [ ] User-facing terms align with validated user mental models (research-backed)
- [ ] Non-obvious naming decisions include rationale
- [ ] Vocabulary includes relationship diagram if >5 interconnected terms
- [ ] Conflicts from different sources are logged with resolution

## Fail criteria
Fail if any are true:

- Any core concept lacks a defined term
- Definition is circular or uses the term to define itself
- Prohibited alternatives are missing
- Same term used for different concepts within the feature
- Different terms used for same concept within the feature
- Term conflicts with established platform conventions without documented rationale
- Term conflicts with adjacent feature vocabulary without resolution
- User-facing term contradicts documented user mental models
- No usage context specified (term is defined but usage location unclear)
- Vocabulary exists only as a list without definitions
- Engineering-internal terms appear in user-facing vocabulary without translation
