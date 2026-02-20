#!/usr/bin/env python3
"""
Validate MCP tool description quality.

Checks:
1. Tool name follows conventions (verb phrase, snake_case)
2. Description includes trigger condition
3. All parameters have descriptions with examples
4. Required parameters are specified
5. Side effects are documented for state-changing tools
6. Enum values have explanations

Usage:
    python validate_tool_description.py <tool_definition.json>
    
Exit codes:
    0 - All checks pass
    1 - Validation errors found
    2 - File not found or parse error
"""

import json
import re
import sys
from pathlib import Path


# Trigger phrases that indicate when-to-use guidance
# Justification: These phrases signal that the description tells the LLM when to invoke the tool
TRIGGER_PATTERNS = [
    r'\buse when\b',
    r'\buse to\b',
    r'\bcall this when\b',
    r'\binvoke when\b',
    r'\buse for\b',
]

# HTTP methods and keywords suggesting state-changing operations
# Justification: These operations have side effects that should be documented
STATE_CHANGING_INDICATORS = [
    'create', 'write', 'update', 'delete', 'remove', 'modify',
    'post', 'put', 'patch', 'send', 'execute', 'run',
]

# Words that suggest side effects exist
SIDE_EFFECT_KEYWORDS = ['warning', 'modifies', 'creates', 'deletes', 'sends', 'writes']


def validate_tool_name(name: str) -> list[str]:
    """Validate tool name conventions."""
    errors = []
    
    # Should be snake_case
    if not re.match(r'^[a-z][a-z0-9_]*$', name):
        errors.append(f"Tool name '{name}' should be snake_case (lowercase with underscores)")
    
    # Should start with a verb or be a clear action noun
    # This is a heuristic check
    if name.split('_')[0] in ['data', 'util', 'helper', 'misc', 'tool']:
        errors.append(f"Tool name '{name}' starts with vague word. Use action verb like 'get_', 'create_', 'search_'")
    
    return errors


def validate_description(description: str, tool_name: str) -> list[str]:
    """Validate tool description quality."""
    errors = []
    
    if not description:
        errors.append("Tool description is empty")
        return errors
    
    # Check for trigger condition
    desc_lower = description.lower()
    has_trigger = any(re.search(p, desc_lower) for p in TRIGGER_PATTERNS)
    if not has_trigger:
        errors.append("Description missing trigger condition (e.g., 'Use when...', 'Use to...')")
    
    # Check for side effect documentation on state-changing tools
    name_lower = tool_name.lower()
    is_state_changing = any(word in name_lower for word in STATE_CHANGING_INDICATORS)
    
    if is_state_changing:
        has_side_effect_doc = any(word in desc_lower for word in SIDE_EFFECT_KEYWORDS)
        if not has_side_effect_doc:
            errors.append("Tool appears to modify state but description lacks side effect warning")
    
    return errors


def validate_parameter(name: str, schema: dict) -> list[str]:
    """Validate individual parameter definition."""
    errors = []
    prefix = f"Parameter '{name}'"
    
    # Must have description
    if 'description' not in schema:
        errors.append(f"{prefix}: Missing description")
        return errors
    
    desc = schema['description']
    
    # Description should have example
    if 'example' not in desc.lower() and 'e.g.' not in desc.lower():
        errors.append(f"{prefix}: Description should include example value")
    
    # Enum values should have explanations
    if 'enum' in schema:
        enum_values = schema['enum']
        # Check if description explains the values
        has_explanations = all(
            str(v).lower() in desc.lower() or ':' in desc
            for v in enum_values[:3]  # Check first few
        )
        if not has_explanations and len(enum_values) > 1:
            errors.append(f"{prefix}: Enum values should have explanations in description")
    
    return errors


def validate_input_schema(schema: dict) -> list[str]:
    """Validate the inputSchema structure."""
    errors = []
    
    if not schema:
        errors.append("inputSchema is empty")
        return errors
    
    if schema.get('type') != 'object':
        errors.append("inputSchema type must be 'object'")
    
    properties = schema.get('properties', {})
    required = schema.get('required', [])
    
    # Validate each parameter
    for param_name, param_schema in properties.items():
        errors.extend(validate_parameter(param_name, param_schema))
    
    # Check that required parameters exist in properties
    for req in required:
        if req not in properties:
            errors.append(f"Required parameter '{req}' not defined in properties")
    
    # Check for vague parameter names
    vague_names = ['data', 'input', 'value', 'info', 'params', 'args']
    for param_name in properties:
        if param_name.lower() in vague_names:
            errors.append(f"Parameter name '{param_name}' is too vague. Use descriptive name.")
    
    return errors


def validate_tool(tool: dict) -> list[str]:
    """Validate complete tool definition."""
    errors = []
    
    # Check required fields
    if 'name' not in tool:
        errors.append("Missing 'name' field")
    else:
        errors.extend(validate_tool_name(tool['name']))
    
    if 'description' not in tool:
        errors.append("Missing 'description' field")
    else:
        errors.extend(validate_description(tool['description'], tool.get('name', '')))
    
    if 'inputSchema' not in tool:
        errors.append("Missing 'inputSchema' field")
    else:
        errors.extend(validate_input_schema(tool['inputSchema']))
    
    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python validate_tool_description.py <tool_definition.json>")
        return 2
    
    filepath = Path(sys.argv[1])
    if not filepath.exists():
        print(f"Error: File not found: {filepath}")
        return 2
    
    try:
        content = filepath.read_text(encoding='utf-8')
        tool = json.loads(content)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON: {e}")
        return 2
    except Exception as e:
        print(f"Error reading file: {e}")
        return 2
    
    errors = validate_tool(tool)
    
    print(f"Validating tool: {tool.get('name', '(unnamed)')}")
    
    if errors:
        print(f"\n{len(errors)} issue(s) found:\n")
        for error in errors:
            print(f"  ✗ {error}")
        return 1
    
    print("✓ Tool definition passes validation")
    return 0


if __name__ == "__main__":
    sys.exit(main())
