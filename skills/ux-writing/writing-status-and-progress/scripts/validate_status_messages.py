#!/usr/bin/env python3
"""
Validator for status and progress messages.
Checks state transitions, progress indicators, and message clarity.

Usage:
    python validate_status_messages.py <yaml_file>
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

# Valid status states
VALID_STATES = [
    'pending', 'in_progress', 'success', 'error', 'warning',
    'paused', 'cancelled', 'queued', 'complete', 'failed'
]

# Constraints
STATUS_MESSAGE_MAX_CHARS = 60
PROGRESS_LABEL_MAX_CHARS = 40

# Anti-patterns
ANTI_PATTERNS = {
    'vague_status': re.compile(r'^(status|state|progress):', re.I),
    'tech_status': re.compile(r'\b(null|undefined|exception|500|error code)\b', re.I),
    'all_caps_status': re.compile(r'^[A-Z]{4,}$'),
}


def validate_status_message(status: dict, name: str = '') -> list:
    """Validate a single status message."""
    errors = []
    identifier = name or status.get('state', status.get('id', 'Status'))
    
    state = status.get('state', '').lower().replace(' ', '_')
    message = status.get('message', status.get('label', ''))
    
    # Check state is valid
    if state and state not in VALID_STATES:
        errors.append(
            f'{identifier}: Unknown state "{state}". '
            f'Valid: {", ".join(VALID_STATES)}'
        )
    
    # Check message
    if message:
        if len(message) > STATUS_MESSAGE_MAX_CHARS:
            errors.append(
                f'{identifier}: Message too long ({len(message)} chars, '
                f'max {STATUS_MESSAGE_MAX_CHARS})'
            )
        
        if ANTI_PATTERNS['vague_status'].match(message):
            errors.append(
                f'{identifier}: Don\'t prefix with "Status:" - be direct.'
            )
        
        if ANTI_PATTERNS['tech_status'].search(message):
            errors.append(
                f'{identifier}: Technical terms in status. '
                f'Use user-friendly language.'
            )
        
        if ANTI_PATTERNS['all_caps_status'].match(message):
            errors.append(
                f'{identifier}: Avoid ALL CAPS for status messages.'
            )
    
    # Error/failure states should have recovery info
    if state in ['error', 'failed']:
        recovery = status.get('recovery', status.get('action', ''))
        if not recovery:
            errors.append(
                f'{identifier}: Error states should include recovery action.'
            )
    
    return errors


def validate_progress_indicator(progress: dict, name: str = '') -> list:
    """Validate a progress indicator definition."""
    errors = []
    identifier = name or 'Progress indicator'
    
    label = progress.get('label', '')
    percentage = progress.get('percentage', progress.get('percent'))
    
    # Check label length
    if label and len(label) > PROGRESS_LABEL_MAX_CHARS:
        errors.append(
            f'{identifier}: Label too long ({len(label)} chars, '
            f'max {PROGRESS_LABEL_MAX_CHARS})'
        )
    
    # Check percentage is valid
    if percentage is not None:
        try:
            pct = float(percentage)
            if pct < 0 or pct > 100:
                errors.append(
                    f'{identifier}: Percentage must be 0-100, got {pct}'
                )
        except (ValueError, TypeError):
            errors.append(
                f'{identifier}: Invalid percentage value "{percentage}"'
            )
    
    return errors


def validate_status_content(data: dict) -> list:
    """Validate status and progress content."""
    errors = []
    
    # Handle status messages
    statuses = (
        data.get('status_messages', []) or
        data.get('statuses', []) or
        data.get('states', [])
    )
    
    if isinstance(statuses, list):
        for i, status in enumerate(statuses):
            name = status.get('state', status.get('id', f'Status {i+1}'))
            errors.extend(validate_status_message(status, name))
    elif isinstance(statuses, dict):
        for state_name, status in statuses.items():
            if isinstance(status, dict):
                errors.extend(validate_status_message(status, state_name))
    
    # Handle progress indicators
    progress = data.get('progress', data.get('progress_indicator'))
    if progress:
        if isinstance(progress, dict):
            errors.extend(validate_progress_indicator(progress))
        elif isinstance(progress, list):
            for i, p in enumerate(progress):
                errors.extend(validate_progress_indicator(p, f'Progress {i+1}'))
    
    # Handle single status
    if 'state' in data or 'message' in data:
        errors.extend(validate_status_message(data, 'Status message'))
    
    return errors


def main():
    parser = argparse.ArgumentParser(
        description='Validate status and progress messages'
    )
    parser.add_argument(
        'file',
        help='YAML file containing status definitions'
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
    
    errors = validate_status_content(data)
    
    if errors:
        print('Validation FAILED:')
        for error in errors:
            print(f'  ✗ {error}')
        sys.exit(1)
    else:
        print('✓ Status messages validation passed')
        sys.exit(0)


if __name__ == '__main__':
    main()
