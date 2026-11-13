"""main.py - FastAPI application exposing a RESTful API.

Run locally:   uvicorn app.main:app --reload
Docs (Swagger): http://localhost:8000/docs
"""
import sqlite3
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException

from app import controllers
from app.database import init_db
from app.models import Item, ItemCreate, Stats, Student, StudentCreate


@asynccontextmanager
async def lifespan(_: FastAPI):
    init_db()  # make sure the tables exist before serving requests
    yield


app = FastAPI(
    title="Campus Records API",
    description="SEN 401 Lab 4 - re-engineered Student & Inventory system",
    version="2.0.0",
    lifespan=lifespan,
)


@app.get("/", tags=["health"])
def health() -> dict:
    return {"status": "ok", "service": "campus-records-api", "version": app.version}


# ------------------------------------------------------------------ students
@app.get("/students", response_model=list[Student], tags=["students"])
def get_students():
    return controllers.list_students()


@app.get("/students/stats", response_model=Stats, tags=["students"])
def get_student_stats():
    return controllers.student_stats()


@app.get("/students/{student_id}", response_model=Student, tags=["students"])
def get_student(student_id: int):
    student = controllers.get_student(student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@app.post("/students", response_model=Student, status_code=201, tags=["students"])
def create_student(data: StudentCreate):
    return controllers.add_student(data)


@app.delete("/students/{student_id}", status_code=204, tags=["students"])
def remove_student(student_id: int):
    if not controllers.delete_student(student_id):
        raise HTTPException(status_code=404, detail="Student not found")


# ------------------------------------------------------------------ items
@app.get("/items", response_model=list[Item], tags=["inventory"])
def get_items():
    return controllers.list_items()


@app.get("/items/stats", response_model=Stats, tags=["inventory"])
def get_item_stats():
    return controllers.item_stats()


@app.get("/items/low-stock", response_model=list[Item], tags=["inventory"])
def get_low_stock(threshold: int = controllers.LOW_STOCK_THRESHOLD):
    return controllers.low_stock_items(threshold)


@app.post("/items", response_model=Item, status_code=201, tags=["inventory"])
def create_item(data: ItemCreate):
    try:
        return controllers.add_item(data)
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=409, detail="Item already exists")


@app.patch("/items/{item_id}/quantity", response_model=Item, tags=["inventory"])
def set_item_quantity(item_id: int, quantity: int):
    if quantity < 0:
        raise HTTPException(status_code=422, detail="Quantity cannot be negative")
    item = controllers.update_item_quantity(item_id, quantity)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
