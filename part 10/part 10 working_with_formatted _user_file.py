

#part 10 Working with formatted user profile

# working_with_Formatted_user_profile_System.py

class UserProfile:
    def __init__(self, name, email, age, city):
        self.name = name
        self.email = email
        self.age = age
        self.city = city

    def formatted_display(self):
        print("\n" + "="*35)
        print("     FORMATTED USER PROFILE")
        print("="*35)
        print(f"  Name  : {self.name.title()}")
        print(f"  Email : {self.email.lower()}")
        print(f"  Age   : {self.age}")
        print(f"  City  : {self.city.title()}")
        print("="*35 + "\n")

def create_profile():
    try:
        name = input("Enter Name: ")
        if not name:
            raise ValueError("Name cannot be empty")

        email = input("Enter Email: ")
        if "@" not in email:
            raise ValueError("Invalid Email. Must contain @")

        age = int(input("Enter Age: "))
        if age < 1 or age > 100:
            raise ValueError("Age must be 1-100")

        city = input("Enter City: ")
        return UserProfile(name, email, age, city)

    except ValueError as ve:
        print(f"Validation Error: {ve}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    while True:
        try:
            user = create_profile()
            if user:
                user.formatted_display()
            else:
                print("Try again.\n")
                continue

            again = input("Create another profile? (yes/no): ").lower()
            if again != "yes":
                print("Thank you!")
                break
        except KeyboardInterrupt:
            print("\nExit by user.")
            break

main()