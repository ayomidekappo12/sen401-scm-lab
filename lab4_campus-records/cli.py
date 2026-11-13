"""cli.py - Console report that reads from the new SQLite backend.

    python cli.py
"""
from app import controllers
from app.database import init_db
from app.utils import naira


def main() -> None:
    init_db()
    s = controllers.student_stats()
    print("STUDENTS (from SQLite)")
    for st in controllers.list_students():
        print(f"  {st.id:<3}{st.name:<12}{st.score:>6.1f}")
    print(f"  count={s.count}  average={s.average}  median={s.median}  "
          f"highest={s.highest}  lowest={s.lowest}\n")

    i = controllers.item_stats()
    print("INVENTORY (from SQLite)")
    for it in controllers.list_items():
        print(f"  {it.id:<3}{it.item_name:<12}{it.quantity:>5}{naira(it.value):>17}")
    print(f"  total value={naira(i.total)}  re-order: "
          f"{', '.join(x.item_name for x in controllers.low_stock_items()) or 'None'}")


if __name__ == "__main__":
    main()
