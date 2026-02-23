import csv
import os

FILE_NAME = "students.csv"

# Create file if it doesn't exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Course", "Phone", "Grade"])


def register_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    course = input("Enter Course: ")
    phone = input("Enter Phone Number: ")

    # Check if student already exists
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == student_id:
                print("Student already exists!")
                return

    # Add new student
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([student_id, name, course, phone, ""])

    print("Student registered successfully!")


def display_students():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)

        if len(rows) <= 1:
            print("No students registered yet.")
            return

        # Print header
        print("\n{:<10} {:<15} {:<15} {:<15} {:<10}".format(
            "ID", "Name", "Course", "Phone", "Grade"))
        print("-" * 70)

        # Print data rows (skip header row)
        for row in rows[1:]:
            print("{:<10} {:<20} {:<15} {:<15} {:<10}".format(
                row[0], row[1], row[2], row[3], row[4]))


def update_course():
    student_id = input("Enter Student ID: ")
    new_course = input("Enter New Course: ")

    rows = []
    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == student_id:
                row[2] = new_course
                found = True
            rows.append(row)

    if found:
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print("Course updated successfully!")
    else:
        print("Student not found.")


def assign_grade():
    student_id = input("Enter Student ID: ")
    grade = input("Enter Grade: ")

    rows = []
    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == student_id:
                row[4] = grade
                found = True
            rows.append(row)

    if found:
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print("Grade assigned successfully!")
    else:
        print("Student not found.")


def menu():
    while True:
        print("\n====== SCHOOL MANAGEMENT SYSTEM ======")
        print("1. Register Student")
        print("2. Display Students")
        print("3. Update Course")
        print("4. Assign Grade")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            register_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            update_course()
        elif choice == "4":
            assign_grade()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    menu()