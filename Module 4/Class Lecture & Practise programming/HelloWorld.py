from tkinter import *

# Creates and assigns a reference to the window
window = Tk()
# Sets the title of the window (optional)
window.title("Hello world in a window")
# Sets the startup size of the window (optional)
window.geometry("700x400")
# Creates a label which will be placed on the window
# and display the text "Hello world!"
label = Label(window, text="Hello world!")
# Displays the label with 200 on the x axis and 50 on the y.
label.pack(padx=200, pady=50)
# Starts listening for events.
window.mainloop()
