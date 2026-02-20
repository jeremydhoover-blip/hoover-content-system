#!/usr/bin/env python3
"""
Validator for error message content.
Checks character limits, required fields, and anti-patterns.

Usage:
    python error_message_validator.py <yaml_file>
    python error_message_validator.py --inline "<message>"
"""

import argparse
import sys
import re
import yaml  # type: ignore
from pathlib import Path

# Character limits per error message spec
TITLE_MAX_CHARS = 60
BODY_MAX_CHARS = 150
ACTION_LABEL_MAX_CHARS = 25

# Anti-patterns to flag
ANTI_PATTERNS = [
    (r'\bError \d+\b', 'Avoid exposing error codes to users'),
    (r'\bException\b', 'Avoid technical exception terminology'),
    (r'\bOops\b', 'Avoid trivializing language'),
    (r'\bYou failed\b', 'Avoid blaming the user'),
    (r'\bYou forgot\b', 'Avoid blaming the user'),
    (r'\bInvalid\b(?! email| URL| format)', 'Avoid vague "invalid" without context'),
    (r'!!+', 'Avoid multiple exclamation points'),
    (r'\b[A-Z]{4,}\b', 'Avoid all-caps words'),
    (r'stack\s*trace', 'Never expose stack traces'),
    (r'null|undefined|NaN', 'Never expose programming literals'),
]

# Required action types
VALID_ACTION_TYPES = {'retry', 'dismiss', 'navigate', 'contact', None}


def validate_char_limit(value: str, max_chars: int, field_name: str) -> list:
    """Check if value exceeds character limit."""
    errors = []
    if value and len(value) > max_chars:
        errors.append(
            f'{field_name} exceeds {max_chars} chars: '
            f'"{value[:50]}..." ({len(value)} chars)'
        )
    return errors


def validate_anti_patterns(text: str, field_name: str) -> list:
    """Check for anti-patterns in text."""
    errors = []
    if not text:
        return errors
    for pattern, message in ANTI_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            errors.append(f'{field_name}: {message}')
    return errors


def validate_error_yaml(data: dict) -> list:
    """Validate structured error message YAML."""
    errors = []
    
    error_obj = data.get('error', data)
    
    # Check required field: title
    title = error_obj.get('title')
    if not title:
        errors.append('Missing required field: title')
    else:
        errors.extend(validate_char_limit(title, TITLE_MAX_CHARS, 'title'))
        errors.extend(validate_anti_patterns(title, 'title'))
    
    # Check optional field: body
    body = error_obj.get('body')
    if body:
        errors.extend(validate_char_limit(body, BODY_MAX_CHARS, 'body'))
        errors.extend(validate_anti_patterns(body, 'body'))
    
    # Check optional field: action
    action = error_obj.get('action')
    if action:
        label = action.get('label')
        if label:
            errors.extend(
                validate_char_limit(label, ACTION_LABEL_MAX_CHARS, 'action.label')
            )
            errors.extend(validate_anti_patterns(label, 'action.label'))
        
        action_type = action.get('type')
        if action_type and action_type not in VALID_ACTION_TYPES:
            errors.append(
                f'Invalid action.type "{action_type}". '
                f'Valid types: {", ".join(str(t) for t in VALID_ACTION_TYPES if t)}'
            )
    
    return errors


def validate_inline_message(message: str) -> list:
    """Validate a single inline error message (e.g., field validation)."""
    errors = []
    
    # Inline messages should be short
    if len(message) > TITLE_MAX_CHARS:
        errors.append(
            f'Inline message exceeds {TITLE_MAX_CHARS} chars: '
            f'"{message[:50]}..." ({len(message)} chars)'
        )
    
    errors.extend(validate_anti_patterns(message, 'message'))
    
    return errors


def main():
    parser = argparse.ArgumentParser(
        description='Validate error message content'
    )
    parser.add_argument(
        'file', 
        nargs='?', 
        help='YAML file containing error message'
    )
    parser.add_argument(
        '--inline', 
        help='Validate a single inline message string'
    )
    
    args = parser.parse_args()
    
    if args.inline:
        errors = validate_inline_message(args.inline)
    elif args.file:
        path = Path(args.file)
        if not path.exists():
            print(f'Error: File not found: {args.file}', file=sys.stderr)
            sys.exit(1)
        with open(path, 'r', encoding='utf-8') as f:
            try:
                data = yaml.safe_load(f)
            except yaml.YAMLError as e:
                print(f'Error: Invalid YAML: {e}', file=sys.stderr)
                sys.exit(1)
        errors = validate_error_yaml(data)
    else:
        parser.print_help()
        sys.exit(1)
    
    if errors:
        print('Validation FAILED:')
        for error in errors:
            print(f'  ✗ {error}')
        sys.exit(1)
    else:
        print('Validation PASSED')
        sys.exit(0)


if __name__ == '__main__':
    main()
