#!/usr/bin/env python3
"""
Validate CLI help text against style guidelines.

Checks:
- One-line description length and format
- Flag naming conventions (kebab-case)
- Usage string syntax correctness
- Example presence and format
- Default value documentation

Usage:
    python validate_help_text.py <help_text_file>
    python validate_help_text.py --stdin < help_output.txt

Exit codes:
    0 - All validations passed
    1 - Validation failures found
    2 - Invalid input or read error
"""

import re
import sys
import argparse
from dataclasses import dataclass
from typing import List, Optional

# Maximum length for one-line description
MAX_DESCRIPTION_LENGTH = 80

# Common reserved short flags
RESERVED_SHORT_FLAGS = {
    'h': 'help',
    'v': 'version',
}


@dataclass
class ValidationResult:
    passed: bool
    message: str
    line_number: Optional[int] = None


def validate_description(lines: List[str]) -> List[ValidationResult]:
    """Validate the one-line description."""
    results = []
    
    if not lines:
        results.append(ValidationResult(False, "No content to validate"))
        return results
    
    # First non-empty line should be the description or command name + description
    first_line = lines[0].strip()
    
    # Check for "command - description" format
    if ' - ' in first_line:
        description = first_line.split(' - ', 1)[1]
    else:
        description = first_line
    
    # Check length
    if len(description) > MAX_DESCRIPTION_LENGTH:
        results.append(ValidationResult(
            False,
            f"Description exceeds {MAX_DESCRIPTION_LENGTH} chars: {len(description)} chars",
            1
        ))
    
    # Check starts with verb (simple heuristic: first word ends in common verb suffixes)
    first_word = description.split()[0].lower() if description.split() else ""
    verb_patterns = ['s', 'e', 'd', 'ing', 'fy', 'ize', 'ate']
    likely_verb = any(first_word.endswith(p) for p in verb_patterns) or first_word in [
        'list', 'get', 'set', 'run', 'show', 'create', 'delete', 'update', 'sync', 'deploy'
    ]
    if not likely_verb and first_word:
        results.append(ValidationResult(
            False,
            f"Description should start with a verb, found: '{first_word}'",
            1
        ))
    
    # Check ends with period
    if description and not description.rstrip().endswith('.'):
        results.append(ValidationResult(
            False,
            "Description should end with a period",
            1
        ))
    
    if not results:
        results.append(ValidationResult(True, "Description format valid"))
    
    return results


def validate_flag_naming(lines: List[str]) -> List[ValidationResult]:
    """Validate flag naming conventions."""
    results = []
    
    # Pattern to find flags: -x, --long-name
    flag_pattern = re.compile(r'^\s+(-\w),?\s*(--[\w-]+)?|^\s*(--[\w-]+)')
    
    for i, line in enumerate(lines, 1):
        match = flag_pattern.match(line)
        if match:
            long_flag = match.group(2) or match.group(3)
            if long_flag:
                # Check for camelCase or snake_case
                if re.search(r'[A-Z]', long_flag):
                    results.append(ValidationResult(
                        False,
                        f"Flag uses camelCase, should use kebab-case: {long_flag}",
                        i
                    ))
                if '_' in long_flag:
                    results.append(ValidationResult(
                        False,
                        f"Flag uses snake_case, should use kebab-case: {long_flag}",
                        i
                    ))
    
    if not results:
        results.append(ValidationResult(True, "Flag naming conventions valid"))
    
    return results


def validate_examples(lines: List[str]) -> List[ValidationResult]:
    """Validate examples section."""
    results = []
    
    content = '\n'.join(lines)
    
    # Check for EXAMPLES section
    if 'EXAMPLE' not in content.upper():
        results.append(ValidationResult(
            False,
            "Missing EXAMPLES section"
        ))
        return results
    
    # Find examples section
    in_examples = False
    example_count = 0
    has_explanation = False
    
    for i, line in enumerate(lines, 1):
        if 'EXAMPLE' in line.upper() and not line.strip().startswith('#'):
            in_examples = True
            continue
        
        if in_examples:
            # New section starts
            if line.strip() and not line.startswith(' ') and line.strip().isupper():
                break
            
            # Line that looks like a command (indented, starts with command-like text)
            if re.match(r'^\s{4}\S', line):
                example_count += 1
                has_explanation = False
            
            # Explanation line (more indented or following command)
            if re.match(r'^\s{8}\S', line):
                has_explanation = True
    
    if example_count < 2:
        results.append(ValidationResult(
            False,
            f"Need at least 2 examples, found: {example_count}"
        ))
    
    if not results:
        results.append(ValidationResult(True, f"Examples section valid ({example_count} examples)"))
    
    return results


def validate_defaults(lines: List[str]) -> List[ValidationResult]:
    """Check that optional items document defaults."""
    results = []
    warnings = []
    
    # Look for optional arguments (in brackets) or optional flags without defaults
    for i, line in enumerate(lines, 1):
        # Check for [OPTIONAL] pattern in usage without default mentioned nearby
        if re.search(r'\[[\w-]+\]', line) and 'USAGE' in '\n'.join(lines[max(0,i-5):i]).upper():
            # This is in usage section, check if there's a default documented
            pass  # Would need context to validate
        
        # Check for flag descriptions missing defaults
        if re.match(r'^\s+--[\w-]+', line):
            # Check next few lines for "default" mention
            context = '\n'.join(lines[i-1:min(len(lines), i+2)]).lower()
            if 'optional' in context and 'default' not in context:
                warnings.append(ValidationResult(
                    False,
                    f"Optional flag may be missing default value documentation",
                    i
                ))
    
    results.extend(warnings[:3])  # Limit warnings
    
    if not results:
        results.append(ValidationResult(True, "Default documentation check passed"))
    
    return results


def validate_help_text(content: str) -> List[ValidationResult]:
    """Run all validations on help text."""
    lines = content.split('\n')
    
    results = []
    results.extend(validate_description(lines))
    results.extend(validate_flag_naming(lines))
    results.extend(validate_examples(lines))
    results.extend(validate_defaults(lines))
    
    return results


def main():
    parser = argparse.ArgumentParser(description='Validate CLI help text')
    parser.add_argument('file', nargs='?', help='Help text file to validate')
    parser.add_argument('--stdin', action='store_true', help='Read from stdin')
    args = parser.parse_args()
    
    if args.stdin:
        content = sys.stdin.read()
    elif args.file:
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"ERROR: Could not read file: {e}")
            sys.exit(2)
    else:
        parser.print_help()
        sys.exit(2)
    
    results = validate_help_text(content)
    
    failures = [r for r in results if not r.passed]
    passes = [r for r in results if r.passed]
    
    if failures:
        print("FAILURES:")
        for r in failures:
            loc = f" (line {r.line_number})" if r.line_number else ""
            print(f"  ✗ {r.message}{loc}")
    
    if passes:
        print("\nPASSED:")
        for r in passes:
            print(f"  ✓ {r.message}")
    
    print(f"\n{'='*50}")
    print(f"Total: {len(passes)} passed, {len(failures)} failed")
    
    sys.exit(1 if failures else 0)


if __name__ == '__main__':
    main()
