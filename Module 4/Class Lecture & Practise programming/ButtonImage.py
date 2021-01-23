from tkinter import *
import tkinter.messagebox as mbox

def show_clicked():
    mbox.showinfo("Info", "Button clicked")

window = Tk()
window.title("Image in a button")
window.geometry("700x100")

img = PhotoImage(file="Noroff.gif")
# Take a sample of the given image every second x and y pixel
img_small = PhotoImage.subsample(img, x=2, y=2)
# Assigns the smaller image to the Button's image property
btn = Button(window, image=img_small, command=show_clicked)
btn.pack(side=TOP, pady=10)

window.mainloop()
