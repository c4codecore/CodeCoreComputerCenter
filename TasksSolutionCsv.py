import os
import csv

def load_students():
    students = []
    if os.path.exists("students.csv"):
        with open("students.csv", mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = {
                    "roll_no": int(row["roll_no"]),
                    "name": row["name"],
                    "age": int(row["age"]),
                    "marks": {
                        "Math": int(row["Math"]),
                        "Science": int(row["Science"]),
                        "English": int(row["English"])
                    }
                }
                students.append(student)
    return students

def append_student(student):
    file_exists = os.path.exists("students.csv")
    with open("students.csv", mode="a", newline="") as file:
        fieldnames = ["Roll_no", "Name", "Age", "Math", "Science", "English"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow({
            "Roll_no": student["roll_no"],
            "Name": student["name"],
            "Age": student["age"],
            "Math": student["marks"]["Math"],
            "Science": student["marks"]["Science"],
            "English": student["marks"]["English"]
        })

def save_students(students):
    with open("students.csv", mode="w", newline="") as file:
        fieldnames = ["Roll_no", "Name", "Age", "Math", "Science", "English"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            writer.writerow({
                "Roll_no": student["roll_no"],
                "Name": student["name"],
                "Age": student["age"],
                "Math": student["marks"]["Math"],
                "Science": student["marks"]["Science"],
                "English": student["marks"]["English"]
            })

def add_student(students):
    roll_no = int(input("Enter Roll Number: "))
    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    marks = {
        "Math": int(input("Enter Math Marks: ")),
        "Science": int(input("Enter Science Marks: ")),
        "English": int(input("Enter English Marks: "))
    }
    student = {
        "roll_no": roll_no,
        "name": name,
        "age": age,
        "marks": marks
    }
    students.append(student)
    append_student(student)
    print(f"Student {name} added successfully!")

def update_marks(students, roll_no):
    for student in students:
        if student["roll_no"] == roll_no:
            print(f"Updating marks for {student['name']}")
            student["marks"]["Math"] = int(input("Enter new Math Marks: "))
            student["marks"]["Science"] = int(input("Enter new Science Marks: "))
            student["marks"]["English"] = int(input("Enter new English Marks: "))
            save_students(students)
            print("Marks updated successfully!")
            return
    print("Student not found!")

def calculate_average(students, roll_no):
    for student in students:
        if student["roll_no"] == roll_no:
            marks = student["marks"]
            average = sum(marks.values()) / len(marks)
            return average
    print("Student not found!")
    return 0

def highest_marks(students, subject):
    highest = -1
    top_student = None
    for student in students:
        if student["marks"][subject] > highest:
            highest = student["marks"][subject]
            top_student = student["name"]
    if top_student:
        print(f"Highest Marks in {subject}: {highest} by {top_student}")
    else:
        print(f"No records found for subject: {subject}")

def display_students(students):
    if not students:
        print("No students to display!")
        return
    for student in students:
        print(f"Roll No: {student['roll_no']}, Name: {student['name']}, Age: {student['age']}, Marks: {student['marks']}")

students = load_students()

while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. Update Student Marks")
    print("3. Calculate Average Marks")
    print("4. Find Highest Marks in a Subject")
    print("5. Display All Students")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student(students)
    elif choice == 2:
        roll_no = int(input("Enter Roll Number: "))
        update_marks(students, roll_no)
    elif choice == 3:
        roll_no = int(input("Enter Roll Number: "))
        average = calculate_average(students, roll_no)
        if average:
            print(f"Average Marks: {average:.2f}")
    elif choice == 4:
        subject = input("Enter Subject (Math/Science/English): ")
        if subject in ["Math", "Science", "English"]:
            highest_marks(students, subject)
        else:
            print("Invalid Subject! Please try again.")
    elif choice == 5:
        display_students(students)
    elif choice == 0:
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
