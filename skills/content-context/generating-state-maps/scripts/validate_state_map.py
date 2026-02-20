#!/usr/bin/env python3
"""
Validate a state map document for completeness and structural integrity.

Usage:
    python validate_state_map.py <path-to-state-map.md>

Exit codes:
    0 - All validations passed
    1 - Validation errors found
    2 - File not found or unreadable
"""

import sys
import re
from pathlib import Path
from typing import NamedTuple
from collections import defaultdict

# --- Constants (justified) ---
# Minimum states for a meaningful feature: entry + at least one other
MIN_STATES = 2
# Minimum edge cases to document per repo requirements
MIN_EDGE_CASES = 2

VALID_STATE_TYPES = {
    'standard', 'error', 'loading', 'empty', 
    'success', 'permission', 'edge'
}

REQUIRED_STATE_SECTIONS = [
    'Type', 'Description', 'Entry triggers', 'Content requirements'
]


class ValidationResult(NamedTuple):
    passed: bool
    message: str


def extract_states_from_diagram(content: str) -> set[str]:
    """Extract state names from Mermaid diagram."""
    states = set()
    
    # Find mermaid block
    mermaid_match = re.search(r'```mermaid\s*\n(.*?)```', content, re.DOTALL)
    if not mermaid_match:
        return states
    
    mermaid_content = mermaid_match.group(1)
    
    # Extract states from transitions (state1 --> state2)
    transitions = re.findall(r'(\w+)\s*-->', mermaid_content)
    states.update(transitions)
    
    targets = re.findall(r'-->\s*(\w+)', mermaid_content)
    states.update(targets)
    
    # Remove special markers
    states.discard('*')  # [*] start/end marker
    
    return states


def extract_documented_states(content: str) -> dict[str, dict]:
    """Extract state details from documentation sections."""
    states = {}
    
    # Find all ### State sections
    state_sections = re.findall(
        r'###\s+([^\n]+)\n(.*?)(?=###|\n## |$)', 
        content, 
        re.DOTALL
    )
    
    for name, body in state_sections:
        name = name.strip()
        if name.lower() in ['change', 'overview']:  # Skip non-state sections
            continue
        
        state_info = {
            'type': None,
            'has_entry_triggers': False,
            'has_exit_transitions': False,
            'has_content_requirements': False,
            'exit_targets': []
        }
        
        # Extract type
        type_match = re.search(r'\*\*Type:\*\*\s*(\w+)', body)
        if type_match:
            state_info['type'] = type_match.group(1).lower()
        
        # Check for required sections
        state_info['has_entry_triggers'] = '**Entry triggers:**' in body
        state_info['has_exit_transitions'] = '**Exit transitions:**' in body or 'Exit transitions' in body
        state_info['has_content_requirements'] = '**Content requirements:**' in body
        
        # Extract exit transition targets
        exit_section = re.search(r'\*\*Exit transitions:\*\*\s*(.*?)(?=\*\*|\n###|$)', body, re.DOTALL)
        if exit_section:
            targets = re.findall(r'→\s*(\w+):', exit_section.group(1))
            state_info['exit_targets'] = targets
        
        states[name] = state_info
    
    return states


def validate_overview(content: str) -> list[ValidationResult]:
    """Validate overview section."""
    results = []
    
    if '## Overview' not in content:
        results.append(ValidationResult(False, "Missing '## Overview' section"))
        return results
    
    results.append(ValidationResult(True, "Overview section present"))
    
    # Check entry state
    if not re.search(r'\*\*Entry state:\*\*\s*\S+', content):
        results.append(ValidationResult(False, "Missing 'Entry state' in overview"))
    else:
        results.append(ValidationResult(True, "Entry state specified"))
    
    # Check terminal states
    if not re.search(r'\*\*Terminal states:\*\*', content):
        results.append(ValidationResult(False, "Missing 'Terminal states' in overview"))
    else:
        results.append(ValidationResult(True, "Terminal states specified"))
    
    return results


def validate_states(content: str) -> list[ValidationResult]:
    """Validate state definitions."""
    results = []
    
    diagram_states = extract_states_from_diagram(content)
    documented_states = extract_documented_states(content)
    
    # Check minimum states
    total_states = len(documented_states)
    if total_states < MIN_STATES:
        results.append(ValidationResult(False, f"Need at least {MIN_STATES} states, found {total_states}"))
    else:
        results.append(ValidationResult(True, f"Found {total_states} documented states"))
    
    # Check diagram vs documentation consistency
    if diagram_states:
        missing_docs = diagram_states - set(documented_states.keys())
        if missing_docs:
            results.append(ValidationResult(False, f"States in diagram but not documented: {missing_docs}"))
        else:
            results.append(ValidationResult(True, "All diagram states are documented"))
    
    # Validate each state
    has_error_state = False
    has_loading_state = False
    
    for state_name, info in documented_states.items():
        # Check type
        if not info['type']:
            results.append(ValidationResult(False, f"State '{state_name}': Missing type"))
        elif info['type'] not in VALID_STATE_TYPES:
            results.append(ValidationResult(False, f"State '{state_name}': Invalid type '{info['type']}'"))
        else:
            if info['type'] == 'error':
                has_error_state = True
            if info['type'] == 'loading':
                has_loading_state = True
        
        # Check required sections
        if not info['has_entry_triggers']:
            results.append(ValidationResult(False, f"State '{state_name}': Missing entry triggers"))
        
        if not info['has_content_requirements']:
            results.append(ValidationResult(False, f"State '{state_name}': Missing content requirements"))
    
    # Check for required state types
    if not has_error_state:
        results.append(ValidationResult(False, "No error state documented — most features need error handling"))
    else:
        results.append(ValidationResult(True, "Error state(s) present"))
    
    return results


def validate_transitions(content: str) -> list[ValidationResult]:
    """Validate transition completeness."""
    results = []
    
    documented_states = extract_documented_states(content)
    
    # Build inbound transition map
    inbound = defaultdict(list)
    for state_name, info in documented_states.items():
        for target in info['exit_targets']:
            inbound[target].append(state_name)
    
    # Check entry state
    entry_match = re.search(r'\*\*Entry state:\*\*\s*(\S+)', content)
    entry_state = entry_match.group(1) if entry_match else None
    
    # Check for orphan states (except entry)
    for state_name in documented_states.keys():
        if state_name != entry_state and state_name not in inbound:
            results.append(ValidationResult(False, f"State '{state_name}' has no inbound transitions (orphan)"))
    
    # Check for dead-end non-terminal states
    terminal_match = re.search(r'\*\*Terminal states:\*\*\s*([^\n]+)', content)
    terminal_states = []
    if terminal_match:
        terminal_text = terminal_match.group(1)
        if terminal_text.lower() != 'none':
            terminal_states = [s.strip() for s in terminal_text.split(',')]
    
    for state_name, info in documented_states.items():
        if state_name not in terminal_states and not info['exit_targets']:
            if info['has_exit_transitions']:  # Section exists but no targets extracted
                continue  # May be formatted differently, don't flag
            results.append(ValidationResult(False, f"State '{state_name}' has no exit transitions (dead end)"))
    
    if not any(not r.passed for r in results):
        results.append(ValidationResult(True, "Transition structure is valid"))
    
    return results


def validate_edge_cases(content: str) -> list[ValidationResult]:
    """Validate edge cases section."""
    results = []
    
    if '## Edge cases' not in content:
        results.append(ValidationResult(False, "Missing '## Edge cases' section"))
        return results
    
    # Count edge case rows
    edge_section = re.search(r'## Edge cases\s*\n\|[^\n]+\n\|[-|\s]+\n((?:\|[^\n]+\n)*)', content)
    if edge_section:
        rows = [r for r in edge_section.group(1).strip().split('\n') if r.strip()]
        if len(rows) < MIN_EDGE_CASES:
            results.append(ValidationResult(False, f"Need at least {MIN_EDGE_CASES} edge cases, found {len(rows)}"))
        else:
            results.append(ValidationResult(True, f"Found {len(rows)} edge cases"))
    else:
        results.append(ValidationResult(False, "Edge cases table not found or malformed"))
    
    return results


def main():
    if len(sys.argv) != 2:
        print("Usage: python validate_state_map.py <path-to-state-map.md>")
        sys.exit(2)
    
    file_path = Path(sys.argv[1])
    
    if not file_path.exists():
        print(f"Error: File not found: {file_path}")
        sys.exit(2)
    
    try:
        content = file_path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(2)
    
    all_results = []
    all_results.extend(validate_overview(content))
    all_results.extend(validate_states(content))
    all_results.extend(validate_transitions(content))
    all_results.extend(validate_edge_cases(content))
    
    # Print results
    print(f"\nState Map Validation: {file_path.name}\n")
    print("-" * 60)
    
    passed = 0
    failed = 0
    
    for result in all_results:
        status = "✓" if result.passed else "✗"
        print(f"{status} {result.message}")
        if result.passed:
            passed += 1
        else:
            failed += 1
    
    print("-" * 60)
    print(f"Passed: {passed} | Failed: {failed}")
    
    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
