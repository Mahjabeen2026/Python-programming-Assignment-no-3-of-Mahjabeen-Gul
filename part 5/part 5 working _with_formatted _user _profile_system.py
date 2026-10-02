

# part 5 Strings and file handling

# File: working_with_Formatted_user_profile_System.py
# Project: Store formatted user profiles

print("--- Formatted User Profile System ---")

name = input("Enter Name: ")
age = input("Enter Age: ")
course = input("Enter Course: ")
city = input("Enter City: ")

# String formatting
profile = f"Name: {name.upper()} | Age: {age} | Course: {course} | City: {city}"
print("\nFormatted Profile:")
print(profile)

# Store in file
with open("students.txt", "a") as file:
    file.write(profile + "\n")

with open("data.txt", "a") as file:
    file.write(f"\nUser: {name}, Age: {age}, Course: {course}, City: {city}\n")

print("\nProfile saved to students.txt and data.txt")

# Show all profiles
print("\n--- All Saved Profiles ---")
try:
    with open("students.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("No file found yet.")