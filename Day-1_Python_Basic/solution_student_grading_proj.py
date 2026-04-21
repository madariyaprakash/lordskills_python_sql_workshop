"""
Student Ranking & Grading System

Features:
- Takes student details as input
- Stores data in list of dictionaries
- Sorts students by marks (descending)
- Prints ranked list using enumerate()
- Assigns grade using match statement
"""

students = []

# Taking number of students
n = int(input("Enter number of students: "))

# Taking student details
for _ in range(n):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    marks = int(input("Enter marks: "))

    students.append({
        "name": name,
        "age": age,
        "marks": marks
    })

# Sorting students by marks (highest first)
students = sorted(students, key=lambda x: x["marks"], reverse=True)

print("\n🏆 Student Ranking:\n")

# Printing ranked list using enumerate
for rank, student in enumerate(students, start=1):

    marks = student["marks"]

    # Assigning grade using match + guards
    match marks:
        case m if m >= 90:
            grade = "A"
        case m if m >= 75:
            grade = "B"
        case m if m >= 50:
            grade = "C"
        case _:
            grade = "Fail"

    print(f"Rank {rank}: {student['name']} | Age: {student['age']} | Marks: {marks} | Grade: {grade}")