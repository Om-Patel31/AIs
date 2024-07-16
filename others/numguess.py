import random

while True:
    num = random.randint(1,10)

    user = int(input("Enter a number between 1 to 10:"))

    if user == num:
        print("You did it!")
    print("The number is:", num)