# Rubric

## Pass criteria
All must be true:

### Docstring requirements
- [ ] First line is a complete sentence summarizing purpose (not "This function...")
- [ ] All parameters documented with type and description
- [ ] Return value documented (or explicitly noted as None)
- [ ] Exceptions documented if function can raise
- [ ] Example included for public APIs
- [ ] Side effects documented if any

### Inline comment requirements
- [ ] Comments explain why, not what
- [ ] Comments placed before the code they explain
- [ ] Complex algorithms have explanatory comments
- [ ] Magic numbers have named constants or comments
- [ ] Non-obvious decisions have justification comments

### Annotation requirements
- [ ] TODOs include what needs to be done, not just "fix this"
- [ ] TODOs include owner or ticket reference for tracking
- [ ] FIXMEs describe the bug and its impact
- [ ] HACKs explain why the proper solution wasn't used

### Language convention requirements
- [ ] Follows language-specific documentation style (Google, NumPy, JSDoc, etc.)
- [ ] Uses correct syntax for documentation generator
- [ ] Consistent formatting across codebase
- [ ] Proper types/signatures in doc strings

### Quality requirements
- [ ] No redundant comments restating code
- [ ] No outdated comments (comments match current code)
- [ ] No commented-out code without explanation
- [ ] Grammar and spelling are correct

## Fail criteria
Fail if any are true:

- Docstring first line starts with "This function..." or "This class..."
- Docstring restates the function signature without adding value
- Parameter documented without type information
- Comment says what code does literally (e.g., `// increment i` before `i++`)
- TODO has no actionable description
- Comment is longer than the code it explains (for simple code)
- Docstring example is incorrect or non-functional
- Public API lacks documentation
- Exception is raised but not documented
- Outdated comment contradicts current code behavior
- Documentation uses abbreviations or jargon without explanation
