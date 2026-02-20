#!/usr/bin/env python3
"""
Validator for onboarding flow structure.
Checks step count, required fields, and sequencing.

Usage:
    python validate_onboarding.py <yaml_file>
"""

import argparse
import sys
from pathlib import Path

try:
    import yaml  # type: ignore
    HAS_YAML = True
except ImportError:
    HAS_YAML = False

# Constraints
MAX_STEPS = 7
MIN_STEPS = 1
HEADLINE_MAX_CHARS = 50
BODY_MAX_CHARS = 150
ACTION_LABEL_MAX_CHARS = 25

# Valid step types
VALID_STEP_TYPES = [
    'welcome', 'setup-required', 'setup-optional',
    'education', 'activation', 'completion'
]


def validate_step(step: dict, step_num: int) -> list:
    """Validate a single onboarding step."""
    errors = []
    
    # Check headline
    headline = step.get('headline')
    if not headline:
        errors.append(f'Step {step_num}: Missing headline')
    elif len(headline) > HEADLINE_MAX_CHARS:
        errors.append(
            f'Step {step_num}: Headline too long ({len(headline)} chars, '
            f'max {HEADLINE_MAX_CHARS})'
        )
    
    # Check body
    body = step.get('body')
    if body and len(body) > BODY_MAX_CHARS:
        errors.append(
            f'Step {step_num}: Body too long ({len(body)} chars, '
            f'max {BODY_MAX_CHARS})'
        )
    
    # Check action
    action = step.get('action')
    if action:
        label = action.get('label')
        if label and len(label) > ACTION_LABEL_MAX_CHARS:
            errors.append(
                f'Step {step_num}: Action label too long ({len(label)} chars, '
                f'max {ACTION_LABEL_MAX_CHARS})'
            )
    
    return errors


def validate_flow(data: dict) -> list:
    """Validate entire onboarding flow."""
    errors = []
    
    flow = data.get('onboarding_flow', data)
    
    # Check flow type
    flow_type = flow.get('type')
    if not flow_type:
        errors.append('Missing flow type')
    
    # Check steps exist
    steps = flow.get('steps', [])
    total_steps = flow.get('total_steps', len(steps))
    
    if not steps:
        errors.append('No steps defined')
        return errors
    
    # Check step count
    if len(steps) > MAX_STEPS:
        errors.append(
            f'Too many steps: {len(steps)} (max {MAX_STEPS}). '
            f'Consider breaking into sections.'
        )
    
    if total_steps != len(steps):
        errors.append(
            f'Step count mismatch: total_steps={total_steps}, '
            f'actual steps={len(steps)}'
        )
    
    # Validate each step
    for i, step in enumerate(steps, start=1):
        step_errors = validate_step(step, i)
        errors.extend(step_errors)
    
    # Check first step is welcoming
    first_step = steps[0]
    first_headline = first_step.get('headline', '').lower()
    welcome_words = ['welcome', 'get started', 'let\'s', 'set up']
    has_welcome_tone = any(w in first_headline for w in welcome_words)
    if not has_welcome_tone:
        errors.append(
            'First step should welcome user or set expectations. '
            f'Got: "{first_step.get("headline", "")}"'
        )
    
    # Check last step has completion feel
    last_step = steps[-1]
    last_headline = last_step.get('headline', '').lower()
    completion_words = ['done', 'set', 'ready', 'complete', 'finished', 'all set']
    has_completion = any(w in last_headline for w in completion_words)
    if len(steps) > 2 and not has_completion:
        errors.append(
            'Last step should confirm completion. Consider: '
            '"You\'re all set!", "Setup complete", etc.'
        )
    
    return errors


def main():
    parser = argparse.ArgumentParser(
        description='Validate onboarding flow structure'
    )
    parser.add_argument(
        'file',
        help='YAML file containing onboarding flow'
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
    
    errors = validate_flow(data)
    
    if errors:
        print('Validation FAILED:')
        for error in errors:
            print(f'  ✗ {error}')
        sys.exit(1)
    else:
        print('✓ Onboarding flow validation passed')
        sys.exit(0)


if __name__ == '__main__':
    main()
