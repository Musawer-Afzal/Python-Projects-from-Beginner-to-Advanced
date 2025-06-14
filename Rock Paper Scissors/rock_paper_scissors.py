import random

user_wins = 0
computer_wins = 0

while True:
    print(f"Computer wins: {computer_wins} User wins: {user_wins}")
    user_input = input("Choose Rock, Paper, or Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in ["rock", "paper", "scissors"]:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    if random_number == 0:
        computer_pick = "rock"
    elif random_number == 1:
        computer_pick = "paper"
    else:
        computer_pick = "scissors"

    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
    else:
        print("You lost!")
        computer_wins += 1