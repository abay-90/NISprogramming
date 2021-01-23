from tkinter import *
import tkinter.messagebox as mbox

def show_clicked():
    mbox.showinfo("Info", "Button clicked")

window = Tk()
window.title("Image textbox")
window.geometry("700x100")

img = PhotoImage(file="Noroff.gif")
img_small = PhotoImage.subsample(img, x=3, y=3)
# Creates a multiline Text entry,
# 50 characters wide and 5 line high
text = Text(window, width=50, height=5)
# Add an image to the Text at the last entered;
# position in the TEXT. This is done using the keyword END.
# The image is displayed in a single line.
text.image_create(END, image=img_small)
# Add text to the Text
text.insert(END, "This is a text box where you can type")
text.pack(side=TOP, pady=10)

window.mainloop()