from tkinter import *


# Called when btn_update is clicked
def update_colour():
    # cget() is used to retrieve the configured value of a specified
    # attribute; in this case bg (background color).  This
    # function basically switches the window background colour
    # between lightgray and lightblue every time the function is called.
    if window.cget("bg") == "lightgray":
        window.configure(bg="lightblue")
    else:
        window.configure(bg="lightgray")


window = Tk()
window.title("Working with buttons")
# configure may be used to modify a specific attribute of a window
# or widget.  In this case the bg (background color) attribute is changed.
window.configure(bg="lightgray")

# Creates a Button on the window and sets it's text to Update colour.
# The command named argument specifies which function should be called when the
# button is clicked.  In this case, the function update_colour will be called.
btn_update = Button(window, text="Update colour", command=update_colour)
# Explicitly states that the button should be placed at the coordinates (20,20)
btn_update.place(x=20, y=20)
# The exit method is assigned as the command.  This is a built-in method
# that ends the program.  An alternative / alias for exit is to call quit.
btn_exit = Button(window, text="Exit", command=exit)
# Explicitly states that the button should be placed at the coordinates #(120,20)
btn_exit.place(x=120, y=20)
window.mainloop()
