import tkinter as tk
import random

def guess_number(event=None):
    global num
    global guess_entry
    guess = guess_entry.get()
    if guess.isdigit():
        guess = int(guess)
        if guess == num:
            result_label.config(text="", bg="green", fg="lightblue")
            new_game()
        else:
            result_label.config(text="Try again!", bg="green", fg="lightblue")
    else:
        result_label.config(text="Invalid input. Please enter a number.", fg="orange")

def new_game():
    global num
    num = random.randint(1, 10)
    result_label.config(text="", fg="black")
    guess_entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Number Guessing Game")
root.configure(bg="orange")

# Generate a random number
num = random.randint(1, 10)

# Styles
button_style = {"font": ("Montserrat", 12), "bg": "green", "fg": "white", "bd": 2, "relief": "raised"}

# Widgets
title_label = tk.Label(root, text="Guess a number between 1 and 10", font=("Montserrat Black", 16), bg="White")
guess_entry = tk.Entry(root, font=("Montserrat", 14))
guess_button = tk.Button(root, text="Guess", command=guess_number, **button_style)
result_label = tk.Label(root, text="", font=("Montserrat", 14), bg="lightblue")
new_game_button = tk.Button(root, text="New Game", command=new_game, **button_style)

# Layout
title_label.pack(pady=10)
guess_entry.pack(pady=5, fill="x", expand=True)
guess_button.pack(pady=5, fill="x", expand=True)
result_label.pack(pady=10)
new_game_button.pack(pady=5, fill="x", expand=True)

# Bind Enter key to guess_number function
root.bind("<Return>", guess_number)

# Run the main loop
root.mainloop()