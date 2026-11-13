"""controllers.py - Business logic: read/write the database and compute stats.

The API (main.py) and the console report (cli.py) both call these functions,
so the logic exists in exactly one place.
"""
from app.database import get_connection
from app.models import Item, ItemCreate, Stats, Student, StudentCreate
from app.utils import highest_by, lowest_by, mean, median

LOW_STOCK_THRESHOLD = 10


# ------------------------------------------------------------------ students
def list_students() -> list[Student]:
    with get_connection() as conn:
        rows = conn.execute("SELECT id, name, score FROM students ORDER BY id").fetchall()
    return [Student(**dict(r)) for r in rows]


def get_student(student_id: int) -> Student | None:
    with get_connection() as conn:
        row = conn.execute(
            "SELECT id, name, score FROM students WHERE id = ?", (student_id,)
        ).fetchone()
    return Student(**dict(row)) if row else None


def add_student(data: StudentCreate) -> Student:
    with get_connection() as conn:
        cur = conn.execute(
            "INSERT INTO students (name, score) VALUES (?, ?)", (data.name, data.score)
        )
    return Student(id=cur.lastrowid, **data.model_dump())


def delete_student(student_id: int) -> bool:
    with get_connection() as conn:
        cur = conn.execute("DELETE FROM students WHERE id = ?", (student_id,))
    return cur.rowcount > 0


def student_stats() -> Stats:
    students = list_students()
    scores = [s.score for s in students]
    top = highest_by(students, key=lambda s: s.score)
    bottom = lowest_by(students, key=lambda s: s.score)
    return Stats(
        count=len(students),
        average=round(mean(scores), 2),
        median=median(scores),
        highest=top.name if top else None,
        lowest=bottom.name if bottom else None,
    )


# ------------------------------------------------------------------ items
def list_items() -> list[Item]:
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT id, item_name, quantity, price FROM items ORDER BY id"
        ).fetchall()
    return [Item(**dict(r)) for r in rows]


def add_item(data: ItemCreate) -> Item:
    with get_connection() as conn:
        cur = conn.execute(
            "INSERT INTO items (item_name, quantity, price) VALUES (?, ?, ?)",
            (data.item_name, data.quantity, data.price),
        )
    return Item(id=cur.lastrowid, **data.model_dump())


def update_item_quantity(item_id: int, quantity: int) -> Item | None:
    with get_connection() as conn:
        conn.execute("UPDATE items SET quantity = ? WHERE id = ?", (quantity, item_id))
        row = conn.execute(
            "SELECT id, item_name, quantity, price FROM items WHERE id = ?", (item_id,)
        ).fetchone()
    return Item(**dict(row)) if row else None


def low_stock_items(threshold: int = LOW_STOCK_THRESHOLD) -> list[Item]:
    return [i for i in list_items() if i.quantity < threshold]


def item_stats() -> Stats:
    items = list_items()
    values = [i.value for i in items]
    top = highest_by(items, key=lambda i: i.quantity)
    bottom = lowest_by(items, key=lambda i: i.quantity)
    return Stats(
        count=len(items),
        total=sum(values),
        average=round(mean(values), 2),
        median=median(values),
        highest=top.item_name if top else None,
        lowest=bottom.item_name if bottom else None,
    )
