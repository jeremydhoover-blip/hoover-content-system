#!/usr/bin/env python3
"""
Validator for loading and latency messaging.
Checks time estimates, latency tier alignment, and message progression.

Usage:
    python validate_latency_messages.py <yaml_file>
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

# Latency tiers (from reference/latency-tiers.md)
LATENCY_TIERS = {
    'instant': {'max_ms': 300, 'indicator': 'none'},
    'short': {'max_ms': 2000, 'indicator': 'spinner'},
    'medium': {'max_ms': 10000, 'indicator': 'progress'},
    'long': {'max_ms': 60000, 'indicator': 'progress_percent'},
    'extended': {'max_ms': None, 'indicator': 'background'},
}

# Constraints
MESSAGE_MAX_CHARS = 60
PROGRESS_MESSAGE_MAX_CHARS = 80

# Anti-patterns
ANTI_PATTERNS = {
    'vague_time': re.compile(r'\b(soon|shortly|moment|bit)\b', re.I),
    'loading': re.compile(r'^loading\.{0,3}$', re.I),
    'please_wait': re.compile(r'^please wait\.{0,3}$', re.I),
}


def validate_loading_state(state: dict, name: str = '') -> list:
    """Validate a single loading state message."""
    errors = []
    identifier = name or state.get('id', 'Loading state')
    
    message = state.get('message', state.get('text', ''))
    tier = state.get('tier', state.get('latency_tier', ''))
    duration = state.get('duration', state.get('duration_ms', 0))
    
    # Check message content
    if message:
        # Check length
        if len(message) > MESSAGE_MAX_CHARS:
            errors.append(
                f'{identifier}: Message too long ({len(message)} chars, '
                f'max {MESSAGE_MAX_CHARS})'
            )
        
        # Check for vague time references
        if ANTI_PATTERNS['vague_time'].search(message):
            errors.append(
                f'{identifier}: Avoid vague time words like "soon" or "moment". '
                f'Be specific or omit time.'
            )
        
        # Check for generic loading text
        if ANTI_PATTERNS['loading'].match(message):
            errors.append(
                f'{identifier}: Generic "Loading..." - add context about what\'s loading.'
            )
        
        if ANTI_PATTERNS['please_wait'].match(message):
            errors.append(
                f'{identifier}: "Please wait" is passive. '
                f'Describe the action instead.'
            )
    
    # Check tier alignment
    if tier and tier in LATENCY_TIERS:
        tier_info = LATENCY_TIERS[tier]
        
        # For long operations, message should exist
        if tier in ['medium', 'long', 'extended'] and not message:
            errors.append(
                f'{identifier}: Operations > 2s (tier "{tier}") should have '
                f'a loading message.'
            )
        
        # Check duration matches tier
        if duration and tier_info['max_ms']:
            if duration > tier_info['max_ms']:
                errors.append(
                    f'{identifier}: Duration {duration}ms exceeds tier "{tier}" '
                    f'max of {tier_info["max_ms"]}ms.'
                )
    
    # Check progress messages for long operations
    progress_messages = state.get('progress_messages', [])
    if tier in ['long', 'extended'] and not progress_messages:
        errors.append(
            f'{identifier}: Long operations should have progress messages.'
        )
    
    for i, prog_msg in enumerate(progress_messages):
        if isinstance(prog_msg, str) and len(prog_msg) > PROGRESS_MESSAGE_MAX_CHARS:
            errors.append(
                f'{identifier}: Progress message {i+1} too long.'
            )
    
    return errors


def validate_latency_messages(data: dict) -> list:
    """Validate latency/loading message content."""
    errors = []
    
    # Handle different structures
    states = (
        data.get('loading_states', []) or
        data.get('states', []) or
        data.get('messages', [])
    )
    
    if isinstance(states, list):
        for i, state in enumerate(states):
            name = state.get('id', state.get('name', f'State {i+1}'))
            errors.extend(validate_loading_state(state, name))
    elif isinstance(states, dict):
        for state_name, state in states.items():
            errors.extend(validate_loading_state(state, state_name))
    
    # Handle single message
    if 'message' in data or 'tier' in data:
        errors.extend(validate_loading_state(data, 'Loading message'))
    
    return errors


def main():
    parser = argparse.ArgumentParser(
        description='Validate loading and latency messages'
    )
    parser.add_argument(
        'file',
        help='YAML file containing loading state definitions'
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
    
    errors = validate_latency_messages(data)
    
    if errors:
        print('Validation FAILED:')
        for error in errors:
            print(f'  ✗ {error}')
        sys.exit(1)
    else:
        print('✓ Latency messages validation passed')
        sys.exit(0)


if __name__ == '__main__':
    main()
