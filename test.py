class Student:
    """Represents a student with a name, ID, and a list of numeric grades."""

    GRADE_MIN = 0.0
    GRADE_MAX = 100.0
    PASS_THRESHOLD = 60.0
    HONOR_THRESHOLD = 90.0

    def __init__(self, student_id: str, name: str) -> None:
        if not student_id or not student_id.strip():
            raise ValueError("Student ID must not be empty.")
        if not name or not name.strip():
            raise ValueError("Student name must not be empty.")

        self.student_id: str = student_id.strip()
        self.name: str = name.strip()
        self.grades: list[float] = []
        self.is_passed: bool = False
        self.is_on_honor_roll: bool = False

    def add_grade(self, grade: float) -> None:
        if not isinstance(grade, (int, float)):
            raise TypeError(
                f"Grade must be a number, got {type(grade).__name__!r}."
            )
        grade = float(grade)
        if grade < self.GRADE_MIN or grade > self.GRADE_MAX:
            raise ValueError(
                f"Grade {grade} is out of range "
                f"({self.GRADE_MIN}–{self.GRADE_MAX})."
            )
        self.grades.append(grade)

    def remove_grade_by_index(self, index: int) -> None:
        if not self.grades:
            print("No grades to remove.")
            return
        if index < 0 or index >= len(self.grades):
            print(
                f"Index {index} is out of bounds "
                f"(valid range: 0–{len(self.grades) - 1})."
            )
            return
        removed = self.grades.pop(index)
        print(f"Grade {removed} removed successfully.")

    def remove_grade_by_value(self, value: float) -> None:
        if value in self.grades:
            self.grades.remove(value)
            print(f"Grade {value} removed successfully.")
        else:
            print(f"Grade {value} not found in the student's records.")

    def calculate_average(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def get_letter_grade(self) -> str:
        average = self.calculate_average()
        if average >= 90:
            return "A"
        if average >= 80:
            return "B"
        if average >= 70:
            return "C"
        if average >= 60:
            return "D"
        return "F"

    def check_pass_fail(self) -> None:
        self.is_passed = self.calculate_average() >= self.PASS_THRESHOLD

    def check_honor_roll(self) -> None:
        self.is_on_honor_roll = self.calculate_average() >= self.HONOR_THRESHOLD

    def generate_report(self) -> str:
        self.check_pass_fail()
        self.check_honor_roll()

        average = self.calculate_average()
        letter = self.get_letter_grade()
        pass_status = "Passed" if self.is_passed else "Failed"
        honor_status = "Yes" if self.is_on_honor_roll else "No"

        separator = "-" * 40
        report = (
            f"\n{separator}\n"
            f"  STUDENT REPORT CARD\n"
            f"{separator}\n"
            f"  ID          : {self.student_id}\n"
            f"  Name        : {self.name}\n"
            f"  Grades (#)  : {len(self.grades)}\n"
            f"  Average     : {average:.2f}\n"
            f"  Letter Grade: {letter}\n"
            f"  Pass/Fail   : {pass_status}\n"
            f"  Honor Roll  : {honor_status}\n"
            f"{separator}\n"
        )
        return report

    def print_report(self) -> None:
        """Print the formatted student report card to standard output."""
        print(self.generate_report())


def run_demo() -> None:

    print("=" * 50)
    print("  Student Grade Management System – Demo")
    print("=" * 50)

    try:
        alice = Student("S001", "Alice Mora")
    except ValueError as error:
        print(f"Could not create student: {error}")
        return

    for grade in [95.0, 87.5, 91.0, 78.0]:
        alice.add_grade(grade)

    print("\n[Testing invalid grade type]")
    try:
        alice.add_grade("Fifty")  # type: ignore[arg-type]
    except TypeError as error:
        print(f"  Error caught: {error}")

    print("\n[Testing out-of-range grade]")
    try:
        alice.add_grade(110.0)
    except ValueError as error:
        print(f"  Error caught: {error}")

    print("\n[Remove grade at index 1]")
    alice.remove_grade_by_index(1)

    print("\n[Remove grade at index 99]")
    alice.remove_grade_by_index(99)

    print("\n[Remove grade by value 95.0]")
    alice.remove_grade_by_value(95.0)

    print("\n[Remove grade by value 50.0 (not present)]")
    alice.remove_grade_by_value(50.0)

    alice.print_report()

    print("[Testing empty student ID]")
    try:
        Student("", "Bob")
    except ValueError as error:
        print(f"  Error caught: {error}")

    print("\n[Student with no grades]")
    bob = Student("S002", "Bob Lara")
    bob.print_report()


if __name__ == "__main__":
    run_demo()