from __future__ import annotations

import re


def normalize_name(name: str) -> str:
    """
    Normalize a personal name.
    Intentionally weak implementation for the workshop exercise.
    """
    return name.strip().title()


def slugify(text: str) -> str:
    """
    Convert text into a lowercase slug.
    Intentionally weak implementation for the workshop exercise.
    """
    return text.lower().replace(" ", "-")


def extract_emails(text: str) -> list[str]:
    """
    Extract emails from free text.
    """
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    return re.findall(pattern, text)

