#!/usr/bin/env python3
"""
Validate configuration documentation completeness.

Checks:
1. All parameters have required fields (type, description, example)
2. Optional parameters have defaults documented
3. Security-sensitive parameters have handling guidance
4. Constraints are documented where patterns suggest they should exist

Usage:
    python validate_config_docs.py <config_doc.md>
    
Exit codes:
    0 - All checks pass
    1 - Validation errors found
    2 - File not found or parse error
"""

import re
import sys
from pathlib import Path
from dataclasses import dataclass
from typing import Optional


@dataclass
class Parameter:
    """Represents a documented configuration parameter."""
    name: str
    line_number: int
    has_type: bool = False
    has_description: bool = False
    has_example: bool = False
    has_default: bool = False
    has_constraints: bool = False
    is_required: bool = False
    is_security_sensitive: bool = False
    has_secure_handling: bool = False


# Patterns that suggest constraints should be documented
# Justification: These types typically have valid ranges or formats
CONSTRAINT_INDICATORS = {
    'port': (1, 65535),
    'timeout': 'positive integer',
    'count': 'non-negative integer',
    'size': 'positive integer with optional unit',
    'percentage': (0, 100),
}

# Patterns indicating security-sensitive parameters
# Justification: These terms commonly appear in secret parameter names
SECURITY_PATTERNS = [
    r'password',
    r'secret',
    r'api[_-]?key',
    r'token',
    r'credential',
    r'private[_-]?key',
    r'auth',
]


def parse_parameters(content: str) -> list[Parameter]:
    """Extract parameters from markdown configuration documentation."""
    parameters = []
    lines = content.split('\n')
    current_param: Optional[Parameter] = None
    in_required_section = False
    in_security_section = False
    
    for i, line in enumerate(lines, 1):
        # Track sections
        if re.match(r'^##\s+Required', line, re.IGNORECASE):
            in_required_section = True
            in_security_section = False
        elif re.match(r'^##\s+Optional', line, re.IGNORECASE):
            in_required_section = False
            in_security_section = False
        elif re.match(r'^##\s+Security', line, re.IGNORECASE):
            in_security_section = True
            in_required_section = False
        elif re.match(r'^##\s+', line):
            in_required_section = False
            in_security_section = False
        
        # Detect parameter heading (### `param_name`)
        param_match = re.match(r'^###\s+`([^`]+)`', line)
        if param_match:
            if current_param:
                parameters.append(current_param)
            current_param = Parameter(
                name=param_match.group(1),
                line_number=i,
                is_required=in_required_section,
                is_security_sensitive=in_security_section or any(
                    re.search(p, param_match.group(1), re.IGNORECASE) 
                    for p in SECURITY_PATTERNS
                )
            )
            continue
        
        if current_param:
            # Check for required fields
            if re.match(r'^-\s+\*\*Type\*\*:', line):
                current_param.has_type = True
            elif re.match(r'^-\s+\*\*Description\*\*:', line):
                current_param.has_description = True
            elif re.match(r'^-\s+\*\*Example\*\*:', line):
                current_param.has_example = True
            elif re.match(r'^-\s+\*\*Default\*\*:', line):
                current_param.has_default = True
            elif re.match(r'^-\s+\*\*Constraints?\*\*:', line):
                current_param.has_constraints = True
            elif re.match(r'^-\s+\*\*Secure handling\*\*:', line):
                current_param.has_secure_handling = True
    
    if current_param:
        parameters.append(current_param)
    
    return parameters


def needs_constraints(param_name: str) -> bool:
    """Determine if parameter name suggests constraints should be documented."""
    name_lower = param_name.lower()
    return any(indicator in name_lower for indicator in CONSTRAINT_INDICATORS)


def validate_parameters(parameters: list[Parameter]) -> list[str]:
    """Validate parameters against documentation requirements."""
    errors = []
    
    for param in parameters:
        prefix = f"Line {param.line_number}, `{param.name}`"
        
        # All parameters must have type
        if not param.has_type:
            errors.append(f"{prefix}: Missing **Type** field")
        
        # All parameters must have description
        if not param.has_description:
            errors.append(f"{prefix}: Missing **Description** field")
        
        # All parameters must have example (unless security-sensitive)
        if not param.has_example and not param.is_security_sensitive:
            errors.append(f"{prefix}: Missing **Example** field")
        
        # Optional parameters must have default
        if not param.is_required and not param.has_default:
            errors.append(f"{prefix}: Optional parameter missing **Default** field")
        
        # Security-sensitive parameters must have secure handling
        if param.is_security_sensitive and not param.has_secure_handling:
            errors.append(f"{prefix}: Security-sensitive parameter missing **Secure handling** field")
        
        # Parameters with typical constraints should document them
        if needs_constraints(param.name) and not param.has_constraints:
            errors.append(f"{prefix}: Parameter name suggests constraints should be documented")
    
    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python validate_config_docs.py <config_doc.md>")
        return 2
    
    filepath = Path(sys.argv[1])
    if not filepath.exists():
        print(f"Error: File not found: {filepath}")
        return 2
    
    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception as e:
        print(f"Error reading file: {e}")
        return 2
    
    parameters = parse_parameters(content)
    
    if not parameters:
        print("Warning: No parameters found in document")
        print("Expected format: ### `parameter_name`")
        return 1
    
    errors = validate_parameters(parameters)
    
    print(f"Validated {len(parameters)} parameters")
    
    if errors:
        print(f"\n{len(errors)} error(s) found:\n")
        for error in errors:
            print(f"  ✗ {error}")
        return 1
    
    print("✓ All parameters pass validation")
    return 0


if __name__ == "__main__":
    sys.exit(main())
