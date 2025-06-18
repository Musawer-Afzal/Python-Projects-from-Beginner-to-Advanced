master__pwd = input("Please enter your master password: ")

def view():
    pass
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", 'a') as f:
        f.write(f"{name} | {pwd}\n")

while True:
    mode = input("Would you like to add or view passwords? (add/view). Type q to quit ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Not a valid option. Try again.")
        continue