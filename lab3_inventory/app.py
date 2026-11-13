"""app.py - Inventory Manager entry point.

Reads the items from inventory.py, calculates the total stock value and
prints a formatted stock report with re-order alerts.
"""
from inventory import Item, items
from utils.helpers import highest_stock_item, lowest_stock_item, naira

LOW_STOCK_THRESHOLD = 10  # items below this quantity need re-ordering
TABLE_WIDTH = 62


def total_stock_value(stock: list[Item]) -> float:
    """Sum of quantity x price for every item."""
    return sum(item.value for item in stock)


def low_stock_items(stock: list[Item], threshold: int = LOW_STOCK_THRESHOLD) -> list[Item]:
    """Items whose quantity is below ``threshold``."""
    return [item for item in stock if item.quantity < threshold]


def stock_status(item: Item) -> str:
    """Human-readable status: OUT OF STOCK, LOW or OK."""
    if item.quantity == 0:
        return "OUT OF STOCK"
    if item.quantity < LOW_STOCK_THRESHOLD:
        return "LOW"
    return "OK"


def print_table(stock: list[Item]) -> None:
    """Print one row per item."""
    print(f"{'Item':<12}{'Qty':>5}{'Unit Price':>15}{'Value':>17}  Status")
    print("-" * TABLE_WIDTH)
    for item in stock:
        print(
            f"{item.item_name:<12}{item.quantity:>5}{naira(item.price):>15}"
            f"{naira(item.value):>17}  {stock_status(item)}"
        )
    print("-" * TABLE_WIDTH)


def print_summary(stock: list[Item]) -> None:
    """Print totals, extremes and the re-order list."""
    if not stock:
        print("Inventory is empty.")
        return
    reorder = ", ".join(i.item_name for i in low_stock_items(stock)) or "None"
    print(f"Total stock value : {naira(total_stock_value(stock))}")
    print(f"Highest stock     : {highest_stock_item(stock).item_name}")
    print(f"Lowest stock      : {lowest_stock_item(stock).item_name}")
    print(f"Re-order needed   : {reorder}")


def main() -> None:
    """Run the inventory report."""
    print("INVENTORY STOCK REPORT".center(TABLE_WIDTH))
    print("=" * TABLE_WIDTH)
    print_table(items)
    print_summary(items)


if __name__ == "__main__":
    main()
