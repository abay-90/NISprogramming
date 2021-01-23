from tkinter import *
import tkinter.messagebox as mbox

def update_description():

    selected = ""

    if len(lb_pizzatype.curselection()) == 0:
        mbox.showerror("No pizza type selected", "Please select a pizza type.")
    else:
        selected = lb_pizzatype.get(lb_pizzatype.curselection())

    if selected == "Hawaiian (50)":
        description.set("Tomato sauce, cheese, pineapple, and ham")
    if selected == "Regina (55)":
        description.set("Tomato sauce, oregano, mozzarella, ham, mushrooms and basil")
    if selected == "Four seasons (80)":
        description.set("1/4 each of Hawaiian, Regina, Something meaty and Vegetarian")
    if selected == "Something meaty (70)":
        description.set("BBQ sauce, ham, pepperoni, bacon, ground beef")
    if selected == "Vegetarian (45)":
        description.set("Tomato sauce, mushroom, olives, pineapple, onion, spring onion")

def calculate():

    price = 0
    selected = ""

    if len(lb_pizzatype.curselection()) != 0:
        selected = lb_pizzatype.get(lb_pizzatype.curselection())

    if selected == "Hawaiian (50)":
        price = 50
    if selected == "Regina (55)":
        price = 55
    if selected == "Four seasons (80)":
        price = 80
    if selected == "Something meaty (70)":
        price = 70
    if selected == "Vegetarian (45)":
        price = 45
    if selected == "":
        mbox.showinfo("Pizza selection", "You have not selected a pizza.  A plain cheese pizza will be dispensed at a price of 30")
        price = 30

    if pizza_base == "Thick base (5)":
        price += 5

    price += topping_1.get() + topping_2.get() + topping_3.get() + topping_4.get() + topping_5.get()

    mbox.showinfo("Pizza price", "Your pizza costs {0:.2f}".format(price))


window = Tk()
window.title("Pizza menu")
window.geometry("700x600")

imgHeader = PhotoImage(file="../../../../Downloads/Module4 Prax Solutions/Solutions/PRG0404 Solutions/Header.gif")
imgLogo = PhotoImage(file="../../../../Downloads/Module4 Prax Solutions/Solutions/PRG0404 Solutions/Logo.gif")

canvas = Canvas(window, width=700, height=600, bg="black")
canvas.create_image(0, 0, image=imgHeader, anchor=NW)
canvas.create_image(500, 250, image=imgLogo, anchor=NW)
canvas.create_text(135, 120, fill="white", font="Helvetica 20 bold",
                   text="Select a pizza type")
canvas.create_text(140, 340, fill="white", font="Helvetica 20 bold",
                   text="Select a pizza base")
canvas.create_text(170, 440, fill="white", font="Helvetica 20 bold",
                   text="Select any extra toppings")

canvas.pack(side=LEFT)

lb_pizzatype = Listbox(window,
                       width=40,
                       bg="black",
                       fg="white",
                       height=5)
lb_pizzatype.insert(END, "Hawaiian (50)")
lb_pizzatype.insert(END, "Regina (55)")
lb_pizzatype.insert(END, "Four seasons (80)")
lb_pizzatype.insert(END, "Something meaty (70)")
lb_pizzatype.insert(END, "Vegetarian (45)")
lb_pizzatype.place(x=50, y=150)

btn_selectpizza = Button(window, text="Select", command=update_description)
btn_selectpizza.place(x=50, y=250)

description = StringVar()
lbl_description = Label(window, textvariable=description, bg="black", fg="red")
lbl_description.place(x=50, y=290)

pizza_base = StringVar()
rad_thick = Radiobutton(window, text="Thick base (5)", value="Thick base", variable=pizza_base, bg="black", fg="white")
rad_thick.place(x=50, y=370)
rad_thin = Radiobutton(window, text="Thin base", value="Thin base", variable=pizza_base, bg="black", fg="white")
rad_thin.place(x=50, y=390)
rad_thin.select()

topping_1 = IntVar()
topping_2 = IntVar()
topping_3 = IntVar()
topping_4 = IntVar()
topping_5 = IntVar()

chk_cheese = Checkbutton(window, onvalue=5, offvalue=0,
                         text="Cheese (5)", variable=topping_1, fg="white", bg="black")
chk_cheese.place(x=50, y=460)
chk_ham = Checkbutton(window, onvalue=10, offvalue=0,
                      text="Ham (10)", variable=topping_2, fg="white", bg="black")
chk_ham.place(x=50, y=480)
chk_avocado = Checkbutton(window, onvalue=9, offvalue=0,
                          text="Avocado (9)", variable=topping_3, fg="white", bg="black")
chk_avocado.place(x=50, y=500)
chk_onions = Checkbutton(window, onvalue=2, offvalue=0,
                        text="Onions (2)", variable=topping_4, fg="white", bg="black")
chk_onions.place(x=50, y=520)
chk_olives = Checkbutton(window, onvalue=8, offvalue=0,
                         text="Olives (8)", variable=topping_4, fg="white", bg="black")
chk_olives.place(x=50, y=520)

btn_order = Button(window, text="Select", command=calculate)
btn_order.place(x=50, y=550)

window.mainloop()
