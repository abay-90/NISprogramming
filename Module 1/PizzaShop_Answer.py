Total = 0

print("Select a pizza base type: ")
print("1.  Thick")
print("2.  Thin")
Base = int(input("Base selection: "))
BaseLine = ""
if Base == 1:
    BaseLine = "{0}Kr{1}".format("Thick base".ljust(20, " "), "10".rjust(5, " "))
    Total += 10
elif Base == 2:
    BaseLine = "{0}Kr{1}".format("Thin base".ljust(20, " "), "5".rjust(5, " "))
    Total += 5

print("Select a pizza size: ")
print("1.  Small")
print("2.  Medium")
print("3.  Large")
Size = int(input("Size selection: "))
SizeLine = ""
if Size == 1:
    SizeLine = "{0}Kr{1}".format("Small".ljust(20, " "), "30".rjust(5, " "))
    Total += 30
elif Size == 2:
    SizeLine = "{0}Kr{1}".format("Medium".ljust(20, " "), "40".rjust(5, " "))
    Total += 40
elif Size == 3:
    SizeLine = "{0}Kr{1}".format("Large".ljust(20, " "), "50".rjust(5, " "))
    Total += 50

print("Select a pizza sauce: ")
print("1.  Tomato")
print("2.  Barbecue")
Sauce = int(input("Sauce selection: "))
SauceLine = ""
if Sauce == 1:
    SauceLine = "{0}Kr{1}".format("Tomato sauce".ljust(20, " "), "5".rjust(5, " "))
    Total += 5
elif Sauce == 2:
    SauceLine = "{0}Kr{1}".format("Barbecue sauce".ljust(20, " "), "10".rjust(5, " "))
    Total += 10

Toppings = ""
result = input("Would you like to add Cheese? (y or n): ")
if result == "y":
    Toppings += "{0}Kr{1}".format("Cheese".ljust(20, " "), "5".rjust(5, " "))
    Total += 5
result = input("Would you like to add Mushrooms? (y or n): ")
if result == "y":
    if len(Toppings) > 0:
        Toppings += "\n"
    Toppings += "{0}Kr{1}".format("Mushrooms".ljust(20, " "), "3".rjust(5, " "))
    Total += 3
result = input("Would you like to add Avocado? (y or n): ")
if result == "y":
    if len(Toppings) > 0:
        Toppings += "\n"
    Toppings += "{0}Kr{1}".format("Avocado".ljust(20, " "), "7".rjust(5, " "))
    Total += 7
result = input("Would you like to add Pineapple? (y or n): ")
if result == "y":
    if len(Toppings) > 0:
        Toppings += "\n"
    Toppings += "{0}Kr{1}".format("Pineapple".ljust(20, " "), "5".rjust(5, " "))
    Total += 5
result = input("Would you like to add Bacon? (y or n): ")
if result == "y":
    if len(Toppings) > 0:
        Toppings += "\n"
    Toppings += "{0}Kr{1}".format("Bacon".ljust(20, " "), "7".rjust(5, " "))
    Total += 7
result = input("Would you like to add Chicken? (y or n): ")
if result == "y":
    if len(Toppings) > 0:
        Toppings += "\n"
    Toppings += "{0}Kr{1}".format("Chicken".ljust(20, " "), "7".rjust(5, " "))
    Total += 7
result = input("Would you like to add Fish? (y or n): ")
if result == "y":
    if len(Toppings) > 0:
        Toppings += "\n"
    Toppings += "{0}Kr{1}".format("Fish".ljust(20, " "), "6".rjust(5, " "))
    Total += 6

print()
print(BaseLine)
print(SizeLine)
print(SauceLine)
print(Toppings)
print("-" * 27)
print("{0}Kr{1}".format("Total".ljust(20, " "), str(Total).rjust(5, " ")))
