#!/usr/bin/env python3
"""
Tone linting script for voice and tone guidelines.

Validates that voice/tone documentation meets structural requirements:
- Required sections present
- Minimum principle count
- This/not-this contrasts exist
- Tone spectrum coverage

Usage:
    python tone_lint.py <path_to_voice_doc.md>

Exit codes:
    0 - All checks passed
    1 - Validation errors found
"""

import sys
import re
from pathlib import Path

# --- Constants (justified) ---
MIN_VOICE_PRINCIPLES = 3  # Minimum to establish differentiated voice
MAX_VOICE_PRINCIPLES = 5  # Beyond 5, principles become hard to remember/apply
MIN_TONE_ZONES = 4        # Need positive/neutral/warning/critical at minimum

REQUIRED_SECTIONS = [
    "voice principles",
    "tone spectrum",
]

REQUIRED_CONTRASTS = [
    ("we are:", "we are not:"),
    ("this:", "not this:"),
]


def load_document(filepath: str) -> str:
    """Load markdown document from file."""
    path = Path(filepath)
    if not path.exists():
        print(f"ERROR: File not found: {filepath}")
        sys.exit(1)
    if not path.suffix.lower() == ".md":
        print(f"ERROR: Expected markdown file, got: {path.suffix}")
        sys.exit(1)
    return path.read_text(encoding="utf-8")


def check_required_sections(content: str) -> list[str]:
    """Check that all required sections are present."""
    errors = []
    content_lower = content.lower()
    for section in REQUIRED_SECTIONS:
        if section not in content_lower:
            errors.append(f"Missing required section: '{section}'")
    return errors


def count_voice_principles(content: str) -> tuple[int, list[str]]:
    """Count voice principles and validate range."""
    errors = []
    # Match headers like "### 1. Principle name" or "### Principle name"
    principle_pattern = r"^###\s+\d*\.?\s*\w+"
    principles = re.findall(principle_pattern, content, re.MULTILINE)
    
    # Filter to only those under "voice principles" section
    voice_section_match = re.search(
        r"##\s*voice\s*principles(.*?)(?=\n##\s|\Z)",
        content,
        re.IGNORECASE | re.DOTALL
    )
    
    if not voice_section_match:
        return 0, ["Could not find voice principles section"]
    
    voice_section = voice_section_match.group(1)
    principle_count = len(re.findall(r"^###\s+", voice_section, re.MULTILINE))
    
    if principle_count < MIN_VOICE_PRINCIPLES:
        errors.append(
            f"Too few voice principles: {principle_count} "
            f"(minimum: {MIN_VOICE_PRINCIPLES})"
        )
    elif principle_count > MAX_VOICE_PRINCIPLES:
        errors.append(
            f"Too many voice principles: {principle_count} "
            f"(maximum: {MAX_VOICE_PRINCIPLES})"
        )
    
    return principle_count, errors


def check_contrasts(content: str) -> list[str]:
    """Verify this/not-this contrasts exist for principles."""
    errors = []
    content_lower = content.lower()
    
    for positive, negative in REQUIRED_CONTRASTS:
        positive_count = content_lower.count(positive)
        negative_count = content_lower.count(negative)
        
        if positive_count == 0:
            errors.append(f"Missing positive contrast pattern: '{positive}'")
        if negative_count == 0:
            errors.append(f"Missing negative contrast pattern: '{negative}'")
        if positive_count > 0 and negative_count > 0:
            if abs(positive_count - negative_count) > 1:
                errors.append(
                    f"Imbalanced contrasts: '{positive}' appears {positive_count}x, "
                    f"'{negative}' appears {negative_count}x"
                )
    
    return errors


def check_tone_spectrum(content: str) -> list[str]:
    """Validate tone spectrum table exists and has minimum rows."""
    errors = []
    
    # Find tone spectrum section
    spectrum_match = re.search(
        r"##\s*tone\s*spectrum(.*?)(?=\n##\s|\Z)",
        content,
        re.IGNORECASE | re.DOTALL
    )
    
    if not spectrum_match:
        errors.append("Tone spectrum section not found")
        return errors
    
    spectrum_section = spectrum_match.group(1)
    
    # Count table rows (lines starting with |)
    table_rows = re.findall(r"^\|[^-]", spectrum_section, re.MULTILINE)
    # Subtract header row
    data_rows = len(table_rows) - 1 if table_rows else 0
    
    if data_rows < MIN_TONE_ZONES:
        errors.append(
            f"Tone spectrum has {data_rows} zones "
            f"(minimum: {MIN_TONE_ZONES})"
        )
    
    return errors


def check_examples_present(content: str) -> list[str]:
    """Verify examples use realistic content, not placeholders."""
    errors = []
    
    # Check for placeholder patterns
    placeholder_patterns = [
        r"\[example\]",
        r"\[sample\]",
        r"\[your .*?\]",
        r"lorem ipsum",
        r"xxx",
        r"\.\.\.",
    ]
    
    for pattern in placeholder_patterns:
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            # Allow [...] in template references, check if in example blocks
            in_example = re.search(
                rf"(this:|not this:).*?{pattern}",
                content,
                re.IGNORECASE | re.DOTALL
            )
            if in_example:
                errors.append(
                    f"Placeholder found in examples: '{pattern}' - "
                    "use realistic content"
                )
    
    return errors


def main():
    """Run all validation checks."""
    if len(sys.argv) != 2:
        print("Usage: python tone_lint.py <path_to_voice_doc.md>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    content = load_document(filepath)
    
    all_errors = []
    
    # Run checks
    all_errors.extend(check_required_sections(content))
    
    principle_count, principle_errors = count_voice_principles(content)
    all_errors.extend(principle_errors)
    
    all_errors.extend(check_contrasts(content))
    all_errors.extend(check_tone_spectrum(content))
    all_errors.extend(check_examples_present(content))
    
    # Report results
    if all_errors:
        print(f"FAIL: {len(all_errors)} issue(s) found\n")
        for error in all_errors:
            print(f"  ✗ {error}")
        sys.exit(1)
    else:
        print(f"PASS: Voice and tone document is valid")
        print(f"  • {principle_count} voice principles defined")
        print(f"  • Required sections present")
        print(f"  • Contrasts balanced")
        sys.exit(0)


if __name__ == "__main__":
    main()
