#!/usr/bin/env python3
"""
Validate tooling workflow documentation completeness.

Checks:
1. All steps have commands, expected output, and troubleshooting
2. Prerequisites include verification commands
3. Workflow diagram exists for complex workflows
4. Rollback procedure exists
5. Verification step exists

Usage:
    python validate_workflow_docs.py <workflow_doc.md>
    
Exit codes:
    0 - All checks pass
    1 - Validation errors found
    2 - File not found or parse error
"""

import re
import sys
from pathlib import Path
from dataclasses import dataclass, field


@dataclass
class WorkflowStep:
    """Represents a documented workflow step."""
    name: str
    line_number: int
    has_command: bool = False
    has_expected_output: bool = False
    has_troubleshooting: bool = False


@dataclass
class WorkflowDoc:
    """Represents a workflow documentation structure."""
    has_overview: bool = False
    has_prerequisites: bool = False
    has_tool_versions: bool = False
    has_verification_commands: bool = False
    has_workflow_diagram: bool = False
    has_rollback: bool = False
    has_final_verification: bool = False
    steps: list = field(default_factory=list)


# Minimum step count that requires a diagram
# Justification: Simple workflows (1-3 steps) are clear without diagrams
MIN_STEPS_FOR_DIAGRAM = 4


def parse_workflow_doc(content: str) -> WorkflowDoc:
    """Parse workflow documentation and extract structure."""
    doc = WorkflowDoc()
    lines = content.split('\n')
    current_step = None
    
    for i, line in enumerate(lines, 1):
        line_lower = line.lower()
        
        # Check top-level sections
        if re.match(r'^##\s+overview', line_lower):
            doc.has_overview = True
        elif re.match(r'^##\s+prerequisite', line_lower):
            doc.has_prerequisites = True
        elif re.match(r'^##\s+(workflow diagram|diagram|flow)', line_lower):
            doc.has_workflow_diagram = True
        elif re.match(r'^##\s+rollback', line_lower):
            doc.has_rollback = True
        elif re.match(r'^##\s+(verification|final verification|verify)', line_lower):
            doc.has_final_verification = True
        
        # Check for tool version table
        if '| tool |' in line_lower and 'version' in line_lower:
            doc.has_tool_versions = True
        
        # Check for verification commands in prerequisites
        if doc.has_prerequisites and ('verify' in line_lower or 'check' in line_lower):
            if '`' in line and ('--version' in line or '-v' in line or 'which' in line):
                doc.has_verification_commands = True
        
        # Check for workflow diagram content (ASCII or Mermaid)
        if '→' in line or '->' in line or '──►' in line:
            doc.has_workflow_diagram = True
        if '```mermaid' in line_lower:
            doc.has_workflow_diagram = True
        
        # Detect step headings (### Step N: or ### N. or ### <action verb>)
        step_match = re.match(r'^###\s+(step\s+\d+|[0-9]+\.|\w+ing\s)', line_lower)
        if step_match and 'troubleshoot' not in line_lower:
            if current_step:
                doc.steps.append(current_step)
            current_step = WorkflowStep(
                name=line.strip('#').strip(),
                line_number=i
            )
            continue
        
        if current_step:
            # Check for command block
            if re.match(r'^\*\*command', line_lower) or re.match(r'^```(bash|sh|powershell|cmd)', line):
                current_step.has_command = True
            # Check for expected output
            if re.match(r'^\*\*expected', line_lower):
                current_step.has_expected_output = True
            # Check for troubleshooting
            if re.match(r'^\*\*troubleshoot', line_lower) or re.match(r'^-\s+if\s+`', line_lower):
                current_step.has_troubleshooting = True
    
    if current_step:
        doc.steps.append(current_step)
    
    return doc


def validate_workflow(doc: WorkflowDoc) -> list[str]:
    """Validate workflow documentation against requirements."""
    errors = []
    
    # Top-level structure checks
    if not doc.has_overview:
        errors.append("Missing '## Overview' section")
    
    if not doc.has_prerequisites:
        errors.append("Missing '## Prerequisites' section")
    
    if doc.has_prerequisites and not doc.has_tool_versions:
        errors.append("Prerequisites should include tool version table with minimum versions")
    
    if doc.has_prerequisites and not doc.has_verification_commands:
        errors.append("Prerequisites should include verification commands (e.g., `tool --version`)")
    
    # Diagram check for complex workflows
    if len(doc.steps) >= MIN_STEPS_FOR_DIAGRAM and not doc.has_workflow_diagram:
        errors.append(f"Workflow has {len(doc.steps)} steps but no workflow diagram (required for {MIN_STEPS_FOR_DIAGRAM}+ steps)")
    
    # Rollback check
    if not doc.has_rollback:
        errors.append("Missing '## Rollback' section")
    
    # Final verification check
    if not doc.has_final_verification:
        errors.append("Missing '## Verification' section (end-to-end check)")
    
    # Per-step checks
    for step in doc.steps:
        prefix = f"Line {step.line_number}, '{step.name}'"
        
        if not step.has_command:
            errors.append(f"{prefix}: Missing command block")
        
        if not step.has_expected_output:
            errors.append(f"{prefix}: Missing expected output")
        
        if not step.has_troubleshooting:
            errors.append(f"{prefix}: Missing troubleshooting guidance")
    
    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python validate_workflow_docs.py <workflow_doc.md>")
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
    
    doc = parse_workflow_doc(content)
    
    print(f"Found {len(doc.steps)} workflow steps")
    
    errors = validate_workflow(doc)
    
    if errors:
        print(f"\n{len(errors)} issue(s) found:\n")
        for error in errors:
            print(f"  ✗ {error}")
        return 1
    
    print("✓ Workflow documentation passes validation")
    return 0


if __name__ == "__main__":
    sys.exit(main())
