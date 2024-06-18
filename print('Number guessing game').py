print('Number guessing game')

import random

def number_guessing_game():
    print("Number Guessing Game!")
    print("Guess from 1 to 100")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        user_guess = input("Enter your guess: ")
        
        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        attempts += 1
        
        if user_guess < secret_number:
            print("Too low. Try again.")
        elif user_guess > secret_number:
            print("Too high. Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts.")
            break

if __name__ == "__main__":
    number_guessing_game()