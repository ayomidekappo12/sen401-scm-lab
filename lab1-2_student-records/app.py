"""app.py - Entry point: runs the Student Records demo application."""
from students import add_student, print_report, students
from utils.helpers import highest_score, lowest_score

LINE = "=" * 31


def show_extremes() -> None:
    """Print the highest- and lowest-scoring students."""
    top, bottom = highest_score(students), lowest_score(students)
    if top and bottom:
        print(f"{'Highest':<16}: {top['name']} ({top['score']})")
        print(f"{'Lowest':<16}: {bottom['name']} ({bottom['score']})")


def demo_validation() -> None:
    """Show that invalid input is rejected instead of crashing the program."""
    try:
        add_student("Bad Data", 150)
    except ValueError as err:
        print(f"\nRejected invalid input -> {err}")


def main() -> None:
    """Run the demo: add a student, print the report and show validation."""
    print(LINE, "   STUDENT RECORDS REPORT", LINE, sep="\n")
    add_student("Chidi", 74)
    print_report(students)
    show_extremes()
    demo_validation()


if __name__ == "__main__":
    main()
