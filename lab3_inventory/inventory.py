"""inventory.py - Inventory data module.

Defines the ``Item`` data class and the list of items currently in stock.
"""
from dataclasses import dataclass


@dataclass
class Item:
    """One stock item.

    Attributes:
        item_name: Name of the product.
        quantity: Units in stock (must be >= 0).
        price: Unit price in Naira (must be >= 0).
    """

    item_name: str
    quantity: int
    price: float

    def __post_init__(self) -> None:
        """Reject impossible values as soon as an Item is created."""
        if self.quantity < 0 or self.price < 0:
            raise ValueError(f"{self.item_name}: quantity and price cannot be negative")

    @property
    def value(self) -> float:
        """Total value of this line: quantity x unit price."""
        return self.quantity * self.price


# Current stock
items: list[Item] = [
    Item("Laptop", 5, 450000),
    Item("Mouse", 40, 7500),
    Item("Keyboard", 25, 12000),
    Item("Monitor", 8, 95000),
    Item("USB Cable", 0, 2500),
]
