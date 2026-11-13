# app.py - reads inventory.py and calculates the total stock value
# Perfective: formatted table, Naira currency, status column, summary block.
from inventory import Item, items
from utils.helpers import highest_stock_item, lowest_stock_item

LOW_STOCK_THRESHOLD = 10


def total_stock_value(items: list[Item]) -> float:
    return sum(item.value for item in items)


def low_stock_items(items: list[Item], threshold: int = LOW_STOCK_THRESHOLD) -> list[Item]:
    return [item for item in items if item.quantity < threshold]


def naira(amount: float) -> str:
    return f"N{amount:,.2f}"


def status(item: Item) -> str:
    if item.quantity == 0:
        return "OUT OF STOCK"
    if item.quantity < LOW_STOCK_THRESHOLD:
        return "LOW"
    return "OK"


if __name__ == "__main__":
    print(f"{'Item':<12}{'Qty':>5}{'Unit Price':>15}{'Value':>17}  Status")
    print("-" * 62)
    for i in items:
        print(f"{i.item_name:<12}{i.quantity:>5}{naira(i.price):>15}{naira(i.value):>17}  {status(i)}")
    print("-" * 62)
    print(f"Total stock value : {naira(total_stock_value(items))}")
    print(f"Highest stock     : {highest_stock_item(items).item_name}")
    print(f"Lowest stock      : {lowest_stock_item(items).item_name}")
    print(f"Re-order needed   : {', '.join(i.item_name for i in low_stock_items(items))}")
