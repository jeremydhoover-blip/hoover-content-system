#!/usr/bin/env python3
"""
Content Pattern Validator

Validates content patterns against the pattern schema.
Checks structure, constraints, and cross-references.
"""

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any, Optional

try:
    import yaml  # type: ignore[import-not-found]
    YAML_AVAILABLE = True
except ImportError:
    YAML_AVAILABLE = False

# ============================================================
# CONSTANTS - Schema definitions
# ============================================================

VALID_CATEGORIES = {
    "feedback",
    "guidance", 
    "action",
    "navigation",
    "form",
    "notification",
    "empty-state",
    "confirmation"
}

VALID_PLATFORMS = {"web", "ios", "android", "all"}

VALID_SLOT_TYPES = {"text", "options", "variable"}

VALID_STATUSES = {"draft", "active", "deprecated"}

VALID_FORMATS = {"sentence", "fragment", "question"}

VALID_TONES = {"neutral", "positive", "urgent"}

REQUIRED_PATTERN_FIELDS = {
    "id",
    "name", 
    "category",
    "description",
    "structure",
    "usage",
    "examples",
    "metadata"
}

REQUIRED_STRUCTURE_FIELDS = {"slots", "syntax"}

REQUIRED_USAGE_FIELDS = {"when_to_use", "when_not_to_use", "platforms"}

REQUIRED_EXAMPLE_FIELDS = {"minimal", "typical", "complex"}

REQUIRED_METADATA_FIELDS = {"created", "updated", "author", "status"}

REQUIRED_SLOT_FIELDS = {"name", "required", "type"}


class Severity(Enum):
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"


@dataclass
class ValidationIssue:
    """A single validation issue."""
    path: str
    rule: str
    message: str
    severity: Severity


@dataclass 
class ValidationResult:
    """Complete validation result for a pattern."""
    pattern_id: str
    is_valid: bool
    issues: list[ValidationIssue] = field(default_factory=list)
    
    def add_issue(self, path: str, rule: str, message: str, 
                  severity: Severity = Severity.ERROR):
        self.issues.append(ValidationIssue(path, rule, message, severity))
        if severity == Severity.ERROR:
            self.is_valid = False
    
    def to_dict(self) -> dict:
        return {
            "pattern_id": self.pattern_id,
            "is_valid": self.is_valid,
            "error_count": sum(1 for i in self.issues if i.severity == Severity.ERROR),
            "warning_count": sum(1 for i in self.issues if i.severity == Severity.WARNING),
            "issues": [
                {
                    "path": i.path,
                    "rule": i.rule,
                    "message": i.message,
                    "severity": i.severity.value
                }
                for i in self.issues
            ]
        }


def validate_id(pattern: dict, result: ValidationResult):
    """Validate pattern ID format."""
    pattern_id = pattern.get("id", "")
    
    if not pattern_id:
        result.add_issue("id", "REQUIRED", "Pattern ID is required")
        return
    
    # Check format (kebab-case)
    if not re.match(r'^[a-z][a-z0-9]*(-[a-z0-9]+)*$', pattern_id):
        result.add_issue("id", "FORMAT", 
                        f"ID '{pattern_id}' must be kebab-case (lowercase, hyphens)")
    
    # Check length
    if len(pattern_id) < 3 or len(pattern_id) > 50:
        result.add_issue("id", "LENGTH", 
                        f"ID must be 3-50 characters (got {len(pattern_id)})")


def validate_category(pattern: dict, result: ValidationResult):
    """Validate pattern category."""
    category = pattern.get("category", "")
    
    if not category:
        result.add_issue("category", "REQUIRED", "Category is required")
        return
    
    if category not in VALID_CATEGORIES:
        result.add_issue("category", "INVALID", 
                        f"Invalid category '{category}'. Valid: {', '.join(sorted(VALID_CATEGORIES))}")


def validate_slots(slots: list, result: ValidationResult):
    """Validate slot definitions."""
    if not slots:
        result.add_issue("structure.slots", "REQUIRED", "At least one slot required")
        return
    
    slot_names = set()
    
    for i, slot in enumerate(slots):
        path = f"structure.slots[{i}]"
        
        # Check required fields
        for field_name in REQUIRED_SLOT_FIELDS:
            if field_name not in slot:
                result.add_issue(f"{path}.{field_name}", "REQUIRED",
                               f"Slot field '{field_name}' is required")
        
        # Validate slot name
        name = slot.get("name", "")
        if name:
            if not re.match(r'^[a-z][a-z0-9_]*$', name):
                result.add_issue(f"{path}.name", "FORMAT",
                               f"Slot name '{name}' must be snake_case")
            if name in slot_names:
                result.add_issue(f"{path}.name", "DUPLICATE",
                               f"Duplicate slot name '{name}'")
            slot_names.add(name)
        
        # Validate slot type
        slot_type = slot.get("type", "")
        if slot_type and slot_type not in VALID_SLOT_TYPES:
            result.add_issue(f"{path}.type", "INVALID",
                           f"Invalid slot type '{slot_type}'. Valid: {', '.join(VALID_SLOT_TYPES)}")
        
        # Validate constraints
        constraints = slot.get("constraints", {})
        if constraints:
            validate_constraints(constraints, f"{path}.constraints", result)
    
    return slot_names


def validate_constraints(constraints: dict, path: str, result: ValidationResult):
    """Validate slot constraints."""
    if "max_chars" in constraints:
        max_chars = constraints["max_chars"]
        if not isinstance(max_chars, int) or max_chars < 1:
            result.add_issue(f"{path}.max_chars", "INVALID",
                           "max_chars must be positive integer")
    
    if "max_words" in constraints:
        max_words = constraints["max_words"]
        if not isinstance(max_words, int) or max_words < 1:
            result.add_issue(f"{path}.max_words", "INVALID",
                           "max_words must be positive integer")
    
    if "format" in constraints:
        fmt = constraints["format"]
        if fmt not in VALID_FORMATS:
            result.add_issue(f"{path}.format", "INVALID",
                           f"Invalid format '{fmt}'. Valid: {', '.join(VALID_FORMATS)}")
    
    if "tone" in constraints:
        tone = constraints["tone"]
        if tone not in VALID_TONES:
            result.add_issue(f"{path}.tone", "INVALID",
                           f"Invalid tone '{tone}'. Valid: {', '.join(VALID_TONES)}")


def validate_syntax(syntax: str, slot_names: set, result: ValidationResult):
    """Validate syntax string against slot definitions."""
    if not syntax:
        result.add_issue("structure.syntax", "REQUIRED", "Syntax is required")
        return
    
    # Extract slot references from syntax
    referenced_slots = set(re.findall(r'\{(\w+)\}', syntax))
    
    # Check all referenced slots exist
    undefined = referenced_slots - slot_names
    if undefined:
        result.add_issue("structure.syntax", "UNDEFINED_SLOT",
                        f"Syntax references undefined slots: {', '.join(undefined)}")
    
    # Warn if required slots not in syntax
    # (This would require knowing which slots are required, simplified check here)


def validate_usage(usage: dict, result: ValidationResult):
    """Validate usage section."""
    for field_name in REQUIRED_USAGE_FIELDS:
        if field_name not in usage:
            result.add_issue(f"usage.{field_name}", "REQUIRED",
                           f"Usage field '{field_name}' is required")
    
    platforms = usage.get("platforms", [])
    for platform in platforms:
        if platform not in VALID_PLATFORMS:
            result.add_issue("usage.platforms", "INVALID",
                           f"Invalid platform '{platform}'. Valid: {', '.join(VALID_PLATFORMS)}")


def validate_examples(examples: dict, result: ValidationResult):
    """Validate examples section."""
    for field_name in REQUIRED_EXAMPLE_FIELDS:
        if field_name not in examples:
            result.add_issue(f"examples.{field_name}", "REQUIRED",
                           f"Example '{field_name}' is required")
        elif not examples[field_name]:
            result.add_issue(f"examples.{field_name}", "EMPTY",
                           f"Example '{field_name}' cannot be empty")


def validate_metadata(metadata: dict, result: ValidationResult):
    """Validate metadata section."""
    for field_name in REQUIRED_METADATA_FIELDS:
        if field_name not in metadata:
            result.add_issue(f"metadata.{field_name}", "REQUIRED",
                           f"Metadata field '{field_name}' is required")
    
    status = metadata.get("status", "")
    if status and status not in VALID_STATUSES:
        result.add_issue("metadata.status", "INVALID",
                        f"Invalid status '{status}'. Valid: {', '.join(VALID_STATUSES)}")


def validate_pattern(pattern: dict) -> ValidationResult:
    """Validate a complete pattern."""
    pattern_id = pattern.get("id", "unknown")
    result = ValidationResult(pattern_id=pattern_id, is_valid=True)
    
    # Check top-level required fields
    for field_name in REQUIRED_PATTERN_FIELDS:
        if field_name not in pattern:
            result.add_issue(field_name, "REQUIRED", f"Field '{field_name}' is required")
    
    # Validate individual sections
    validate_id(pattern, result)
    validate_category(pattern, result)
    
    # Validate description
    desc = pattern.get("description", "")
    if not desc:
        result.add_issue("description", "REQUIRED", "Description is required")
    elif len(desc) < 20 or len(desc) > 200:
        result.add_issue("description", "LENGTH", 
                        f"Description should be 20-200 chars (got {len(desc)})",
                        Severity.WARNING)
    
    # Validate structure
    structure = pattern.get("structure", {})
    if structure:
        for field_name in REQUIRED_STRUCTURE_FIELDS:
            if field_name not in structure:
                result.add_issue(f"structure.{field_name}", "REQUIRED",
                               f"Structure field '{field_name}' is required")
        
        slot_names = validate_slots(structure.get("slots", []), result)
        if slot_names:
            validate_syntax(structure.get("syntax", ""), slot_names, result)
    
    # Validate usage
    usage = pattern.get("usage", {})
    if usage:
        validate_usage(usage, result)
    
    # Validate examples
    examples = pattern.get("examples", {})
    if examples:
        validate_examples(examples, result)
    
    # Validate metadata
    metadata = pattern.get("metadata", {})
    if metadata:
        validate_metadata(metadata, result)
    
    return result


def validate_library(patterns: list, known_ids: Optional[set] = None) -> list[ValidationResult]:
    """Validate multiple patterns, checking cross-references."""
    results = []
    pattern_ids = set()
    
    # First pass: validate individual patterns and collect IDs
    for pattern in patterns:
        result = validate_pattern(pattern)
        results.append(result)
        
        pattern_id = pattern.get("id", "")
        if pattern_id:
            if pattern_id in pattern_ids:
                result.add_issue("id", "DUPLICATE_IN_LIBRARY",
                               f"Pattern ID '{pattern_id}' is duplicated in library")
            pattern_ids.add(pattern_id)
    
    # Second pass: validate cross-references
    all_ids = pattern_ids | (known_ids or set())
    
    for pattern, result in zip(patterns, results):
        related = pattern.get("metadata", {}).get("related_patterns", [])
        for ref_id in related:
            if ref_id not in all_ids:
                result.add_issue("metadata.related_patterns", "UNRESOLVED_REFERENCE",
                               f"Related pattern '{ref_id}' not found in library",
                               Severity.WARNING)
    
    return results


def load_pattern_file(filepath: Path) -> dict:
    """Load pattern from YAML or JSON file."""
    content = filepath.read_text(encoding='utf-8')
    
    if filepath.suffix in ('.yaml', '.yml'):
        if not YAML_AVAILABLE:
            raise ImportError(
                "PyYAML is required for YAML files. "
                "Install with: pip install pyyaml"
            )
        return yaml.safe_load(content)
    elif filepath.suffix == '.json':
        return json.loads(content)
    else:
        # Try JSON first (no external dependency), then YAML
        try:
            return json.loads(content)
        except json.JSONDecodeError:
            if YAML_AVAILABLE:
                return yaml.safe_load(content)
            raise ValueError(
                f"Could not parse {filepath}. "
                "For YAML files, install PyYAML: pip install pyyaml"
            )


def main():
    parser = argparse.ArgumentParser(description="Validate content patterns")
    
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    
    # Single file validation
    single_parser = subparsers.add_parser("validate", help="Validate a pattern file")
    single_parser.add_argument("file", help="Pattern file (YAML or JSON)")
    
    # Library validation
    lib_parser = subparsers.add_parser("library", help="Validate pattern library")
    lib_parser.add_argument("directory", help="Directory containing pattern files")
    lib_parser.add_argument("--output", "-o", help="Output file for results")
    
    # Schema info
    subparsers.add_parser("schema", help="Print schema requirements")
    
    args = parser.parse_args()
    
    if args.command == "validate":
        filepath = Path(args.file)
        if not filepath.exists():
            print(f"Error: File not found: {filepath}", file=sys.stderr)
            sys.exit(1)
        
        pattern = load_pattern_file(filepath)
        
        # Handle wrapped pattern (pattern: {...})
        if "pattern" in pattern:
            pattern = pattern["pattern"]
        
        result = validate_pattern(pattern)
        print(json.dumps(result.to_dict(), indent=2))
        sys.exit(0 if result.is_valid else 1)
    
    elif args.command == "library":
        dirpath = Path(args.directory)
        if not dirpath.is_dir():
            print(f"Error: Not a directory: {dirpath}", file=sys.stderr)
            sys.exit(1)
        
        patterns = []
        for filepath in dirpath.glob("**/*.yaml"):
            pattern = load_pattern_file(filepath)
            if "pattern" in pattern:
                pattern = pattern["pattern"]
            patterns.append(pattern)
        
        for filepath in dirpath.glob("**/*.yml"):
            pattern = load_pattern_file(filepath)
            if "pattern" in pattern:
                pattern = pattern["pattern"]
            patterns.append(pattern)
        
        for filepath in dirpath.glob("**/*.json"):
            pattern = load_pattern_file(filepath)
            if "pattern" in pattern:
                pattern = pattern["pattern"]
            patterns.append(pattern)
        
        if not patterns:
            print("No pattern files found", file=sys.stderr)
            sys.exit(1)
        
        results = validate_library(patterns)
        
        summary = {
            "total_patterns": len(results),
            "valid_patterns": sum(1 for r in results if r.is_valid),
            "invalid_patterns": sum(1 for r in results if not r.is_valid),
            "results": [r.to_dict() for r in results]
        }
        
        output = json.dumps(summary, indent=2)
        
        if args.output:
            Path(args.output).write_text(output, encoding='utf-8')
            print(f"Results written to {args.output}")
        else:
            print(output)
        
        invalid_count = summary["invalid_patterns"]
        if invalid_count:
            print(f"\n{invalid_count} of {len(results)} patterns have errors", file=sys.stderr)
            sys.exit(1)
    
    elif args.command == "schema":
        print("Content Pattern Schema Requirements")
        print("=" * 40)
        print(f"\nValid categories: {', '.join(sorted(VALID_CATEGORIES))}")
        print(f"Valid platforms: {', '.join(sorted(VALID_PLATFORMS))}")
        print(f"Valid slot types: {', '.join(sorted(VALID_SLOT_TYPES))}")
        print(f"Valid statuses: {', '.join(sorted(VALID_STATUSES))}")
        print(f"\nRequired top-level fields: {', '.join(sorted(REQUIRED_PATTERN_FIELDS))}")
    
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
