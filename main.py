# main.py
# Task 3 - Guess the Number and Word Scramble
# Name: Gopala Krishnan M

import random

# Guess the Number game
def guess_number() -> None:
    print("Have fun with Guess the Number game!")
    number =45
    guess =0

    while guess != number:
        guess = int(input("Enter your guess (1–50): "))

        if guess < number:
            print("Too low! Try again or Run the program again for new games.")
        elif guess > number:
            print("Too high! Try again or Run the program again for new games.")
        else:
            print("Correct! The number was:", number,"Run the program again for new games")


# Word Scramble game
def word_scramble():
    words = ['python', 'javascript', 'java', 'automation', 'pytest', 'guvi', 'selenium']
    word = random.choice(words)
    scrambled = ''.join(random.sample(word, len(word)))

    print("\nUnscramble the word:", scrambled)
    guess = ""

    while guess != word:
        guess = input("Enter your guess: ").lower()

        if guess == word:
            print("Correct! The word was:", word,"Run the program again for new games")
        else:
            print(" Wrong! Try again or Run the program again for new games")


# Main menu
print("Welcome to fun Games!")
print("Choose a game to play:")
print("1. Guess the Number")
print("2. Word Scramble")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    guess_number()
elif choice == "2":
    word_scramble()
else:
    print("Invalid choice! Please choose 1 or 2 only. Try the program again.")
