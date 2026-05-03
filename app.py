from tkinter import *
from tkinter import ttk


def update_label():
    pass

def press_number():
    pass

def press_op():
    pass

def calculate():
    pass

# Creates the Top Level Window, (root window), main window of application
root = Tk()
# Create a Frame Widget (which holds the app)= Frame inside Root
frm = ttk.Frame(root, padding=10)
frm.grid()

# Create a Paned Window (which holds the label) = Paned Window inside Frame
pw = ttk.Panedwindow(frm, orient='vertical')
pw.grid()

# Display Label Widget
displayStr = "Expression"
ttk.Label(pw, text="Expression_Test", textvariable=displayStr).grid(column=0, row=0)

## TODO error, Label won't show up

# Calculator Buttons Widgets - frame to hold the buttons - at bottom of Paned Window
calcFrm = ttk.Frame(pw, padding=10).grid(column=0, row=1)

# Numbers
ttk.Button(calcFrm, text="7", command=press_number).grid(column=0, row=0)
ttk.Button(calcFrm, text="8", command=press_number).grid(column=1, row=0)
ttk.Button(calcFrm, text="9", command=press_number).grid(column=2, row=0)

ttk.Button(calcFrm, text="4", command=press_number).grid(column=0, row=1)
ttk.Button(calcFrm, text="5", command=press_number).grid(column=1, row=1)
ttk.Button(calcFrm, text="6", command=press_number).grid(column=2, row=1)

ttk.Button(calcFrm, text="1", command=press_number).grid(column=0, row=2)
ttk.Button(calcFrm, text="2", command=press_number).grid(column=1, row=2)
ttk.Button(calcFrm, text="3", command=press_number).grid(column=2, row=2)

# Operators
ttk.Button(calcFrm, text="+", command=press_op).grid(column=3, row=0)
ttk.Button(calcFrm, text="-", command=press_op).grid(column=3, row=1)
ttk.Button(calcFrm, text="*", command=press_op).grid(column=3, row=2)
ttk.Button(calcFrm, text="/", command=press_op).grid(column=3, row=3)

# 0 Button
ttk.Button(calcFrm, text="0", command=press_number).grid(column=1, row=3)
# Calculate Button
ttk.Button(calcFrm, text="=", command=calculate).grid(column=0, row=3)


# # Button Widget - this one can destroy the window (aka close out)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

## When creating a child widget, must pass parent widget as first argument to the widget constructor
## Use on any widget - configure() for dictionary of info about object, keys() get the names of each option

# Puts everything on display, and responds to user input until the program terminates
root.mainloop()
