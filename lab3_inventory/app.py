# app.py - reads inventory.py and calculates the total stock value
from inventory import items
from utils.helpers import highest_stock_item, lowest_stock_item


def total_stock_value(items):
    total = 0
    for item in items:
        # Corrective (BUG-1): value is quantity TIMES price, not quantity + price
        total += item["quantity"] * item["price"]
    return total


print("Inventory:", items)
print("Total stock value:", total_stock_value(items))
print("Highest stock item:", highest_stock_item(items)["item_name"])
print("Lowest stock item:", lowest_stock_item(items)["item_name"])
