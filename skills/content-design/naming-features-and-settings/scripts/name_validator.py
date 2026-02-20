#!/usr/bin/env python3
"""
Name Validator

Validates feature and setting names against naming rules and banned terms.
Checks character limits, capitalization, and vocabulary compliance.
"""

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

# ============================================================
# CONSTANTS - Banned terms organized by category
# ============================================================

BANNED_TECHNICAL_JARGON = {
    "cache", "buffer", "token", "webhook", "api", "sdk", "regex",
    "query", "payload", "callback", "instance", "thread", "parse",
    "render", "compile", "deprecated"
}

BANNED_AMBIGUOUS_VERBS = {
    "manage", "process", "handle", "execute", "implement",
    "utilize", "leverage", "facilitate"
}

BANNED_ABSOLUTIST = {
    "always", "never", "guaranteed", "100%", "instantly",
    "forever", "permanently", "perfect", "best", "ultimate",
    "revolutionary"
}

BANNED_NEGATIVE = {
    "fail", "failed", "error", "invalid", "kill", "terminate",
    "abort", "fatal", "destroy", "nuke", "purge", "force",
    "reject", "rejected", "forbidden", "illegal", "warning"
}

BANNED_EXCLUSIONARY = {
    "simple", "simply", "easy", "easily", "just", "obviously",
    "clearly", "of course", "as you know", "master", "slave",
    "whitelist", "blacklist", "sanity check", "crazy", "insane",
    "blind", "cripple", "dummy", "guys"
}

BANNED_LEGAL_RISK = {
    "free", "secure", "security", "safe", "certified",
    "compliant", "anonymous", "confidential", "guarantee",
    "promise", "rights"
}

ALL_BANNED_TERMS = (
    BANNED_TECHNICAL_JARGON |
    BANNED_AMBIGUOUS_VERBS |
    BANNED_ABSOLUTIST |
    BANNED_NEGATIVE |
    BANNED_EXCLUSIONARY |
    BANNED_LEGAL_RISK
)

# ============================================================
# CONSTANTS - Character limits by element type
# ============================================================

CHARACTER_LIMITS = {
    "feature_name": 30,
    "setting_name": 40,
    "menu_item": 25,
    "tab_label": 15,
    "navigation_item": 20,
    "button_label": 25
}

WORD_LIMITS = {
    "feature_name": 3,
    "setting_name": 4,
    "menu_item": 3,
    "tab_label": 2
}


class ElementType(Enum):
    FEATURE_NAME = "feature_name"
    SETTING_NAME = "setting_name"
    MENU_ITEM = "menu_item"
    TAB_LABEL = "tab_label"
    NAVIGATION_ITEM = "navigation_item"
    BUTTON_LABEL = "button_label"


class Severity(Enum):
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"


@dataclass
class ValidationIssue:
    """A single validation issue found in a name."""
    rule: str
    message: str
    severity: Severity
    suggestion: Optional[str] = None


@dataclass
class ValidationResult:
    """Complete validation result for a name."""
    name: str
    element_type: ElementType
    is_valid: bool
    issues: list[ValidationIssue] = field(default_factory=list)
    
    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "element_type": self.element_type.value,
            "is_valid": self.is_valid,
            "issues": [
                {
                    "rule": issue.rule,
                    "message": issue.message,
                    "severity": issue.severity.value,
                    "suggestion": issue.suggestion
                }
                for issue in self.issues
            ]
        }


def check_banned_terms(name: str) -> list[ValidationIssue]:
    """Check name for banned terms."""
    issues = []
    name_lower = name.lower()
    words = set(re.findall(r'\b\w+\b', name_lower))
    
    # Check single-word banned terms
    for term in ALL_BANNED_TERMS:
        if term in words or term in name_lower:
            category = get_ban_category(term)
            issues.append(ValidationIssue(
                rule="BANNED_TERM",
                message=f"Contains banned term '{term}' ({category})",
                severity=Severity.ERROR,
                suggestion=f"Replace '{term}' with approved alternative"
            ))
    
    # Check multi-word banned phrases
    multi_word_banned = {"of course", "as you know", "sanity check", "100%"}
    for phrase in multi_word_banned:
        if phrase in name_lower:
            issues.append(ValidationIssue(
                rule="BANNED_PHRASE",
                message=f"Contains banned phrase '{phrase}'",
                severity=Severity.ERROR,
                suggestion=f"Remove or replace '{phrase}'"
            ))
    
    return issues


def get_ban_category(term: str) -> str:
    """Get the category a banned term belongs to."""
    if term in BANNED_TECHNICAL_JARGON:
        return "technical jargon"
    if term in BANNED_AMBIGUOUS_VERBS:
        return "ambiguous verb"
    if term in BANNED_ABSOLUTIST:
        return "absolutist language"
    if term in BANNED_NEGATIVE:
        return "negative/alarming"
    if term in BANNED_EXCLUSIONARY:
        return "exclusionary language"
    if term in BANNED_LEGAL_RISK:
        return "legal/compliance risk"
    return "unknown category"


def check_character_limit(name: str, element_type: ElementType) -> list[ValidationIssue]:
    """Check if name exceeds character limit for element type."""
    issues = []
    limit = CHARACTER_LIMITS.get(element_type.value)
    
    if limit and len(name) > limit:
        issues.append(ValidationIssue(
            rule="CHARACTER_LIMIT",
            message=f"Exceeds {limit} character limit ({len(name)} chars)",
            severity=Severity.ERROR,
            suggestion=f"Shorten to {limit} characters or fewer"
        ))
    
    return issues


def check_word_limit(name: str, element_type: ElementType) -> list[ValidationIssue]:
    """Check if name exceeds word limit for element type."""
    issues = []
    limit = WORD_LIMITS.get(element_type.value)
    
    if limit:
        words = name.split()
        if len(words) > limit:
            issues.append(ValidationIssue(
                rule="WORD_LIMIT",
                message=f"Exceeds {limit} word limit ({len(words)} words)",
                severity=Severity.WARNING,
                suggestion=f"Reduce to {limit} words or fewer"
            ))
    
    return issues


def check_capitalization(name: str) -> list[ValidationIssue]:
    """Check for sentence case capitalization."""
    issues = []
    
    # Check if first letter is capitalized
    if name and not name[0].isupper():
        issues.append(ValidationIssue(
            rule="CAPITALIZATION",
            message="Should start with capital letter (sentence case)",
            severity=Severity.WARNING,
            suggestion=name[0].upper() + name[1:] if len(name) > 1 else name.upper()
        ))
    
    # Check for all caps (excluding acronyms)
    words = name.split()
    for word in words[1:]:  # Skip first word
        if word.isupper() and len(word) > 3:  # Allow short acronyms
            issues.append(ValidationIssue(
                rule="CAPITALIZATION",
                message=f"'{word}' appears to be ALL CAPS (use sentence case)",
                severity=Severity.WARNING,
                suggestion=word.capitalize()
            ))
    
    return issues


def check_punctuation(name: str, element_type: ElementType) -> list[ValidationIssue]:
    """Check for prohibited punctuation."""
    issues = []
    
    # No trailing punctuation for most elements
    if name and name[-1] in '.!?':
        issues.append(ValidationIssue(
            rule="PUNCTUATION",
            message="Should not end with punctuation",
            severity=Severity.WARNING,
            suggestion=name.rstrip('.!?')
        ))
    
    # No ellipsis in names
    if '...' in name:
        issues.append(ValidationIssue(
            rule="PUNCTUATION",
            message="Should not contain ellipsis",
            severity=Severity.WARNING,
            suggestion=name.replace('...', '')
        ))
    
    return issues


def check_structure(name: str, element_type: ElementType) -> list[ValidationIssue]:
    """Check grammatical structure based on element type."""
    issues = []
    words = name.split()
    
    if not words:
        return issues
    
    first_word = words[0].lower()
    
    # Feature names should be verb + noun (for action features)
    # Settings should be noun phrases
    if element_type == ElementType.SETTING_NAME:
        # Common verbs that shouldn't start setting names
        verb_starters = {'enable', 'disable', 'show', 'hide', 'allow', 'turn', 'set'}
        if first_word in verb_starters:
            issues.append(ValidationIssue(
                rule="STRUCTURE",
                message="Settings should use noun phrases, not verb phrases",
                severity=Severity.WARNING,
                suggestion=f"Consider using just the feature noun (toggle implies enable/disable)"
            ))
    
    return issues


def validate_name(name: str, element_type: ElementType) -> ValidationResult:
    """Validate a single name against all rules."""
    issues = []
    
    # Run all checks
    issues.extend(check_banned_terms(name))
    issues.extend(check_character_limit(name, element_type))
    issues.extend(check_word_limit(name, element_type))
    issues.extend(check_capitalization(name))
    issues.extend(check_punctuation(name, element_type))
    issues.extend(check_structure(name, element_type))
    
    # Determine validity (errors make it invalid, warnings don't)
    has_errors = any(issue.severity == Severity.ERROR for issue in issues)
    
    return ValidationResult(
        name=name,
        element_type=element_type,
        is_valid=not has_errors,
        issues=issues
    )


def validate_batch(names: list[dict]) -> list[dict]:
    """Validate multiple names from JSON input."""
    results = []
    
    for item in names:
        name = item.get("name", "")
        type_str = item.get("type", "feature_name")
        
        try:
            element_type = ElementType(type_str)
        except ValueError:
            element_type = ElementType.FEATURE_NAME
        
        result = validate_name(name, element_type)
        results.append(result.to_dict())
    
    return results


def main():
    parser = argparse.ArgumentParser(
        description="Validate feature and setting names"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    
    # Single name validation
    single_parser = subparsers.add_parser("validate", help="Validate a single name")
    single_parser.add_argument("name", help="The name to validate")
    single_parser.add_argument(
        "--type", "-t",
        choices=[e.value for e in ElementType],
        default="feature_name",
        help="Type of UI element"
    )
    
    # Batch validation from file
    batch_parser = subparsers.add_parser("batch", help="Validate names from JSON file")
    batch_parser.add_argument("input", help="Input JSON file with names to validate")
    batch_parser.add_argument("--output", "-o", help="Output file for results")
    
    # Check term
    check_parser = subparsers.add_parser("check-term", help="Check if a term is banned")
    check_parser.add_argument("term", help="Term to check")
    
    args = parser.parse_args()
    
    if args.command == "validate":
        element_type = ElementType(args.type)
        result = validate_name(args.name, element_type)
        print(json.dumps(result.to_dict(), indent=2))
        sys.exit(0 if result.is_valid else 1)
    
    elif args.command == "batch":
        with open(args.input, 'r', encoding='utf-8') as f:
            names = json.load(f)
        
        results = validate_batch(names)
        output = json.dumps(results, indent=2)
        
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(output)
            print(f"Results written to {args.output}")
        else:
            print(output)
        
        # Exit with error if any names invalid
        invalid_count = sum(1 for r in results if not r["is_valid"])
        if invalid_count:
            print(f"\n{invalid_count} of {len(results)} names have errors", file=sys.stderr)
            sys.exit(1)
    
    elif args.command == "check-term":
        term = args.term.lower()
        if term in ALL_BANNED_TERMS:
            category = get_ban_category(term)
            print(f"BANNED: '{term}' is banned ({category})")
            sys.exit(1)
        else:
            print(f"OK: '{term}' is not in the banned terms list")
            sys.exit(0)
    
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
