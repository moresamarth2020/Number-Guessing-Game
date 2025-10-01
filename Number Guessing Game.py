import random

def number_guessing_game():
    print("🎮 Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print("Can you guess it? 🤔\n")
    
    number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            attempts += 1
            
            if guess < number:
                print("📉 Too low! Try again.\n")
            elif guess > number:
                print("📈 Too high! Try again.\n")
            else:
                print(f"🎉 Congratulations! You guessed the number {number} in {attempts} attempts.")
                break
        except ValueError:
            print("⚠ Please enter a valid number!\n")

# Run the game
number_guessing_game()
