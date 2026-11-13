# students.py - data module: holds the list of students and basic operations
# Adaptive maintenance: updated for Python 3.12+ and Pydantic v2 validation.
# Perfective maintenance: median score, letter grades and a formatted report.
import statistics

from pydantic import BaseModel, Field, ValidationError

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
        return 0
    total = 0
    for d in data:
        total += d["score"]
    return total / len(data)


def median_score(data: list[StudentRecord]) -> float:
    if len(data) == 0:
        return 0
    return statistics.median(d["score"] for d in data)


def grade(score: float) -> str:
    if score >= 70:
        return "A"
    if score >= 60:
        return "B"
    if score >= 50:
        return "C"
    if score >= 45:
        return "D"
    return "F"


def add_student(name: str, score: float) -> None:
    try:
        student = Student(name=name, score=score)
    except ValidationError as err:
        raise ValueError(f"Invalid student data: {err.errors()[0]['msg']}") from err
    students.append(student.model_dump())


def print_report(data: list[StudentRecord]) -> None:
    print(f"{'#':<3} {'Name':<12} {'Score':>6}  Grade")
    print("-" * 31)
    for i, d in enumerate(sorted(data, key=lambda s: s["score"], reverse=True), 1):
        print(f"{i:<3} {d['name']:<12} {d['score']:>6.1f}  {grade(d['score'])}")
    print("-" * 31)
    print(f"{'Students':<16}: {len(data)}")
    print(f"{'Average score':<16}: {average_score(data):.2f}")
    print(f"{'Median score':<16}: {median_score(data):.2f}")


if __name__ == "__main__":
    print_report(students)
