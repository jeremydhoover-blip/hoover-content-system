# Forbidden Phrases

Terms, patterns, and phrases to avoid in error messages.

---

## Technical jargon

| Forbidden | Why | Use instead |
|-----------|-----|-------------|
| Exception | Technical term | "Something went wrong" |
| Null, undefined, NaN | Programming literals | Omit or describe actual problem |
| Stack trace | Internal debugging info | Omit entirely |
| Error code (alone) | Meaningless to users | Add human explanation |
| Timeout exception | Technical | "Taking too long" or "Request timed out" |
| 500, 404, 403 (alone) | HTTP codes mean nothing | Describe the problem |
| Parse error | Technical | "Couldn't read the data" |
| Malformed | Technical | "Invalid format" or specific guidance |
| Deprecated | Technical | "No longer available" or "Use [X] instead" |
| Runtime error | Technical | "Something went wrong" |
| Fatal error | Alarming and vague | Describe actual impact |

---

## Blame language

| Forbidden | Why | Use instead |
|-----------|-----|-------------|
| "You failed to..." | Blames user | "Please [action]" or "[Action] required" |
| "You forgot to..." | Blames user | "Enter [field]" |
| "You entered invalid..." | Blames user | "Enter a valid [field]" |
| "Your mistake" | Blames user | Omit — focus on fix |
| "User error" | Blames user | Describe how to fix |
| "You should have..." | Condescending | "Try [action]" |

---

## Alarming language

| Forbidden | Why | Use instead |
|-----------|-----|-------------|
| "FATAL" | Creates panic | Describe actual impact |
| "CRITICAL" | Alarming | State what happened calmly |
| "DANGER" | Alarming | "Warning" if truly needed |
| "!!!" | Unprofessional, alarming | One or zero exclamation points |
| "URGENT" | Creates anxiety | State timeline if relevant |
| "Immediately" | Often untrue, creates pressure | Be specific about timing |

---

## Vague phrases

| Forbidden | Why | Use instead |
|-----------|-----|-------------|
| "An error occurred" | Says nothing useful | State what error |
| "Something went wrong" (alone) | No guidance | Add what user can do |
| "Invalid input" | Doesn't say what's invalid | Specify which input and why |
| "Bad request" | Technical and vague | State what was wrong |
| "Unknown error" | Unhelpful | "Something went wrong. Please try again." |
| "Error" (alone) | Meaningless | Describe the error |
| "Failed" (alone) | No context | "[Action] failed" with reason |
| "Please try again later" (alone) | No context | Add what happened |

---

## Outdated/inappropriate tone

| Forbidden | Why | Use instead |
|-----------|-----|-------------|
| "Oops!" | Trivializes user's problem | Omit |
| "Whoops!" | Trivializes user's problem | Omit |
| "Uh oh!" | Trivializes user's problem | Omit |
| "Bummer" | Too casual | Omit |
| "Our bad" | Too casual | "We're working on it" (if true) |
| "Yikes" | Too casual | Omit |
| "LOL" / "lol" | Inappropriate | Never |

---

## Overpromising

| Forbidden | Why | Use instead |
|-----------|-----|-------------|
| "This will never happen again" | Can't guarantee | Omit |
| "We're fixing this right now" | May not be true | "We're looking into this" |
| "This will be resolved shortly" | Vague, may disappoint | Give realistic timeline or omit |
| "100% uptime" | Impossible promise | Omit |

---

## Regex patterns for linting

```python
FORBIDDEN_PATTERNS = [
    # Technical jargon
    (r'\bexception\b', 'Avoid technical term "exception"'),
    (r'\bnull\b', 'Avoid programming literal "null"'),
    (r'\bundefined\b', 'Avoid programming literal "undefined"'),
    (r'\bNaN\b', 'Avoid programming literal "NaN"'),
    (r'\bstack\s*trace\b', 'Never expose stack traces'),
    (r'\b[45]\d{2}\b', 'Avoid raw HTTP status codes'),
    
    # Blame language
    (r'\byou failed\b', 'Avoid blame language'),
    (r'\byou forgot\b', 'Avoid blame language'),
    (r'\byour mistake\b', 'Avoid blame language'),
    (r'\buser error\b', 'Avoid blame language'),
    
    # Alarming
    (r'\bFATAL\b', 'Avoid alarming language'),
    (r'\bCRITICAL\b', 'Avoid alarming language'),
    (r'!!!', 'Avoid multiple exclamation points'),
    
    # Vague
    (r'^Error$', 'Too vague — describe the error'),
    (r'^Failed$', 'Too vague — describe what failed'),
    
    # Inappropriate tone
    (r'\b[Oo]ops\b', 'Avoid trivializing language'),
    (r'\b[Ww]hoops\b', 'Avoid trivializing language'),
    (r'\b[Uu]h oh\b', 'Avoid trivializing language'),
]
```
