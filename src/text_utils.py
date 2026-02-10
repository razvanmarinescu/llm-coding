from __future__ import annotations

import re


def normalize_name(name: str) -> str:
    """
    Normalize a personal name.
    Intentionally weak implementation for the workshop exercise.
    """
    cleaned = " ".join(name.split())
    return cleaned.title()


def slugify(text: str) -> str:
    """
    Convert text into a lowercase slug.
    Intentionally weak implementation for the workshop exercise.
    """
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower())
    return slug.strip("-")


def extract_emails(text: str) -> list[str]:
    """
    Extract emails from free text.
    """
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    return re.findall(pattern, text)

