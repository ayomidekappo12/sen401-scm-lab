# students.py - data module: holds the list of students and basic operations

students = [
    {"name": "James", "score": 45},
    {"name": "Deborah", "score": 82},
    {"name": "Tunde", "score": 67},
    {"name": "Amaka", "score": 91},
]


def average_score(data):
    if len(data) == 0:
        return 0  # Corrective fix (BUG-1): avoid ZeroDivisionError on empty list
    total = 0
    for d in data:
        total += d["score"]
    return total / len(data)


def add_student(name, score):
    # Corrective fix (BUG-2): reject bad scores ("abc", -5, 150) that would
    # later crash average_score() or produce nonsense results.
    if isinstance(score, bool) or not isinstance(score, (int, float)):
        raise ValueError(f"Score for {name!r} must be a number, got {score!r}")
    if not 0 <= score <= 100:
        raise ValueError(f"Score for {name!r} must be between 0 and 100, got {score}")
    students.append({"name": name, "score": score})


# Corrective fix (BUG-3): these prints used to run every time app.py imported
# this module, producing duplicate output. Now they only run when executed directly.
if __name__ == "__main__":
    print("Current Students:", students)
    print("Average Score:", average_score(students))
