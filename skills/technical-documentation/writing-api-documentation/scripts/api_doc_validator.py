#!/usr/bin/env python3
"""
Validate API documentation completeness and consistency.

Checks:
- Required sections present
- Parameter tables have required columns
- Examples are syntactically valid JSON
- HTTP methods and paths are documented
- Response documentation exists

Usage:
    python api_doc_validator.py <path-to-markdown-file>

Exit codes:
    0 — All checks pass
    1 — Validation errors found
    2 — File not found or unreadable
"""

import sys
import re
import json
from pathlib import Path
from typing import Optional

# Required sections for endpoint documentation
REQUIRED_SECTIONS = ["Endpoint", "Authentication", "Response", "Example"]

# Required columns in parameter tables
PARAMETER_TABLE_COLUMNS = {"Parameter", "Field", "Type"}

# Valid HTTP methods
HTTP_METHODS = {"GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS"}


def extract_sections(content: str) -> dict[str, str]:
    """Extract sections by H2 headings."""
    sections = {}
    current_section = None
    current_content = []
    
    for line in content.splitlines():
        if line.startswith("## "):
            if current_section:
                sections[current_section] = "\n".join(current_content)
            current_section = line[3:].strip()
            current_content = []
        elif current_section:
            current_content.append(line)
    
    if current_section:
        sections[current_section] = "\n".join(current_content)
    
    return sections


def validate_required_sections(sections: dict[str, str]) -> list[str]:
    """Check that required sections exist."""
    errors = []
    for section in REQUIRED_SECTIONS:
        if section not in sections:
            errors.append(f"Missing required section: '{section}'")
    return errors


def validate_endpoint_format(sections: dict[str, str]) -> list[str]:
    """Validate endpoint section has method and path."""
    errors = []
    endpoint_content = sections.get("Endpoint", "")
    
    # Look for pattern like `GET /path` or `POST /path/to/resource`
    method_path_pattern = r"`(GET|POST|PUT|PATCH|DELETE|HEAD|OPTIONS)\s+/[^`]+`"
    
    if not re.search(method_path_pattern, endpoint_content):
        errors.append("Endpoint section must contain HTTP method and path in format `METHOD /path`")
    
    return errors


def extract_json_blocks(content: str) -> list[tuple[str, int]]:
    """Extract JSON code blocks with their line numbers."""
    blocks = []
    in_json_block = False
    block_content = []
    block_start = 0
    
    for i, line in enumerate(content.splitlines(), start=1):
        if line.strip() == "```json":
            in_json_block = True
            block_start = i
            block_content = []
        elif line.strip() == "```" and in_json_block:
            in_json_block = False
            blocks.append(("\n".join(block_content), block_start))
        elif in_json_block:
            block_content.append(line)
    
    return blocks


def validate_json_blocks(content: str) -> list[str]:
    """Validate that JSON code blocks are syntactically valid."""
    errors = []
    json_blocks = extract_json_blocks(content)
    
    for block_content, line_num in json_blocks:
        try:
            json.loads(block_content)
        except json.JSONDecodeError as e:
            errors.append(f"Invalid JSON at line {line_num}: {e.msg}")
    
    return errors


def validate_parameter_tables(content: str) -> list[str]:
    """Validate parameter tables have required columns."""
    errors = []
    
    # Find markdown tables
    table_pattern = r"\|([^|]+\|)+\n\|[-:|]+\|"
    tables = re.finditer(table_pattern, content)
    
    for match in tables:
        header_line = match.group(0).split("\n")[0]
        headers = {h.strip() for h in header_line.split("|") if h.strip()}
        
        # Check if this looks like a parameter table
        if headers & {"Parameter", "Field"}:
            if "Type" not in headers:
                errors.append("Parameter table missing 'Type' column")
    
    return errors


def validate_example_section(sections: dict[str, str]) -> list[str]:
    """Validate example section contains curl command or code."""
    errors = []
    example_content = sections.get("Example", "")
    
    # Look for curl command or code block
    has_curl = "curl" in example_content.lower()
    has_code_block = "```" in example_content
    
    if not (has_curl or has_code_block):
        errors.append("Example section must contain a curl command or code example")
    
    return errors


def validate_file(filepath: Path) -> tuple[bool, list[str]]:
    """Run all validations on a file."""
    try:
        content = filepath.read_text(encoding="utf-8")
    except FileNotFoundError:
        return False, [f"File not found: {filepath}"]
    except Exception as e:
        return False, [f"Error reading file: {e}"]
    
    sections = extract_sections(content)
    
    all_errors = []
    all_errors.extend(validate_required_sections(sections))
    all_errors.extend(validate_endpoint_format(sections))
    all_errors.extend(validate_json_blocks(content))
    all_errors.extend(validate_parameter_tables(content))
    all_errors.extend(validate_example_section(sections))
    
    return len(all_errors) == 0, all_errors


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <path-to-markdown-file>")
        sys.exit(2)
    
    filepath = Path(sys.argv[1])
    passed, errors = validate_file(filepath)
    
    if passed:
        print(f"✓ {filepath.name}: All API documentation checks passed")
        sys.exit(0)
    else:
        print(f"✗ {filepath.name}: {len(errors)} error(s) found")
        for error in errors:
            print(f"  - {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
