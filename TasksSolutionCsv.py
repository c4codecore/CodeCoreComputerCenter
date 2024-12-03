import csv
import os

# File to store student data
csv_file = "students.csv"

# Function to load students from CSV
def load_students():
    students = []
    if os.path.exists(csv_file):  # Check if the file exists
        with open(csv_file, mode="r", newline="") as file:
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

# Function to append a new student to the CSV file
def append_student(student):
    # Check if the file exists to determine whether to write a header
    file_exists = os.path.exists(csv_file)
    with open(csv_file, mode="a", newline="") as file:
        fieldnames = ["roll_no", "name", "age", "Math", "Science", "English"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists:  # If the file is new, write the header
            writer.writeheader()
        writer.writerow({
            "roll_no": student["roll_no"],
            "name": student["name"],
            "age": student["age"],
            "Math": student["marks"]["Math"],
            "Science": student["marks"]["Science"],
            "English": student["marks"]["English"]
        })


# Function to save students to CSV
def save_students(students):
    with open(csv_file, mode="w", newline="") as file:
        fieldnames = ["roll_no", "name", "age", "Math", "Science", "English"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            writer.writerow({
                "roll_no": student["roll_no"],
                "name": student["name"],
                "age": student["age"],
                "Math": student["marks"]["Math"],
                "Science": student["marks"]["Science"],
                "English": student["marks"]["English"]
            })

# Initialize student list from CSV
students = load_students()

# Function to add a new student
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
    append_student(students)
    print(f"Student {name} added successfully!")

# Function to update student marks
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

# Function to calculate the average marks of a student
def calculate_average(students, roll_no):
    for student in students:
        if student["roll_no"] == roll_no:
            marks = student["marks"]
            average = sum(marks.values()) / len(marks)
            return average
    print("Student not found!")
    return 0

# Function to find the highest marks in a specific subject
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

# Function to display all students
def display_students(students):
    if not students:
        print("No students to display!")
        return
    for student in students:
        print(f"Roll No: {student['roll_no']}, Name: {student['name']}, Age: {student['age']}, Marks: {student['marks']}")

# Main loop for the Student Management System
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
