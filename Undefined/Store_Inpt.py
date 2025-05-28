#imports
import os
import tkinter as tk
from tkinter import messagebox

# Example usage:
messagebox.showinfo(title="Greetings", message="Hello, World!")

root = tk.Tk()
root.withdraw()  # Hide the root window

root.option_add("*Dialog.msg.width*", 700)
#root.option_add("*Dialog.msg.wraplength*", 600)

messagebox.showinfo(title="test", message="A longer asdfasdfa sdf sdaf sadf  ")

root.destroy()

