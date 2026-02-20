#!/usr/bin/env python3
"""
audit_report_generator.py

Generates structured audit report from findings data.
Validates report completeness and severity consistency.

Usage:
    python audit_report_generator.py --input findings.json --output report.md
    python audit_report_generator.py --validate report.md
"""

import argparse
import json
import sys
from datetime import datetime
from typing import Any

# Severity levels in priority order
SEVERITY_LEVELS = ["critical", "major", "minor"]

# Required fields for each finding
REQUIRED_FINDING_FIELDS = [
    "id",
    "location",
    "copy",
    "severity",
    "issue_type",
    "problem",
    "recommendation"
]

# Valid issue types
VALID_ISSUE_TYPES = [
    "inconsistency",
    "clarity",
    "tone",
    "accessibility",
    "action_mismatch",
    "redundancy",
    "jargon",
    "error_recovery"
]


def validate_finding(finding: dict, index: int) -> list[str]:
    """Validate a single finding has all required fields."""
    errors = []
    
    for field in REQUIRED_FINDING_FIELDS:
        if field not in finding:
            errors.append(f"Finding {index}: missing required field '{field}'")
        elif not finding[field]:
            errors.append(f"Finding {index}: empty value for '{field}'")
    
    # Validate severity
    if finding.get("severity", "").lower() not in SEVERITY_LEVELS:
        errors.append(
            f"Finding {index}: invalid severity '{finding.get('severity')}'. "
            f"Must be one of: {', '.join(SEVERITY_LEVELS)}"
        )
    
    # Validate issue type
    if finding.get("issue_type", "").lower() not in VALID_ISSUE_TYPES:
        errors.append(
            f"Finding {index}: invalid issue_type '{finding.get('issue_type')}'. "
            f"Must be one of: {', '.join(VALID_ISSUE_TYPES)}"
        )
    
    # Validate recommendation has before/after
    rec = finding.get("recommendation", {})
    if isinstance(rec, dict):
        if "before" not in rec or "after" not in rec:
            errors.append(
                f"Finding {index}: recommendation must include 'before' and 'after'"
            )
    
    return errors


def validate_findings(findings: list[dict]) -> list[str]:
    """Validate all findings in the audit."""
    errors = []
    
    if not findings:
        errors.append("No findings provided")
        return errors
    
    finding_ids = set()
    for i, finding in enumerate(findings):
        # Check for duplicate IDs
        fid = finding.get("id")
        if fid in finding_ids:
            errors.append(f"Duplicate finding ID: {fid}")
        finding_ids.add(fid)
        
        # Validate individual finding
        errors.extend(validate_finding(finding, i + 1))
    
    return errors


def count_by_severity(findings: list[dict]) -> dict[str, int]:
    """Count findings by severity level."""
    counts = {level: 0 for level in SEVERITY_LEVELS}
    for finding in findings:
        severity = finding.get("severity", "").lower()
        if severity in counts:
            counts[severity] += 1
    return counts


def generate_report(audit_data: dict) -> str:
    """Generate markdown audit report from structured data."""
    findings = audit_data.get("findings", [])
    metadata = audit_data.get("metadata", {})
    
    # Validate first
    errors = validate_findings(findings)
    if errors:
        return f"# Validation Errors\n\n" + "\n".join(f"- {e}" for e in errors)
    
    counts = count_by_severity(findings)
    
    report = []
    
    # Header
    report.append("# UI Copy Audit Report\n")
    
    # Metadata
    report.append("## Audit scope")
    report.append(f"- **Screens reviewed**: {metadata.get('screens_reviewed', 'N/A')}")
    report.append(f"- **Copy elements evaluated**: {metadata.get('elements_evaluated', 'N/A')}")
    report.append(f"- **Date**: {metadata.get('date', datetime.now().strftime('%Y-%m-%d'))}")
    report.append(f"- **Auditor**: {metadata.get('auditor', 'N/A')}\n")
    
    # Executive summary
    report.append("## Executive summary")
    report.append(metadata.get("summary", "[Summary not provided]"))
    report.append("")
    
    # Findings by severity
    report.append("## Findings by severity\n")
    
    for severity in SEVERITY_LEVELS:
        severity_findings = [
            f for f in findings 
            if f.get("severity", "").lower() == severity
        ]
        report.append(f"### {severity.capitalize()} ({counts[severity]})")
        
        if severity_findings:
            for f in severity_findings:
                report.append(f"- {f['id']}: {f['problem'][:80]}")
        else:
            report.append("None")
        report.append("")
    
    # Detailed findings
    report.append("## Detailed findings\n")
    
    for finding in findings:
        report.append(f"### {finding['id']}: {finding['problem'][:50]}\n")
        report.append(f"**Location**: {finding['location']}")
        report.append(f"**Copy**: \"{finding['copy']}\"")
        report.append(f"**Severity**: {finding['severity'].capitalize()}")
        report.append(f"**Issue type**: {finding['issue_type'].capitalize()}\n")
        report.append(f"**Problem**: {finding['problem']}")
        
        if finding.get("impact"):
            report.append(f"**Impact**: {finding['impact']}")
        
        rec = finding.get("recommendation", {})
        if isinstance(rec, dict):
            report.append("\n**Recommendation**:")
            report.append(f"- Before: \"{rec.get('before', '')}\"")
            report.append(f"- After: \"{rec.get('after', '')}\"")
        
        if finding.get("rationale"):
            report.append(f"\n**Rationale**: {finding['rationale']}")
        
        report.append("\n---\n")
    
    return "\n".join(report)


def validate_report(report_path: str) -> list[str]:
    """Validate a markdown report has required sections."""
    errors = []
    
    required_sections = [
        "# UI Copy Audit Report",
        "## Audit scope",
        "## Executive summary",
        "## Findings by severity",
        "### Critical",
        "### Major", 
        "### Minor",
        "## Detailed findings"
    ]
    
    try:
        with open(report_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        return [f"Report file not found: {report_path}"]
    
    for section in required_sections:
        if section not in content:
            errors.append(f"Missing required section: {section}")
    
    return errors


def main():
    parser = argparse.ArgumentParser(
        description="Generate or validate UI copy audit reports"
    )
    parser.add_argument(
        "--input", "-i",
        help="Input JSON file with findings data"
    )
    parser.add_argument(
        "--output", "-o", 
        help="Output markdown file for report"
    )
    parser.add_argument(
        "--validate", "-v",
        help="Validate an existing report file"
    )
    
    args = parser.parse_args()
    
    if args.validate:
        errors = validate_report(args.validate)
        if errors:
            print("Validation failed:")
            for e in errors:
                print(f"  - {e}")
            sys.exit(1)
        else:
            print("Report validation passed")
            sys.exit(0)
    
    if not args.input:
        parser.error("--input required when not using --validate")
    
    try:
        with open(args.input, 'r', encoding='utf-8') as f:
            audit_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: Input file not found: {args.input}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in input file: {e}")
        sys.exit(1)
    
    report = generate_report(audit_data)
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"Report generated: {args.output}")
    else:
        print(report)


if __name__ == "__main__":
    main()
