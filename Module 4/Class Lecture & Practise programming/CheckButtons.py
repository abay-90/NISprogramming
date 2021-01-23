from tkinter import *


def calculate():
    # This method calls get() on each of the 3 IntVar objects and adds the
    # value to the running total.
    # The result of each get() will either be the associated checkbutton's
    # onvalue (if it is selected) or offvalue.

    total = 0
    total += topping_1.get()
    total += topping_2.get()
    total += topping_3.get()

    # Updates the value of the calculation StringVar,
    # which in turn updates the label.
    calculation.set("Total cost:\t{}.".format(total))


window = Tk()
window.title("Calculating a sandwich price with checkbuttons")
window.geometry("700x140")

frame_toppings = Frame(window)
frame_toppings.place(x=10, y=10)

# Since the onvalue and offvalue of all 3 the Checkbuttons are numeric,
# IntVar objects are used instead of StringVar objects.
topping_1 = IntVar()
topping_2 = IntVar()
topping_3 = IntVar()

# 3 CheckButtons are created and added to a frame.  Each are assigned
# an onvalue as the price of the topping and an offvalue of 0.  This means
# that if the Checkbutton is selected the onvalue will be copied to the
# associated InVar object. If the Checkbutton is de-selected, the offvalue
# will be assigned to the associated InVar object.  All 3 Checkbuttons
# are assigned the same command function as calculate.  This function
# will be called whenever any of the 3 are selected or de-selected.
chk_cheese = Checkbutton(frame_toppings, onvalue=5, offvalue=0,
                         text="Cheese", variable=topping_1, command=calculate)
chk_cheese.pack(side=TOP, anchor=W)
chk_ham = Checkbutton(frame_toppings, onvalue=10, offvalue=0,
                      text="Ham", variable=topping_2, command=calculate)
chk_ham.pack(side=TOP, anchor=W)
chk_tomato = Checkbutton(frame_toppings, onvalue=3, offvalue=0,
                         text="Tomato", variable=topping_3, command=calculate)
chk_tomato.pack(side=TOP, anchor=W)

# Creates a StringVar to associated with the label to display the price
calculation = StringVar()
# Calls the calculate function to calculate and display the initial
# sandwich price.
calculate()
# Creates the label and associates it with the calculation StringVar
lbl_calculation = Label(frame_toppings, textvariable=calculation)
lbl_calculation.pack(anchor=W, pady=10)

window.mainloop()
