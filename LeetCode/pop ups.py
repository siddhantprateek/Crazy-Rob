# Python 3.x code
# Imports
import tkinter
from tkinter import messagebox
from tkinter.messagebox import YES

# This code is to hide the main tkinter window
root = tkinter.Tk()
root.withdraw()

# Message Box
# messagebox.showinfo("Title", "Pop it")
# messagebox.showwarning("Title", "Don't")
answer = messagebox.askquestion("Title", "Do you want a Sandwich?")
if answer == YES:
    messagebox.showinfo("Title", "Order Confirmed")
else:
    messagebox.showinfo("Title", "Order Cancelled")
