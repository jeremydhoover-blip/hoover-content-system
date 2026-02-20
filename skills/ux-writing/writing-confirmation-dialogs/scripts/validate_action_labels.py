#!/usr/bin/env python3
"""
Validator for confirmation dialog action labels.
Checks that confirm/cancel buttons follow UX writing best practices.

Usage:
    python validate_action_labels.py <yaml_file>
    python validate_action_labels.py --confirm "Delete" --cancel "Cancel"
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

# Character limits
CONFIRM_MAX_CHARS = 20
CANCEL_MAX_CHARS = 15
HEADLINE_MAX_CHARS = 60
BODY_MAX_CHARS = 200

# Generic labels that should be avoided for confirm buttons
GENERIC_CONFIRM_LABELS = [
    'yes',
    'ok',
    'okay',
    'confirm',
    'submit',
    'continue',
    'proceed',
]

# Acceptable cancel labels
VALID_CANCEL_LABELS = [
    'cancel',
    'go back',
    'keep',
    'never mind',
    'not now',
    'no',
    'dismiss',
]

# Destructive action verbs that need destructive styling
DESTRUCTIVE_VERBS = [
    'delete',
    'remove',
    'destroy',
    'erase',
    'discard',
    'revoke',
    'terminate',
    'permanently',
]


def validate_confirm_label(label: str) -> list:
    """Validate confirm button label."""
    errors = []
    label_lower = label.lower().strip()
    
    # Check length
    if len(label) > CONFIRM_MAX_CHARS:
        errors.append(
            f'Confirm label too long: {len(label)} chars (max {CONFIRM_MAX_CHARS})'
        )
    
    # Check for generic labels
    if label_lower in GENERIC_CONFIRM_LABELS:
        errors.append(
            f'Confirm label "{label}" is too generic. '
            f'Use a specific verb that describes the action (e.g., "Delete", "Remove").'
        )
    
    # Confirm should start with a verb (basic heuristic)
    # This is a soft check — some valid labels might not match
    
    return errors


def validate_cancel_label(label: str) -> list:
    """Validate cancel button label."""
    errors = []
    label_lower = label.lower().strip()
    
    # Check length
    if len(label) > CANCEL_MAX_CHARS:
        errors.append(
            f'Cancel label too long: {len(label)} chars (max {CANCEL_MAX_CHARS})'
        )
    
    return errors


def check_destructive_styling(confirm_label: str, style: str) -> list:
    """Check if destructive actions have proper styling."""
    errors = []
    label_lower = confirm_label.lower()
    
    is_destructive_action = any(
        verb in label_lower for verb in DESTRUCTIVE_VERBS
    )
    
    if is_destructive_action and style != 'destructive':
        errors.append(
            f'Destructive action "{confirm_label}" should use destructive styling. '
            f'Got: "{style}"'
        )
    
    return errors


def validate_dialog_yaml(data: dict) -> list:
    """Validate full confirmation dialog YAML."""
    errors = []
    
    dialog = data.get('confirmation_dialog', data)
    
    # Validate headline
    headline = dialog.get('headline')
    if headline:
        if len(headline) > HEADLINE_MAX_CHARS:
            errors.append(
                f'Headline too long: {len(headline)} chars (max {HEADLINE_MAX_CHARS})'
            )
        # Check for vague headlines
        vague_headlines = ['are you sure', 'confirm', 'warning']
        if headline.lower().strip().rstrip('?') in vague_headlines:
            errors.append(
                f'Headline "{headline}" is too vague. '
                f'State what will happen.'
            )
    else:
        errors.append('Missing required field: headline')
    
    # Validate body
    body = dialog.get('body')
    if body and len(body) > BODY_MAX_CHARS:
        errors.append(
            f'Body too long: {len(body)} chars (max {BODY_MAX_CHARS})'
        )
    
    # Validate confirm button
    confirm = dialog.get('confirm')
    if confirm:
        label = confirm.get('label')
        if label:
            errors.extend(validate_confirm_label(label))
            
            # Check styling
            style = confirm.get('style', 'default')
            errors.extend(check_destructive_styling(label, style))
        else:
            errors.append('Missing confirm.label')
    else:
        errors.append('Missing required field: confirm')
    
    # Validate cancel button
    cancel = dialog.get('cancel')
    if cancel:
        label = cancel.get('label')
        if label:
            errors.extend(validate_cancel_label(label))
    else:
        errors.append('Missing required field: cancel')
    
    return errors


def main():
    parser = argparse.ArgumentParser(
        description='Validate confirmation dialog action labels'
    )
    parser.add_argument(
        'file',
        nargs='?',
        help='YAML file containing dialog definition'
    )
    parser.add_argument(
        '--confirm',
        help='Validate a confirm button label directly'
    )
    parser.add_argument(
        '--cancel',
        help='Validate a cancel button label directly'
    )
    
    args = parser.parse_args()
    
    errors = []
    
    if args.confirm:
        errors.extend(validate_confirm_label(args.confirm))
    
    if args.cancel:
        errors.extend(validate_cancel_label(args.cancel))
    
    if args.confirm or args.cancel:
        if errors:
            print('Validation FAILED:')
            for error in errors:
                print(f'  ✗ {error}')
            sys.exit(1)
        else:
            print('✓ Labels valid')
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
        
        errors = validate_dialog_yaml(data)
        if errors:
            print('Validation FAILED:')
            for error in errors:
                print(f'  ✗ {error}')
            sys.exit(1)
        else:
            print('✓ Dialog validation passed')
            sys.exit(0)
    
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()
