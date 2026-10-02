  

# Part 10 Combined hands-on Exercises

# masterclass.py - Combined with Exception Handling

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
    
    def display_profile(self):
        print(f"Name: {self.name} | Age: {self.age} | Course: {self.course}")

def add_student(student_list):
    try:
        name = input("Enter Student Name: ")
        if not name.strip():
            raise ValueError("Name cannot be empty")
        
        age = int(input("Enter Age: "))
        if age <= 0:
            raise ValueError("Age must be positive number")
        
        course = input("Enter Course: ")
        if not course.strip():
            raise ValueError("Course cannot be empty")
        
        student_list.append(Student(name, age, course))
        print(f"Student {name} added successfully!\n")
    
    except ValueError as ve:
        print(f"Input Error: {ve}\n")
    except Exception as e:
        print(f"Unexpected Error: {e}\n")

def show_all_students(student_list):
    try:
        if not student_list:
            raise Exception("No students found. Add student first.")
        
        print("\n--- All Students ---")
        for i, s in enumerate(student_list, 1):
            print(f"{i}. ", end="")
            s.display_profile()
        print()
    except Exception as e:
        print(f"Note: {e}\n")

def main():
    students = []
    while True:
        try:
            print("=== Masterclass Combined Project ===")
            print("1. Add Student")
            print("2. Show All Students")
            print("3. Exit")
            choice = input("Enter choice (1-3): ")
            
            if choice == "1":
                add_student(students)
            elif choice == "2":
                show_all_students(students)
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                raise ValueError("Please choose only 1, 2 or 3")
        except ValueError as ve:
            print(f"Error: {ve}\n")
        except KeyboardInterrupt:
            print("\nProgram stopped by user.")
            break

main()