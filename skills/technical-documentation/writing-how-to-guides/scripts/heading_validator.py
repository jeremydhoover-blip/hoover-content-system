#!/usr/bin/env python3
"""
Validate heading structure in how-to guide markdown files.

Checks:
- Single H1 title
- Title follows "How to [verb] [object]" pattern
- No skipped heading levels
- Required sections present
- Heading depth does not exceed H4

Usage:
    python heading_validator.py <path-to-markdown-file>

Exit codes:
    0 — All checks pass
    1 — Validation errors found
    2 — File not found or unreadable
"""

import sys
import re
from pathlib import Path

# Constants
MAX_HEADING_DEPTH = 4
REQUIRED_SECTIONS = ["Prerequisites", "Steps", "Verify"]
HOW_TO_PATTERN = r"^How to [a-z]+"


def extract_headings(content: str) -> list[tuple[int, str, int]]:
    """
    Extract all markdown headings with their level and line number.
    
    Returns:
        List of tuples: (level, text, line_number)
    """
    headings = []
    for line_num, line in enumerate(content.splitlines(), start=1):
        match = re.match(r"^(#{1,6})\s+(.+)$", line)
        if match:
            level = len(match.group(1))
            text = match.group(2).strip()
            headings.append((level, text, line_num))
    return headings


def validate_single_h1(headings: list[tuple[int, str, int]]) -> list[str]:
    """Check that exactly one H1 exists."""
    errors = []
    h1_headings = [(text, line) for level, text, line in headings if level == 1]
    
    if len(h1_headings) == 0:
        errors.append("Missing H1 title")
    elif len(h1_headings) > 1:
        locations = ", ".join(f"line {line}" for _, line in h1_headings)
        errors.append(f"Multiple H1 headings found at: {locations}")
    
    return errors


def validate_how_to_title(headings: list[tuple[int, str, int]]) -> list[str]:
    """Check that H1 follows 'How to [verb]' pattern."""
    errors = []
    h1_headings = [(text, line) for level, text, line in headings if level == 1]
    
    if h1_headings:
        title, line = h1_headings[0]
        if not re.match(HOW_TO_PATTERN, title, re.IGNORECASE):
            errors.append(
                f"Line {line}: Title '{title}' does not match 'How to [verb] [object]' pattern"
            )
    
    return errors


def validate_heading_hierarchy(headings: list[tuple[int, str, int]]) -> list[str]:
    """Check for skipped heading levels."""
    errors = []
    prev_level = 0
    
    for level, text, line in headings:
        if level > prev_level + 1 and prev_level > 0:
            errors.append(
                f"Line {line}: Skipped heading level (H{prev_level} to H{level}) at '{text}'"
            )
        if level > MAX_HEADING_DEPTH:
            errors.append(
                f"Line {line}: Heading depth H{level} exceeds maximum H{MAX_HEADING_DEPTH}"
            )
        prev_level = level
    
    return errors


def validate_required_sections(headings: list[tuple[int, str, int]]) -> list[str]:
    """Check that required H2 sections exist."""
    errors = []
    h2_texts = {text for level, text, _ in headings if level == 2}
    
    for section in REQUIRED_SECTIONS:
        # Check for section name at start (e.g., "Verify your setup" matches "Verify")
        found = any(h2.startswith(section) for h2 in h2_texts)
        if not found:
            errors.append(f"Missing required section: '{section}'")
    
    return errors


def validate_file(filepath: Path) -> tuple[bool, list[str]]:
    """
    Run all validations on a file.
    
    Returns:
        Tuple of (passed, errors)
    """
    try:
        content = filepath.read_text(encoding="utf-8")
    except FileNotFoundError:
        return False, [f"File not found: {filepath}"]
    except Exception as e:
        return False, [f"Error reading file: {e}"]
    
    headings = extract_headings(content)
    
    if not headings:
        return False, ["No headings found in document"]
    
    all_errors = []
    all_errors.extend(validate_single_h1(headings))
    all_errors.extend(validate_how_to_title(headings))
    all_errors.extend(validate_heading_hierarchy(headings))
    all_errors.extend(validate_required_sections(headings))
    
    return len(all_errors) == 0, all_errors


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <path-to-markdown-file>")
        sys.exit(2)
    
    filepath = Path(sys.argv[1])
    passed, errors = validate_file(filepath)
    
    if passed:
        print(f"✓ {filepath.name}: All heading checks passed")
        sys.exit(0)
    else:
        print(f"✗ {filepath.name}: {len(errors)} error(s) found")
        for error in errors:
            print(f"  - {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
