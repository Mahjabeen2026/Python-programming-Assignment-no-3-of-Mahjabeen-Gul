

#part 8 Json and Data Storage

# File: json_data_storage.py
# Part 8 - JSON & Data Storage
# Tasks: Read/write JSON, Student data management system

import json
import os

FILE_NAME = "student.json"

# Function to read JSON data
def read_data():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

# Function to write JSON data
def write_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)
    print("Data saved successfully to student.json")

# Function to add new student
def add_student():
    data = read_data()
    
    student_id = int(input("Enter Student ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    marks = int(input("Enter Marks: "))

    new_student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    data.append(new_student)
    write_data(data)
    print(f"Student {name} added successfully!")

# Function to show all students
def show_all_students():
    data = read_data()
    if not data:
        print("No students found.")
        return

    print("\n--- All Students ---")
    for s in data:
        print(f"ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Course: {s['course']} | Marks: {s['marks']}")

# Function to search student
def search_student():
    name = input("Enter name to search: ")
    data = read_data()
    found = False
    for s in data:
        if s['name'].lower() == name.lower():
            print(f"Found: {s}")
            found = True
    if not found:
        print("Student not found.")

# --- Main Menu System ---
while True:
    print("\n--- Student Data Management System (JSON) ---")
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_all_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.")