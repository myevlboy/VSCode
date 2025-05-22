import tkinter as tk
from tkinter import simpledialog, messagebox
import getpass
import random

#makes popup
root = tk.Tk()
root.withdraw()


#Game rules
print("play against computer")
print("who ever is closer to the number\n")

#Random numbe generator

goal = random.randint(1, 20) #random number 1-20
CPU = random.randint(1, 20)
player1  = simpledialog.askinteger("Intput" ," enter a number between 1 and 20\n")

#compare to see who is closer
diff1 = (goal - player1)
diff2 = (goal - CPU)

#determines results/winner
if diff1 < diff2:
    winner = "YOU ARE THE WINNER!!!!!"
elif diff2 < diff1:
    winner = "CPU is The winner"
else:
    winner = "Results are tied"

message = (
    f"Your number is: {player1}\n"
    f"CPU's number is: {CPU}\n"
    f"Computer's number is: {goal}\n"
    f"{winner}"
)
messagebox.showinfo("results", message)



#testing
#sadf
#test

 #a
