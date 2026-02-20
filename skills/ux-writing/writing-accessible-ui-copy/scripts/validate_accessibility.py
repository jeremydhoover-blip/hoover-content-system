#!/usr/bin/env python3
"""
Validator for accessible UI copy.
Checks alt text, link text, labels, and heading structure.

Usage:
    python validate_accessibility.py <yaml_file>
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
ALT_TEXT_MAX_CHARS = 150
LINK_TEXT_MAX_CHARS = 100
LABEL_MAX_CHARS = 50

# Anti-patterns
ALT_ANTI_PATTERNS = {
    'image_of': re.compile(r'^(image|photo|picture|graphic|icon)\s+(of|showing)\s+', re.I),
    'filename': re.compile(r'\.(jpg|jpeg|png|gif|svg|webp)$', re.I),
    'placeholder': re.compile(r'^(image|photo|placeholder|untitled)$', re.I),
}

LINK_ANTI_PATTERNS = {
    'click_here': re.compile(r'^click\s*here$', re.I),
    'learn_more': re.compile(r'^learn\s*more$', re.I),
    'read_more': re.compile(r'^read\s*more$', re.I),
    'here': re.compile(r'^here$', re.I),
    'more': re.compile(r'^more$', re.I),
    'link': re.compile(r'^link$', re.I),
}

LABEL_ANTI_PATTERNS = {
    'click_to': re.compile(r'^click\s+(to|for)\s+', re.I),
    'please': re.compile(r'^please\s+', re.I),
}


def validate_alt_text(item: dict, name: str = '') -> list:
    """Validate image alt text."""
    errors = []
    identifier = name or item.get('id', 'Image')
    
    alt = item.get('alt', item.get('alt_text', ''))
    image_type = item.get('type', 'informative')
    
    # Decorative images should have empty alt
    if image_type == 'decorative':
        if alt and alt.strip():
            errors.append(
                f'{identifier}: Decorative images should have empty alt=""'
            )
        return errors
    
    # Informative images must have alt
    if not alt:
        errors.append(f'{identifier}: Missing alt text for informative image')
        return errors
    
    # Check length
    if len(alt) > ALT_TEXT_MAX_CHARS:
        errors.append(
            f'{identifier}: Alt text too long ({len(alt)} chars, '
            f'max {ALT_TEXT_MAX_CHARS}). Consider using aria-describedby '
            f'for complex images.'
        )
    
    # Check for anti-patterns
    if ALT_ANTI_PATTERNS['image_of'].match(alt):
        errors.append(
            f'{identifier}: Don\'t start alt text with "image of" or '
            f'"photo of". Just describe what\'s shown.'
        )
    
    if ALT_ANTI_PATTERNS['filename'].search(alt):
        errors.append(
            f'{identifier}: Alt text appears to be filename. '
            f'Describe the image content instead.'
        )
    
    if ALT_ANTI_PATTERNS['placeholder'].match(alt):
        errors.append(
            f'{identifier}: Generic alt text "{alt}". Be specific.'
        )
    
    return errors


def validate_link_text(item: dict, name: str = '') -> list:
    """Validate link text accessibility."""
    errors = []
    identifier = name or item.get('id', 'Link')
    
    text = item.get('text', item.get('label', ''))
    
    if not text:
        errors.append(f'{identifier}: Missing link text')
        return errors
    
    # Check length
    if len(text) > LINK_TEXT_MAX_CHARS:
        errors.append(
            f'{identifier}: Link text too long ({len(text)} chars)'
        )
    
    # Check for anti-patterns
    for pattern_name, pattern in LINK_ANTI_PATTERNS.items():
        if pattern.match(text):
            errors.append(
                f'{identifier}: Avoid "{text}" as link text. '
                f'Describe the destination instead.'
            )
            break
    
    return errors


def validate_label(item: dict, name: str = '') -> list:
    """Validate form/button labels."""
    errors = []
    identifier = name or item.get('id', 'Element')
    
    label = item.get('label', item.get('text', ''))
    
    if not label:
        errors.append(f'{identifier}: Missing label')
        return errors
    
    # Check length
    if len(label) > LABEL_MAX_CHARS:
        errors.append(
            f'{identifier}: Label too long ({len(label)} chars)'
        )
    
    # Check for anti-patterns
    for pattern_name, pattern in LABEL_ANTI_PATTERNS.items():
        if pattern.match(label):
            errors.append(
                f'{identifier}: Avoid "{pattern_name.replace("_", " ")}" '
                f'pattern in labels. Be direct.'
            )
    
    return errors


def validate_headings(headings: list) -> list:
    """Validate heading structure."""
    errors = []
    
    if not headings:
        return errors
    
    prev_level = 0
    h1_count = 0
    
    for i, heading in enumerate(headings):
        level = heading.get('level', 0)
        text = heading.get('text', '')
        
        # Extract level number if string like "h1", "h2"
        if isinstance(level, str):
            match = re.match(r'h(\d)', level.lower())
            if match:
                level = int(match.group(1))
            else:
                continue
        
        # Check h1 count
        if level == 1:
            h1_count += 1
            if h1_count > 1:
                errors.append(
                    f'Heading "{text}": Multiple h1 elements. '
                    f'Use only one h1 per page.'
                )
        
        # Check for skipped levels
        if prev_level > 0 and level > prev_level + 1:
            errors.append(
                f'Heading "{text}": Skipped from h{prev_level} to h{level}. '
                f'Don\'t skip heading levels.'
            )
        
        # Check for empty headings
        if not text or not text.strip():
            errors.append(f'Heading level {level}: Empty heading text')
        
        prev_level = level
    
    # Check for missing h1
    if h1_count == 0:
        errors.append('Missing h1 heading. Every page should have one h1.')
    
    return errors


def validate_accessibility(data: dict) -> list:
    """Validate accessibility content."""
    errors = []
    
    # Validate images/alt text
    images = data.get('images', data.get('alt_texts', []))
    if isinstance(images, list):
        for i, img in enumerate(images):
            name = img.get('id', img.get('name', f'Image {i+1}'))
            errors.extend(validate_alt_text(img, name))
    
    # Validate links
    links = data.get('links', [])
    if isinstance(links, list):
        for i, link in enumerate(links):
            name = link.get('id', f'Link {i+1}')
            errors.extend(validate_link_text(link, name))
    
    # Validate labels
    labels = data.get('labels', data.get('buttons', []))
    if isinstance(labels, list):
        for i, label in enumerate(labels):
            name = label.get('id', f'Element {i+1}')
            errors.extend(validate_label(label, name))
    
    # Validate headings
    headings = data.get('headings', [])
    if headings:
        errors.extend(validate_headings(headings))
    
    return errors


def main():
    parser = argparse.ArgumentParser(
        description='Validate accessible UI copy'
    )
    parser.add_argument(
        'file',
        help='YAML file containing accessibility content'
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
    
    errors = validate_accessibility(data)
    
    if errors:
        print('Validation FAILED:')
        for error in errors:
            print(f'  ✗ {error}')
        sys.exit(1)
    else:
        print('✓ Accessibility validation passed')
        sys.exit(0)


if __name__ == '__main__':
    main()
