# app.py - entry point that runs the demo application
from students import students, add_student, print_report
from utils.helpers import highest_score, lowest_score


def main():
    print("=" * 31)
    print("   STUDENT RECORDS REPORT")
    print("=" * 31)
    add_student("Chidi", 74)

    print_report(students)

    top = highest_score(students)
    bottom = lowest_score(students)
    print(f"{'Highest':<16}: {top['name']} ({top['score']})")
    print(f"{'Lowest':<16}: {bottom['name']} ({bottom['score']})")

    # Demonstrate validation: an invalid score is rejected cleanly
    try:
        add_student("Bad Data", 150)
    except ValueError as err:
        print(f"\nRejected invalid input -> {err}")


if __name__ == "__main__":
    main()
