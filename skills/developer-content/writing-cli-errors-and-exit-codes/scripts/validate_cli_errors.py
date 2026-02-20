#!/usr/bin/env python3
"""
Validate CLI error message format and exit code usage.

Checks:
- Error message structure (command: error: message)
- Presence of actionable guidance
- Exit code consistency and documentation
- Sensitive data exposure

Usage:
    python validate_cli_errors.py <error_messages_file>
    python validate_cli_errors.py --check-codes <exit_codes_doc>

Exit codes:
    0 - All validations passed
    1 - Validation failures found
    2 - Invalid input
"""

import re
import sys
import argparse
from dataclasses import dataclass
from typing import List, Optional

# Patterns that indicate sensitive data exposure
SENSITIVE_PATTERNS = [
    r'password[=:]\s*\S+',
    r'token[=:]\s*[A-Za-z0-9_-]{20,}',
    r'api[_-]?key[=:]\s*\S+',
    r'secret[=:]\s*\S+',
    r'/home/\w+/',  # Home directory paths
    r'Bearer\s+[A-Za-z0-9_-]+',
]

# Patterns indicating missing actionable guidance
UNHELPFUL_PHRASES = [
    r'an error occurred',
    r'something went wrong',
    r'operation failed',
    r'error: error',
    r'unknown error',
]

# Exit codes that should be documented
STANDARD_EXIT_CODES = {0, 1, 2, 64, 65, 66, 68, 69, 70, 71, 73, 74, 75, 77, 78}


@dataclass
class ValidationError:
    message: str
    line: Optional[int] = None
    severity: str = "error"


def validate_error_format(content: str) -> List[ValidationError]:
    """Validate error message format."""
    errors = []
    lines = content.strip().split('\n')
    
    if not lines:
        return [ValidationError("Empty content")]
    
    first_line = lines[0]
    
    # Check for proper format: command: error: message
    if ': error:' not in first_line.lower() and 'error:' not in first_line.lower():
        errors.append(ValidationError(
            "Error message should follow 'command: error: message' format",
            line=1
        ))
    
    # Check for ALL CAPS (too aggressive)
    if first_line.isupper() and len(first_line) > 20:
        errors.append(ValidationError(
            "Error message should not be entirely uppercase",
            line=1
        ))
    
    return errors


def validate_actionable_guidance(content: str) -> List[ValidationError]:
    """Check for presence of helpful guidance."""
    errors = []
    content_lower = content.lower()
    
    # Check for unhelpful phrases
    for pattern in UNHELPFUL_PHRASES:
        if re.search(pattern, content_lower):
            errors.append(ValidationError(
                f"Unhelpful error phrase detected: '{pattern}'",
                severity="warning"
            ))
    
    # Check for actionable keywords
    action_indicators = ['try:', 'run:', 'check:', 'fix:', 'to ', 'use ', 'set ']
    has_action = any(ind in content_lower for ind in action_indicators)
    
    # Only flag if error seems recoverable (not internal error)
    if not has_action and 'internal error' not in content_lower:
        # Check if there's any suggestion-like content
        if 'contact' not in content_lower and 'report' not in content_lower:
            errors.append(ValidationError(
                "Error message may be missing actionable guidance for recovery",
                severity="warning"
            ))
    
    return errors


def validate_sensitive_data(content: str) -> List[ValidationError]:
    """Check for sensitive data exposure."""
    errors = []
    
    for pattern in SENSITIVE_PATTERNS:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            errors.append(ValidationError(
                f"Potential sensitive data exposure: '{match.group()[:20]}...'",
                severity="error"
            ))
    
    return errors


def validate_length(content: str) -> List[ValidationError]:
    """Check error message isn't excessively long."""
    errors = []
    lines = content.strip().split('\n')
    
    # Without --verbose, errors shouldn't exceed 10-15 lines
    if len(lines) > 15:
        errors.append(ValidationError(
            f"Error message is {len(lines)} lines. Consider using --verbose for details.",
            severity="warning"
        ))
    
    return errors


def validate_exit_code_doc(content: str) -> List[ValidationError]:
    """Validate exit code documentation completeness."""
    errors = []
    
    # Find documented exit codes
    documented_codes = set()
    for match in re.finditer(r'^\s*(\d+)\s+', content, re.MULTILINE):
        documented_codes.add(int(match.group(1)))
    
    # Check for essential codes
    essential_codes = {0, 1}
    missing_essential = essential_codes - documented_codes
    if missing_essential:
        errors.append(ValidationError(
            f"Missing essential exit codes: {missing_essential}"
        ))
    
    # Check for code 0 description
    if '0' in content and 'success' not in content.lower():
        errors.append(ValidationError(
            "Exit code 0 should be documented as 'Success'",
            severity="warning"
        ))
    
    return errors


def validate_error_message(content: str) -> List[ValidationError]:
    """Run all validations on error message content."""
    all_errors = []
    all_errors.extend(validate_error_format(content))
    all_errors.extend(validate_actionable_guidance(content))
    all_errors.extend(validate_sensitive_data(content))
    all_errors.extend(validate_length(content))
    return all_errors


def main():
    parser = argparse.ArgumentParser(description='Validate CLI error messages')
    parser.add_argument('file', nargs='?', help='File containing error message(s)')
    parser.add_argument('--check-codes', metavar='FILE', 
                        help='Validate exit code documentation')
    parser.add_argument('--stdin', action='store_true', help='Read from stdin')
    args = parser.parse_args()
    
    if args.check_codes:
        try:
            with open(args.check_codes, 'r', encoding='utf-8') as f:
                content = f.read()
            errors = validate_exit_code_doc(content)
        except Exception as e:
            print(f"ERROR: {e}")
            sys.exit(2)
    elif args.stdin:
        content = sys.stdin.read()
        errors = validate_error_message(content)
    elif args.file:
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                content = f.read()
            errors = validate_error_message(content)
        except Exception as e:
            print(f"ERROR: {e}")
            sys.exit(2)
    else:
        parser.print_help()
        sys.exit(2)
    
    # Output results
    error_count = sum(1 for e in errors if e.severity == "error")
    warning_count = sum(1 for e in errors if e.severity == "warning")
    
    if errors:
        for error in errors:
            prefix = "ERROR" if error.severity == "error" else "WARNING"
            loc = f" (line {error.line})" if error.line else ""
            print(f"[{prefix}]{loc} {error.message}")
    
    print(f"\n{'='*50}")
    print(f"Total: {error_count} errors, {warning_count} warnings")
    
    sys.exit(1 if error_count > 0 else 0)


if __name__ == '__main__':
    main()
