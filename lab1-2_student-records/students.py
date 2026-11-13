# students.py - data module: holds the list of students and basic operations

students = [
    {"name": "James", "score": 45},
    {"name": "Deborah", "score": 82},
    {"name": "Tunde", "score": 67},
    {"name": "Amaka", "score": 91},
]


def average_score(data):
    total = 0
    for d in data:
        total += d["score"]
    return total / len(data)


def add_student(name, score):
    students.append({"name": name, "score": score})


print("Current Students:", students)
print("Average Score:", average_score(students))
