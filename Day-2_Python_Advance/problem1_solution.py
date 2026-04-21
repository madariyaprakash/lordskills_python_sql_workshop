class Student:
    def __init__(self, name, enroll_no, marks):
        self.name = name
        self.enroll_no = enroll_no
        self.marks = marks
        self.grade = self.assign_grade()

    # instance method to assign grade
    def assign_grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 75:
            return "A"
        elif self.marks >= 60:
            return "B"
        elif self.marks >= 40:
            return "C"
        else:
            return "F"
        
    def display(self):
        print(f"Name: {self.name}, Enroll No: {self.enroll_no}, Marks: {self.marks}")

    
class StudentManagementSystem:
    def __init__(self):
        self.students = []

    # Add student record
    def add_student(self, name, roll_no, marks):
        student = Student(name, roll_no, marks)
        self.students.append(student)

    # display all students
    def display_all(self):
        for student in self.students:
            student.display()

    # find topper
    def find_topper(self):
        topper = max(self.students, key=lambda s: s.marks)
        print("\nTopper:")
        topper.display()

    # rank students
    def rank_students(self):
        ranked = sorted(self.students, key = lambda s : s.marks, reverse=True)
        print("\nRanked Students:")
        for i, student in enumerate(ranked, start=1):
            print(f"Rank {i} : {student.name} ({student.marks})")

    # list students by grade
    def list_by_grade(self, grade):
        print(f"\nStudent with grade {grade}")
        for student in self.students:
            if student.grade == grade:
                student.display()
    
    # students needed improvement
    def need_improvement(self):
        print("\nNeeded improvement")
        for student in self.students:
            if student.grade in ["F", "C"]:
                student.display()


sms = StudentManagementSystem()
print("hi")
# adding students
sms.add_student("Prakash", 101, 85)
sms.add_student("Anita", 102, 35)
sms.add_student("Rahul", 103, 92)
sms.add_student("Sneha", 104, 60)

# display all records
sms.display_all()

# find topper
sms.find_topper()

# rank students
sms.rank_students()

# list student by grade
sms.list_by_grade("A")

# need improvement
sms.need_improvement()
