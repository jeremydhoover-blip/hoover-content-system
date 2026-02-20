# Rubric

## Pass criteria
All must be true:

### Structure requirements
- [ ] One-line description is ≤80 characters and starts with a verb
- [ ] Usage string accurately reflects required vs. optional arguments
- [ ] Every argument has a description with type or constraints
- [ ] Every flag has both short (-x) and long (--extended) form, or justifies why not
- [ ] Examples section includes at least 2 realistic examples
- [ ] Each example has a one-line explanation of what it does

### Consistency requirements
- [ ] Argument names use UPPER_CASE in usage, lower-case in prose
- [ ] Flag names use kebab-case (--output-format, not --outputFormat)
- [ ] Consistent terminology (same term for same concept across all commands)
- [ ] Default values documented for all optional arguments and flags

### Completeness requirements
- [ ] Boolean flags document both the positive and negative form if applicable
- [ ] Environment variable overrides documented if they exist
- [ ] Related commands referenced in SEE ALSO section
- [ ] Mutually exclusive options clearly indicated

### Behavioral requirements
- [ ] Descriptions explain what the option does, not just what it is
- [ ] Constraints are explicit (file must exist, value range, enum options)
- [ ] Destructive operations are labeled

## Fail criteria
Fail if any are true:

- One-line description exceeds 80 characters
- One-line description doesn't start with a verb
- Usage string shows required argument as optional or vice versa
- Argument or flag has no description
- Flag uses camelCase or snake_case instead of kebab-case
- Example doesn't work with the documented syntax
- Example has no explanation
- Mutually exclusive options not indicated in usage string
- Default value missing for optional argument
- Technical jargon used without explanation in user-facing help
- Help text includes version numbers that will become outdated
