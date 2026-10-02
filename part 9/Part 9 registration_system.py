

#Part 9 Registration System

import json
import os
import re

FILE_NAME = "student.json"

def is_valid_email(email):
    # Simple email validation
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def register_user():
    print("--- Registration System ---")
    
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    password = input("Enter Password: ")

    # Validation
    if not is_valid_email(email):
        print("Error: Invalid email format. Example: ali@gmail.com")
        return

    if len(password) < 6:
        print("Error: Password must be at least 6 characters long.")
        return

    # Load existing data
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            try:
                data = json.load(f)
            except:
                data = []
    else:
        data = []

    # Check if user already exists
    for user in data:
        if user["email"] == email:
            print("Error: This email is already registered.")
            return

    # New user data
    new_user = {
        "name": name,
        "email": email,
        "password": password  # In real projects, password should be hashed
    }

    data.append(new_user)

    # Store data in JSON file
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

    print(f"Registration Successful! User {name} saved to {FILE_NAME}")

# Run
register_user()