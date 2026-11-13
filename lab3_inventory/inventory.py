# inventory.py - list of items in stock
# Adaptive: Python 3.12 dataclasses with type hints replace raw dictionaries.
from dataclasses import dataclass


@dataclass
class Item:
    item_name: str
    quantity: int
    price: float

    def __post_init__(self):
        if self.quantity < 0 or self.price < 0:
            raise ValueError(f"{self.item_name}: quantity and price cannot be negative")

    @property
    def value(self) -> float:
        return self.quantity * self.price


items: list[Item] = [
    Item("Laptop", 5, 450000),
    Item("Mouse", 40, 7500),
    Item("Keyboard", 25, 12000),
    Item("Monitor", 8, 95000),
    Item("USB Cable", 0, 2500),
]
