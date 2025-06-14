import random

top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    quit()

secret_number = random.randint(1, top_of_range)

guess = 0
guesses = 0
while guess != secret_number:
    guesses += 1
    guess = input("Make a guess: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Please type a number next time.")
        continue

    if guess == secret_number:
        print(f"You got it in {guesses} guesses!")
    elif guess > secret_number:
        print("You were above the number!")
    else:
        print("You were below the number!")