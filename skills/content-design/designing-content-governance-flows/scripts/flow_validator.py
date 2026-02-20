#!/usr/bin/env python3
"""
Content Governance Flow Validator

Validates governance workflow definitions against required structure.
Checks role assignments, SLA compliance, and stage transitions.
"""

import argparse
import json
import sys
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Optional

try:
    import yaml  # type: ignore[import-not-found]
    YAML_AVAILABLE = True
except ImportError:
    YAML_AVAILABLE = False

# ============================================================
# CONSTANTS - Governance workflow schema
# ============================================================

VALID_ROLES = {
    "content_owner",
    "content_author",
    "content_reviewer",
    "content_approver",
    "content_publisher",
    "legal_reviewer",
    "localization_lead",
    "style_reviewer"
}

REQUIRED_STAGES = {
    "draft",
    "review",
    "approval",
    "publication"
}

VALID_STAGE_STATUSES = {
    "not_started",
    "in_progress",
    "completed",
    "blocked",
    "skipped"
}

SLA_TIERS = {
    "standard": {
        "review_days": 3,
        "revision_days": 2,
        "approval_days": 2,
        "publication_hours": 24
    },
    "priority": {
        "review_days": 1,
        "revision_days": 1,
        "approval_days": 1,
        "publication_hours": 4
    },
    "urgent": {
        "review_hours": 4,
        "revision_hours": 2,
        "approval_hours": 2,
        "publication_hours": 1
    },
    "emergency": {
        "review_hours": 1,
        "approval_minutes": 30,
        "publication_minutes": 30
    }
}

REQUIRED_FLOW_FIELDS = {
    "id",
    "name",
    "stages",
    "sla_tier"
}

REQUIRED_STAGE_FIELDS = {
    "name",
    "assigned_role",
    "required"
}


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
    """Complete validation result for a flow."""
    flow_id: str
    is_valid: bool
    issues: list[ValidationIssue] = field(default_factory=list)
    
    def add_issue(self, path: str, rule: str, message: str,
                  severity: Severity = Severity.ERROR):
        self.issues.append(ValidationIssue(path, rule, message, severity))
        if severity == Severity.ERROR:
            self.is_valid = False
    
    def to_dict(self) -> dict:
        return {
            "flow_id": self.flow_id,
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


def validate_flow_structure(flow: dict, result: ValidationResult):
    """Validate top-level flow structure."""
    for field_name in REQUIRED_FLOW_FIELDS:
        if field_name not in flow:
            result.add_issue(field_name, "REQUIRED",
                           f"Flow field '{field_name}' is required")


def validate_stages(stages: list, result: ValidationResult):
    """Validate stage definitions."""
    if not stages:
        result.add_issue("stages", "REQUIRED", "At least one stage required")
        return set()
    
    stage_names = set()
    found_required_stages = set()
    
    for i, stage in enumerate(stages):
        path = f"stages[{i}]"
        
        # Check required fields
        for field_name in REQUIRED_STAGE_FIELDS:
            if field_name not in stage:
                result.add_issue(f"{path}.{field_name}", "REQUIRED",
                               f"Stage field '{field_name}' is required")
        
        # Validate stage name
        name = stage.get("name", "")
        if name:
            if name in stage_names:
                result.add_issue(f"{path}.name", "DUPLICATE",
                               f"Duplicate stage name '{name}'")
            stage_names.add(name)
            
            # Track required stages
            if name in REQUIRED_STAGES:
                found_required_stages.add(name)
        
        # Validate assigned role
        role = stage.get("assigned_role", "")
        if role and role not in VALID_ROLES:
            result.add_issue(f"{path}.assigned_role", "INVALID_ROLE",
                           f"Invalid role '{role}'. Valid: {', '.join(sorted(VALID_ROLES))}")
        
        # Validate transitions
        transitions = stage.get("transitions", [])
        for j, transition in enumerate(transitions):
            trans_path = f"{path}.transitions[{j}]"
            validate_transition(transition, trans_path, stage_names, result)
    
    # Check all required stages present
    missing_stages = REQUIRED_STAGES - found_required_stages
    if missing_stages:
        result.add_issue("stages", "MISSING_REQUIRED",
                        f"Missing required stages: {', '.join(sorted(missing_stages))}")
    
    return stage_names


def validate_transition(transition: dict, path: str, 
                       valid_targets: set, result: ValidationResult):
    """Validate a stage transition."""
    target = transition.get("to", "")
    
    if not target:
        result.add_issue(f"{path}.to", "REQUIRED",
                        "Transition target is required")
        return
    
    # Note: Can't fully validate target until all stages defined
    # This is a simplified check
    
    # Validate condition if present
    condition = transition.get("condition")
    if condition:
        valid_conditions = {"approved", "rejected", "revision_requested", "escalated"}
        if condition not in valid_conditions:
            result.add_issue(f"{path}.condition", "INVALID_CONDITION",
                           f"Unknown condition '{condition}'",
                           Severity.WARNING)


def validate_sla(flow: dict, result: ValidationResult):
    """Validate SLA configuration."""
    sla_tier = flow.get("sla_tier", "")
    
    if not sla_tier:
        result.add_issue("sla_tier", "REQUIRED", "SLA tier is required")
        return
    
    if sla_tier not in SLA_TIERS:
        result.add_issue("sla_tier", "INVALID_TIER",
                        f"Invalid SLA tier '{sla_tier}'. Valid: {', '.join(SLA_TIERS.keys())}")
        return
    
    # Validate custom SLA overrides
    custom_sla = flow.get("sla_overrides", {})
    tier_sla = SLA_TIERS[sla_tier]
    
    for stage, override in custom_sla.items():
        if not isinstance(override, (int, float)):
            result.add_issue(f"sla_overrides.{stage}", "INVALID_VALUE",
                           f"SLA override must be numeric")
            continue
        
        if override <= 0:
            result.add_issue(f"sla_overrides.{stage}", "INVALID_VALUE",
                           f"SLA override must be positive")


def validate_roles(flow: dict, result: ValidationResult):
    """Validate role assignments across flow."""
    stages = flow.get("stages", [])
    assigned_roles = set()
    
    for stage in stages:
        role = stage.get("assigned_role", "")
        if role:
            assigned_roles.add(role)
    
    # Check for common missing roles
    critical_roles = {"content_approver", "content_publisher"}
    missing_critical = critical_roles - assigned_roles
    
    if missing_critical:
        result.add_issue("stages", "MISSING_CRITICAL_ROLE",
                        f"Flow missing critical roles: {', '.join(missing_critical)}",
                        Severity.WARNING)
    
    # Warn if same role at consecutive stages
    prev_role = None
    for i, stage in enumerate(stages):
        role = stage.get("assigned_role", "")
        if role and role == prev_role:
            result.add_issue(f"stages[{i}]", "CONSECUTIVE_SAME_ROLE",
                           f"Same role '{role}' assigned to consecutive stages",
                           Severity.INFO)
        prev_role = role


def validate_flow(flow: dict) -> ValidationResult:
    """Validate a complete governance flow."""
    flow_id = flow.get("id", "unknown")
    result = ValidationResult(flow_id=flow_id, is_valid=True)
    
    # Validate structure
    validate_flow_structure(flow, result)
    
    # Validate stages
    stages = flow.get("stages", [])
    if stages:
        validate_stages(stages, result)
    
    # Validate SLA
    validate_sla(flow, result)
    
    # Validate role assignments
    validate_roles(flow, result)
    
    return result


def generate_flow_template(sla_tier: str = "standard") -> dict:
    """Generate a template governance flow."""
    return {
        "id": "example-content-flow",
        "name": "Example Content Governance Flow",
        "description": "Template governance flow for content approval",
        "sla_tier": sla_tier,
        "stages": [
            {
                "name": "draft",
                "assigned_role": "content_author",
                "required": True,
                "transitions": [
                    {"to": "review", "condition": "submitted"}
                ]
            },
            {
                "name": "review",
                "assigned_role": "content_reviewer",
                "required": True,
                "transitions": [
                    {"to": "approval", "condition": "approved"},
                    {"to": "draft", "condition": "revision_requested"}
                ]
            },
            {
                "name": "approval",
                "assigned_role": "content_approver",
                "required": True,
                "transitions": [
                    {"to": "publication", "condition": "approved"},
                    {"to": "review", "condition": "rejected"}
                ]
            },
            {
                "name": "publication",
                "assigned_role": "content_publisher",
                "required": True,
                "transitions": [
                    {"to": "complete", "condition": "published"}
                ]
            }
        ],
        "metadata": {
            "created": "2024-01-01",
            "author": "content-team",
            "version": "1.0"
        }
    }


def calculate_sla_deadline(flow: dict, stage: str) -> dict:
    """Calculate SLA deadlines for a stage."""
    tier = flow.get("sla_tier", "standard")
    tier_slas = SLA_TIERS.get(tier, SLA_TIERS["standard"])
    overrides = flow.get("sla_overrides", {})
    
    result = {
        "tier": tier,
        "stage": stage,
        "sla": {}
    }
    
    # Map stage to SLA keys
    stage_sla_map = {
        "review": ["review_days", "review_hours"],
        "revision": ["revision_days", "revision_hours"],
        "approval": ["approval_days", "approval_hours", "approval_minutes"],
        "publication": ["publication_days", "publication_hours", "publication_minutes"]
    }
    
    for sla_key in stage_sla_map.get(stage, []):
        if sla_key in tier_slas:
            value = overrides.get(stage, tier_slas[sla_key])
            unit = sla_key.split("_")[1]
            result["sla"][unit] = value
            break
    
    return result


def load_flow_file(filepath: Path) -> dict:
    """Load flow from YAML or JSON file."""
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
    parser = argparse.ArgumentParser(description="Validate content governance flows")
    
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    
    # Validate command
    val_parser = subparsers.add_parser("validate", help="Validate a flow file")
    val_parser.add_argument("file", help="Flow file (YAML or JSON)")
    
    # Template command
    tmpl_parser = subparsers.add_parser("template", help="Generate flow template")
    tmpl_parser.add_argument("--tier", "-t", choices=list(SLA_TIERS.keys()),
                            default="standard", help="SLA tier for template")
    tmpl_parser.add_argument("--output", "-o", help="Output file")
    
    # SLA command
    sla_parser = subparsers.add_parser("sla", help="Show SLA information")
    sla_parser.add_argument("--tier", "-t", choices=list(SLA_TIERS.keys()),
                           help="Specific tier to show")
    
    # Roles command
    subparsers.add_parser("roles", help="List valid governance roles")
    
    args = parser.parse_args()
    
    if args.command == "validate":
        filepath = Path(args.file)
        if not filepath.exists():
            print(f"Error: File not found: {filepath}", file=sys.stderr)
            sys.exit(1)
        
        flow = load_flow_file(filepath)
        result = validate_flow(flow)
        print(json.dumps(result.to_dict(), indent=2))
        sys.exit(0 if result.is_valid else 1)
    
    elif args.command == "template":
        template = generate_flow_template(args.tier)
        if YAML_AVAILABLE:
            output = yaml.dump(template, default_flow_style=False, sort_keys=False)
        else:
            output = json.dumps(template, indent=2)
        
        if args.output:
            Path(args.output).write_text(output, encoding='utf-8')
            print(f"Template written to {args.output}")
        else:
            print(output)
    
    elif args.command == "sla":
        if args.tier:
            tiers_to_show = {args.tier: SLA_TIERS[args.tier]}
        else:
            tiers_to_show = SLA_TIERS
        
        print("Content Governance SLA Tiers")
        print("=" * 40)
        for tier_name, sla in tiers_to_show.items():
            print(f"\n{tier_name.upper()}:")
            for key, value in sla.items():
                print(f"  {key}: {value}")
    
    elif args.command == "roles":
        print("Valid Governance Roles")
        print("=" * 40)
        for role in sorted(VALID_ROLES):
            print(f"  - {role}")
    
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
