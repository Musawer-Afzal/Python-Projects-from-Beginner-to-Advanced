name = input("Please type your name: ")

print("Hello", name, "and welcome to the game!")
answer = input("You are on a road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across: ").lower()

    if answer == "swim":
        print("You swam accross and were eaten by a shark!")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game!")
    else:
        print("Not a valid option. You lose!")

elif answer == "right":
    answer = input("You came across a bridge, it looks wobbly. Do you want to cross it or head back? (cross/back). ").lower()

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them? (yes/no) ").lower()

        if answer == "yes":
            print("You talk to the stranger and they give you gold. You win!")
        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose!")
        else:
            print("Not a valid option. You lose!")
    else:
        print("Not a valid option. You lose!")
else:
    print("Not a valid option. You lose!")

print(f"Thank you for trying my game {name}! Goodbye!")