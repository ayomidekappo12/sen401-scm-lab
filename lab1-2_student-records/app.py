# app.py - entry point that runs the demo application
from students import students, average_score, add_student
from utils.helpers import highest_score, lowest_score


def main():
    print("=== Student Records Demo ===")
    add_student("Chidi", 74)

    print("All students:", students)
    print("Average score:", average_score(students))

    top = highest_score(students)
    bottom = lowest_score(students)
    print("Highest:", top["name"], top["score"])
    print("Lowest:", bottom["name"], bottom["score"])


if __name__ == "__main__":
    main()
