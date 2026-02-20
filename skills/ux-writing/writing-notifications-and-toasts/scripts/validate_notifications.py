#!/usr/bin/env python3
"""
Validator for notifications and toast messages.
Checks notification type alignment, message length, and action patterns.

Usage:
    python validate_notifications.py <yaml_file>
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

# Valid notification types
VALID_TYPES = [
    'success', 'error', 'warning', 'info',
    'alert', 'confirmation', 'announcement'
]

# Constraints by type
TYPE_CONSTRAINTS = {
    'success': {'max_chars': 60, 'requires_action': False},
    'error': {'max_chars': 80, 'requires_action': True},
    'warning': {'max_chars': 80, 'requires_action': False},
    'info': {'max_chars': 100, 'requires_action': False},
    'alert': {'max_chars': 80, 'requires_action': True},
    'confirmation': {'max_chars': 60, 'requires_action': False},
    'announcement': {'max_chars': 120, 'requires_action': False},
}

DEFAULT_MAX_CHARS = 80
TITLE_MAX_CHARS = 40
ACTION_LABEL_MAX_CHARS = 20

# Anti-patterns
ANTI_PATTERNS = {
    'success_exclaim': re.compile(r'!{2,}'),
    'all_caps': re.compile(r'\b[A-Z]{4,}\b'),
    'vague_error': re.compile(r'^(error|something went wrong|oops)\.?$', re.I),
    'tech_terms': re.compile(r'\b(exception|null|undefined|500|404|timeout)\b', re.I),
}


def validate_notification(notification: dict, index: int = 0) -> list:
    """Validate a single notification message."""
    errors = []
    
    notif_type = notification.get('type', 'info').lower()
    title = notification.get('title', notification.get('headline', ''))
    message = notification.get('message', notification.get('body', ''))
    action = notification.get('action', notification.get('cta'))
    
    identifier = title or f'Notification {index + 1}'
    
    # Check type is valid
    if notif_type not in VALID_TYPES:
        errors.append(
            f'{identifier}: Unknown type "{notif_type}". '
            f'Valid: {", ".join(VALID_TYPES)}'
        )
    
    # Get constraints for this type
    constraints = TYPE_CONSTRAINTS.get(notif_type, {'max_chars': DEFAULT_MAX_CHARS})
    
    # Check title
    if title:
        if len(title) > TITLE_MAX_CHARS:
            errors.append(
                f'{identifier}: Title too long ({len(title)} chars, '
                f'max {TITLE_MAX_CHARS})'
            )
        
        if ANTI_PATTERNS['all_caps'].search(title):
            errors.append(
                f'{identifier}: Avoid ALL CAPS in title.'
            )
    
    # Check message
    if message:
        max_chars = constraints.get('max_chars', DEFAULT_MAX_CHARS)
        if len(message) > max_chars:
            errors.append(
                f'{identifier}: Message too long for {notif_type} '
                f'({len(message)} chars, max {max_chars})'
            )
        
        if ANTI_PATTERNS['success_exclaim'].search(message):
            errors.append(
                f'{identifier}: Avoid multiple exclamation marks.'
            )
        
        if notif_type == 'error' and ANTI_PATTERNS['vague_error'].match(message):
            errors.append(
                f'{identifier}: Vague error message. Be specific about what happened.'
            )
        
        if ANTI_PATTERNS['tech_terms'].search(message):
            errors.append(
                f'{identifier}: Technical terms in user-facing message. '
                f'Use plain language.'
            )
    else:
        errors.append(f'{identifier}: Missing message content')
    
    # Check action requirement
    if constraints.get('requires_action') and not action:
        errors.append(
            f'{identifier}: {notif_type.title()} notifications should '
            f'include an action.'
        )
    
    # Check action label length
    if action:
        action_label = action if isinstance(action, str) else action.get('label', '')
        if action_label and len(action_label) > ACTION_LABEL_MAX_CHARS:
            errors.append(
                f'{identifier}: Action label too long ({len(action_label)} chars)'
            )
    
    return errors


def validate_notifications(data: dict) -> list:
    """Validate notification content."""
    errors = []
    
    # Handle list of notifications
    notifications = (
        data.get('notifications', []) or
        data.get('toasts', []) or
        data.get('messages', [])
    )
    
    if isinstance(notifications, list):
        for i, notif in enumerate(notifications):
            errors.extend(validate_notification(notif, i))
    elif isinstance(notifications, dict):
        for notif_name, notif in notifications.items():
            if isinstance(notif, dict):
                notif_with_name = {**notif, 'title': notif.get('title', notif_name)}
                errors.extend(validate_notification(notif_with_name))
    
    # Handle single notification
    if 'message' in data or 'type' in data:
        errors.extend(validate_notification(data))
    
    return errors


def main():
    parser = argparse.ArgumentParser(
        description='Validate notifications and toast messages'
    )
    parser.add_argument(
        'file',
        help='YAML file containing notification definitions'
    )
    
    args = parser.parse_args()
    
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
    
    errors = validate_notifications(data)
    
    if errors:
        print('Validation FAILED:')
        for error in errors:
            print(f'  ✗ {error}')
        sys.exit(1)
    else:
        print('✓ Notification validation passed')
        sys.exit(0)


if __name__ == '__main__':
    main()
