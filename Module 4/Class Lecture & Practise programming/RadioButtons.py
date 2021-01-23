from tkinter import *

def show_option():
    # Updates the options StringVar by retrieving the values from;
    # the gender and agerange StringVar objects.
    options.set("{} aged {}. ".format(gender.get(), agerange.get()))

window = Tk()
window.title("Providing options with Radiobuttons")
window.geometry("700x140")

# All widgets in this example have their background color;
# Set to "lightgray" to demonstrate that it is possible to,
# set these attributes via the widget's constructor.

# Creates a frame for containing the gender "radiobuttons",
# and place it at the coordinates 10,10.
frame_gender = Frame(window, bg="lightgray")
frame_gender.place(x=10, y=10)

# Create a frame for containing the age_range radiobuttons;
# and place it at the coordinates 120,80.
frame_agerange = Frame(window, bg="lightgray")
frame_agerange.place(x=120, y=10)

# Create a button for displaying the currently selected radiobutton values.
btn_select = Button(window, text="Select", command=show_option)
btn_select.place(x=10, y=80)

# Creates a StringVar to be linked to the 2 gender radiobuttons.
gender = StringVar()

# Creates radiobuttons for a Female and Male options.
# Both radiobuttons are given display text, a value and linked to the gender StringVar.
# When either of the two radiobuttons are selected, the other is automatically deselected.
# The selected radiobuttons's value is then assigned to the gender StringVar object.
# Both radiobuttons are placed at the top of the frame_gender and anchored on # their left side,
# by using the W anchor.
rad_female = Radiobutton(frame_gender, text="Female", value="Female", variable=gender, bg="lightgray")
rad_female.pack(side=TOP, anchor=W)
rad_male = Radiobutton(frame_gender, text="Male", value="Male", variable=gender, bg="lightgray")
rad_male.pack(side=TOP, anchor=W)
# Select rad_females as the default option.
rad_female.select()

# Creates a StingVar to be linked to the 3 agerange radiobuttons.
agerange = StringVar()
# Creates radiobuttons for 3 age range options.
# All 3 radiobuttons are given display text, a value and linked to be gender StringVar.
# When any of the 3 radiobuttons are selected, the other are automatically deselected.
# The selected radiobuttons's value is then assigned to the age_range StringVar object.
# All 3 radiobuttons are place at the top of frame_agerange and anchored # on their left side;
# by using the W anchor.
rad_under18 = Radiobutton(frame_agerange, text="Under 18", value="Under 18", variable=agerange, bg="lightgray")
rad_under18.pack(side=TOP, anchor=W)
rad_18to30 = Radiobutton(frame_agerange, text="18 to 30", value="18 to 30", variable=agerange, bg="lightgray")
rad_18to30.pack(side=TOP, anchor=W)
rad_over30 = Radiobutton(frame_agerange, text="Over 30", value="Over 30", variable=agerange, bg="lightgray")
rad_over30.pack(side=TOP, anchor=W)
# Selects rad_18to30 as the default option.
rad_18to30.select()

# Declares a StringVar object to be linked to lbl_options.
options = StringVar()
# Sets the initial text by calling the show_options().
# Even though this function is linked to btn_select, it may still be called;
# anywhere else in code.
# Since this function has already been set up to retrieve the values from the gender;
# and "agerange" StringVar objects and assign it to the function that to rewrite the # code.
show_option()
# Create a lable in the window and links it to the option StringVar object.
lbl_options = Label(window, textvariable=options)
# The label is places at the coordinates 10,110.
lbl_options.place(x=10, y=110)

# Starts listening for events.
window.mainloop()
