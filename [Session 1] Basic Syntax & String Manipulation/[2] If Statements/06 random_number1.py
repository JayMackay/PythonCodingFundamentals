import random

user_name = input("Hello! What is your name? ")

# Unusually for Python, the second value is included in the range
number = random.randint(1, 10)

print(f"Well, {user_name}, I am thinking of a number between 1 and 10.")

guess = int(input("Take a guess: "))

if guess == number:
    print(f"Good job, {user_name}! You guessed my number.")
