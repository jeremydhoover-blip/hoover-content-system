#!/usr/bin/env python3
"""
Linter for jargon and forbidden phrases in error messages.
Checks text against forbidden patterns defined in reference/forbidden-phrases.md.

Usage:
    python lint_jargon.py <file_or_text>
    python lint_jargon.py --text "Your error message here"
    python lint_jargon.py --file messages.yaml
"""

import argparse
import re
import sys
from pathlib import Path

# Forbidden patterns with explanations
# Sourced from reference/forbidden-phrases.md
FORBIDDEN_PATTERNS = [
    # Technical jargon
    (r'\bexception\b', 'Avoid technical term "exception"'),
    (r'\bnull\b', 'Avoid programming literal "null"'),
    (r'\bundefined\b', 'Avoid programming literal "undefined"'),
    (r'\bNaN\b', 'Avoid programming literal "NaN"'),
    (r'\bstack\s*trace\b', 'Never expose stack traces'),
    (r'\bparse\s*error\b', 'Avoid technical term "parse error"'),
    (r'\bmalformed\b', 'Avoid technical term "malformed"'),
    (r'\bruntime\b', 'Avoid technical term "runtime"'),
    (r'\bdeprecated\b', 'Avoid technical term "deprecated"'),
    (r'\b[45]\d{2}\s*error\b', 'Avoid raw HTTP status codes'),
    (r'\berror\s*code\s*\d+\b', 'Avoid exposing error codes alone'),
    
    # Blame language
    (r'\byou\s+failed\b', 'Avoid blame language — rephrase without "you failed"'),
    (r'\byou\s+forgot\b', 'Avoid blame language — rephrase without "you forgot"'),
    (r'\byour\s+mistake\b', 'Avoid blame language'),
    (r'\buser\s+error\b', 'Avoid blame language'),
    (r'\byou\s+should\s+have\b', 'Avoid condescending language'),
    (r'\byou\s+entered\s+invalid\b', 'Rephrase to "Enter a valid..."'),
    
    # Alarming language
    (r'\bFATAL\b', 'Avoid alarming language — describe impact calmly'),
    (r'\bCRITICAL\b', 'Avoid alarming language'),
    (r'\bDANGER\b', 'Avoid alarming language — use "Warning" if needed'),
    (r'\bURGENT\b', 'Avoid alarming language'),
    (r'!{2,}', 'Avoid multiple exclamation points'),
    (r'\bimmediately\b', 'Often creates unnecessary pressure'),
    
    # Vague phrases (start/end anchored for standalone use)
    (r'^error$', 'Too vague — describe what error occurred'),
    (r'^failed$', 'Too vague — describe what failed'),
    (r'^invalid\s+input$', 'Too vague — specify which input'),
    (r'^bad\s+request$', 'Too vague and technical'),
    (r'^unknown\s+error$', 'Unhelpful — try "Something went wrong"'),
    (r'an\s+error\s+occurred', 'Too vague — describe what happened'),
    
    # Inappropriate tone
    (r'\boops\b', 'Avoid trivializing — remove "oops"'),
    (r'\bwhoops\b', 'Avoid trivializing — remove "whoops"'),
    (r'\buh\s*oh\b', 'Avoid trivializing — remove "uh oh"'),
    (r'\byikes\b', 'Avoid trivializing'),
    (r'\bbummer\b', 'Too casual for error messages'),
    (r'\bour\s+bad\b', 'Too casual — try "We\'re working on it"'),
    (r'\blol\b', 'Inappropriate for error messages'),
]


def lint_text(text: str) -> list:
    """Check text for forbidden patterns. Returns list of (pattern, message) tuples."""
    violations = []
    text_lower = text.lower()
    
    for pattern, message in FORBIDDEN_PATTERNS:
        flags = re.IGNORECASE
        if re.search(pattern, text, flags):
            violations.append((pattern, message))
    
    return violations


def lint_file(filepath: Path) -> dict:
    """Lint all text content in a file. Returns dict of line_number: violations."""
    results = {}
    
    with open(filepath, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, start=1):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            violations = lint_text(line)
            if violations:
                results[line_num] = {
                    'text': line[:80] + ('...' if len(line) > 80 else ''),
                    'violations': violations
                }
    
    return results


def main():
    parser = argparse.ArgumentParser(
        description='Lint error messages for jargon and forbidden phrases'
    )
    parser.add_argument(
        '--text',
        help='Text to lint directly'
    )
    parser.add_argument(
        '--file',
        help='File to lint'
    )
    parser.add_argument(
        'input',
        nargs='?',
        help='Text or file path to lint'
    )
    
    args = parser.parse_args()
    
    # Determine input source
    if args.text:
        text = args.text
        violations = lint_text(text)
        if violations:
            print(f'Linting: "{text[:60]}{"..." if len(text) > 60 else ""}"')
            print(f'\nFound {len(violations)} violation(s):')
            for pattern, message in violations:
                print(f'  ✗ {message}')
            sys.exit(1)
        else:
            print('✓ No forbidden patterns found')
            sys.exit(0)
    
    elif args.file or args.input:
        filepath = Path(args.file or args.input)
        if not filepath.exists():
            print(f'Error: File not found: {filepath}', file=sys.stderr)
            sys.exit(1)
        
        results = lint_file(filepath)
        if results:
            print(f'Found violations in {len(results)} line(s):\n')
            for line_num, data in results.items():
                print(f'Line {line_num}: {data["text"]}')
                for pattern, message in data['violations']:
                    print(f'  ✗ {message}')
                print()
            sys.exit(1)
        else:
            print(f'✓ No forbidden patterns found in {filepath}')
            sys.exit(0)
    
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()
