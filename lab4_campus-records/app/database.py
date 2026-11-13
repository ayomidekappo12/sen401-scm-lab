"""database.py - SQLite connection and schema.

The database file location comes from the DB_PATH environment variable so the
same code works locally and inside Docker (where it lives on a shared volume).
"""
import os
import sqlite3
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path

DEFAULT_DB = Path(__file__).resolve().parent.parent / "data" / "app.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS students (
    id    INTEGER PRIMARY KEY AUTOINCREMENT,
    name  TEXT    NOT NULL,
    score REAL    NOT NULL CHECK (score BETWEEN 0 AND 100)
);
CREATE TABLE IF NOT EXISTS items (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT    NOT NULL UNIQUE,
    quantity  INTEGER NOT NULL CHECK (quantity >= 0),
    price     REAL    NOT NULL CHECK (price >= 0)
);
"""


def db_path() -> str:
    """Path of the SQLite file (DB_PATH env var, else data/app.db)."""
    return os.environ.get("DB_PATH", str(DEFAULT_DB))


@contextmanager
def get_connection() -> Iterator[sqlite3.Connection]:
    """Open a connection, commit on success, roll back on error, always close."""
    conn = sqlite3.connect(db_path())
    conn.row_factory = sqlite3.Row  # rows behave like dictionaries
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def init_db() -> None:
    """Create the tables if they do not exist yet."""
    Path(db_path()).parent.mkdir(parents=True, exist_ok=True)
    with get_connection() as conn:
        conn.executescript(SCHEMA)
