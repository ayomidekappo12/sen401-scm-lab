"""utils/helpers.py - Reusable helper functions for the inventory."""
from inventory import Item


def highest_stock_item(items: list[Item]) -> Item | None:
    """Return the item with the most units in stock, or None if empty."""
    return max(items, key=lambda i: i.quantity) if items else None


def lowest_stock_item(items: list[Item]) -> Item | None:
    """Return the item with the fewest units in stock, or None if empty."""
    return min(items, key=lambda i: i.quantity) if items else None


def naira(amount: float) -> str:
    """Format a number as Naira, e.g. 1500 -> 'N1,500.00'."""
    return f"N{amount:,.2f}"
