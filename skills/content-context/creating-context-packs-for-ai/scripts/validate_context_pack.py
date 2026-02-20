#!/usr/bin/env python3
"""
Validate an AI context pack for completeness and schema compliance.

Usage:
    python validate_context_pack.py <path-to-context-pack.md>

Exit codes:
    0 - All validations passed
    1 - Validation errors found
    2 - File not found or unreadable
"""

import sys
import re
from pathlib import Path
from typing import NamedTuple

# --- Constants (justified) ---
# Minimum examples required per completeness checklist
MIN_EXAMPLES = 3
# Minimum vocabulary terms for meaningful context
MIN_VOCAB_TERMS = 2
# Minimum states for stateful content
MIN_STATES = 2
# Maximum token budget (reasonable limit for most AI systems)
MAX_TOKEN_BUDGET = 10000
# Minimum edge cases to document
MIN_EDGE_CASES = 2


class ValidationResult(NamedTuple):
    passed: bool
    message: str


def validate_metadata(content: str) -> list[ValidationResult]:
    """Validate required metadata fields."""
    results = []
    
    if '## Metadata' not in content:
        results.append(ValidationResult(False, "Missing '## Metadata' section"))
        return results
    
    required_fields = [
        ('Feature:', 'feature name'),
        ('Version:', 'version'),
        ('Last updated:', 'last updated date'),
        ('Target AI system:', 'target AI system'),
        ('Token budget:', 'token budget')
    ]
    
    for field, description in required_fields:
        if f'**{field}**' not in content:
            results.append(ValidationResult(False, f"Missing metadata: {description}"))
        else:
            results.append(ValidationResult(True, f"Metadata present: {description}"))
    
    # Validate token budget is reasonable
    budget_match = re.search(r'\*\*Token budget:\*\*\s*~?(\d+)', content)
    if budget_match:
        budget = int(budget_match.group(1))
        if budget > MAX_TOKEN_BUDGET:
            results.append(ValidationResult(False, f"Token budget ({budget}) exceeds maximum ({MAX_TOKEN_BUDGET})"))
    
    return results


def validate_feature_overview(content: str) -> list[ValidationResult]:
    """Validate feature overview section."""
    results = []
    
    if '## Feature overview' not in content:
        results.append(ValidationResult(False, "Missing '## Feature overview' section"))
        return results
    
    # Extract overview content
    overview_match = re.search(r'## Feature overview\s*\n(.*?)(?=\n## |$)', content, re.DOTALL)
    if overview_match:
        overview_text = overview_match.group(1).strip()
        # Check for minimum content (at least 50 characters of meaningful content)
        if len(overview_text) < 50:
            results.append(ValidationResult(False, "Feature overview too brief (min 50 chars)"))
        else:
            results.append(ValidationResult(True, "Feature overview present and substantive"))
    
    return results


def validate_content_scope(content: str) -> list[ValidationResult]:
    """Validate content scope section."""
    results = []
    
    if '## Content generation scope' not in content and '## Scope' not in content:
        results.append(ValidationResult(False, "Missing content scope section"))
        return results
    
    # Check for generates list
    if not re.search(r'(enables AI to generate|Generate:)', content):
        results.append(ValidationResult(False, "Missing list of what AI should generate"))
    else:
        results.append(ValidationResult(True, "Content generation scope defined"))
    
    # Check for exclusions
    if not re.search(r'(does NOT cover|NOT cover|excludes?:)', content, re.IGNORECASE):
        results.append(ValidationResult(False, "Missing list of what AI should NOT generate"))
    else:
        results.append(ValidationResult(True, "Content exclusions defined"))
    
    return results


def validate_vocabulary(content: str) -> list[ValidationResult]:
    """Validate vocabulary section."""
    results = []
    
    if '## Vocabulary' not in content and '## Terms' not in content:
        results.append(ValidationResult(False, "Missing vocabulary section"))
        return results
    
    results.append(ValidationResult(True, "Vocabulary section present"))
    
    # Count vocabulary terms in tables
    term_rows = re.findall(r'\|\s*(\w+[^|]*)\s*\|\s*(\w+[^|]*)\s*\|\s*(\w+[^|]*)\s*\|', content)
    # Filter out header rows
    term_count = len([r for r in term_rows if 'Use this' not in r[1] and 'Never' not in r[1] and 'Term' not in r[0]])
    
    if term_count < MIN_VOCAB_TERMS:
        results.append(ValidationResult(False, f"Need at least {MIN_VOCAB_TERMS} vocabulary terms, found ~{term_count}"))
    else:
        results.append(ValidationResult(True, f"Found {term_count} vocabulary terms"))
    
    # Check for prohibited alternatives
    if not re.search(r'(Never use|Prohibited|Never:)', content, re.IGNORECASE):
        results.append(ValidationResult(False, "Missing prohibited alternatives in vocabulary"))
    else:
        results.append(ValidationResult(True, "Prohibited alternatives defined"))
    
    return results


def validate_states(content: str) -> list[ValidationResult]:
    """Validate states section."""
    results = []
    
    if '## States' not in content:
        results.append(ValidationResult(False, "Missing '## States' section"))
        return results
    
    results.append(ValidationResult(True, "States section present"))
    
    # Count state entries in table
    states_section = re.search(r'## States\s*\n.*?\|[^\n]+\n\|[-|\s]+\n((?:\|[^\n]+\n)+)', content, re.DOTALL)
    if states_section:
        state_rows = states_section.group(1).strip().split('\n')
        if len(state_rows) < MIN_STATES:
            results.append(ValidationResult(False, f"Need at least {MIN_STATES} states, found {len(state_rows)}"))
        else:
            results.append(ValidationResult(True, f"Found {len(state_rows)} states"))
    
    return results


def validate_constraints(content: str) -> list[ValidationResult]:
    """Validate constraints section."""
    results = []
    
    if '## Constraints' not in content:
        results.append(ValidationResult(False, "Missing '## Constraints' section"))
        return results
    
    results.append(ValidationResult(True, "Constraints section present"))
    
    # Check for hard constraints
    if not re.search(r'(Hard constraints|Hard:)', content, re.IGNORECASE):
        results.append(ValidationResult(False, "Missing hard constraints"))
    else:
        results.append(ValidationResult(True, "Hard constraints defined"))
    
    # Check for character limits
    if not re.search(r'(Character limits|chars|Limit)', content, re.IGNORECASE):
        results.append(ValidationResult(False, "Missing character limits"))
    else:
        results.append(ValidationResult(True, "Character limits defined"))
    
    # Check for prohibited content
    if not re.search(r'(Prohibited|Never:)', content, re.IGNORECASE):
        results.append(ValidationResult(False, "Missing prohibited content patterns"))
    else:
        results.append(ValidationResult(True, "Prohibited patterns defined"))
    
    return results


def validate_tone(content: str) -> list[ValidationResult]:
    """Validate tone section."""
    results = []
    
    if '## Tone' not in content:
        results.append(ValidationResult(False, "Missing '## Tone' section"))
        return results
    
    results.append(ValidationResult(True, "Tone section present"))
    
    # Check for tone boundaries
    if not re.search(r'(Never sound|never sound|Never:.*sound)', content, re.IGNORECASE):
        results.append(ValidationResult(False, "Missing 'never sound like' tone boundaries"))
    else:
        results.append(ValidationResult(True, "Tone boundaries defined"))
    
    return results


def validate_examples(content: str) -> list[ValidationResult]:
    """Validate examples section."""
    results = []
    
    if '## Examples' not in content:
        results.append(ValidationResult(False, "Missing '## Examples' section"))
        return results
    
    results.append(ValidationResult(True, "Examples section present"))
    
    # Count examples
    example_count = len(re.findall(r'### Example \d+', content))
    if example_count < MIN_EXAMPLES:
        results.append(ValidationResult(False, f"Need at least {MIN_EXAMPLES} examples, found {example_count}"))
    else:
        results.append(ValidationResult(True, f"Found {example_count} examples"))
    
    # Check for good/bad pairs
    good_count = len(re.findall(r'(✓.*Good|Good:)', content))
    bad_count = len(re.findall(r'(✗.*Bad|Bad:)', content))
    
    if good_count < MIN_EXAMPLES:
        results.append(ValidationResult(False, "Missing 'good' examples"))
    else:
        results.append(ValidationResult(True, "Good examples present"))
    
    if bad_count < MIN_EXAMPLES:
        results.append(ValidationResult(False, "Missing 'bad' examples"))
    else:
        results.append(ValidationResult(True, "Bad examples present"))
    
    # Check for explanations
    if not re.search(r'(Why it works|Why it fails|explanation)', content, re.IGNORECASE):
        results.append(ValidationResult(False, "Examples missing explanations (why good/bad)"))
    else:
        results.append(ValidationResult(True, "Example explanations present"))
    
    return results


def validate_edge_cases(content: str) -> list[ValidationResult]:
    """Validate edge cases section."""
    results = []
    
    if '## Edge cases' not in content:
        results.append(ValidationResult(False, "Missing '## Edge cases' section"))
        return results
    
    # Count edge case rows
    edge_section = re.search(r'## Edge cases\s*\n\|[^\n]+\n\|[-|\s]+\n((?:\|[^\n]+\n)*)', content)
    if edge_section:
        rows = [r for r in edge_section.group(1).strip().split('\n') if r.strip()]
        if len(rows) < MIN_EDGE_CASES:
            results.append(ValidationResult(False, f"Need at least {MIN_EDGE_CASES} edge cases, found {len(rows)}"))
        else:
            results.append(ValidationResult(True, f"Found {len(rows)} edge cases"))
    else:
        results.append(ValidationResult(False, "Edge cases table not found"))
    
    return results


def main():
    if len(sys.argv) != 2:
        print("Usage: python validate_context_pack.py <path-to-context-pack.md>")
        sys.exit(2)
    
    file_path = Path(sys.argv[1])
    
    if not file_path.exists():
        print(f"Error: File not found: {file_path}")
        sys.exit(2)
    
    try:
        content = file_path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(2)
    
    all_results = []
    all_results.extend(validate_metadata(content))
    all_results.extend(validate_feature_overview(content))
    all_results.extend(validate_content_scope(content))
    all_results.extend(validate_vocabulary(content))
    all_results.extend(validate_states(content))
    all_results.extend(validate_constraints(content))
    all_results.extend(validate_tone(content))
    all_results.extend(validate_examples(content))
    all_results.extend(validate_edge_cases(content))
    
    # Print results
    print(f"\nContext Pack Validation: {file_path.name}\n")
    print("-" * 60)
    
    passed = 0
    failed = 0
    
    for result in all_results:
        status = "✓" if result.passed else "✗"
        print(f"{status} {result.message}")
        if result.passed:
            passed += 1
        else:
            failed += 1
    
    print("-" * 60)
    print(f"Passed: {passed} | Failed: {failed}")
    
    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
