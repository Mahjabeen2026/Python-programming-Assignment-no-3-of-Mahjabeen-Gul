
# Part 3 DATA Structures
# File: Data_str_Stud_mark_system.py
# Project: Create a student mark system storing grades

students = {} # dictionary me data store hoga

# Create - Add Students
students["Ali"] = 85
students["Sara"] = 92
students["Ahmed"] = 78

print("Student Marks System")
print(students)

# Read - Show all grades
print("\n--- All Student Grades ---")
for name, marks in students.items():
    if marks >= 80:
        grade = "A+"
    elif marks >= 60:
        grade = "B"
    else:
        grade = "C"
    print(f"{name} - Marks: {marks}, Grade: {grade}")

# Update - Update marks
students["Ahmed"] = 88
print("\nAfter Update Ahmed marks:", students)

# Delete - Remove a student
del students["Ali"]
print("After Deleting Ali:", students)