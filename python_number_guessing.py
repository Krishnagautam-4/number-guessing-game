import random

number_to_guess = random.randint(1, 100)
attempts = 0

print("🎯 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while True:
    guess = input("Enter your guess: ")

    if not guess.isdigit():
        print("❌ Please enter a valid number.")
        continue

    guess = int(guess)
    attempts += 1

    if guess < number_to_guess:
        print("Too low! 📉")
    elif guess > number_to_guess:
        print("Too high! 📈")
    else:
        print(f"🎉 Correct! You guessed it in {attempts} attempts.")
        break
