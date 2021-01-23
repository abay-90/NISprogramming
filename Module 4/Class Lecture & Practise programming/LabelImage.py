from tkinter import *

window = Tk()
window.title("Image in a label")
window.geometry("700x200")

# Create a PhotoImage object by pointing it to the file
# to be loaded.
img = PhotoImage(file="Noroff.gif")
# Create a label and assign the PhotoImage object to its
# image property.
label = Label(window, image=img)
label.pack(side=TOP, pady=10)

window.mainloop()
