#!/usr/bin/env python3
"""
Validator for form labels and help text.
Checks label format, help text length, and placeholder patterns.

Usage:
    python validate_form_fields.py <yaml_file>
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
LABEL_MAX_WORDS = 4
HELP_TEXT_MAX_CHARS = 80
PLACEHOLDER_MAX_CHARS = 40
ERROR_MAX_CHARS = 80

# Anti-patterns
ANTI_PATTERNS = {
    'please': re.compile(r'^please\s', re.I),
    'enter_your': re.compile(r'\benter (your|the|a)\b', re.I),
    'colon_label': re.compile(r':$'),
    'all_caps': re.compile(r'^[A-Z]{3,}$'),
    'period_label': re.compile(r'\.$'),
    'vague_error': re.compile(r'^(invalid|error|wrong|bad)\s*(input|value|data)?\.?$', re.I),
}


def validate_field(field: dict, index: int = 0) -> list:
    """Validate a single form field."""
    errors = []
    field_name = field.get('name', field.get('label', f'Field {index}'))
    
    # Check label
    label = field.get('label', '')
    if not label:
        errors.append(f'{field_name}: Missing label')
    else:
        # Check label format
        if ANTI_PATTERNS['colon_label'].search(label):
            errors.append(f'{field_name}: Label should not end with colon')
        
        if ANTI_PATTERNS['period_label'].search(label):
            errors.append(f'{field_name}: Label should not end with period')
        
        if ANTI_PATTERNS['all_caps'].match(label):
            errors.append(f'{field_name}: Avoid ALL CAPS labels: "{label}"')
        
        if ANTI_PATTERNS['please'].match(label):
            errors.append(
                f'{field_name}: Don\'t start label with "Please": "{label}"'
            )
        
        word_count = len(label.split())
        if word_count > LABEL_MAX_WORDS:
            errors.append(
                f'{field_name}: Label too long ({word_count} words, '
                f'max {LABEL_MAX_WORDS})'
            )
    
    # Check help text
    help_text = field.get('help_text', field.get('description', ''))
    if help_text:
        if len(help_text) > HELP_TEXT_MAX_CHARS:
            errors.append(
                f'{field_name}: Help text too long ({len(help_text)} chars, '
                f'max {HELP_TEXT_MAX_CHARS})'
            )
        
        if ANTI_PATTERNS['enter_your'].search(help_text):
            errors.append(
                f'{field_name}: Avoid "enter your/the" in help text. '
                f'Be more specific.'
            )
    
    # Check placeholder
    placeholder = field.get('placeholder', '')
    if placeholder:
        if len(placeholder) > PLACEHOLDER_MAX_CHARS:
            errors.append(
                f'{field_name}: Placeholder too long ({len(placeholder)} chars)'
            )
        
        # Check if placeholder duplicates label
        if placeholder.lower().strip() == label.lower().strip():
            errors.append(
                f'{field_name}: Placeholder duplicates label. '
                f'Use an example instead.'
            )
    
    # Check error messages
    error_messages = field.get('errors', field.get('validation', {}))
    if isinstance(error_messages, dict):
        for error_type, message in error_messages.items():
            if message:
                if len(message) > ERROR_MAX_CHARS:
                    errors.append(
                        f'{field_name}: Error message "{error_type}" too long'
                    )
                
                if ANTI_PATTERNS['vague_error'].match(message):
                    errors.append(
                        f'{field_name}: Vague error message "{message}". '
                        f'Explain what\'s wrong and how to fix.'
                    )
    
    return errors


def validate_form(data: dict) -> list:
    """Validate a form definition."""
    errors = []
    
    # Handle different structures
    if 'fields' in data:
        fields = data['fields']
    elif 'form' in data:
        fields = data['form'].get('fields', [])
    elif isinstance(data, list):
        fields = data
    else:
        fields = [data]
    
    for i, field in enumerate(fields):
        field_errors = validate_field(field, i)
        errors.extend(field_errors)
    
    return errors


def main():
    parser = argparse.ArgumentParser(
        description='Validate form labels and help text'
    )
    parser.add_argument(
        'file',
        help='YAML file containing form field definitions'
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
    
    errors = validate_form(data)
    
    if errors:
        print('Validation FAILED:')
        for error in errors:
            print(f'  ✗ {error}')
        sys.exit(1)
    else:
        print('✓ Form field validation passed')
        sys.exit(0)


if __name__ == '__main__':
    main()
