from tkinter import *
from tkinter import ttk


# TODO Consolidate press_number & press_op & calculate to run through update_label
def update_label():
    pass


def press_number(btnval=int):
    dv = displayVar.get()
    
    # Initial Number, replaces the DisplayVar if its been CLEARED or after a RESULT
    if (dv == "0") or (dv == "RESULT"):
        displayVar.set(f'{btnval}')
        
    # When Numbers are Pressed, update DisplayVar to append the number
    else:
        displayVar.set(f'{dv}{btnval}')

    # DEBUG    
    print("clicked number button", btnval)


def press_op(btnOp=StringVar):
    # When Operator is pressed, update DisplayVar to append to operator
    dv = displayVar.get()
    displayVar.set(f'{dv}{btnOp}')

    print("clicked operator button", btnOp)
    

def calculate():
    # Apply the corresponding operation to the inputted numbers
    # Reset and update DisplayVar with the result

    # Numbers
    # Operator

    # replace displayVar with the result
    # result = 0  # Eventually, will be an integer result. For now, String
    result = "RESULT"
    displayVar.set(f'{result}')


def clearCalc():
    # Reset the Display
    displayVar.set("0")

    # Remove any numbers or operators in the deques
    ##


def callback(*args):
    print("variable changed!")

### GUI Creation ###
# Creates the Top Level Window, (root window), main window of application
root = Tk()
# Create a Frame Widget (which holds the app)= Frame inside Root
frm = ttk.Frame(root, padding=10)
frm.grid()

# Display Label Widget
displayVar = StringVar()
displayVar.trace("w", callback)     # Tracking when it gets changed
displayVar.set("0")                 # Display starts at showing 0

ttk.Label(frm, textvariable=displayVar).grid(column=0, row=0)
#ttk.Label(frm, text="ExpressionLabelStatic").grid(column=0, row=0)

# Calculator Buttons Widgets - frame to hold the buttons
calcFrm = ttk.Frame(frm, padding=10) #.grid(column=0, row=1)
calcFrm.grid()

# Numbers
ttk.Button(calcFrm, text="7", command= lambda: press_number(7)).grid(column=0, row=0)
ttk.Button(calcFrm, text="8", command= lambda: press_number(8)).grid(column=1, row=0)
ttk.Button(calcFrm, text="9", command= lambda: press_number(9)).grid(column=2, row=0)

ttk.Button(calcFrm, text="4", command= lambda: press_number(4)).grid(column=0, row=1)
ttk.Button(calcFrm, text="5", command= lambda: press_number(5)).grid(column=1, row=1)
ttk.Button(calcFrm, text="6", command= lambda: press_number(6)).grid(column=2, row=1)

ttk.Button(calcFrm, text="1", command= lambda: press_number(1)).grid(column=0, row=2)
ttk.Button(calcFrm, text="2", command= lambda: press_number(2)).grid(column=1, row=2)
ttk.Button(calcFrm, text="3", command= lambda: press_number(3)).grid(column=2, row=2)

# Operators
ttk.Button(calcFrm, text="+", command= lambda: press_op("+")).grid(column=3, row=0)
ttk.Button(calcFrm, text="-", command= lambda: press_op("-")).grid(column=3, row=1)
ttk.Button(calcFrm, text="*", command= lambda: press_op("*")).grid(column=3, row=2)
ttk.Button(calcFrm, text="/", command= lambda: press_op("/")).grid(column=3, row=3)

# CLEAR Button
ttk.Button(calcFrm, text="CC", command=clearCalc).grid(column=0, row=3)
# 0 Button
ttk.Button(calcFrm, text="0", command= lambda: press_number(0)).grid(column=1, row=3)
#ttk.Button(calcFrm, text="0", command= lambda: press_number(0)).grid(column=1, row=3)
# Calculate Button
ttk.Button(calcFrm, text="=", command=calculate).grid(column=2, row=3)
#ttk.Button(calcFrm, text="=", command=calculate).grid(column=0, columnspan=2, row=3, sticky="NSEW")


## When creating a child widget, must pass parent widget as first argument to the widget constructor
## Use on any widget - configure() for dictionary of info about object, keys() get the names of each option

# Puts everything on display, and responds to user input until the program terminates
root.mainloop()
