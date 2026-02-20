#!/usr/bin/env python3
"""
Validate code documentation quality.

Checks:
- Docstring presence for public elements
- Docstring format compliance
- Comment quality (not stating the obvious)
- TODO/FIXME formatting

Usage:
    python validate_documentation.py <source_file>
    python validate_documentation.py --dir <directory> --lang python

Exit codes:
    0 - All validations passed
    1 - Validation failures found
    2 - Invalid input
"""

import re
import sys
import argparse
import ast
from pathlib import Path
from dataclasses import dataclass
from typing import List, Optional

# Patterns indicating low-quality comments
OBVIOUS_COMMENT_PATTERNS = [
    r'#\s*(increment|decrement)\s+\w+',
    r'#\s*set\s+\w+\s+to',
    r'#\s*import',
    r'#\s*loop\s+(through|over)',
    r'#\s*if\s+\w+\s+is',
    r'#\s*return\s+\w+',
    r'#\s*create\s+(a\s+)?(new\s+)?instance',
    r'#\s*initialize',
    r'#\s*call\s+\w+',
]

# Patterns for bad docstring starts
BAD_DOCSTRING_STARTS = [
    r'^This\s+(function|method|class)',
    r'^A\s+(function|method|class)\s+(that|which|to)',
    r'^Function\s+(that|which|to)',
    r'^Method\s+(that|which|to)',
]

# Required TODO format
TODO_PATTERN = r'#\s*TODO(\([^)]+\))?:'


@dataclass
class DocIssue:
    line: int
    message: str
    severity: str = "warning"


class PythonDocValidator(ast.NodeVisitor):
    """AST visitor that checks Python docstrings."""
    
    def __init__(self, source_lines: List[str]):
        self.source_lines = source_lines
        self.issues: List[DocIssue] = []
    
    def visit_FunctionDef(self, node: ast.FunctionDef):
        self._check_function_doc(node)
        self.generic_visit(node)
    
    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef):
        self._check_function_doc(node)
        self.generic_visit(node)
    
    def visit_ClassDef(self, node: ast.ClassDef):
        self._check_class_doc(node)
        self.generic_visit(node)
    
    def _check_function_doc(self, node):
        # Skip private functions
        if node.name.startswith('_') and not node.name.startswith('__'):
            return
        
        docstring = ast.get_docstring(node)
        
        if not docstring:
            if not node.name.startswith('_'):
                self.issues.append(DocIssue(
                    node.lineno,
                    f"Public function '{node.name}' missing docstring",
                    "error"
                ))
            return
        
        # Check first line
        first_line = docstring.split('\n')[0]
        for pattern in BAD_DOCSTRING_STARTS:
            if re.match(pattern, first_line, re.IGNORECASE):
                self.issues.append(DocIssue(
                    node.lineno,
                    f"Docstring shouldn't start with '{first_line[:30]}...'",
                    "warning"
                ))
                break
        
        # Check for parameter documentation
        params = [arg.arg for arg in node.args.args if arg.arg != 'self']
        for param in params:
            if param not in docstring:
                self.issues.append(DocIssue(
                    node.lineno,
                    f"Parameter '{param}' not documented in '{node.name}'",
                    "warning"
                ))
        
        # Check for return documentation (if function returns something)
        has_return = any(
            isinstance(n, ast.Return) and n.value is not None
            for n in ast.walk(node)
        )
        if has_return and 'return' not in docstring.lower():
            self.issues.append(DocIssue(
                node.lineno,
                f"Return value not documented in '{node.name}'",
                "warning"
            ))
    
    def _check_class_doc(self, node):
        if node.name.startswith('_'):
            return
        
        docstring = ast.get_docstring(node)
        
        if not docstring:
            self.issues.append(DocIssue(
                node.lineno,
                f"Public class '{node.name}' missing docstring",
                "error"
            ))


def check_inline_comments(content: str) -> List[DocIssue]:
    """Check inline comments for quality issues."""
    issues = []
    lines = content.split('\n')
    
    for i, line in enumerate(lines, 1):
        # Skip docstrings
        if '"""' in line or "'''" in line:
            continue
        
        # Check for obvious comments
        for pattern in OBVIOUS_COMMENT_PATTERNS:
            if re.search(pattern, line, re.IGNORECASE):
                issues.append(DocIssue(
                    i,
                    f"Comment may be stating the obvious: {line.strip()[:50]}",
                    "warning"
                ))
                break
        
        # Check TODO format
        if re.search(r'#\s*TODO', line, re.IGNORECASE):
            if not re.search(TODO_PATTERN, line):
                issues.append(DocIssue(
                    i,
                    "TODO should follow format: # TODO(owner): description",
                    "warning"
                ))
        
        # Check for commented-out code (heuristic)
        comment_match = re.search(r'#\s*(.+)', line)
        if comment_match:
            comment_text = comment_match.group(1).strip()
            # Looks like code if it has common code patterns
            if re.match(r'^(if|for|while|def|class|return|import)\s', comment_text):
                issues.append(DocIssue(
                    i,
                    "Possible commented-out code - remove or explain",
                    "warning"
                ))
    
    return issues


def validate_python_file(filepath: Path) -> List[DocIssue]:
    """Run all validations on a Python file."""
    try:
        content = filepath.read_text(encoding='utf-8')
        tree = ast.parse(content)
    except SyntaxError as e:
        return [DocIssue(e.lineno or 0, f"Syntax error: {e}", "error")]
    except Exception as e:
        return [DocIssue(0, f"Could not parse file: {e}", "error")]
    
    lines = content.split('\n')
    
    # AST-based checks
    visitor = PythonDocValidator(lines)
    visitor.visit(tree)
    issues = visitor.issues
    
    # Line-based checks
    issues.extend(check_inline_comments(content))
    
    return issues


def main():
    parser = argparse.ArgumentParser(description='Validate code documentation')
    parser.add_argument('file', nargs='?', help='File to validate')
    parser.add_argument('--dir', help='Directory to validate recursively')
    parser.add_argument('--lang', default='python', choices=['python'],
                        help='Language (currently only Python supported)')
    args = parser.parse_args()
    
    if args.dir:
        if args.lang == 'python':
            files = list(Path(args.dir).rglob('*.py'))
        else:
            files = []
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
        
        issues = validate_python_file(filepath)
        
        if issues:
            print(f"\n{filepath}:")
            for issue in sorted(issues, key=lambda x: x.line):
                prefix = "ERROR" if issue.severity == "error" else "WARNING"
                print(f"  Line {issue.line}: [{prefix}] {issue.message}")
                if issue.severity == "error":
                    total_errors += 1
                else:
                    total_warnings += 1
    
    print(f"\n{'='*50}")
    print(f"Total: {total_errors} errors, {total_warnings} warnings")
    
    sys.exit(1 if total_errors > 0 else 0)


if __name__ == '__main__':
    main()
