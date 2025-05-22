import tkinter as tk
from tkinter import simpledialog, messagebox
import random

# Set up the root window (hidden)
root = tk.Tk()
root.withdraw()  # Hide the root window

# Ask the user for a number using a popup
user_input = simpledialog.askinteger("Input", "Enter a number between 1 and 100:")

if user_input is not None:
    # Generate target and computer number
    target = random.randint(1, 100)
    computer = random.randint(1, 100)

    # Compare distances
    diff_user = abs(target - user_input)
    diff_comp = abs(target - computer)

    # Determine result
    if diff_user < diff_comp:
        result = "You are closer to the target!"
    elif diff_comp < diff_user:
        result = "The computer is closer to the target!"
    else:
        result = "It's a tie! Both are equally close."

    # Show result in a popup
    message = (
        f"Target number: {target}\n"
        f"Your number: {user_input}\n"
        f"Computer's number: {computer}\n\n"
        f"{result}"
    )
    messagebox.showinfo("Results", message)
else:
    messagebox.showinfo("Cancelled", "No number was entered.")