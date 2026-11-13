# utils/helpers.py - helper functions for the inventory
# Adaptive: works with Item dataclass objects (attribute access, type hints).


def highest_stock_item(items):
    if not items:
        return None
    return max(items, key=lambda i: i.quantity)


def lowest_stock_item(items):
    if not items:
        return None
    return min(items, key=lambda i: i.quantity)
