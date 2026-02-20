#!/usr/bin/env python3
"""
Validator for permission and access messages.
Checks permission request copy, denial messages, and role descriptions.

Usage:
    python validate_permissions.py <yaml_file>
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

# Constraints
HEADLINE_MAX_CHARS = 50
BODY_MAX_CHARS = 120
ACTION_LABEL_MAX_CHARS = 25

# Anti-patterns
ANTI_PATTERNS = {
    'vague_reason': re.compile(
        r'\b(to improve your experience|for better service|to help you)\b', re.I
    ),
    'we_focused': re.compile(r'^we (need|require|want)', re.I),
    'demanding': re.compile(r'\b(must|have to|need to)\s+(allow|grant|give)', re.I),
    'technical': re.compile(
        r'\b(API|SDK|endpoint|runtime|daemon|service)\b(?!\s+account)', re.I
    ),
}

# Required elements
PERMISSION_TYPES = [
    'camera', 'microphone', 'location', 'contacts', 'calendar',
    'photos', 'files', 'notifications', 'bluetooth', 'storage'
]


def validate_permission_request(request: dict, name: str = '') -> list:
    """Validate a permission request message."""
    errors = []
    identifier = name or request.get('permission', 'Request')
    
    headline = request.get('headline', '')
    body = request.get('body', request.get('description', ''))
    
    # Check headline
    if not headline:
        errors.append(f'{identifier}: Missing headline')
    else:
        if len(headline) > HEADLINE_MAX_CHARS:
            errors.append(
                f'{identifier}: Headline too long ({len(headline)} chars, '
                f'max {HEADLINE_MAX_CHARS})'
            )
        
        # Check for we-focused language
        if ANTI_PATTERNS['we_focused'].match(headline):
            errors.append(
                f'{identifier}: Headline is company-focused. '
                f'Reframe around user benefit.'
            )
    
    # Check body
    if not body:
        errors.append(f'{identifier}: Missing body/description explaining why')
    else:
        if len(body) > BODY_MAX_CHARS:
            errors.append(
                f'{identifier}: Body too long ({len(body)} chars, '
                f'max {BODY_MAX_CHARS})'
            )
        
        # Check for vague reasons
        if ANTI_PATTERNS['vague_reason'].search(body):
            errors.append(
                f'{identifier}: Vague justification. Be specific about '
                f'what user can do with this permission.'
            )
        
        # Check for demanding language
        if ANTI_PATTERNS['demanding'].search(body):
            errors.append(
                f'{identifier}: Demanding tone. '
                f'Frame as user choice, not requirement.'
            )
    
    # Check action labels
    actions = request.get('actions', request.get('action', {}))
    if isinstance(actions, dict):
        for action_type, label in actions.items():
            if label and len(label) > ACTION_LABEL_MAX_CHARS:
                errors.append(
                    f'{identifier}: Action "{action_type}" too long '
                    f'({len(label)} chars)'
                )
    
    return errors


def validate_denial_message(denial: dict, name: str = '') -> list:
    """Validate a permission denial message."""
    errors = []
    identifier = name or 'Denial message'
    
    headline = denial.get('headline', '')
    body = denial.get('body', denial.get('description', ''))
    
    # Denial should explain what's blocked and how to fix
    if not headline and not body:
        errors.append(f'{identifier}: Missing denial message content')
        return errors
    
    text = f'{headline} {body}'.lower()
    
    # Should mention settings or alternative
    mentions_fix = any(word in text for word in [
        'settings', 'enable', 'allow', 'turn on', 'alternative', 'instead'
    ])
    
    if not mentions_fix:
        errors.append(
            f'{identifier}: Denial message should explain how to enable '
            f'or offer an alternative.'
        )
    
    # Check for technical jargon
    if ANTI_PATTERNS['technical'].search(f'{headline} {body}'):
        errors.append(f'{identifier}: Avoid technical jargon in user-facing messages')
    
    return errors


def validate_permissions(data: dict) -> list:
    """Validate permission-related content."""
    errors = []
    
    # Handle permission requests
    requests = data.get('permission_requests', data.get('requests', []))
    if isinstance(requests, list):
        for i, req in enumerate(requests):
            name = req.get('permission', f'Request {i+1}')
            errors.extend(validate_permission_request(req, name))
    elif isinstance(requests, dict):
        for perm_name, req in requests.items():
            errors.extend(validate_permission_request(req, perm_name))
    
    # Handle denial messages
    denials = data.get('denial_messages', data.get('denials', []))
    if isinstance(denials, list):
        for i, denial in enumerate(denials):
            name = denial.get('type', f'Denial {i+1}')
            errors.extend(validate_denial_message(denial, name))
    elif isinstance(denials, dict):
        for denial_type, denial in denials.items():
            errors.extend(validate_denial_message(denial, denial_type))
    
    # Handle single permission request
    if 'headline' in data or 'body' in data:
        errors.extend(validate_permission_request(data, 'Permission request'))
    
    return errors


def main():
    parser = argparse.ArgumentParser(
        description='Validate permission and access messages'
    )
    parser.add_argument(
        'file',
        help='YAML file containing permission messages'
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
    
    errors = validate_permissions(data)
    
    if errors:
        print('Validation FAILED:')
        for error in errors:
            print(f'  ✗ {error}')
        sys.exit(1)
    else:
        print('✓ Permission messages validation passed')
        sys.exit(0)


if __name__ == '__main__':
    main()
