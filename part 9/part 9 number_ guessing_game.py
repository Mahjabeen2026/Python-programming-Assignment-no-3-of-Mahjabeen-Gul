

#PART 9 Interactive Game-Number Guessing Game

import random

def number_guessing_game():
    print("--- Number Guessing Game ---")
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    print("I have selected a number between 1 and 100. Try to guess it!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Hint: Higher! Try a bigger number.")
            elif guess > secret_number:
                print("Hint: Lower! Try a smaller number.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                print(f"The secret number was {secret_number}")
                break
        except ValueError:
            print("Please enter a valid number.")

# Run the game
number_guessing_game()