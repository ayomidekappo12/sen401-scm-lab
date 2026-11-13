# students.py - data module: holds the list of students and basic operations
# Adaptive maintenance: updated for Python 3.12+ and Pydantic v2 validation.
from pydantic import BaseModel, Field, ValidationError

# Python 3.12 'type' statement (PEP 695) - a modern type alias
type StudentRecord = dict[str, str | float]


class Student(BaseModel):
    """Pydantic model: validates a student's name and score automatically."""
    name: str = Field(min_length=1, max_length=50)
    score: float = Field(ge=0, le=100)


students: list[StudentRecord] = [
    {"name": "James", "score": 45},
    {"name": "Deborah", "score": 82},
    {"name": "Tunde", "score": 67},
    {"name": "Amaka", "score": 91},
]


def average_score(data: list[StudentRecord]) -> float:
    if len(data) == 0:
        return 0  # avoid ZeroDivisionError on empty list
    total = 0
    for d in data:
        total += d["score"]
    return total / len(data)


def add_student(name: str, score: float) -> None:
    # New feature: Pydantic replaces the hand-written checks from step 1
    try:
        student = Student(name=name, score=score)
    except ValidationError as err:
        raise ValueError(f"Invalid student data: {err.errors()[0]['msg']}") from err
    students.append(student.model_dump())


if __name__ == "__main__":
    print("Current Students:", students)
    print("Average Score:", average_score(students))
