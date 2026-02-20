#!/usr/bin/env python3
"""
Validate a context change record for completeness and schema compliance.

Usage:
    python validate_change_record.py <path-to-change-record.md>

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
# Minimum feedback sources: at least 1 required per repo doctrine
MIN_FEEDBACK_SOURCES = 1
# Minimum changes: at least 1 required for a valid update
MIN_CHANGES = 1
# Semver pattern: standard semantic versioning
SEMVER_PATTERN = r'^\d+\.\d+\.\d+(-[\w.]+)?$'
# ISO date pattern: YYYY-MM-DD
DATE_PATTERN = r'^\d{4}-\d{2}-\d{2}$'

VALID_SOURCE_TYPES = {
    'user-research', 'support-ticket', 'analytics', 
    'pm-input', 'internal-review', 'social-feedback'
}

VALID_AFFECTED_SECTIONS = {
    'vocabulary', 'states', 'actions', 'constraints',
    'error-taxonomy', 'tone-boundaries', 'success-metrics',
    'regulatory', 'other'
}

VALID_FEEDBACK_TYPES = {'gap', 'correction', 'expansion', 'deprecation', 'conflict'}
VALID_CHANGE_TYPES = {'additive', 'modifying', 'removing'}


class ValidationResult(NamedTuple):
    passed: bool
    message: str


def validate_metadata(content: str) -> list[ValidationResult]:
    """Validate required metadata fields."""
    results = []
    
    # Check context pack
    if not re.search(r'\*\*Context pack:\*\*\s*\S+', content):
        results.append(ValidationResult(False, "Missing or empty 'Context pack' field"))
    else:
        results.append(ValidationResult(True, "Context pack field present"))
    
    # Check previous version
    prev_match = re.search(r'\*\*Previous version:\*\*\s*(\S+)', content)
    if not prev_match:
        results.append(ValidationResult(False, "Missing 'Previous version' field"))
    elif not re.match(SEMVER_PATTERN, prev_match.group(1)):
        results.append(ValidationResult(False, f"Previous version '{prev_match.group(1)}' is not valid semver"))
    else:
        results.append(ValidationResult(True, "Previous version is valid semver"))
    
    # Check new version
    new_match = re.search(r'\*\*New version:\*\*\s*(\S+)', content)
    if not new_match:
        results.append(ValidationResult(False, "Missing 'New version' field"))
    elif not re.match(SEMVER_PATTERN, new_match.group(1)):
        results.append(ValidationResult(False, f"New version '{new_match.group(1)}' is not valid semver"))
    else:
        results.append(ValidationResult(True, "New version is valid semver"))
    
    # Check update date
    date_match = re.search(r'\*\*Update date:\*\*\s*(\S+)', content)
    if not date_match:
        results.append(ValidationResult(False, "Missing 'Update date' field"))
    elif not re.match(DATE_PATTERN, date_match.group(1)):
        results.append(ValidationResult(False, f"Update date '{date_match.group(1)}' is not ISO 8601 (YYYY-MM-DD)"))
    else:
        results.append(ValidationResult(True, "Update date is valid ISO 8601"))
    
    # Check update author
    if not re.search(r'\*\*Update author:\*\*\s*\S+', content):
        results.append(ValidationResult(False, "Missing or empty 'Update author' field"))
    else:
        results.append(ValidationResult(True, "Update author field present"))
    
    return results


def validate_feedback_sources(content: str) -> list[ValidationResult]:
    """Validate feedback sources table."""
    results = []
    
    # Find feedback sources table
    table_match = re.search(r'## Feedback sources\s*\n\|[^\n]+\n\|[-|\s]+\n((?:\|[^\n]+\n)+)', content)
    if not table_match:
        results.append(ValidationResult(False, "Missing feedback sources table"))
        return results
    
    rows = table_match.group(1).strip().split('\n')
    if len(rows) < MIN_FEEDBACK_SOURCES:
        results.append(ValidationResult(False, f"Need at least {MIN_FEEDBACK_SOURCES} feedback source(s), found {len(rows)}"))
    else:
        results.append(ValidationResult(True, f"Found {len(rows)} feedback source(s)"))
    
    for i, row in enumerate(rows, 1):
        cells = [c.strip() for c in row.split('|')[1:-1]]
        if len(cells) >= 1:
            source_type = cells[0].lower().replace(' ', '-')
            if source_type not in VALID_SOURCE_TYPES and source_type != '<user-research':
                results.append(ValidationResult(False, f"Row {i}: Invalid source type '{cells[0]}'"))
    
    return results


def validate_changes(content: str) -> list[ValidationResult]:
    """Validate change entries."""
    results = []
    
    # Find all change sections
    changes = re.findall(r'### Change \d+:[^\n]+\n(.*?)(?=### Change|\n## |$)', content, re.DOTALL)
    
    if len(changes) < MIN_CHANGES:
        results.append(ValidationResult(False, f"Need at least {MIN_CHANGES} change(s), found {len(changes)}"))
        return results
    
    results.append(ValidationResult(True, f"Found {len(changes)} change(s)"))
    
    for i, change in enumerate(changes, 1):
        # Check affected section
        section_match = re.search(r'\*\*Affected section:\*\*\s*(\S+)', change)
        if not section_match:
            results.append(ValidationResult(False, f"Change {i}: Missing 'Affected section'"))
        elif section_match.group(1).lower() not in VALID_AFFECTED_SECTIONS:
            results.append(ValidationResult(False, f"Change {i}: Invalid affected section '{section_match.group(1)}'"))
        
        # Check feedback type
        fb_match = re.search(r'\*\*Feedback type:\*\*\s*(\S+)', change)
        if not fb_match:
            results.append(ValidationResult(False, f"Change {i}: Missing 'Feedback type'"))
        elif fb_match.group(1).lower() not in VALID_FEEDBACK_TYPES:
            results.append(ValidationResult(False, f"Change {i}: Invalid feedback type '{fb_match.group(1)}'"))
        
        # Check change type
        ct_match = re.search(r'\*\*Change type:\*\*\s*(\S+)', change)
        if not ct_match:
            results.append(ValidationResult(False, f"Change {i}: Missing 'Change type'"))
        elif ct_match.group(1).lower() not in VALID_CHANGE_TYPES:
            results.append(ValidationResult(False, f"Change {i}: Invalid change type '{ct_match.group(1)}'"))
        
        # Check before/after
        if '**Before:**' not in change:
            results.append(ValidationResult(False, f"Change {i}: Missing 'Before' content"))
        if '**After:**' not in change:
            results.append(ValidationResult(False, f"Change {i}: Missing 'After' content"))
        
        # Check rationale
        if '**Rationale:**' not in change:
            results.append(ValidationResult(False, f"Change {i}: Missing 'Rationale'"))
        else:
            rationale_match = re.search(r'\*\*Rationale:\*\*\s*(.+?)(?=\*\*|$)', change, re.DOTALL)
            if rationale_match:
                rationale = rationale_match.group(1).strip()
                if len(rationale) < 20:  # Minimum 20 chars for meaningful rationale
                    results.append(ValidationResult(False, f"Change {i}: Rationale too short (min 20 chars)"))
                if 'per feedback' in rationale.lower() and len(rationale) < 50:
                    results.append(ValidationResult(False, f"Change {i}: Rationale uses 'per feedback' without specifics"))
    
    return results


def validate_changelog(content: str) -> list[ValidationResult]:
    """Validate changelog entry exists and uses imperative mood."""
    results = []
    
    changelog_match = re.search(r'## Changelog entry\s*\n-\s*(.+)', content)
    if not changelog_match:
        results.append(ValidationResult(False, "Missing changelog entry"))
        return results
    
    entry = changelog_match.group(1)
    
    # Check for past tense indicators (simple heuristic)
    past_tense_words = ['updated', 'changed', 'added', 'removed', 'fixed', 'was', 'were']
    words = entry.lower().split()
    for word in past_tense_words:
        if word in words[:3]:  # Check first 3 words
            results.append(ValidationResult(False, f"Changelog may use past tense ('{word}'). Use imperative mood."))
            break
    else:
        results.append(ValidationResult(True, "Changelog entry present"))
    
    return results


def main():
    if len(sys.argv) != 2:
        print("Usage: python validate_change_record.py <path-to-change-record.md>")
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
    all_results.extend(validate_feedback_sources(content))
    all_results.extend(validate_changes(content))
    all_results.extend(validate_changelog(content))
    
    # Print results
    print(f"\nValidation Results for: {file_path.name}\n")
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
