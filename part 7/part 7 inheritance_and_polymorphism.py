

# part 7 Object_oriented programming



# File: inheritance_&_polymorphism.py
# Tasks: Inheritance, Polymorphism, Student and Teacher subclass

# Base Class
class Student:
    def __init__(self, name, age, roll_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no

    def display_info(self):
        print(f"Student -> Name: {self.name}, Age: {self.age}, Roll No: {self.roll_no}")

    def get_role(self):  # For Polymorphism
        return "I am a Student"

# Subclass - Inheritance from Student
class Teacher(Student):
    def __init__(self, name, age, roll_no, subject, salary):
        # Call parent constructor
        super().__init__(name, age, roll_no)
        self.subject = subject
        self.salary = salary

    # Method Overriding - Polymorphism
    def display_info(self):
        print(f"Teacher -> Name: {self.name}, Age: {self.age}, ID: {self.roll_no}, Subject: {self.subject}, Salary: {self.salary}")

    def get_role(self):  # Polymorphism - same method, different behavior
        return "I am a Teacher"

# --- Hands-on Testing ---

print("--- Inheritance Example ---")
student1 = Student("Ali", 21, "S101")
teacher1 = Teacher("Sir Ahmed", 35, "T01", "Python Programming", 80000)

student1.display_info()
teacher1.display_info()

print("\n--- Polymorphism Example ---")
# Same method name, works differently for different objects
people = [student1, teacher1]

for person in people:
    print(person.get_role())
    person.display_info()
    print()

print("\n--- All OOP Concepts Covered ---")
print("1. Class & Object: Student, Teacher objects created")
print("2. Constructor: __init__ used")
print("3. Methods: display_info(), get_role()")
print("4. Inheritance: Teacher inherits from Student")
print("5. Polymorphism: get_role() and display_info() overridden")
print("6. Encapsulation: Shown in previous file with __balance")