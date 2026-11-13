# app.py - reads inventory.py and calculates the total stock value
from inventory import Item, items
from utils.helpers import highest_stock_item, lowest_stock_item

LOW_STOCK_THRESHOLD = 10


def total_stock_value(items: list[Item]) -> float:
    return sum(item.value for item in items)


# New feature: list items that need re-ordering
def low_stock_items(items: list[Item], threshold: int = LOW_STOCK_THRESHOLD) -> list[Item]:
    return [item for item in items if item.quantity < threshold]


if __name__ == "__main__":
    print("Inventory:", items)
    print("Total stock value:", total_stock_value(items))
    print("Highest stock item:", highest_stock_item(items).item_name)
    print("Lowest stock item:", lowest_stock_item(items).item_name)
    print("Low stock:", [i.item_name for i in low_stock_items(items)])
