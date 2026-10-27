
students = [
    {
        "name": "Aarav",
        "roll_no": "101",
        "marks": {"Python": 85, "Maths": 78, "English": 90}
    },
    {
        "name": "Priya",
        "roll_no": "102",
        "marks": {"Python": 92, "Maths": 88, "English": 95}
    },
    {
        "name": "Rahul",
        "roll_no": "103",
        "marks": {"Python": 55, "Maths": 60, "English": 58}
    },
    {
        "name": "Ananya",
        "roll_no": "104",
        "marks": {"Python": 76, "Maths": 82, "English": 80}
    },
    {
        "name": "Vikram",
        "roll_no": "105",
        "marks": {"Python": 35, "Maths": 42, "English": 48}
    }
]


PASS_MARKS = 35


def calculate_percentage(marks):
    total = sum(marks.values())
    maximum = len(marks) * 100
    return (total / maximum) * 100


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 35:
        return "E"
    else:
        return "F"


def student_result(student):
    marks = student["marks"]
    percentage = calculate_percentage(marks)
    passed = all(mark >= PASS_MARKS for mark in marks.values())

    return percentage, passed


def show_all_students():
    print("\n--- Student Performance Report ---")

    for student in students:
        percentage, passed = student_result(student)
        grade = calculate_grade(percentage)
        total = sum(student["marks"].values())

        print(f"\nName: {student['name']}")
        print(f"Roll Number: {student['roll_no']}")
        print(f"Marks: {student['marks']}")
        print(f"Total: {total}/{len(student['marks']) * 100}")
        print(f"Percentage: {percentage:.2f}%")
        print(f"Grade: {grade}")
        print(f"Result: {'PASS' if passed else 'FAIL'}")


def show_class_analytics():
    percentages = [
        calculate_percentage(student["marks"])
        for student in students
    ]

    average = sum(percentages) / len(percentages)

    topper = max(
        students,
        key=lambda student: calculate_percentage(student["marks"])
    )

    passed_count = sum(
        1 for student in students
        if student_result(student)[1]
    )

    print("\n--- Class Analytics ---")
    print(f"Total Students: {len(students)}")
    print(f"Class Average: {average:.2f}%")
    print(f"Highest Scorer: {topper['name']}")
    print(
        "Topper Percentage: "
        f"{calculate_percentage(topper['marks']):.2f}%"
    )
    print(f"Students Passed: {passed_count}")
    print(f"Students Failed: {len(students) - passed_count}")


def show_subject_analytics():
    subjects = students[0]["marks"].keys()

    print("\n--- Subject-wise Analytics ---")

    for subject in subjects:
        marks = [
            student["marks"][subject]
            for student in students
        ]

        average = sum(marks) / len(marks)
        highest = max(marks)
        lowest = min(marks)

        print(f"\nSubject: {subject}")
        print(f"Average Marks: {average:.2f}")
        print(f"Highest Marks: {highest}")
        print(f"Lowest Marks: {lowest}")


def show_students_needing_improvement():
    print("\n--- Students Needing Improvement ---")

    found = False

    for student in students:
        percentage, passed = student_result(student)

        weak_subjects = [
            subject
            for subject, mark in student["marks"].items()
            if mark < 50
        ]

        if not passed or weak_subjects:
            found = True
            print(f"\nName: {student['name']}")
            print(f"Percentage: {percentage:.2f}%")

            if weak_subjects:
                print("Subjects to improve:", ", ".join(weak_subjects))

            if not passed:
                print("Status: Failed in at least one subject")

    if not found:
        print("All students are performing well!")


def search_student():
    roll_no = input("Enter student roll number: ").strip()

    for student in students:
        if student["roll_no"] == roll_no:
            percentage, passed = student_result(student)

            print(f"\nName: {student['name']}")
            print(f"Marks: {student['marks']}")
            print(f"Percentage: {percentage:.2f}%")
            print(f"Grade: {calculate_grade(percentage)}")
            print(f"Result: {'PASS' if passed else 'FAIL'}")
            return

    print("Student not found.")


def main():
    while True:
        print("\n" + "=" * 42)
        print("      STUDENT PERFORMANCE ANALYTICS")
        print("=" * 42)
        print("1. View all student results")
        print("2. View class analytics")
        print("3. View subject-wise analytics")
        print("4. Find students needing improvement")
        print("5. Search student by roll number")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            show_all_students()
        elif choice == "2":
            show_class_analytics()
        elif choice == "3":
            show_subject_analytics()
        elif choice == "4":
            show_students_needing_improvement()
        elif choice == "5":
            search_student()
        elif choice == "6":
            print("Thank you for using Student Performance Analytics!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
