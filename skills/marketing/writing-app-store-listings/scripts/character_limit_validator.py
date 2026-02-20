#!/usr/bin/env python3
"""
App Store Listing Character Limit Validator

Validates app store listing content against iOS App Store and Google Play
character limits. Returns pass/fail status with specific violations.

Usage:
    python character_limit_validator.py <listing_file.md>
    python character_limit_validator.py --platform ios <listing_file.md>
    python character_limit_validator.py --platform android <listing_file.md>
"""

import argparse
import re
import sys
from dataclasses import dataclass
from typing import Optional

# Platform character limits (source: Apple/Google documentation, verified Feb 2026)
IOS_LIMITS = {
    "app_name": 30,
    "subtitle": 30,
    "promotional_text": 170,
    "description": 4000,
    "keywords": 100,
    "whats_new": 4000,
}

ANDROID_LIMITS = {
    "app_name": 30,
    "short_description": 80,
    "full_description": 4000,
    "whats_new": 500,
}


@dataclass
class ValidationResult:
    field: str
    content: str
    limit: int
    actual: int
    passed: bool

    def __str__(self) -> str:
        status = "✓ PASS" if self.passed else "✗ FAIL"
        return f"{status}: {self.field} ({self.actual}/{self.limit} chars)"


def count_characters(text: str) -> int:
    """
    Count characters as app stores do.
    Strips leading/trailing whitespace but preserves internal formatting.
    """
    return len(text.strip())


def extract_field(content: str, field_header: str) -> Optional[str]:
    """
    Extract content under a markdown header.
    Returns content between the header and the next header of same or higher level.
    """
    # Match ## Header or variations
    pattern = rf"##\s*{re.escape(field_header)}\s*\n(.*?)(?=\n##\s|\Z)"
    match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return None


def validate_ios(content: str) -> list[ValidationResult]:
    """Validate content against iOS App Store limits."""
    results = []
    
    field_mapping = {
        "app_name": ["App Name", "Name"],
        "subtitle": ["Subtitle"],
        "promotional_text": ["Promotional Text", "Promo Text"],
        "description": ["Description"],
        "keywords": ["Keywords"],
        "whats_new": ["What's New", "Whats New", "Release Notes"],
    }
    
    for field, headers in field_mapping.items():
        limit = IOS_LIMITS[field]
        extracted = None
        
        for header in headers:
            extracted = extract_field(content, header)
            if extracted:
                break
        
        if extracted:
            char_count = count_characters(extracted)
            results.append(ValidationResult(
                field=field,
                content=extracted[:50] + "..." if len(extracted) > 50 else extracted,
                limit=limit,
                actual=char_count,
                passed=char_count <= limit
            ))
    
    return results


def validate_android(content: str) -> list[ValidationResult]:
    """Validate content against Google Play Store limits."""
    results = []
    
    field_mapping = {
        "app_name": ["App Name", "Name"],
        "short_description": ["Short Description", "Short Desc"],
        "full_description": ["Full Description", "Description"],
        "whats_new": ["What's New", "Whats New", "Release Notes"],
    }
    
    for field, headers in field_mapping.items():
        limit = ANDROID_LIMITS[field]
        extracted = None
        
        for header in headers:
            extracted = extract_field(content, header)
            if extracted:
                break
        
        if extracted:
            char_count = count_characters(extracted)
            results.append(ValidationResult(
                field=field,
                content=extracted[:50] + "..." if len(extracted) > 50 else extracted,
                limit=limit,
                actual=char_count,
                passed=char_count <= limit
            ))
    
    return results


def detect_platform(content: str) -> str:
    """Auto-detect platform based on field presence."""
    if "subtitle" in content.lower() or "promotional text" in content.lower():
        return "ios"
    if "short description" in content.lower():
        return "android"
    return "both"


def main():
    parser = argparse.ArgumentParser(
        description="Validate app store listing character limits"
    )
    parser.add_argument("file", help="Markdown file containing listing content")
    parser.add_argument(
        "--platform",
        choices=["ios", "android", "both"],
        default="auto",
        help="Target platform (default: auto-detect)"
    )
    
    args = parser.parse_args()
    
    try:
        with open(args.file, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File not found: {args.file}", file=sys.stderr)
        sys.exit(1)
    except IOError as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)
    
    platform = args.platform if args.platform != "auto" else detect_platform(content)
    
    all_results = []
    
    if platform in ("ios", "both"):
        print("\n=== iOS App Store Validation ===")
        ios_results = validate_ios(content)
        for result in ios_results:
            print(result)
        all_results.extend(ios_results)
    
    if platform in ("android", "both"):
        print("\n=== Google Play Store Validation ===")
        android_results = validate_android(content)
        for result in android_results:
            print(result)
        all_results.extend(android_results)
    
    # Summary
    if not all_results:
        print("\nWarning: No fields detected. Check file format.", file=sys.stderr)
        sys.exit(1)
    
    passed = sum(1 for r in all_results if r.passed)
    total = len(all_results)
    
    print(f"\n=== Summary: {passed}/{total} fields passed ===")
    
    if passed < total:
        print("\nFailed fields:")
        for r in all_results:
            if not r.passed:
                over = r.actual - r.limit
                print(f"  - {r.field}: {over} characters over limit")
        sys.exit(1)
    
    print("\nAll character limits validated.")
    sys.exit(0)


if __name__ == "__main__":
    main()
