# utils/helpers.py - helper functions for the inventory


def highest_stock_item(items):
    if not items:
        return None  # Corrective: max() crashes on an empty list
    return max(items, key=lambda i: i["quantity"])


def lowest_stock_item(items):
    if not items:
        return None  # Corrective: min() crashes on an empty list
    # Corrective (BUG-2): was max(), so it returned the HIGHEST item
    return min(items, key=lambda i: i["quantity"])
