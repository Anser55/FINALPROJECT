print('Typing master')
import random
import time

def generate_random_word():
    words = ['typing', 'master', 'drink', 'more', 'beer', 'anser', 'gwapo', 'do', 'not', 'copy']
    return random.choice(words)

def typing_master_game():
    print("TYPE TYPE")
    print("Type the word as fast as you can. Press 'Enter' to start.")
    input("Press Enter to start...")

    word = generate_random_word()
    print(f"Type this word: {word}")

    start_time = time.time()
    user_input = input("Your word: ")

    end_time = time.time()
    time_taken = end_time - start_time

    if user_input.strip().lower() == word:
        print(f"Correct! Time taken: {time_taken:.2f} seconds")
    else:
        print("Incorrect! Try again.")

typing_master_game()