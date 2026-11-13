"""students.py - Student data module.

Holds the in-memory list of students and every operation on it:
validation, adding, statistics (average, median) and a formatted report.

Maintenance history
-------------------
v1.0  Initial baseline.
v1.1  Corrective : empty-list guard, score validation, no prints on import.
      Adaptive   : Python 3.12 type syntax, Pydantic v2 validation.
      Perfective : median score, letter grades, formatted report.
      Preventive : refactored into small documented functions + constants.
"""
import statistics

from pydantic import BaseModel, Field, ValidationError

# ---------------------------------------------------------------- constants
MIN_SCORE = 0
MAX_SCORE = 100
# Grade boundaries, checked from highest to lowest: (minimum score, grade)
GRADE_BOUNDARIES = [(70, "A"), (60, "B"), (50, "C"), (45, "D"), (0, "F")]

# Python 3.12 type alias (PEP 695): one student as a plain dictionary
type StudentRecord = dict[str, str | float]


# ---------------------------------------------------------------- model
class Student(BaseModel):
    """A validated student: non-empty name, score between 0 and 100."""

    name: str = Field(min_length=1, max_length=50)
    score: float = Field(ge=MIN_SCORE, le=MAX_SCORE)


# ---------------------------------------------------------------- data
students: list[StudentRecord] = [
    {"name": "James", "score": 45},
    {"name": "Deborah", "score": 82},
    {"name": "Tunde", "score": 67},
    {"name": "Amaka", "score": 91},
]


# ---------------------------------------------------------------- helpers
def _scores(data: list[StudentRecord]) -> list[float]:
    """Return just the scores. Shared by every statistic (DRY)."""
    return [record["score"] for record in data]


# ---------------------------------------------------------------- operations
def add_student(name: str, score: float, data: list[StudentRecord] | None = None) -> StudentRecord:
    """Validate and add a student.

    Args:
        name: Student's name (1-50 characters).
        score: Score between MIN_SCORE and MAX_SCORE.
        data: List to add to; defaults to the module-level ``students`` list.

    Returns:
        The record that was added.

    Raises:
        ValueError: If the name or score is invalid.
    """
    target = students if data is None else data
    try:
        record = Student(name=name, score=score).model_dump()
    except ValidationError as err:
        raise ValueError(f"Invalid student data: {err.errors()[0]['msg']}") from err
    target.append(record)
    return record


def average_score(data: list[StudentRecord]) -> float:
    """Mean score, or 0 for an empty list (prevents ZeroDivisionError)."""
    scores = _scores(data)
    return statistics.fmean(scores) if scores else 0


def median_score(data: list[StudentRecord]) -> float:
    """Median score, or 0 for an empty list."""
    scores = _scores(data)
    return statistics.median(scores) if scores else 0


def grade(score: float) -> str:
    """Convert a numeric score to a letter grade using GRADE_BOUNDARIES."""
    for minimum, letter in GRADE_BOUNDARIES:
        if score >= minimum:
            return letter
    return "F"


# ---------------------------------------------------------------- output
def format_report(data: list[StudentRecord]) -> str:
    """Build the report as a string (easy to test, print or save to a file)."""
    lines = [f"{'#':<3} {'Name':<12} {'Score':>6}  Grade", "-" * 31]
    ranked = sorted(data, key=lambda r: r["score"], reverse=True)
    for rank, record in enumerate(ranked, start=1):
        lines.append(
            f"{rank:<3} {record['name']:<12} {record['score']:>6.1f}  {grade(record['score'])}"
        )
    lines += [
        "-" * 31,
        f"{'Students':<16}: {len(data)}",
        f"{'Average score':<16}: {average_score(data):.2f}",
        f"{'Median score':<16}: {median_score(data):.2f}",
    ]
    return "\n".join(lines)


def print_report(data: list[StudentRecord]) -> None:
    """Print the formatted report to the console."""
    print(format_report(data))


if __name__ == "__main__":
    print_report(students)
