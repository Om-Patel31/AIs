import random

def guess():
    global g_number
    global num
    while True:
        num = random.randint(1, 10)
        user_input = input("Guess a number between 1 to 10:")
        if user_input.isdigit():
            g_number = int(user_input)
            break
        else:
            print("Invalid input. Please enter a valid integer.")
            print()

while True:
    guess()
    if num == g_number:
        print(f"The number is {num}")
        print("You did it!")
        yn = input("Do you want to continue? (yes/no)")
        if "n" in yn.lower():
            print("Thank you for playing.")
            break
    elif g_number > 10:
        print("Please enter a number below 10.")
        print()
    else:
        print(f"The number is {num}")
        print("Wrong guess! Try again.")
    print()