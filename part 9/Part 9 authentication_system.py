

# Part 9 Authentication system

import json
import os

FILE_NAME = "student.json"

def login_user():
    print("--- Authentication System - Login ---")
    
    email = input("Enter Email: ")
    password = input("Enter Password: ")

    # Check if file exists
    if not os.path.exists(FILE_NAME):
        print("Error: No registered users found. Please register first.")
        return

    with open(FILE_NAME, "r") as f:
        try:
            users = json.load(f)
        except:
            print("Error: Database file is empty or corrupted.")
            return

    # Check credentials against stored data
    for user in users:
        if user["email"] == email and user["password"] == password:
            print("\nLogin SUCCESS!")
            print(f"Welcome, {user['name']}!")
            print(f"Email: {user['email']}")
            return

    # If loop finishes, login failed
    print("\nLogin FAILED!")
    print("Invalid email or password. Please try again.")

# Run
login_user()