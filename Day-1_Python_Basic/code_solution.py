# creating empty list
students = []

n = int(input("Enter number of students:"))

for _ in range(n):
    name = input("Enter name:")
    age = int(input("Enter age:"))
    marks = int(input("Enter marks:"))

    students.append({
        "name": name,
        "age": age,
        "marks": marks