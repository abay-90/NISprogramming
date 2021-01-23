from tkinter import *
import tkinter.messagebox as mbox


def perform_add():
    value1 = int(ent_value1.get())
    value2 = int(ent_value2.get())

    result = value1 + value2

    mbox.showinfo("Addition result", "{0} + {1} = {2}".format(value1, value2, result))


def perform_subtract():
    value1 = int(ent_value1.get())
    value2 = int(ent_value2.get())

    result = value1 - value2

    mbox.showinfo("Subtraction result", "{0} - {1} = {2}".format(value1, value2, result))


def perform_multiply():
    value1 = int(ent_value1.get())
    value2 = int(ent_value2.get())

    result = value1 * value2

    mbox.showinfo("Multiplication result", "{0} * {1} = {2}".format(value1, value2, result))


window = Tk()
window.title("Calculate")
window.geometry("700x100")

lbl_value1 = Label(window, text="Value 1:")
lbl_value1.place(x=5, y=10)
ent_value1 = Entry(window)
ent_value1.place(x=150, y=5)

lbl_value2 = Label(window, text="Value 2:")
lbl_value2.place(x=5, y=40)
ent_value2 = Entry(window)
ent_value2.place(x=150, y=35)

btn_add = Button(window, text="Add", command=perform_add)
btn_add.place(x=197, y=65)
btn_subtract = Button(window, text="Subtract", command=perform_subtract)
btn_subtract.place(x=230, y=65)
btn_multiply = Button(window, text="Multiply", command=perform_multiply)
btn_multiply.place(x=290, y=65)

window.mainloop()


