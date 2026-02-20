#!/usr/bin/env python3
"""
Context Pack Validator

Validates context packs for completeness, consistency, and correctness.
Outputs structured validation report with severity levels.

Usage:
    python validate_context_pack.py <context_pack.yaml>
    python validate_context_pack.py <context_pack.json>

Exit codes:
    0: PASS (no blocking issues)
    1: FAIL (blocking issues found)
    2: ERROR (invalid input or processing error)
"""

import sys
import json
import re
from pathlib import Path
from dataclasses import dataclass, field
from typing import Any
from enum import Enum

# Constants with justification
REQUIRED_SECTIONS = [
    "feature",
    "user_goals", 
    "core_actions",
    "states",
    "transitions",
    "error_taxonomy",
    "vocabulary"
]  # Per required-fields.md specification

REQUIRED_FEATURE_FIELDS = ["name", "purpose"]  # Minimum for feature identification
REQUIRED_STATE_FIELDS = ["entry", "exit", "content_guidance"]  # Per state model requirements
REQUIRED_TRANSITION_FIELDS = ["from", "to", "trigger"]  # Minimum for valid transition
REQUIRED_ERROR_FIELDS = ["code", "message_pattern", "recovery"]  # Per error taxonomy spec

NAME_PATTERN = re.compile(r"^[a-z][a-z0-9-]*$")  # lowercase-hyphenated per naming rules
SNAKE_CASE_PATTERN = re.compile(r"^[a-z][a-z0-9_]*$")  # for states and actions


class Severity(Enum):
    BLOCKING = "blocking"
    WARNING = "warning"
    SUGGESTION = "suggestion"


@dataclass
class Issue:
    code: str
    severity: Severity
    location: str
    message: str
    remediation: str = ""


@dataclass
class ValidationResult:
    pack_name: str = "unknown"
    version: str = "unknown"
    issues: list = field(default_factory=list)
    
    @property
    def status(self) -> str:
        blocking = [i for i in self.issues if i.severity == Severity.BLOCKING]
        warnings = [i for i in self.issues if i.severity == Severity.WARNING]
        if blocking:
            return "FAIL"
        if warnings:
            return "PASS_WITH_WARNINGS"
        return "PASS"
    
    def add(self, code: str, severity: Severity, location: str, message: str, remediation: str = ""):
        self.issues.append(Issue(code, severity, location, message, remediation))
    
    def to_json(self) -> dict:
        return {
            "pack": self.pack_name,
            "version": self.version,
            "status": self.status,
            "blocking": [
                {"code": i.code, "location": i.location, "message": i.message}
                for i in self.issues if i.severity == Severity.BLOCKING
            ],
            "warnings": [
                {"code": i.code, "location": i.location, "message": i.message}
                for i in self.issues if i.severity == Severity.WARNING
            ],
            "suggestions": [
                {"code": i.code, "location": i.location, "message": i.message}
                for i in self.issues if i.severity == Severity.SUGGESTION
            ]
        }


def load_context_pack(file_path: Path) -> dict:
    """Load context pack from YAML or JSON file."""
    content = file_path.read_text(encoding="utf-8")
    
    if file_path.suffix in [".yaml", ".yml"]:
        try:
            import yaml  # type: ignore[import-not-found]
            return yaml.safe_load(content)
        except ImportError:
            # Fallback: try to parse as JSON if yaml not available
            print("Warning: PyYAML not installed, attempting JSON parse", file=sys.stderr)
            return json.loads(content)
    else:
        return json.loads(content)


def validate_structure(pack: dict, result: ValidationResult) -> None:
    """Check required sections and fields exist."""
    issue_counter = 1
    
    # Check required sections
    for section in REQUIRED_SECTIONS:
        if section not in pack:
            result.add(
                f"BLOCK-{issue_counter:03d}",
                Severity.BLOCKING,
                section,
                f"Missing required section: {section}",
                f"Add {section} section to context pack"
            )
            issue_counter += 1
    
    # Check feature fields
    if "feature" in pack:
        feature = pack["feature"]
        for field_name in REQUIRED_FEATURE_FIELDS:
            if field_name not in feature:
                result.add(
                    f"BLOCK-{issue_counter:03d}",
                    Severity.BLOCKING,
                    f"feature.{field_name}",
                    f"Missing required field: feature.{field_name}",
                    f"Add {field_name} to feature section"
                )
                issue_counter += 1
        
        # Validate feature name format
        if "name" in feature:
            result.pack_name = feature["name"]
            if not NAME_PATTERN.match(feature["name"]):
                result.add(
                    f"BLOCK-{issue_counter:03d}",
                    Severity.BLOCKING,
                    "feature.name",
                    f"Feature name must be lowercase-hyphenated: {feature['name']}",
                    "Rename to lowercase with hyphens only"
                )
                issue_counter += 1
        
        if "version" in feature:
            result.version = feature["version"]
    
    # Check minimum counts
    if "user_goals" in pack and len(pack["user_goals"]) < 1:
        result.add(
            f"BLOCK-{issue_counter:03d}",
            Severity.BLOCKING,
            "user_goals",
            "At least one user_goal required",
            "Add at least one user goal"
        )
        issue_counter += 1
    
    if "core_actions" in pack and len(pack["core_actions"]) < 1:
        result.add(
            f"BLOCK-{issue_counter:03d}",
            Severity.BLOCKING,
            "core_actions",
            "At least one core_action required",
            "Add at least one core action"
        )
        issue_counter += 1


def validate_states(pack: dict, result: ValidationResult) -> None:
    """Validate state definitions."""
    if "states" not in pack:
        return
    
    states = pack["states"]
    issue_counter = len([i for i in result.issues if i.severity == Severity.BLOCKING]) + 1
    warn_counter = len([i for i in result.issues if i.severity == Severity.WARNING]) + 1
    
    for state_name, state_def in states.items():
        if not isinstance(state_def, dict):
            result.add(
                f"BLOCK-{issue_counter:03d}",
                Severity.BLOCKING,
                f"states.{state_name}",
                f"State must be an object: {state_name}",
                "Define state as object with entry, exit, content_guidance"
            )
            issue_counter += 1
            continue
        
        # Check required state fields
        for field_name in ["entry", "exit"]:
            if field_name not in state_def:
                result.add(
                    f"BLOCK-{issue_counter:03d}",
                    Severity.BLOCKING,
                    f"states.{state_name}.{field_name}",
                    f"State missing {field_name} condition: {state_name}",
                    f"Add {field_name} condition to state"
                )
                issue_counter += 1
        
        if "content_guidance" not in state_def:
            result.add(
                f"BLOCK-{issue_counter:03d}",
                Severity.BLOCKING,
                f"states.{state_name}.content_guidance",
                f"State missing content_guidance: {state_name}",
                "Add content_guidance to state"
            )
            issue_counter += 1
        
        # Check error handling for states that might need it
        state_might_fail = any(keyword in state_name.lower() 
                              for keyword in ["form", "input", "submit", "upload", "request"])
        if state_might_fail and "error_handling" not in state_def:
            result.add(
                f"WARN-{warn_counter:03d}",
                Severity.WARNING,
                f"states.{state_name}",
                f"State may need error_handling: {state_name}",
                "Consider adding error_handling for failure scenarios"
            )
            warn_counter += 1


def validate_transitions(pack: dict, result: ValidationResult) -> None:
    """Validate transitions reference defined states."""
    if "transitions" not in pack or "states" not in pack:
        return
    
    transitions = pack["transitions"]
    states = set(pack["states"].keys())
    states.add("any")  # Special wildcard state
    
    issue_counter = len([i for i in result.issues if i.severity == Severity.BLOCKING]) + 1
    
    for i, transition in enumerate(transitions):
        if not isinstance(transition, dict):
            result.add(
                f"BLOCK-{issue_counter:03d}",
                Severity.BLOCKING,
                f"transitions[{i}]",
                "Transition must be an object",
                "Define transition with from, to, trigger fields"
            )
            issue_counter += 1
            continue
        
        # Check required fields
        for field_name in REQUIRED_TRANSITION_FIELDS:
            if field_name not in transition:
                result.add(
                    f"BLOCK-{issue_counter:03d}",
                    Severity.BLOCKING,
                    f"transitions[{i}].{field_name}",
                    f"Transition missing {field_name}",
                    f"Add {field_name} to transition"
                )
                issue_counter += 1
        
        # Check state references
        if "from" in transition:
            from_state = transition["from"]
            # Handle comma-separated states
            from_states = [s.strip() for s in from_state.split(",")]
            for fs in from_states:
                if fs not in states:
                    result.add(
                        f"BLOCK-{issue_counter:03d}",
                        Severity.BLOCKING,
                        f"transitions[{i}].from",
                        f"Transition from undefined state: {fs}",
                        f"Define state '{fs}' or fix reference"
                    )
                    issue_counter += 1
        
        if "to" in transition and transition["to"] not in states:
            result.add(
                f"BLOCK-{issue_counter:03d}",
                Severity.BLOCKING,
                f"transitions[{i}].to",
                f"Transition to undefined state: {transition['to']}",
                f"Define state '{transition['to']}' or fix reference"
            )
            issue_counter += 1


def validate_vocabulary(pack: dict, result: ValidationResult) -> None:
    """Validate vocabulary for circular and conflicting definitions."""
    if "vocabulary" not in pack:
        return
    
    vocabulary = pack["vocabulary"]
    terms = set(vocabulary.keys())
    
    issue_counter = len([i for i in result.issues if i.severity == Severity.BLOCKING]) + 1
    
    # Check for circular definitions
    for term, definition in vocabulary.items():
        if not isinstance(definition, str):
            continue
        
        # Simple circular check: term A defines using B, B defines using A
        definition_lower = definition.lower()
        for other_term in terms:
            if other_term != term and other_term.lower() in definition_lower:
                other_def = vocabulary.get(other_term, "")
                if isinstance(other_def, str) and term.lower() in other_def.lower():
                    result.add(
                        f"BLOCK-{issue_counter:03d}",
                        Severity.BLOCKING,
                        f"vocabulary.{term}",
                        f"Circular definition: {term} <-> {other_term}",
                        f"Break circular reference by defining one term independently"
                    )
                    issue_counter += 1
                    break


def validate_error_taxonomy(pack: dict, result: ValidationResult) -> None:
    """Validate error taxonomy completeness."""
    if "error_taxonomy" not in pack:
        return
    
    errors = pack["error_taxonomy"]
    issue_counter = len([i for i in result.issues if i.severity == Severity.BLOCKING]) + 1
    
    for i, error in enumerate(errors):
        if not isinstance(error, dict):
            result.add(
                f"BLOCK-{issue_counter:03d}",
                Severity.BLOCKING,
                f"error_taxonomy[{i}]",
                "Error must be an object",
                "Define error with code, message_pattern, recovery"
            )
            issue_counter += 1
            continue
        
        for field_name in REQUIRED_ERROR_FIELDS:
            if field_name not in error:
                result.add(
                    f"BLOCK-{issue_counter:03d}",
                    Severity.BLOCKING,
                    f"error_taxonomy[{i}].{field_name}",
                    f"Error missing {field_name}",
                    f"Add {field_name} to error definition"
                )
                issue_counter += 1


def validate(pack: dict) -> ValidationResult:
    """Run all validations and return result."""
    result = ValidationResult()
    
    validate_structure(pack, result)
    validate_states(pack, result)
    validate_transitions(pack, result)
    validate_vocabulary(pack, result)
    validate_error_taxonomy(pack, result)
    
    return result


def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_context_pack.py <context_pack.yaml|json>", file=sys.stderr)
        sys.exit(2)
    
    file_path = Path(sys.argv[1])
    
    if not file_path.exists():
        print(f"Error: File not found: {file_path}", file=sys.stderr)
        sys.exit(2)
    
    try:
        pack = load_context_pack(file_path)
    except Exception as e:
        print(f"Error: Failed to parse file: {e}", file=sys.stderr)
        sys.exit(2)
    
    result = validate(pack)
    
    # Output JSON result
    print(json.dumps(result.to_json(), indent=2))
    
    # Exit with appropriate code
    if result.status == "FAIL":
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
