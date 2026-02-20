# Rubric

## Pass criteria
All must be true:

### Message structure requirements
- [ ] Error message starts with command name followed by `: error:`
- [ ] Message states what happened (not just error code)
- [ ] Message includes why it happened or what was expected
- [ ] Message includes actionable fix or next step for recoverable errors
- [ ] Error goes to stderr, not stdout

### Content requirements
- [ ] Includes relevant context values (file path, provided value, constraint)
- [ ] Does not expose sensitive data (passwords, tokens, internal paths)
- [ ] Uses consistent terminology with help text
- [ ] Avoids technical jargon unexplained to target audience

### Exit code requirements
- [ ] Exit code 0 reserved exclusively for success
- [ ] Exit codes are consistent across similar error types
- [ ] Exit codes documented in --help or man page
- [ ] Different error categories use different exit codes

### Recoverability requirements
- [ ] Recoverable errors include specific fix instructions
- [ ] Non-recoverable errors suggest reporting mechanism or workaround
- [ ] Rate limit errors include retry timing
- [ ] Network errors suggest connectivity checks

### Script compatibility requirements
- [ ] Error format is consistent and parseable
- [ ] JSON output mode produces valid JSON with error details
- [ ] Exit codes are meaningful for conditional scripting

## Fail criteria
Fail if any are true:

- Error message is a bare exception or stack trace without context
- Error says "an error occurred" without specifying what
- Recoverable error has no suggested fix
- Exit code 0 used for any error condition
- Different error types use the same exit code
- Error leaks sensitive information (credentials, internal IPs)
- Error includes implementation details irrelevant to user
- Error blames the user ("you did X wrong") instead of stating the issue
- Error message is entirely uppercase
- Error spans more than 10 lines without verbose flag
