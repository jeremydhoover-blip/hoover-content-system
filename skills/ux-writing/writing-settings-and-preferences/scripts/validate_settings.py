#!/usr/bin/env python3
"""
Validator for settings and preferences content.
Checks label format, description length, and common anti-patterns.

Usage:
    python validate_settings.py <yaml_file>
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
LABEL_MAX_CHARS = 40
DESCRIPTION_MAX_CHARS = 80

# Anti-patterns
ANTI_PATTERNS = {
    'question': re.compile(r'^(do you|would you|can you|should|will you)', re.I),
    'command': re.compile(r'^(enable|disable|turn on|turn off|set|configure)', re.I),
    'double_negative': re.compile(r'\b(don\'?t|not|never)\b.*(disable|hide|off|no)\b', re.I),
    'jargon': re.compile(r'\b(SSO|MFA|2FA|API|OAuth|SAML)\b(?!\s*\()'),
    'marketing': re.compile(r'\b(supercharge|turbo|boost|amazing|awesome|powerful)\b', re.I),
}


def validate_setting(setting: dict, path: str = '') -> list:
    """Validate a single setting entry."""
    errors = []
    
    label = setting.get('label', '')
    description = setting.get('description', '')
    
    # Check label exists
    if not label:
        errors.append(f'{path}: Missing label')
        return errors
    
    # Check label length
    if len(label) > LABEL_MAX_CHARS:
        errors.append(
            f'{path}: Label too long ({len(label)} chars, '
            f'max {LABEL_MAX_CHARS}): "{label}"'
        )
    
    # Check label format - should not start with verb
    if ANTI_PATTERNS['command'].match(label):
        errors.append(
            f'{path}: Label should be noun phrase, not command: "{label}". '
            f'Try removing the verb.'
        )
    
    # Check label format - should not be question
    if ANTI_PATTERNS['question'].match(label):
        errors.append(
            f'{path}: Label should not be a question: "{label}"'
        )
    
    # Check description length
    if description and len(description) > DESCRIPTION_MAX_CHARS:
        errors.append(
            f'{path}: Description too long ({len(description)} chars, '
            f'max {DESCRIPTION_MAX_CHARS})'
        )
    
    # Check for double negatives
    text = f'{label} {description}'
    if ANTI_PATTERNS['double_negative'].search(text):
        errors.append(
            f'{path}: Possible double negative in "{label}". '
            f'Rephrase positively.'
        )
    
    # Check for unexpanded jargon
    jargon_match = ANTI_PATTERNS['jargon'].search(text)
    if jargon_match:
        errors.append(
            f'{path}: Jargon "{jargon_match.group()}" should be expanded '
            f'or explained.'
        )
    
    # Check for marketing language
    marketing_match = ANTI_PATTERNS['marketing'].search(text)
    if marketing_match:
        errors.append(
            f'{path}: Avoid marketing language: "{marketing_match.group()}"'
        )
    
    # Recursively check children
    children = setting.get('children', setting.get('settings', []))
    for i, child in enumerate(children):
        child_path = f'{path} > {child.get("label", f"[{i}]")}'
        errors.extend(validate_setting(child, child_path))
    
    return errors


def validate_settings(data: dict) -> list:
    """Validate a settings structure."""
    errors = []
    
    # Handle different structures
    if 'settings' in data:
        settings = data['settings']
    elif 'categories' in data:
        for cat in data['categories']:
            cat_name = cat.get('name', cat.get('label', 'Unknown'))
            for setting in cat.get('settings', []):
                path = f'{cat_name} > {setting.get("label", "?")}'
                errors.extend(validate_setting(setting, path))
        return errors
    elif isinstance(data, list):
        settings = data
    else:
        settings = [data]
    
    for setting in settings:
        label = setting.get('label', '?')
        errors.extend(validate_setting(setting, label))
    
    return errors


def main():
    parser = argparse.ArgumentParser(
        description='Validate settings and preferences content'
    )
    parser.add_argument(
        'file',
        help='YAML file containing settings definitions'
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
    
    errors = validate_settings(data)
    
    if errors:
        print('Validation FAILED:')
        for error in errors:
            print(f'  ✗ {error}')
        sys.exit(1)
    else:
        print('✓ Settings validation passed')
        sys.exit(0)


if __name__ == '__main__':
    main()
