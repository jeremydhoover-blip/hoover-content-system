#!/usr/bin/env python3
"""
Validates feature content context packs against schema requirements.

Checks:
- Required sections present
- State coverage (happy path, errors, edge cases)
- Terminology section completeness
- Component character limits defined
- User need documented for all states

Usage:
    python validate_context_pack.py <path_to_context_pack.md>

Exit codes:
    0 - All checks passed
    1 - Validation errors found
"""

import sys
import re
from pathlib import Path
from dataclasses import dataclass

# --- Constants ---
REQUIRED_SECTIONS = [
    "feature overview",
    "user context",
    "feature states",
    "ui component inventory",
    "terminology",
]

REQUIRED_STATE_CATEGORIES = [
    "happy path",
    "error states",
]

MIN_HAPPY_PATH_STATES = 2  # At minimum: empty and success
MIN_ERROR_STATES = 1  # At least one error must be documented
MIN_VOCABULARY_TERMS = 1  # At least one term defined
MIN_AVOID_TERMS = 1  # At least one term to avoid


@dataclass
class ValidationResult:
    passed: bool
    errors: list
    warnings: list


def load_document(filepath: str) -> str:
    """Load markdown document from file."""
    path = Path(filepath)
    if not path.exists():
        print(f"ERROR: File not found: {filepath}")
        sys.exit(1)
    return path.read_text(encoding="utf-8")


def check_required_sections(content: str) -> list[str]:
    """Check that all required sections are present."""
    errors = []
    content_lower = content.lower()
    
    for section in REQUIRED_SECTIONS:
        # Check for ## header with section name
        pattern = rf"##\s*{re.escape(section)}"
        if not re.search(pattern, content_lower):
            errors.append(f"Missing required section: '{section}'")
    
    return errors


def check_state_coverage(content: str) -> tuple[list[str], list[str]]:
    """Validate state documentation coverage."""
    errors = []
    warnings = []
    content_lower = content.lower()
    
    # Check for state categories
    for category in REQUIRED_STATE_CATEGORIES:
        if category not in content_lower:
            errors.append(f"Missing state category: '{category}'")
    
    # Count states in happy path section
    happy_path_match = re.search(
        r"###\s*happy\s*path\s*states?(.*?)(?=###\s*error|###\s*edge|\Z)",
        content_lower,
        re.DOTALL
    )
    if happy_path_match:
        state_count = len(re.findall(r"####\s+", happy_path_match.group(1)))
        if state_count < MIN_HAPPY_PATH_STATES:
            errors.append(
                f"Insufficient happy path states: {state_count} "
                f"(minimum: {MIN_HAPPY_PATH_STATES})"
            )
    
    # Count error states
    error_match = re.search(
        r"###\s*error\s*states?(.*?)(?=###\s*edge|##\s*ui|\Z)",
        content_lower,
        re.DOTALL
    )
    if error_match:
        error_count = len(re.findall(r"####\s+", error_match.group(1)))
        if error_count < MIN_ERROR_STATES:
            errors.append(
                f"Insufficient error states: {error_count} "
                f"(minimum: {MIN_ERROR_STATES})"
            )
    
    # Check for edge cases (warning, not error)
    if "edge case" not in content_lower:
        warnings.append("No edge cases documented (recommended but not required)")
    
    return errors, warnings


def check_user_needs(content: str) -> list[str]:
    """Verify each state documents user need."""
    errors = []
    
    # Find all state blocks (#### headers in states section)
    states_section = re.search(
        r"##\s*feature\s*states(.*?)(?=##\s*ui\s*component|\Z)",
        content,
        re.IGNORECASE | re.DOTALL
    )
    
    if states_section:
        section_content = states_section.group(1)
        state_blocks = re.findall(
            r"####\s+([^\n]+)(.*?)(?=####|\Z)",
            section_content,
            re.DOTALL
        )
        
        for state_name, state_content in state_blocks:
            if "user need" not in state_content.lower():
                errors.append(
                    f"State '{state_name.strip()}' missing 'User need' field"
                )
    
    return errors


def check_terminology(content: str) -> list[str]:
    """Validate terminology section completeness."""
    errors = []
    content_lower = content.lower()
    
    # Check for vocabulary table
    vocab_match = re.search(
        r"###\s*feature\s*vocabulary(.*?)(?=###|\Z)",
        content_lower,
        re.DOTALL
    )
    if vocab_match:
        # Count table rows (| at start of line, excluding headers)
        rows = re.findall(r"^\|[^-|]", vocab_match.group(1), re.MULTILINE)
        if len(rows) - 1 < MIN_VOCABULARY_TERMS:  # -1 for header
            errors.append(
                f"Insufficient vocabulary terms: need at least {MIN_VOCABULARY_TERMS}"
            )
    else:
        errors.append("Missing 'Feature vocabulary' subsection")
    
    # Check for terms to avoid
    avoid_match = re.search(
        r"###\s*terms\s*to\s*avoid(.*?)(?=##|\Z)",
        content_lower,
        re.DOTALL
    )
    if avoid_match:
        rows = re.findall(r"^\|[^-|]", avoid_match.group(1), re.MULTILINE)
        if len(rows) - 1 < MIN_AVOID_TERMS:
            errors.append(
                f"Insufficient 'terms to avoid': need at least {MIN_AVOID_TERMS}"
            )
    else:
        errors.append("Missing 'Terms to avoid' subsection")
    
    return errors


def check_components(content: str) -> list[str]:
    """Validate component inventory has character limits."""
    errors = []
    
    # Find components section
    components_section = re.search(
        r"##\s*ui\s*component\s*inventory(.*?)(?=##\s*business|\Z)",
        content,
        re.IGNORECASE | re.DOTALL
    )
    
    if components_section:
        section_content = components_section.group(1)
        component_blocks = re.findall(
            r"###\s+([^\n]+)(.*?)(?=###|\Z)",
            section_content,
            re.DOTALL
        )
        
        for component_name, component_content in component_blocks:
            if "character limit" not in component_content.lower():
                errors.append(
                    f"Component '{component_name.strip()}' missing character limit"
                )
    
    return errors


def validate(filepath: str) -> ValidationResult:
    """Run all validation checks."""
    content = load_document(filepath)
    
    all_errors = []
    all_warnings = []
    
    # Run checks
    all_errors.extend(check_required_sections(content))
    
    state_errors, state_warnings = check_state_coverage(content)
    all_errors.extend(state_errors)
    all_warnings.extend(state_warnings)
    
    all_errors.extend(check_user_needs(content))
    all_errors.extend(check_terminology(content))
    all_errors.extend(check_components(content))
    
    return ValidationResult(
        passed=len(all_errors) == 0,
        errors=all_errors,
        warnings=all_warnings
    )


def main():
    """Run validation and report results."""
    if len(sys.argv) != 2:
        print("Usage: python validate_context_pack.py <path_to_context_pack.md>")
        sys.exit(1)
    
    result = validate(sys.argv[1])
    
    if result.warnings:
        print(f"WARNINGS: {len(result.warnings)}")
        for warning in result.warnings:
            print(f"  ⚠ {warning}")
        print()
    
    if result.passed:
        print("✓ PASS: Context pack is valid")
        sys.exit(0)
    else:
        print(f"✗ FAIL: {len(result.errors)} error(s) found\n")
        for error in result.errors:
            print(f"  ✗ {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
