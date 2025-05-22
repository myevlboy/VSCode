import tkinter as tk
from tkinter import simpledialog, messagebox
import getpass
import random

#makes popup
root = tk.Tk()
root.withdraw()

#Initial popup
messagebox.showinfo("Calc", "welcome to the calculator")

x = simpledialog.askinteger("Input", "Enter a number:")
y = simpledialog.askinteger("Input", "Enter another number:")


def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y
def calculator():
    operation = simpledialog.askstring("Input", "Enter operation (+, -, *, /):")
    if operation == '+':
        result = add(x, y)
    elif operation == '-':
        result = subtract(x, y)
    elif operation == '*':
        result = multiply(x, y)
    elif operation == '/':
        result = divide(x, y)
    else:
        result = "Invalid operation"
    
    messagebox.showinfo("Result", f"The result is: {result}")
calculator()
#testing

