#!/usr/bin/env python3
"""
Validate SDK documentation code samples for completeness and consistency.

Checks:
- Code blocks have language specifier
- Samples include import statements
- Placeholder patterns are consistent
- Required comments are present for complex samples
- Parameter tables follow required format

Usage:
    python validate_code_samples.py <markdown_file>
    python validate_code_samples.py --dir <directory>

Exit codes:
    0 - All validations passed
    1 - Validation failures found
    2 - File not found or read error
"""

import re
import sys
import argparse
from pathlib import Path
from dataclasses import dataclass
from typing import List, Tuple

# Minimum lines for a sample to require a purpose comment
MIN_LINES_FOR_PURPOSE_COMMENT = 5

# Languages that require import statements
LANGUAGES_REQUIRING_IMPORTS = {
    'python', 'javascript', 'typescript', 'java', 'go', 'csharp', 'cs', 'rust'
}

# Valid placeholder patterns (uppercase with underscores or kebab-case)
PLACEHOLDER_PATTERNS = [
    r'YOUR_[A-Z_]+',           # YOUR_API_KEY
    r'your-[a-z-]+',           # your-bucket-name
    r'sk_test_[a-z]+',         # sk_test_xxx
    r'tok_[a-z]+',             # tok_visa
    r'[a-z]+@example\.com',    # user@example.com
]

# Banned comment patterns (too obvious)
BANNED_COMMENTS = [
    r'//\s*[Cc]reate\s+(a\s+)?client',
    r'//\s*[Ii]mport',
    r'//\s*[Ss]et\s+\w+\s+to',
    r'//\s*[Dd]efine\s+variable',
    r'#\s*[Cc]reate\s+(a\s+)?client',
    r'#\s*[Ii]mport',
]


@dataclass
class ValidationError:
    line_number: int
    message: str
    severity: str  # 'error' or 'warning'


def extract_code_blocks(content: str) -> List[Tuple[int, str, str]]:
    """Extract code blocks with line numbers, language, and content."""
    blocks = []
    lines = content.split('\n')
    in_block = False
    block_start = 0
    block_lang = ''
    block_content = []
    
    for i, line in enumerate(lines, 1):
        if line.startswith('```') and not in_block:
            in_block = True
            block_start = i
            block_lang = line[3:].strip().lower()
            block_content = []
        elif line.startswith('```') and in_block:
            in_block = False
            blocks.append((block_start, block_lang, '\n'.join(block_content)))
        elif in_block:
            block_content.append(line)
    
    return blocks


def validate_language_specifier(blocks: List[Tuple[int, str, str]]) -> List[ValidationError]:
    """Check that all code blocks have language specifiers."""
    errors = []
    for line_num, lang, _ in blocks:
        if not lang:
            errors.append(ValidationError(
                line_num,
                "Code block missing language specifier",
                "error"
            ))
    return errors


def validate_imports(blocks: List[Tuple[int, str, str]]) -> List[ValidationError]:
    """Check that code samples include import statements where expected."""
    errors = []
    import_patterns = {
        'python': r'^(from|import)\s+',
        'javascript': r'^(import|const|let|var)\s+.*require|^import\s+',
        'typescript': r'^import\s+',
        'java': r'^import\s+',
        'go': r'^import\s+',
        'csharp': r'^using\s+',
        'cs': r'^using\s+',
        'rust': r'^use\s+',
    }
    
    for line_num, lang, content in blocks:
        if lang not in LANGUAGES_REQUIRING_IMPORTS:
            continue
        
        lines = [l for l in content.split('\n') if l.strip() and not l.strip().startswith('//') and not l.strip().startswith('#')]
        
        # Skip very short samples (likely fragments)
        if len(lines) < 3:
            continue
        
        pattern = import_patterns.get(lang)
        if pattern and not any(re.match(pattern, line.strip()) for line in lines[:10]):
            errors.append(ValidationError(
                line_num,
                f"Code sample appears to be missing import statements for {lang}",
                "warning"
            ))
    
    return errors


def validate_placeholders(blocks: List[Tuple[int, str, str]]) -> List[ValidationError]:
    """Check placeholder patterns are consistent."""
    errors = []
    
    # Bad placeholder patterns
    bad_patterns = [
        (r"'test'", "Use descriptive placeholder like 'your-resource-name'"),
        (r'"test"', "Use descriptive placeholder like 'your-resource-name'"),
        (r"'xxx'", "Use specific placeholder pattern"),
        (r'"xxx"', "Use specific placeholder pattern"),
        (r"api[_-]?key\s*=\s*['\"][^Y]", "API key should use YOUR_API_KEY pattern"),
    ]
    
    for line_num, lang, content in blocks:
        for pattern, message in bad_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                errors.append(ValidationError(
                    line_num,
                    message,
                    "warning"
                ))
                break  # One warning per block
    
    return errors


def validate_comments(blocks: List[Tuple[int, str, str]]) -> List[ValidationError]:
    """Check for banned obvious comments and required purpose comments."""
    errors = []
    
    for line_num, lang, content in blocks:
        lines = content.split('\n')
        
        # Check for banned obvious comments
        for i, line in enumerate(lines):
            for pattern in BANNED_COMMENTS:
                if re.search(pattern, line):
                    errors.append(ValidationError(
                        line_num + i,
                        f"Obvious comment detected: '{line.strip()}' - remove or make more specific",
                        "warning"
                    ))
        
        # Check for purpose comment on longer samples
        code_lines = [l for l in lines if l.strip()]
        if len(code_lines) >= MIN_LINES_FOR_PURPOSE_COMMENT:
            first_line = code_lines[0].strip() if code_lines else ''
            if not (first_line.startswith('//') or first_line.startswith('#') or first_line.startswith('/*')):
                errors.append(ValidationError(
                    line_num,
                    f"Sample with {len(code_lines)} lines should start with a purpose comment",
                    "warning"
                ))
    
    return errors


def validate_parameter_tables(content: str) -> List[ValidationError]:
    """Check parameter tables have required columns."""
    errors = []
    lines = content.split('\n')
    
    # Find table headers
    for i, line in enumerate(lines, 1):
        if '| Parameter |' in line or '| parameter |' in line.lower():
            # Check for required columns
            required_cols = ['type', 'required', 'description']
            line_lower = line.lower()
            for col in required_cols:
                if col not in line_lower:
                    errors.append(ValidationError(
                        i,
                        f"Parameter table missing '{col}' column",
                        "error"
                    ))
    
    return errors


def validate_file(filepath: Path) -> List[ValidationError]:
    """Run all validations on a file."""
    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception as e:
        return [ValidationError(0, f"Could not read file: {e}", "error")]
    
    blocks = extract_code_blocks(content)
    
    errors = []
    errors.extend(validate_language_specifier(blocks))
    errors.extend(validate_imports(blocks))
    errors.extend(validate_placeholders(blocks))
    errors.extend(validate_comments(blocks))
    errors.extend(validate_parameter_tables(content))
    
    return errors


def main():
    parser = argparse.ArgumentParser(description='Validate SDK documentation code samples')
    parser.add_argument('file', nargs='?', help='Markdown file to validate')
    parser.add_argument('--dir', help='Directory to validate recursively')
    args = parser.parse_args()
    
    if args.dir:
        files = list(Path(args.dir).rglob('*.md'))
    elif args.file:
        files = [Path(args.file)]
    else:
        parser.print_help()
        sys.exit(2)
    
    total_errors = 0
    total_warnings = 0
    
    for filepath in files:
        if not filepath.exists():
            print(f"ERROR: File not found: {filepath}")
            sys.exit(2)
        
        errors = validate_file(filepath)
        if errors:
            print(f"\n{filepath}:")
            for error in errors:
                prefix = "ERROR" if error.severity == "error" else "WARNING"
                print(f"  Line {error.line_number}: [{prefix}] {error.message}")
                if error.severity == "error":
                    total_errors += 1
                else:
                    total_warnings += 1
    
    print(f"\n{'='*50}")
    print(f"Total: {total_errors} errors, {total_warnings} warnings")
    
    if total_errors > 0:
        sys.exit(1)
    sys.exit(0)


if __name__ == '__main__':
    main()
