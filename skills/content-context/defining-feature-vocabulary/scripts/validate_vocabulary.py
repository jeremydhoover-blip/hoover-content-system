#!/usr/bin/env python3
"""
Validate a feature vocabulary document for completeness and conflict detection.

Usage:
    python validate_vocabulary.py <path-to-vocabulary.md>

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
# Minimum vocabulary entries: at least 3 terms for a meaningful vocabulary
MIN_TERMS = 3
# Minimum definition length: enough to be meaningful (not just a synonym)
MIN_DEFINITION_LENGTH = 20
# Characters that indicate a prohibited alternatives section
PROHIBITED_MARKERS = ['prohibited', 'don\'t use', 'avoid', 'not this', 'instead of']


class ValidationResult(NamedTuple):
    passed: bool
    message: str


def extract_vocabulary_table(content: str) -> list[dict]:
    """Extract terms from vocabulary table."""
    terms = []
    
    # Find vocabulary table
    table_match = re.search(
        r'\|\s*Term\s*\|[^\n]+\n\|[-|\s]+\n((?:\|[^\n]+\n)+)', 
        content, 
        re.IGNORECASE
    )
    
    if not table_match:
        return terms
    
    rows = table_match.group(1).strip().split('\n')
    for row in rows:
        cells = [c.strip() for c in row.split('|')[1:-1]]
        if len(cells) >= 3:
            terms.append({
                'term': cells[0],
                'definition': cells[1] if len(cells) > 1 else '',
                'prohibited': cells[3] if len(cells) > 3 else ''
            })
    
    return terms


def extract_detailed_definitions(content: str) -> dict[str, dict]:
    """Extract detailed term definitions from ### sections."""
    definitions = {}
    
    # Find all ### Term sections under ## Detailed definitions
    detailed_section = re.search(
        r'## Detailed definitions\s*\n(.*?)(?=\n## |$)', 
        content, 
        re.DOTALL
    )
    
    if not detailed_section:
        return definitions
    
    section_content = detailed_section.group(1)
    term_sections = re.findall(
        r'###\s+([^\n]+)\n(.*?)(?=###|$)', 
        section_content, 
        re.DOTALL
    )
    
    for term_name, term_body in term_sections:
        term_name = term_name.strip()
        definitions[term_name] = {
            'has_canonical': '**Canonical form:**' in term_body,
            'has_definition': '**Definition:**' in term_body,
            'has_usage': '**Usage context:**' in term_body,
            'has_prohibited': '**Prohibited alternatives:**' in term_body,
            'has_examples': 'Examples:' in term_body or '✓' in term_body,
            'definition_text': ''
        }
        
        # Extract definition text
        def_match = re.search(r'\*\*Definition:\*\*\s*(.+?)(?=\*\*|$)', term_body)
        if def_match:
            definitions[term_name]['definition_text'] = def_match.group(1).strip()
    
    return definitions


def validate_metadata(content: str) -> list[ValidationResult]:
    """Validate required metadata fields."""
    results = []
    
    if '## Metadata' not in content:
        results.append(ValidationResult(False, "Missing '## Metadata' section"))
        return results
    
    required_fields = ['Feature:', 'Version:', 'Last updated:', 'Owner:']
    for field in required_fields:
        if f'**{field}**' not in content:
            results.append(ValidationResult(False, f"Missing metadata field: {field}"))
        else:
            results.append(ValidationResult(True, f"Metadata field present: {field}"))
    
    return results


def validate_vocabulary_table(content: str) -> list[ValidationResult]:
    """Validate vocabulary table presence and structure."""
    results = []
    
    terms = extract_vocabulary_table(content)
    
    if len(terms) < MIN_TERMS:
        results.append(ValidationResult(False, f"Need at least {MIN_TERMS} terms, found {len(terms)}"))
    else:
        results.append(ValidationResult(True, f"Found {len(terms)} terms in vocabulary table"))
    
    # Check for prohibited alternatives column
    has_prohibited = any(term.get('prohibited', '').strip() for term in terms)
    if not has_prohibited:
        results.append(ValidationResult(False, "Vocabulary table missing prohibited alternatives"))
    else:
        results.append(ValidationResult(True, "Prohibited alternatives column present"))
    
    return results


def validate_definitions(content: str) -> list[ValidationResult]:
    """Validate detailed definitions for each term."""
    results = []
    
    definitions = extract_detailed_definitions(content)
    
    if not definitions:
        results.append(ValidationResult(False, "No detailed definitions found"))
        return results
    
    results.append(ValidationResult(True, f"Found {len(definitions)} detailed definitions"))
    
    for term_name, term_info in definitions.items():
        # Check required sections
        if not term_info['has_definition']:
            results.append(ValidationResult(False, f"Term '{term_name}': Missing definition"))
        else:
            # Check definition length
            if len(term_info['definition_text']) < MIN_DEFINITION_LENGTH:
                results.append(ValidationResult(False, f"Term '{term_name}': Definition too short (min {MIN_DEFINITION_LENGTH} chars)"))
            # Check for circular definition
            if term_name.lower() in term_info['definition_text'].lower().split()[:5]:
                results.append(ValidationResult(False, f"Term '{term_name}': Definition may be circular (uses term to define itself)"))
        
        if not term_info['has_prohibited']:
            results.append(ValidationResult(False, f"Term '{term_name}': Missing prohibited alternatives"))
        
        if not term_info['has_usage']:
            results.append(ValidationResult(False, f"Term '{term_name}': Missing usage context"))
        
        if not term_info['has_examples']:
            results.append(ValidationResult(False, f"Term '{term_name}': Missing examples"))
    
    return results


def detect_conflicts(content: str) -> list[ValidationResult]:
    """Detect potential terminology conflicts."""
    results = []
    
    terms = extract_vocabulary_table(content)
    definitions = extract_detailed_definitions(content)
    
    # Check for duplicate terms (case-insensitive)
    term_names = [t['term'].lower() for t in terms]
    seen = set()
    duplicates = []
    for name in term_names:
        if name in seen:
            duplicates.append(name)
        seen.add(name)
    
    if duplicates:
        results.append(ValidationResult(False, f"Duplicate terms detected: {duplicates}"))
    else:
        results.append(ValidationResult(True, "No duplicate terms"))
    
    # Check for terms appearing in each other's prohibited lists
    term_to_prohibited = {}
    for term in terms:
        prohibited = term.get('prohibited', '').lower()
        term_to_prohibited[term['term'].lower()] = prohibited
    
    for term_name, prohibited in term_to_prohibited.items():
        for other_term in term_to_prohibited.keys():
            if other_term != term_name and other_term in prohibited:
                results.append(ValidationResult(False, f"Term '{other_term}' appears as prohibited alternative for '{term_name}' but is also a canonical term"))
    
    return results


def validate_cross_feature_alignment(content: str) -> list[ValidationResult]:
    """Check for cross-feature alignment section."""
    results = []
    
    if '## Cross-feature alignment' not in content:
        results.append(ValidationResult(False, "Missing '## Cross-feature alignment' section"))
    else:
        results.append(ValidationResult(True, "Cross-feature alignment section present"))
    
    return results


def main():
    if len(sys.argv) != 2:
        print("Usage: python validate_vocabulary.py <path-to-vocabulary.md>")
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
    all_results.extend(validate_metadata(content))
    all_results.extend(validate_vocabulary_table(content))
    all_results.extend(validate_definitions(content))
    all_results.extend(detect_conflicts(content))
    all_results.extend(validate_cross_feature_alignment(content))
    
    # Print results
    print(f"\nVocabulary Validation: {file_path.name}\n")
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
