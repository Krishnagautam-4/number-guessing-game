import random

number = random.randint(1, 100)
attempts = 0

print("🎯 Welcome to the Number Guessing Game!")
print("I'm thinking 🤔 of a number between 1 and 100.")

while True:
    try:
        guess = int(input("Enter your guess 🤗: "))
    except ValueError:
        print("Please enter a valid number 🤥.")
        continue

    attempts += 1

    if guess < number:
        print("Too low! 📉")
    elif guess > number:
        print("Too high! 📈")
    else:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break