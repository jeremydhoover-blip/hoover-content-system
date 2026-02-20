#!/usr/bin/env python3
"""
Validator for empty state CTAs (calls-to-action).
Checks CTA labels for clarity, length, and anti-patterns.

Usage:
    python validate_cta.py <yaml_file>
    python validate_cta.py --label "Create project"
"""

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml  # type: ignore
    HAS_YAML = True
except ImportError:
    HAS_YAML = False

# CTA label constraints
MAX_LABEL_LENGTH = 25

# Vague labels to flag
VAGUE_LABELS = [
    'click here',
    'get started',
    'submit',
    'go',
    'ok',
    'continue',
    'next',
    'learn more',  # Acceptable as secondary, flag if primary
]

# Anti-pattern phrases
ANTI_PATTERNS = [
    (r'^click\s+here$', 'Avoid "click here" — use descriptive label'),
    (r'^go$', 'Too vague — specify destination'),
    (r'^submit$', 'Avoid generic "submit" — describe the action'),
    (r'^ok$', 'Too vague for primary CTA'),
]

# Recommended verb starters for CTAs
STRONG_VERBS = [
    'create', 'add', 'import', 'export', 'clear', 'reset',
    'search', 'browse', 'explore', 'view', 'open', 'start',
    'write', 'upload', 'download', 'invite', 'share', 'try',
]


def validate_label(label: str, is_primary: bool = True) -> list:
    """Validate a CTA label. Returns list of error messages."""
    errors = []
    label_lower = label.lower().strip()
    
    # Check length
    if len(label) > MAX_LABEL_LENGTH:
        errors.append(
            f'Label too long: {len(label)} chars (max {MAX_LABEL_LENGTH}). '
            f'Label: "{label}"'
        )
    
    # Check anti-patterns
    for pattern, message in ANTI_PATTERNS:
        if re.match(pattern, label_lower):
            errors.append(message)
    
    # Check for vague labels (stricter for primary CTAs)
    if is_primary and label_lower in VAGUE_LABELS:
        errors.append(
            f'Vague primary CTA: "{label}". '
            f'Be specific about what happens.'
        )
    
    # Check for verb-first (recommended)
    first_word = label_lower.split()[0] if label_lower.split() else ''
    if first_word and first_word not in STRONG_VERBS:
        # Warning, not error
        if is_primary:
            errors.append(
                f'Consider starting with a strong verb. '
                f'Got: "{first_word}". '
                f'Recommended: {", ".join(STRONG_VERBS[:5])}...'
            )
    
    return errors


def validate_empty_state_yaml(data: dict) -> list:
    """Validate empty state YAML structure for CTAs."""
    errors = []
    
    empty_state = data.get('empty_state', data)
    
    # Check primary action
    action = empty_state.get('action')
    if action:
        label = action.get('label')
        if label:
            label_errors = validate_label(label, is_primary=True)
            errors.extend(label_errors)
        else:
            # Label is null — check if intentional
            action_type = action.get('type')
            if action_type and action_type != 'null':
                errors.append(
                    'Action type specified but no label provided'
                )
    
    # Check secondary action if present
    secondary = empty_state.get('secondary_action')
    if secondary:
        label = secondary.get('label')
        if label:
            label_errors = validate_label(label, is_primary=False)
            errors.extend(label_errors)
    
    return errors


def main():
    parser = argparse.ArgumentParser(
        description='Validate empty state CTA labels'
    )
    parser.add_argument(
        'file',
        nargs='?',
        help='YAML file containing empty state definition'
    )
    parser.add_argument(
        '--label',
        help='Validate a single CTA label directly'
    )
    parser.add_argument(
        '--secondary',
        action='store_true',
        help='Treat the label as a secondary CTA (less strict)'
    )
    
    args = parser.parse_args()
    
    if args.label:
        errors = validate_label(args.label, is_primary=not args.secondary)
        if errors:
            print(f'CTA validation FAILED for: "{args.label}"')
            for error in errors:
                print(f'  ✗ {error}')
            sys.exit(1)
        else:
            print(f'✓ CTA label is valid: "{args.label}"')
            sys.exit(0)
    
    elif args.file:
        if not HAS_YAML:
            print('Error: PyYAML required. Install with: pip install pyyaml',
                  file=sys.stderr)
            sys.exit(1)
        
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
        
        errors = validate_empty_state_yaml(data)
        if errors:
            print('CTA validation FAILED:')
            for error in errors:
                print(f'  ✗ {error}')
            sys.exit(1)
        else:
            print('✓ CTA validation passed')
            sys.exit(0)
    
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()
