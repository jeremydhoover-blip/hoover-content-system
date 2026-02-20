# Rubric

Pass if all are true:
- Total context budget is explicitly stated with breakdown by category
- Each context source has defined: content, limit, trigger, and format
- Context ordering is specified with rationale for position
- Retrieval rules include trigger condition and selection criteria
- Compression strategy addresses over-budget scenarios
- Freshness requirements are specified for time-sensitive sources
- Fallback behavior is defined for unavailable or empty sources
- Static vs. dynamic context is clearly distinguished
- Token limits sum to less than or equal to total budget
- Attribution or source markers are included in context format

Fail if any are true:
- Token budget is undefined or allocations exceed total
- Context sources lack selection criteria or limits
- No compression or truncation strategy for over-budget scenarios
- Real-time or time-sensitive sources lack freshness rules
- Missing fallback for critical context sources
- Context ordering is arbitrary without rationale
- No distinction between context types
- Retrieval triggers are vague or missing
