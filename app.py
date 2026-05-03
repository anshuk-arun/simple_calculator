from tkinter import *
from tkinter import ttk

# Creates the Top Level Window, (root window), main window of application
root = Tk()
# Create a Frame Widget (which will hold the label and button) = Frame inside Root
frm = ttk.Frame(root, padding=10)
frm.grid()

# Label Widget
ttk.Label(frm, text="Calculator").grid(column=0, row=0)
# Button Widget - this one can destroy the window (aka close out)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

## When creating a child widget, must pass parent widget as first argument to the widget constructor
## Use on any widget - configure() for dictionary of info about object, keys() get the names of each option

# Puts everything on display, and responds to user input until the program terminates
root.mainloop()
