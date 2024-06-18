print('Dice roll')
import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("Dice game ni Bai!")
    
    while True:
        input("Pinduta ang Enter to roll the Dice")
        
        dice_result = roll_dice()
        print(f"You rolled: {dice_result}")
        
        play_again = input("Do you want to roll again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Saalamat!")
            break

if __name__ == "__main__":
    main()