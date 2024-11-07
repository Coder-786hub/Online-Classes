# Tkinter (GUI Programming)
# Tkinter is a graphical user interface (GUI) module for Python, you can make desktop apps with Python. You can make windows, buttons, show text and images amongst other things.

# Tk and Tkinter apps can run on most Unix platforms. This also works on Windows and Mac OS X.
# The module Tkinter is an interface to the Tk GUI toolkit.


"""Tkinter module
This example opens a blank desktop window. The tkinter module is part of the standard library.
To use tkinter, import the tkinter module.

from tkinter import *
This is tkinter with underscore t, it has been renamed in Python 3."""


# Setup the window
# Start tk and create a window.


# root = Tk()
# The program below shows an empty tkinter window.
# Run with the program below:

# from tkinter import *

# initialize tkinter
# root = Tk()

# set window title
# root.title("Tkinter window")

# show window
# root.mainloop()

# from tkinter import *
# print(TkVersion)


# import tkinter as tk
from tkinter import *




root = Tk()
# root.geometry("500x400+50+100")
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()
# # root.attributes("-fullscreen", True)
# root.geometry(f"{screen_width}x{screen_height}")
root.geometry("500x400")
root.title("Tkinter")
root.resizable(0,0)
root.config(bg = "green")

# label = Label(root,text = "Tkinter Window", font = ("arial", 35, "bold"), bg = "green", fg = "white")
# label.pack(fill = "x", ipadx = 30)

label2 =Label(root, text = "Label2", font = ("arial", 35, "bold"), bg = "green", fg = "white")
label2.place(x = 30, y = 200)


label3 = Label(root, text = "LAbel3",font = ("arial", 35, "bold"), bg = "green", fg = "white")
label3.grid( padx = 20)

# label4 = Label(root, text = "LAbel3",font = ("arial", 35, "bold"), bg = "blue", fg = "white")
# label4.grid(padx = 20, pady = 20)

# label5 = Label(root, text = "LAbel3",font = ("arial", 35, "bold"), bg = "red", fg = "white")
# label5.grid( padx = 20, pady = 20)

# label6 = Label(root, text = "LAbel3",font = ("arial", 35, "bold"), bg = "green", fg = "white")
# label6.grid( padx = 20, pady = 20)

root.mainloop()

