"""utils/helpers.py - Reusable utility functions for student records."""


def highest_score(data: list[dict]) -> dict | None:
    """Return the student with the highest score, or None if the list is empty."""
    return max(data, key=lambda s: s["score"]) if data else None


def lowest_score(data: list[dict]) -> dict | None:
    """Return the student with the lowest score, or None if the list is empty."""
    return min(data, key=lambda s: s["score"]) if data else None
