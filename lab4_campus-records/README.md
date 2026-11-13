# Campus Records v2.0 - Re-engineered (SEN 401 Lab 4)

The Student Records (Lab 2) and Inventory (Lab 3) apps, re-engineered into a
layered, modular application with a **SQLite** database, a **FastAPI** REST API
and **Docker Compose** deployment. Design notes and diagrams: [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md).

## Run with Docker (recommended)

```bash
docker compose up --build
```

| URL | What |
|-----|------|
| http://localhost:8000/docs | Swagger UI - try every endpoint |
| http://localhost:8000/students/stats | Student statistics (JSON) |
| http://localhost:8080 | SQLite web viewer - browse the migrated tables |

Stop: `docker compose down` (add `-v` to also delete the database volume).

## Run without Docker

```bash
pip install -r requirements-dev.txt
python -m migrations.migrate      # JSON/CSV -> data/app.db
python cli.py                     # console report from SQLite
uvicorn app.main:app --reload     # API on http://localhost:8000/docs
pytest -q                         # automated tests
```

## API endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Health check |
| GET | `/students` | List students |
| GET | `/students/{id}` | One student |
| POST | `/students` | Add student `{"name": "...", "score": 0-100}` |
| DELETE | `/students/{id}` | Remove student |
| GET | `/students/stats` | Count, average, median, highest, lowest |
| GET | `/items` | List items (with computed `value`) |
| POST | `/items` | Add item |
| PATCH | `/items/{id}/quantity?quantity=N` | Update stock level |
| GET | `/items/low-stock?threshold=10` | Items that need re-ordering |
| GET | `/items/stats` | Total stock value and statistics |
