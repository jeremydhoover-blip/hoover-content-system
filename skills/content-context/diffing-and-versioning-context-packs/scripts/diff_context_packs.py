#!/usr/bin/env python3
"""
Context Pack Diff Tool

Compares two context pack versions and generates a semantic diff report.
Classifies changes as breaking, additive, or corrective.
Recommends version increment based on semver rules.

Usage:
    python diff_context_packs.py <base.yaml> <head.yaml>
    python diff_context_packs.py <base.json> <head.json>

Output:
    JSON diff report with change classification and version recommendation

Exit codes:
    0: Success
    1: Breaking changes detected
    2: Error (invalid input)
"""

import sys
import json
import re
from pathlib import Path
from dataclasses import dataclass, field
from typing import Any, Optional
from enum import Enum


class ChangeType(Enum):
    BREAKING = "breaking"
    ADDITIVE = "additive"
    CORRECTIVE = "corrective"


class VersionBump(Enum):
    MAJOR = "MAJOR"
    MINOR = "MINOR"
    PATCH = "PATCH"
    NONE = "NONE"


@dataclass
class Change:
    code: str
    change_type: ChangeType
    section: str
    description: str
    base_value: Any = None
    head_value: Any = None
    migration: str = ""


@dataclass
class DiffResult:
    pack_name: str = "unknown"
    base_version: str = "unknown"
    head_version: str = "unknown"
    changes: list = field(default_factory=list)
    
    @property
    def breaking(self) -> list:
        return [c for c in self.changes if c.change_type == ChangeType.BREAKING]
    
    @property
    def additive(self) -> list:
        return [c for c in self.changes if c.change_type == ChangeType.ADDITIVE]
    
    @property
    def corrective(self) -> list:
        return [c for c in self.changes if c.change_type == ChangeType.CORRECTIVE]
    
    @property
    def version_bump(self) -> VersionBump:
        if self.breaking:
            return VersionBump.MAJOR
        if self.additive:
            return VersionBump.MINOR
        if self.corrective:
            return VersionBump.PATCH
        return VersionBump.NONE
    
    @property
    def recommended_version(self) -> str:
        if self.base_version == "unknown":
            return "unknown"
        
        try:
            parts = self.base_version.split(".")
            major, minor, patch = int(parts[0]), int(parts[1]), int(parts[2].split("-")[0])
        except (ValueError, IndexError):
            return "unknown"
        
        bump = self.version_bump
        if bump == VersionBump.MAJOR:
            return f"{major + 1}.0.0"
        elif bump == VersionBump.MINOR:
            return f"{major}.{minor + 1}.0"
        elif bump == VersionBump.PATCH:
            return f"{major}.{minor}.{patch + 1}"
        return self.base_version
    
    def to_json(self) -> dict:
        return {
            "pack": self.pack_name,
            "base_version": self.base_version,
            "head_version": self.head_version,
            "recommended_version": self.recommended_version,
            "increment_type": self.version_bump.value,
            "summary": {
                "breaking": len(self.breaking),
                "additive": len(self.additive),
                "corrective": len(self.corrective)
            },
            "breaking": [
                {
                    "code": c.code,
                    "section": c.section,
                    "description": c.description,
                    "migration": c.migration
                }
                for c in self.breaking
            ],
            "additive": [
                {
                    "code": c.code,
                    "section": c.section,
                    "description": c.description
                }
                for c in self.additive
            ],
            "corrective": [
                {
                    "code": c.code,
                    "section": c.section,
                    "description": c.description
                }
                for c in self.corrective
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
            return json.loads(content)
    else:
        return json.loads(content)


def is_typo_fix(old_val: str, new_val: str) -> bool:
    """Detect if change is a typo fix (high similarity, low edit distance)."""
    if not isinstance(old_val, str) or not isinstance(new_val, str):
        return False
    
    # Simple Levenshtein-like check: same length, few character differences
    if abs(len(old_val) - len(new_val)) > 3:
        return False
    
    # Count character differences
    differences = sum(1 for a, b in zip(old_val.lower(), new_val.lower()) if a != b)
    differences += abs(len(old_val) - len(new_val))
    
    # Threshold: 3 or fewer character differences is likely a typo
    return differences <= 3


def is_clarification(old_val: str, new_val: str) -> bool:
    """Detect if change is a clarification (superset of old meaning)."""
    if not isinstance(old_val, str) or not isinstance(new_val, str):
        return False
    
    old_words = set(old_val.lower().split())
    new_words = set(new_val.lower().split())
    
    # If all old words appear in new text, likely a clarification
    return old_words.issubset(new_words) and len(new_words) > len(old_words)


def is_meaning_change(old_val: str, new_val: str) -> bool:
    """Detect if change alters meaning (key nouns/verbs changed)."""
    if not isinstance(old_val, str) or not isinstance(new_val, str):
        return True  # Non-string changes are breaking by default
    
    # Extract key words (nouns, verbs - simplified as words > 4 chars)
    old_keywords = {w.lower() for w in old_val.split() if len(w) > 4}
    new_keywords = {w.lower() for w in new_val.split() if len(w) > 4}
    
    # If keywords significantly differ, meaning changed
    if not old_keywords or not new_keywords:
        return False
    
    overlap = len(old_keywords & new_keywords)
    total = len(old_keywords | new_keywords)
    
    # Less than 50% keyword overlap suggests meaning change
    return overlap / total < 0.5 if total > 0 else False


def diff_states(base: dict, head: dict, result: DiffResult, counters: dict) -> None:
    """Diff states section."""
    base_states = base.get("states", {})
    head_states = head.get("states", {})
    
    base_keys = set(base_states.keys())
    head_keys = set(head_states.keys())
    
    # Removed states (breaking)
    for state in base_keys - head_keys:
        counters["break"] += 1
        result.changes.append(Change(
            code=f"BREAK-{counters['break']:03d}",
            change_type=ChangeType.BREAKING,
            section=f"states.{state}",
            description=f"State removed: {state}",
            base_value=base_states[state],
            migration=f"Remove all content referencing '{state}' state"
        ))
    
    # Added states (additive)
    for state in head_keys - base_keys:
        counters["add"] += 1
        result.changes.append(Change(
            code=f"ADD-{counters['add']:03d}",
            change_type=ChangeType.ADDITIVE,
            section=f"states.{state}",
            description=f"State added: {state}",
            head_value=head_states[state]
        ))
    
    # Modified states
    for state in base_keys & head_keys:
        base_state = base_states[state]
        head_state = head_states[state]
        
        if base_state == head_state:
            continue
        
        # Check each field
        for field_name in ["entry", "exit", "content_guidance", "error_handling"]:
            old_val = base_state.get(field_name)
            new_val = head_state.get(field_name)
            
            if old_val == new_val:
                continue
            
            if old_val is None and new_val is not None:
                counters["add"] += 1
                result.changes.append(Change(
                    code=f"ADD-{counters['add']:03d}",
                    change_type=ChangeType.ADDITIVE,
                    section=f"states.{state}.{field_name}",
                    description=f"Field added to state {state}: {field_name}",
                    head_value=new_val
                ))
            elif old_val is not None and new_val is None:
                counters["break"] += 1
                result.changes.append(Change(
                    code=f"BREAK-{counters['break']:03d}",
                    change_type=ChangeType.BREAKING,
                    section=f"states.{state}.{field_name}",
                    description=f"Field removed from state {state}: {field_name}",
                    base_value=old_val,
                    migration=f"Update content that depends on {field_name}"
                ))
            elif is_typo_fix(str(old_val), str(new_val)):
                counters["corr"] += 1
                result.changes.append(Change(
                    code=f"CORR-{counters['corr']:03d}",
                    change_type=ChangeType.CORRECTIVE,
                    section=f"states.{state}.{field_name}",
                    description=f"Typo fixed in {state}.{field_name}",
                    base_value=old_val,
                    head_value=new_val
                ))
            elif is_clarification(str(old_val), str(new_val)):
                counters["corr"] += 1
                result.changes.append(Change(
                    code=f"CORR-{counters['corr']:03d}",
                    change_type=ChangeType.CORRECTIVE,
                    section=f"states.{state}.{field_name}",
                    description=f"Clarification in {state}.{field_name}",
                    base_value=old_val,
                    head_value=new_val
                ))
            elif is_meaning_change(str(old_val), str(new_val)):
                counters["break"] += 1
                result.changes.append(Change(
                    code=f"BREAK-{counters['break']:03d}",
                    change_type=ChangeType.BREAKING,
                    section=f"states.{state}.{field_name}",
                    description=f"Meaning changed in {state}.{field_name}",
                    base_value=old_val,
                    head_value=new_val,
                    migration=f"Review content using {state} state"
                ))
            else:
                counters["corr"] += 1
                result.changes.append(Change(
                    code=f"CORR-{counters['corr']:03d}",
                    change_type=ChangeType.CORRECTIVE,
                    section=f"states.{state}.{field_name}",
                    description=f"Updated {state}.{field_name}",
                    base_value=old_val,
                    head_value=new_val
                ))


def diff_vocabulary(base: dict, head: dict, result: DiffResult, counters: dict) -> None:
    """Diff vocabulary section."""
    base_vocab = base.get("vocabulary", {})
    head_vocab = head.get("vocabulary", {})
    
    base_terms = set(base_vocab.keys())
    head_terms = set(head_vocab.keys())
    
    # Removed terms (breaking)
    for term in base_terms - head_terms:
        counters["break"] += 1
        result.changes.append(Change(
            code=f"BREAK-{counters['break']:03d}",
            change_type=ChangeType.BREAKING,
            section=f"vocabulary.{term}",
            description=f"Vocabulary term removed: {term}",
            base_value=base_vocab[term],
            migration=f"Replace all uses of '{term}' with new terminology"
        ))
    
    # Added terms (additive)
    for term in head_terms - base_terms:
        counters["add"] += 1
        result.changes.append(Change(
            code=f"ADD-{counters['add']:03d}",
            change_type=ChangeType.ADDITIVE,
            section=f"vocabulary.{term}",
            description=f"Vocabulary term added: {term}",
            head_value=head_vocab[term]
        ))
    
    # Modified terms
    for term in base_terms & head_terms:
        old_def = base_vocab[term]
        new_def = head_vocab[term]
        
        if old_def == new_def:
            continue
        
        if is_typo_fix(str(old_def), str(new_def)):
            counters["corr"] += 1
            result.changes.append(Change(
                code=f"CORR-{counters['corr']:03d}",
                change_type=ChangeType.CORRECTIVE,
                section=f"vocabulary.{term}",
                description=f"Typo fixed in definition of '{term}'",
                base_value=old_def,
                head_value=new_def
            ))
        elif is_meaning_change(str(old_def), str(new_def)):
            counters["break"] += 1
            result.changes.append(Change(
                code=f"BREAK-{counters['break']:03d}",
                change_type=ChangeType.BREAKING,
                section=f"vocabulary.{term}",
                description=f"Definition meaning changed: {term}",
                base_value=old_def,
                head_value=new_def,
                migration=f"Review all content using '{term}'"
            ))
        else:
            counters["corr"] += 1
            result.changes.append(Change(
                code=f"CORR-{counters['corr']:03d}",
                change_type=ChangeType.CORRECTIVE,
                section=f"vocabulary.{term}",
                description=f"Definition clarified: {term}",
                base_value=old_def,
                head_value=new_def
            ))


def diff_array_section(base: dict, head: dict, section: str, 
                       result: DiffResult, counters: dict,
                       removal_breaking: bool = True) -> None:
    """Diff an array section (user_goals, core_actions)."""
    base_items = set(base.get(section, []))
    head_items = set(head.get(section, []))
    
    # Removed items
    for item in base_items - head_items:
        if removal_breaking:
            counters["break"] += 1
            result.changes.append(Change(
                code=f"BREAK-{counters['break']:03d}",
                change_type=ChangeType.BREAKING,
                section=section,
                description=f"Removed from {section}: {item}",
                base_value=item,
                migration=f"Remove references to '{item}'"
            ))
        else:
            counters["corr"] += 1
            result.changes.append(Change(
                code=f"CORR-{counters['corr']:03d}",
                change_type=ChangeType.CORRECTIVE,
                section=section,
                description=f"Removed from {section}: {item}",
                base_value=item
            ))
    
    # Added items
    for item in head_items - base_items:
        counters["add"] += 1
        result.changes.append(Change(
            code=f"ADD-{counters['add']:03d}",
            change_type=ChangeType.ADDITIVE,
            section=section,
            description=f"Added to {section}: {item}",
            head_value=item
        ))


def diff_error_taxonomy(base: dict, head: dict, result: DiffResult, counters: dict) -> None:
    """Diff error taxonomy section."""
    base_errors = {e.get("code"): e for e in base.get("error_taxonomy", [])}
    head_errors = {e.get("code"): e for e in head.get("error_taxonomy", [])}
    
    base_codes = set(base_errors.keys())
    head_codes = set(head_errors.keys())
    
    # Removed errors (breaking)
    for code in base_codes - head_codes:
        counters["break"] += 1
        result.changes.append(Change(
            code=f"BREAK-{counters['break']:03d}",
            change_type=ChangeType.BREAKING,
            section=f"error_taxonomy.{code}",
            description=f"Error code removed: {code}",
            base_value=base_errors[code],
            migration=f"Update error handling for '{code}'"
        ))
    
    # Added errors (additive)
    for code in head_codes - base_codes:
        counters["add"] += 1
        result.changes.append(Change(
            code=f"ADD-{counters['add']:03d}",
            change_type=ChangeType.ADDITIVE,
            section=f"error_taxonomy.{code}",
            description=f"Error code added: {code}",
            head_value=head_errors[code]
        ))
    
    # Modified errors
    for code in base_codes & head_codes:
        base_err = base_errors[code]
        head_err = head_errors[code]
        
        if base_err == head_err:
            continue
        
        # Check message pattern changes
        old_msg = base_err.get("message_pattern", "")
        new_msg = head_err.get("message_pattern", "")
        
        if old_msg != new_msg:
            if is_typo_fix(old_msg, new_msg):
                counters["corr"] += 1
                result.changes.append(Change(
                    code=f"CORR-{counters['corr']:03d}",
                    change_type=ChangeType.CORRECTIVE,
                    section=f"error_taxonomy.{code}.message_pattern",
                    description=f"Error message typo fixed: {code}",
                    base_value=old_msg,
                    head_value=new_msg
                ))
            else:
                counters["corr"] += 1
                result.changes.append(Change(
                    code=f"CORR-{counters['corr']:03d}",
                    change_type=ChangeType.CORRECTIVE,
                    section=f"error_taxonomy.{code}.message_pattern",
                    description=f"Error message updated: {code}",
                    base_value=old_msg,
                    head_value=new_msg
                ))


def diff(base: dict, head: dict) -> DiffResult:
    """Run full diff and return result."""
    result = DiffResult()
    counters = {"break": 0, "add": 0, "corr": 0}
    
    # Extract metadata
    if "feature" in base:
        result.pack_name = base["feature"].get("name", "unknown")
        result.base_version = base["feature"].get("version", "unknown")
    
    if "feature" in head:
        result.head_version = head["feature"].get("version", result.base_version)
    
    # Diff each section
    diff_states(base, head, result, counters)
    diff_vocabulary(base, head, result, counters)
    diff_array_section(base, head, "user_goals", result, counters, removal_breaking=True)
    diff_array_section(base, head, "core_actions", result, counters, removal_breaking=True)
    diff_error_taxonomy(base, head, result, counters)
    
    return result


def main():
    if len(sys.argv) < 3:
        print("Usage: python diff_context_packs.py <base.yaml> <head.yaml>", file=sys.stderr)
        sys.exit(2)
    
    base_path = Path(sys.argv[1])
    head_path = Path(sys.argv[2])
    
    for p in [base_path, head_path]:
        if not p.exists():
            print(f"Error: File not found: {p}", file=sys.stderr)
            sys.exit(2)
    
    try:
        base = load_context_pack(base_path)
        head = load_context_pack(head_path)
    except Exception as e:
        print(f"Error: Failed to parse files: {e}", file=sys.stderr)
        sys.exit(2)
    
    result = diff(base, head)
    
    # Output JSON result
    print(json.dumps(result.to_json(), indent=2))
    
    # Exit with 1 if breaking changes
    if result.breaking:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
