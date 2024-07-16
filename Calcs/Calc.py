import tkinter as tk

def button_click(button_text):
    current_text = display_label.cget("text")
    if button_text == "C":
        # Clear the display
        display_label.config(text="")
    elif button_text == "=":
        # Calculate the result
        try:
            result = eval(current_text)
            display_label.config(text=str(result))
        except Exception as e:
            display_label.config(text="Error")
    else:
        # Append the button text to the current display
        display_label.config(text=current_text + button_text)

def key_press(event):
    # Map keys to corresponding button texts
    key_mapping = {
        "0": "0", "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9",
        "+": "+", "-": "-", "*": "*", "/": "/", ".": ".", "<Return>": "=", "<BackSpace>": "C"
    }
    key = event.keysym
    if key in key_mapping:
        button_click(key_mapping[key])

# Create the main window
window = tk.Tk()

# Get screen dimensions
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Set window size to full screen
window.geometry(f"{screen_width}x{screen_height}")

# Set the title of the window
window.title("Calculator")

# Create a label to display the input and output
display_label = tk.Label(window, text="", font=("Helvetica", 16), width=20, borderwidth=2, relief="groove")
display_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define the button texts
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+", "C"
]

# Calculate button width and height based on screen size
button_width = screen_width // 100
button_height = screen_height // 100

# Create buttons and place them in a grid
row_index = 1
col_index = 0
for button_text in buttons:
    button = tk.Button(window, text=button_text, width=button_width, height=button_height, command=lambda text=button_text: button_click(text))
    button.grid(row=row_index, column=col_index, padx=5, pady=5, sticky="nsew")
    col_index += 1
    if col_index > 3:
        col_index = 0
        row_index += 1

# Bind keyboard events
window.bind("<Key>", key_press)

# Run the main event loop
window.mainloop()
