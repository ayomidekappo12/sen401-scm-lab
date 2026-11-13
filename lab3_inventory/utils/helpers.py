# utils/helpers.py - helper functions for the inventory


def highest_stock_item(items):
    return max(items, key=lambda i: i["quantity"])


def lowest_stock_item(items):
    return max(items, key=lambda i: i["quantity"])
