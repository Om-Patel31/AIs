import random

def guess():
    global user_input
    global num
    user_input = input("Enter a number between 1 to 100:")
    num = random.randint(1, 100)
    if user_input == num:
        print("You did it!")
        yn = input("Do you want to continue?(yes/no)")
        if yn.lower() == "yes":
            guess()
        else:
            print("Thanks for playing.")
    else:
        print("Try again!")
        guess()
guess()