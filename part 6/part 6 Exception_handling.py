

# Part 6: Exception and Error Handling
# File 2: Exception_handling.py

import datetime

def log_error(error_msg):
    with open("error_log.txt", "a") as file:
        time = datetime.datetime.now()
        file.write(f"[{time}] - ERROR: {error_msg}\n")

try:
    a = int(input("Number 1: "))
    b = int(input("Number 2: "))
    print(f"Answer: {a/b}")

    my_list = [10, 20, 30]
    index = int(input("Index (0-2): "))
    print(f"Value: {my_list[index]}")

except ZeroDivisionError as e:
    print("Error: Divide by zero!")
    log_error(f"ZeroDivisionError - {e}")
except ValueError as e:
    print("Error: Invalid value!")
    log_error(f"ValueError - {e}")
except IndexError as e:
    print("Error: Index out of range!")
    log_error(f"IndexError - {e}")
except Exception as e:
    log_error(f"Unknown Error - {e}")

# File 3: error_log.txt will be created automatically after error
