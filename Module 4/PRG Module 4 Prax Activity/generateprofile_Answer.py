from tkinter import *
import tkinter.messagebox as mbox


def ask_questions():
    total = 0
    if mbox.askquestion("Question", "Do you like exercise?") == "yes":
        total += 1
    if mbox.askquestion("Question", "Do you like healthy food?") == "yes":
        total += 1
    if mbox.askquestion("Question", "Do you get enough sleep?") == "yes":
        total += 1

    message = ""

    if total <= 1:
        message = "You do not live a healthy lifestyle."

    if total == 2:
        message = "You are doing a few healthy things, but could live healthier."

    if total == 3:
        message = "You live a healthy lifestyle. Congratulations!"

    mbox.showinfo("Quiz result", message)


window = Tk()
window.title("Calculate")
window.geometry("700x100")

btn_add = Button(window, text="Start", command=ask_questions)
btn_add.place(x=330, y=40)

window.mainloop()