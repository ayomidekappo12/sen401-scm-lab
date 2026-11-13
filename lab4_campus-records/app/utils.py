"""utils.py - Generic, reusable helpers.

In Labs 2 and 3, highest_score()/lowest_score() and highest_stock_item()/
lowest_stock_item() were four near-identical functions. They are replaced by
two generic functions that work for any record and any numeric field (DRY).
"""
import statistics
from collections.abc import Callable, Sequence
from typing import TypeVar

T = TypeVar("T")


def highest_by(records: Sequence[T], key: Callable[[T], float]) -> T | None:
    """Record with the largest ``key`` value, or None if empty."""
    return max(records, key=key) if records else None


def lowest_by(records: Sequence[T], key: Callable[[T], float]) -> T | None:
    """Record with the smallest ``key`` value, or None if empty."""
    return min(records, key=key) if records else None


def mean(values: Sequence[float]) -> float:
    """Average, or 0 for an empty sequence (no ZeroDivisionError)."""
    return statistics.fmean(values) if values else 0.0


def median(values: Sequence[float]) -> float:
    """Median, or 0 for an empty sequence."""
    return float(statistics.median(values)) if values else 0.0


def naira(amount: float) -> str:
    """Format a number as Naira, e.g. 1500 -> 'N1,500.00'."""
    return f"N{amount:,.2f}"
