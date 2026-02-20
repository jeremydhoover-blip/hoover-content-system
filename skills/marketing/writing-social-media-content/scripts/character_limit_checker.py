#!/usr/bin/env python3
"""
Social Media Character Limit Checker

Validates social media post content against platform-specific character limits.
Returns pass/fail status with specific violations and remaining characters.

Usage:
    python character_limit_checker.py <post_file.md>
    python character_limit_checker.py --platform twitter <post_file.md>
    python character_limit_checker.py --platform linkedin <post_file.md>
    python character_limit_checker.py --text "Your post content here" --platform twitter
"""

import argparse
import re
import sys
from dataclasses import dataclass
from typing import Optional

# Platform limits (verified Feb 2026)
# Source: Platform documentation and API specifications
PLATFORM_LIMITS = {
    "twitter": {
        "standard": 280,
        "premium": 25000,
        "link_cost": 23,  # t.co shortening
    },
    "linkedin": {
        "post": 3000,
        "optimal_min": 700,
        "optimal_max": 1300,
    },
    "instagram": {
        "caption": 2200,
        "visible_preview": 125,
    },
    "facebook": {
        "post": 63206,
        "optimal_max": 80,
    },
    "threads": {
        "post": 500,
    },
}


@dataclass
class ValidationResult:
    platform: str
    content_length: int
    limit: int
    passed: bool
    remaining: int
    warnings: list[str]

    def __str__(self) -> str:
        status = "✓ PASS" if self.passed else "✗ FAIL"
        result = f"{status}: {self.platform} ({self.content_length}/{self.limit} chars)"
        if self.remaining >= 0:
            result += f" — {self.remaining} remaining"
        else:
            result += f" — {abs(self.remaining)} over limit"
        return result


def count_characters(text: str, platform: str) -> int:
    """
    Count characters accounting for platform-specific rules.
    """
    text = text.strip()
    char_count = len(text)
    
    # Twitter: Links consume fixed 23 characters regardless of actual length
    if platform == "twitter":
        url_pattern = r'https?://\S+'
        urls = re.findall(url_pattern, text)
        for url in urls:
            # Remove actual URL length, add Twitter's shortened length
            char_count = char_count - len(url) + PLATFORM_LIMITS["twitter"]["link_cost"]
    
    return char_count


def count_hashtags(text: str) -> int:
    """Count hashtags in text."""
    return len(re.findall(r'#\w+', text))


def validate_twitter(content: str, premium: bool = False) -> ValidationResult:
    """Validate Twitter/X post."""
    limit = PLATFORM_LIMITS["twitter"]["premium"] if premium else PLATFORM_LIMITS["twitter"]["standard"]
    char_count = count_characters(content, "twitter")
    hashtag_count = count_hashtags(content)
    
    warnings = []
    if hashtag_count > 3:
        warnings.append(f"Too many hashtags ({hashtag_count}). Recommend 1-3 for engagement.")
    
    return ValidationResult(
        platform="Twitter/X" + (" Premium" if premium else ""),
        content_length=char_count,
        limit=limit,
        passed=char_count <= limit,
        remaining=limit - char_count,
        warnings=warnings
    )


def validate_linkedin(content: str) -> ValidationResult:
    """Validate LinkedIn post."""
    limit = PLATFORM_LIMITS["linkedin"]["post"]
    char_count = len(content.strip())
    hashtag_count = count_hashtags(content)
    
    warnings = []
    optimal_min = PLATFORM_LIMITS["linkedin"]["optimal_min"]
    optimal_max = PLATFORM_LIMITS["linkedin"]["optimal_max"]
    
    if char_count < optimal_min:
        warnings.append(f"Below optimal length ({char_count} chars). Consider {optimal_min}-{optimal_max} for best engagement.")
    elif char_count > optimal_max and char_count <= limit:
        warnings.append(f"Above optimal length. {optimal_min}-{optimal_max} chars typically performs best.")
    
    if hashtag_count > 5:
        warnings.append(f"Too many hashtags ({hashtag_count}). Recommend 3-5 for LinkedIn.")
    
    return ValidationResult(
        platform="LinkedIn",
        content_length=char_count,
        limit=limit,
        passed=char_count <= limit,
        remaining=limit - char_count,
        warnings=warnings
    )


def validate_instagram(content: str) -> ValidationResult:
    """Validate Instagram caption."""
    limit = PLATFORM_LIMITS["instagram"]["caption"]
    char_count = len(content.strip())
    hashtag_count = count_hashtags(content)
    preview_limit = PLATFORM_LIMITS["instagram"]["visible_preview"]
    
    warnings = []
    
    first_line = content.strip().split('\n')[0] if content.strip() else ""
    if len(first_line) > preview_limit:
        warnings.append(f"First line ({len(first_line)} chars) exceeds visible preview ({preview_limit}). Hook may be cut off.")
    
    if hashtag_count > 30:
        warnings.append(f"Too many hashtags ({hashtag_count}). Instagram allows max 30.")
    elif hashtag_count > 15:
        warnings.append(f"High hashtag count ({hashtag_count}). 5-15 recommended for best reach.")
    
    return ValidationResult(
        platform="Instagram",
        content_length=char_count,
        limit=limit,
        passed=char_count <= limit,
        remaining=limit - char_count,
        warnings=warnings
    )


def validate_facebook(content: str) -> ValidationResult:
    """Validate Facebook post."""
    limit = PLATFORM_LIMITS["facebook"]["post"]
    char_count = len(content.strip())
    
    warnings = []
    optimal_max = PLATFORM_LIMITS["facebook"]["optimal_max"]
    
    if char_count > optimal_max:
        warnings.append(f"Above optimal length for engagement ({optimal_max} chars). Shorter posts often perform better on Facebook.")
    
    return ValidationResult(
        platform="Facebook",
        content_length=char_count,
        limit=limit,
        passed=char_count <= limit,
        remaining=limit - char_count,
        warnings=warnings
    )


def validate_threads(content: str) -> ValidationResult:
    """Validate Threads post."""
    limit = PLATFORM_LIMITS["threads"]["post"]
    char_count = len(content.strip())
    hashtag_count = count_hashtags(content)
    
    warnings = []
    if hashtag_count > 0:
        warnings.append(f"Threads doesn't support hashtags. Remove {hashtag_count} hashtag(s).")
    
    return ValidationResult(
        platform="Threads",
        content_length=char_count,
        limit=limit,
        passed=char_count <= limit,
        remaining=limit - char_count,
        warnings=warnings
    )


def validate_all(content: str) -> list[ValidationResult]:
    """Validate content against all platforms."""
    return [
        validate_twitter(content),
        validate_linkedin(content),
        validate_instagram(content),
        validate_facebook(content),
        validate_threads(content),
    ]


def main():
    parser = argparse.ArgumentParser(
        description="Validate social media post character limits"
    )
    parser.add_argument("file", nargs="?", help="File containing post content")
    parser.add_argument("--text", "-t", help="Post content as string")
    parser.add_argument(
        "--platform", "-p",
        choices=["twitter", "linkedin", "instagram", "facebook", "threads", "all"],
        default="all",
        help="Target platform (default: all)"
    )
    parser.add_argument(
        "--premium", action="store_true",
        help="Use Twitter Premium limits (25,000 chars)"
    )
    
    args = parser.parse_args()
    
    # Get content
    if args.text:
        content = args.text
    elif args.file:
        try:
            with open(args.file, "r", encoding="utf-8") as f:
                content = f.read()
        except FileNotFoundError:
            print(f"Error: File not found: {args.file}", file=sys.stderr)
            sys.exit(1)
        except IOError as e:
            print(f"Error reading file: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print("Error: Provide either a file or --text argument", file=sys.stderr)
        sys.exit(1)
    
    # Validate
    results = []
    
    if args.platform == "all":
        results = validate_all(content)
    elif args.platform == "twitter":
        results = [validate_twitter(content, args.premium)]
    elif args.platform == "linkedin":
        results = [validate_linkedin(content)]
    elif args.platform == "instagram":
        results = [validate_instagram(content)]
    elif args.platform == "facebook":
        results = [validate_facebook(content)]
    elif args.platform == "threads":
        results = [validate_threads(content)]
    
    # Output
    print("\n=== Social Media Character Validation ===\n")
    
    all_passed = True
    for result in results:
        print(result)
        if result.warnings:
            for warning in result.warnings:
                print(f"   ⚠ {warning}")
        if not result.passed:
            all_passed = False
        print()
    
    # Summary
    passed_count = sum(1 for r in results if r.passed)
    print(f"=== {passed_count}/{len(results)} platforms passed ===")
    
    sys.exit(0 if all_passed else 1)


if __name__ == "__main__":
    main()
