import tkinter as tk
from tkinter import simpledialog, messagebox
import getpass
import random

#makes popup
root = tk.Tk()
root.withdraw()

messagebox.showinfo("welcome to the calculator")

user = getpass.getuser()
messagebox.showinfo("welcome", f"Hello {user} welcome to the calculator")