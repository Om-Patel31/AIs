while True:
    x = input("Enter your name:")
    print(f"Hi, {x}")
    input("How are you?")
    if "fine" or "good":
        print("That's good to hear")
        y = input("How was your day")
        if "good" or "fine" or "nice":
            print("Ok, good day ahead!")
    else:
        print("Have a good day!")
        break