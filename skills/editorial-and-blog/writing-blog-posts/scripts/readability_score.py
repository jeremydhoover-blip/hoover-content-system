#!/usr/bin/env python3
"""
Blog Post Readability Score Calculator

Analyzes blog post content and returns readability metrics including
Flesch-Kincaid grade level, reading time, and actionable suggestions.

Usage:
    python readability_score.py <blog_post.md>
    python readability_score.py --target-grade 8 <blog_post.md>
"""

import argparse
import re
import sys
from dataclasses import dataclass

# Constants for readability formulas
# Flesch-Kincaid Grade Level formula constants (standard)
FK_SENTENCE_WEIGHT = 0.39
FK_SYLLABLE_WEIGHT = 11.8
FK_CONSTANT = -15.59

# Average reading speed (words per minute) for general audience
READING_SPEED_WPM = 238

# Target grade level ranges
GRADE_RECOMMENDATIONS = {
    "general": (6, 8),      # General audience blogs
    "technical": (8, 10),   # Technical documentation
    "academic": (10, 12),   # Research, white papers
    "executive": (10, 12),  # Business leadership
}


@dataclass
class ReadabilityResult:
    word_count: int
    sentence_count: int
    syllable_count: int
    avg_words_per_sentence: float
    avg_syllables_per_word: float
    flesch_kincaid_grade: float
    reading_time_minutes: int
    passed: bool
    suggestions: list[str]


def count_syllables(word: str) -> int:
    """
    Estimate syllable count for a word.
    Uses a heuristic approach counting vowel groups.
    """
    word = word.lower().strip()
    if not word:
        return 0
    
    # Handle common endings
    if word.endswith('e') and len(word) > 2:
        word = word[:-1]
    if word.endswith('le') and len(word) > 2:
        word = word[:-2] + 'l'
    
    # Count vowel groups
    vowels = 'aeiouy'
    count = 0
    prev_was_vowel = False
    
    for char in word:
        is_vowel = char in vowels
        if is_vowel and not prev_was_vowel:
            count += 1
        prev_was_vowel = is_vowel
    
    # Every word has at least one syllable
    return max(1, count)


def extract_text(markdown: str) -> str:
    """
    Extract readable text from markdown, removing code blocks,
    frontmatter, and other non-prose elements.
    """
    text = markdown
    
    # Remove YAML frontmatter
    text = re.sub(r'^---\s*\n.*?\n---\s*\n', '', text, flags=re.DOTALL)
    
    # Remove code blocks
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    text = re.sub(r'`[^`]+`', '', text)
    
    # Remove markdown links but keep text
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    
    # Remove images
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
    
    # Remove headers markers but keep text
    text = re.sub(r'^#+\s*', '', text, flags=re.MULTILINE)
    
    # Remove emphasis markers
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
    text = re.sub(r'\*([^*]+)\*', r'\1', text)
    text = re.sub(r'__([^_]+)__', r'\1', text)
    text = re.sub(r'_([^_]+)_', r'\1', text)
    
    # Remove blockquotes
    text = re.sub(r'^>\s*', '', text, flags=re.MULTILINE)
    
    # Remove list markers
    text = re.sub(r'^[\-\*\+]\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\d+\.\s+', '', text, flags=re.MULTILINE)
    
    # Remove HTML comments
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
    
    # Clean up extra whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = text.strip()
    
    return text


def count_words(text: str) -> int:
    """Count words in text."""
    words = re.findall(r'\b[a-zA-Z\']+\b', text)
    return len(words)


def count_sentences(text: str) -> int:
    """Count sentences in text."""
    # Split on sentence-ending punctuation
    sentences = re.split(r'[.!?]+', text)
    # Filter out empty strings
    sentences = [s.strip() for s in sentences if s.strip()]
    return max(1, len(sentences))


def calculate_readability(text: str, target_grade: float = 8.0) -> ReadabilityResult:
    """
    Calculate readability metrics for the given text.
    """
    words = re.findall(r'\b[a-zA-Z\']+\b', text)
    word_count = len(words)
    sentence_count = count_sentences(text)
    
    # Calculate syllables
    syllable_count = sum(count_syllables(word) for word in words)
    
    # Avoid division by zero
    if word_count == 0 or sentence_count == 0:
        return ReadabilityResult(
            word_count=0,
            sentence_count=0,
            syllable_count=0,
            avg_words_per_sentence=0,
            avg_syllables_per_word=0,
            flesch_kincaid_grade=0,
            reading_time_minutes=0,
            passed=False,
            suggestions=["No readable content found."]
        )
    
    avg_words_per_sentence = word_count / sentence_count
    avg_syllables_per_word = syllable_count / word_count
    
    # Flesch-Kincaid Grade Level
    fk_grade = (FK_SENTENCE_WEIGHT * avg_words_per_sentence + 
                FK_SYLLABLE_WEIGHT * avg_syllables_per_word + 
                FK_CONSTANT)
    fk_grade = max(0, round(fk_grade, 1))
    
    # Reading time
    reading_time = max(1, round(word_count / READING_SPEED_WPM))
    
    # Generate suggestions
    suggestions = []
    passed = True
    
    if fk_grade > target_grade + 2:
        passed = False
        suggestions.append(f"Grade level ({fk_grade}) exceeds target ({target_grade}). Simplify vocabulary and shorten sentences.")
    elif fk_grade > target_grade:
        suggestions.append(f"Grade level ({fk_grade}) slightly above target ({target_grade}). Consider simplifying complex sections.")
    
    if avg_words_per_sentence > 25:
        suggestions.append(f"Average sentence length ({avg_words_per_sentence:.1f} words) is high. Target 15-20 words.")
        if avg_words_per_sentence > 30:
            passed = False
    
    if avg_syllables_per_word > 1.7:
        suggestions.append(f"Many complex words. Try replacing long words with simpler alternatives.")
    
    if word_count < 300:
        suggestions.append(f"Content may be too short ({word_count} words) for substantial blog post.")
    
    if not suggestions:
        suggestions.append("Readability looks good!")
    
    return ReadabilityResult(
        word_count=word_count,
        sentence_count=sentence_count,
        syllable_count=syllable_count,
        avg_words_per_sentence=round(avg_words_per_sentence, 1),
        avg_syllables_per_word=round(avg_syllables_per_word, 2),
        flesch_kincaid_grade=fk_grade,
        reading_time_minutes=reading_time,
        passed=passed,
        suggestions=suggestions
    )


def main():
    parser = argparse.ArgumentParser(
        description="Calculate readability score for blog posts"
    )
    parser.add_argument("file", help="Markdown file to analyze")
    parser.add_argument(
        "--target-grade", "-g",
        type=float,
        default=8.0,
        help="Target grade level (default: 8.0)"
    )
    parser.add_argument(
        "--audience",
        choices=["general", "technical", "academic", "executive"],
        default="general",
        help="Audience type for grade recommendations"
    )
    
    args = parser.parse_args()
    
    # Adjust target based on audience if not explicitly set
    if args.audience != "general" and args.target_grade == 8.0:
        min_grade, max_grade = GRADE_RECOMMENDATIONS[args.audience]
        args.target_grade = (min_grade + max_grade) / 2
    
    try:
        with open(args.file, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File not found: {args.file}", file=sys.stderr)
        sys.exit(1)
    except IOError as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Extract text and analyze
    text = extract_text(content)
    result = calculate_readability(text, args.target_grade)
    
    # Output results
    print("\n=== Readability Analysis ===\n")
    print(f"Word count:           {result.word_count:,}")
    print(f"Sentence count:       {result.sentence_count:,}")
    print(f"Reading time:         {result.reading_time_minutes} min")
    print()
    print(f"Avg words/sentence:   {result.avg_words_per_sentence}")
    print(f"Avg syllables/word:   {result.avg_syllables_per_word}")
    print()
    print(f"Flesch-Kincaid Grade: {result.flesch_kincaid_grade}")
    print(f"Target Grade:         {args.target_grade}")
    print()
    
    status = "✓ PASS" if result.passed else "✗ NEEDS WORK"
    print(f"Status: {status}")
    print()
    
    print("Suggestions:")
    for suggestion in result.suggestions:
        print(f"  • {suggestion}")
    
    sys.exit(0 if result.passed else 1)


if __name__ == "__main__":
    main()
