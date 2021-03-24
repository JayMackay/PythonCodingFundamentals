import random

MAX_GOES = 5

myName = input("Hello! What is your name? ")

number = random.randint(1, 100)

print(f"Well, {myName}, I am thinking of a number between 1 and 100.")
print("Can you guess what it is? You have 5 goes.\n")

guessed = False
no_of_goes = 0

while no_of_goes < MAX_GOES:
    guess = int(input("Take a guess: ") )
    no_of_goes += 1

    if guess < number:
        print("Guess is too low")
    elif guess > number:
        print("Guess is too high")     
    elif guess == number:
        guessed = True
        break

if guessed:
    print(f"Good job, {myName}. You guessed my number.")
    print("Well done!")
else:
    print(f"Better luck next time. The number was {number}.")
