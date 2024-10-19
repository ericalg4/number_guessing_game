import random

def number_guessing_game():
    # Step 1: Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Step 2: Loop until the user guesses correctly
    while not guessed:
        try:
            # Step 3: Ask for user input and check if it's a valid number
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Step 4: Give feedback
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
        except ValueError:
            print("Please enter a valid number.")
        
# Start the game
number_guessing_game()
