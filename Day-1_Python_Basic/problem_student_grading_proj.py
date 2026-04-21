"""
Problem Statement

Create a program that:
Takes number of students as input.
For each student, take:
    name
    branch  
    marks

Store data in a list of dictionaries.
Sort students by marks using lambda.
Print ranked list using enumerate().
Use match statement to assign grade:
    90+ → A
    75+ → B
    50+ → C
    Otherwise → Fail
"""

# students = []


# n = int(input("Enter number of students: "))

# for _ in range(n):
#     name = input("Enter name: ")
#     branch = input("Enter branch: ")
#     marks = int(input("Enter marks: "))

#     students.append({
#         "name": name,
#         "branch": branch,
#         "marks": marks
#     })

# # Sort students by marks (descending)
# sorted_students = sorted(students, key=lambda x: x["marks"], reverse=True)

# # Print ranking using enumerate()
# for rank, student in enumerate(sorted_students, start=1):
#     marks = student["marks"]
#     match marks:
#         case m if m >= 90:
#             grade = "A"
#         case m if m >= 75:
#             grade = "B"
#         case m if m >= 50:
#             grade = "C"
#         case _:
#             grade = "Fail"

# # Assign grade using match

students = []


n = int(input("Enter number of students:"))

for _ in range(n):
    name = input("Enter name:")
    branch = input("Enter branch:")
    marks = int(input("Enter marks:"))

    students.append({
        "name": name,
        "branch": branch,
        "marks": marks
    })

# Sort students by marks (highest first)
students = sorted(students, key = lambda x: x["marks"], reverse=True)
print(students)



