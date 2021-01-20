from tkinter import *
import tkinter.messagebox as mbox


def show_info():
    # An information messagebox
    mbox.showinfo("Information", "Some information")


def show_warning():
    # A warning messagebox
    mbox.showwarning("Warning", "A warning")


def show_error():
    # An error messagebox
    mbox.showerror("Error", "An error has occurred")


def show_askquestion():
    # The messagebox asks the user a question to which the response
    # will either be "yes" or "no".
    answer = mbox.askquestion("Question", "Are you sure?")
    if answer == "yes":
        mbox.showinfo("Response", "You answered yes")
    else:
        mbox.showinfo("Response", "You answered no")


def show_askokcancel():
    # The messagebox asks the user a question to which the response
    # will either be 1 for OK or no response for Cancel.
    answer = mbox.askokcancel("Question", "Click OK to proceed or Cancel?")
    if answer == 1:
        mbox.showinfo("Response", "You answered OK")
    else:
        mbox.showinfo("Response", "You answered Cancel")


def show_askyesno():
    # The messagebox asks the user a question to which the response
    # will either be 1 for Yes or no response for No.
    answer = mbox.askyesno("Question", "Yes or No?")
    if answer == 1:
        mbox.showinfo("Response", "You answered Yes")
    else:
        mbox.showinfo("Response", "You answered No")


def show_askretrycancel():
    # The messagebox asks the user a question to which the response
    # will either be 1 for Retry or no response for Cancel.
    answer = mbox.askretrycancel("Question", "Retry or Cancel?")
    if answer == 1:
        mbox.showinfo("Response", "You answered Retry")
    else:
        mbox.showinfo("Response", "You answered Cancel")


window = Tk()
window.title("Messagebox examples")
window.geometry("700x400")

btn_info = Button(window, text="Info", command=show_info)
btn_info.place(x=30, y=30)
btn_warning = Button(window, text="Warning", command=show_warning)
btn_warning.place(x=130, y=30)
btn_error = Button(window, text="Error", command=show_error)
btn_error.place(x=230, y=30)
btn_askquestion = Button(window, text="Question", command=show_askquestion)
btn_askquestion.place(x=330, y=30)
btn_askokcancel = Button(window, text="Ok / Cancel", command=show_askokcancel)
btn_askokcancel.place(x=30, y=60)
btn_askyesno = Button(window, text="Yes / No", command=show_askyesno)
btn_askyesno.place(x=130, y=60)
btn_askretrycancel = Button(window, text="Retry / Cancel", command=show_askretrycancel)
btn_askretrycancel.place(x=230, y=60)

window.mainloop()
