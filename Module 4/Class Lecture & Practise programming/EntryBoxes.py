from tkinter import *
import tkinter.messagebox as mbox


def login():
    # Uses the entry boxes' get() method to return their current content.
    username = ent_username.get()
    password = ent_password.get()

    # Simulates a login process by checking the values of the two entry
    # boxes against a predefined username and password.  If they match,
    # i.e. the login was successful an information messagebox is
    # displayed; otherwise an error messagebox is displayed.
    if username == "JohnD" and password == "12345678":
        mbox.showinfo("Login result", "Successful login")
    else:
        mbox.showerror("Login result", "Incorrect credentials provided.")


window = Tk()
window.title("Capture input with entry boxes")
window.geometry("700x100")

lbl_username = Label(window, text="Username:")
lbl_username.place(x=5, y=10)
# Creates a basic entry box
ent_username = Entry(window)
ent_username.place(x=150, y=5)

lbl_password = Label(window, text="Password:")
lbl_password.place(x=5, y=40)
# Creates an entry box and sets the show character to *.
# This means that any character typed in the box will be shown as *.
ent_password = Entry(window, show="*")
ent_password.place(x=150, y=35)

btn_login = Button(window, text="Login", command=login)
btn_login.place(x=300, y=65)

window.mainloop()
