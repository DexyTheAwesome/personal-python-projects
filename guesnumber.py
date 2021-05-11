import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("\nSorry, guess again. Too low")
        elif guess > random_number:
            print("\nSorry, guess again. Too high")
    
    print(f"\nYaaaaay, congrats. You have guessed the number {random_number} correctly ")  
guess(15)

# def computer_guess(x)