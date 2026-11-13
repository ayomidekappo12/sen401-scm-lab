# Service 2: one-shot job that migrates JSON/CSV data into SQLite
FROM python:3.12-slim
WORKDIR /code
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
RUN pip install --no-cache-dir "pydantic>=2.5"
COPY app/ app/
COPY migrations/ migrations/
COPY data/students.json data/inventory.csv data/
CMD ["python", "-m", "migrations.migrate"]
