from tkinter import *

window = Tk()
window.title("Drawing on a canvas")
window.geometry("700x400")

img = PhotoImage(file="Noroff.gif")
# Create a sub-sample of the Noroff.gif, by selecting only ever 3rd x and y pixel.
img_small = PhotoImage.subsample(img, x=3, y=3)

# Create a 700x400 Canvas with a lightblue background.
canvas = Canvas(window, width=700, height=400, bg="lightblue")
# Draws the normal size image at 100,50 and anchors it at the top and left # sides.
canvas.create_image(100, 50, image=img_small, anchor=NW)
# Draws the smaller size image at 520,300 and anchors it at the top and # left sides.
canvas.create_image(520, 300, image=img_small, anchor=NW)
# Draw a white line, 20 pixels in width from 400,0 to 400,400.
canvas.create_line(400, 0, 400, 400, width=20, fill="white")
# Draw the text "Noroff" in white, using Helvetica 40 Bold at 500,150.
canvas.create_text(100, 50, fill="white", font="Helvetica 40 bold",
                   text="Noroff")
canvas.pack(side=LEFT)

# Starts listening for events.
window.mainloop()
