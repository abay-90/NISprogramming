from tkinter import *

def show_selection():
    # The set function of the stringVar message is used to update its contents.
    # listbox.curselection returns to the index(es) of the selected item(s).
    # listbox.get is used to retrieve selected item by specifying an index.
    message.set("Index:\t{}\nValue:\t{}".format(listbox.curselection(),
                                                 listbox.get(listbox.curselection())))


window = Tk()
window.title("NIS 2nd year syllabus.")
window.geometry("700x250")

# Creates a frame inside the window
frame = Frame(window)
# Places the frame at the top of the window, but with 10 pixels,
# of vertical padding.
frame.pack(side=TOP, pady=10)

# Creates a listbox 40 characters in width and place it inside the frame.
listbox = Listbox(frame, width=40)
# Add 7 items to the listbox.
# The index is used by the listbox to insert an item before the specified line;
# E.g. when an index of 2 is specified the item is inserted at line 1.
# tkinter provides a built-in keyword END which may be used instead of an index.
# This will always add an item as the last item.
# That means all of the numbered indexes below could have been replaced with END.
listbox.insert(1, "LAW061 - Security and the Law")
listbox.insert(2, "SEC061 - Network Security")
listbox.insert(3, "RAS061 - Preventive Security")
listbox.insert(END, "HIR071 - Hacking Tools, Incidents and Response")
listbox.insert(5, "PRG111 - Programming")
listbox.insert(6, "SQL051 - Databases")
listbox.insert(END, "COF061 - Computer Forensics")
# Places the listbox on the left side of the frame, with 5 pixels of horizontal padding.
listbox.pack(side=LEFT, padx=5)

btn = Button(frame, text="Select", command=show_selection)
# Place the button on the right side of the frame.
btn.pack(side=RIGHT)

# Creates a new StringVar object
message = StringVar()
# Sets the initial content of the StringVar
message.set("No selection made")
# Creates a label and assign it to the window.
# The label's content is linked to the content of the StringVar,
# object using the textvariable named argument.
lbl_selected = Label(window, textvariable=message)
# Place the label at the bottom of the window with 10 pixels of vertical padding.
lbl_selected.pack(side=BOTTOM, pady=10)

# Starts listening for events.
window.mainloop()