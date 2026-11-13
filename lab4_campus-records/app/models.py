"""models.py - Data models (Pydantic v2).

``*Create`` models validate incoming data; the full models add the database id.
"""
from pydantic import BaseModel, Field


class StudentCreate(BaseModel):
    """Data needed to create a student."""

    name: str = Field(min_length=1, max_length=50)
    score: float = Field(ge=0, le=100)


class Student(StudentCreate):
    """A stored student, including its database id."""

    id: int


class ItemCreate(BaseModel):
    """Data needed to create an inventory item."""

    item_name: str = Field(min_length=1, max_length=50)
    quantity: int = Field(ge=0)
    price: float = Field(ge=0)


class Item(ItemCreate):
    """A stored item, including its id and computed stock value."""

    id: int
    value: float = 0

    def model_post_init(self, __context) -> None:
        self.value = self.quantity * self.price


class Stats(BaseModel):
    """Summary statistics returned by the /stats endpoints."""

    count: int
    total: float | None = None
    average: float
    median: float
    highest: str | None
    lowest: str | None
