"""migrate.py - One-off data migration: JSON/CSV files -> SQLite database.

    python -m migrations.migrate

Reads data/students.json and data/inventory.csv, validates every record with
the Pydantic models, and inserts it into SQLite. Safe to run more than once:
tables that already contain data are skipped.
"""
import csv
import json
from pathlib import Path

from app.database import db_path, get_connection, init_db
from app.models import ItemCreate, StudentCreate

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def _table_empty(table: str) -> bool:
    with get_connection() as conn:
        return conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0] == 0


def migrate_students(path: Path = DATA_DIR / "students.json") -> int:
    if not _table_empty("students"):
        print("students: already migrated - skipped")
        return 0
    records = [StudentCreate(**r) for r in json.loads(path.read_text())]
    with get_connection() as conn:
        conn.executemany(
            "INSERT INTO students (name, score) VALUES (?, ?)",
            [(r.name, r.score) for r in records],
        )
    print(f"students: migrated {len(records)} rows from {path.name}")
    return len(records)


def migrate_items(path: Path = DATA_DIR / "inventory.csv") -> int:
    if not _table_empty("items"):
        print("items: already migrated - skipped")
        return 0
    with path.open(newline="") as f:
        records = [ItemCreate(**row) for row in csv.DictReader(f)]
    with get_connection() as conn:
        conn.executemany(
            "INSERT INTO items (item_name, quantity, price) VALUES (?, ?, ?)",
            [(r.item_name, r.quantity, r.price) for r in records],
        )
    print(f"items: migrated {len(records)} rows from {path.name}")
    return len(records)


def main() -> None:
    print(f"Migrating into SQLite database: {db_path()}")
    init_db()
    migrate_students()
    migrate_items()
    print("Migration complete.")


if __name__ == "__main__":
    main()
