menu_pizza_base = [
    [1, "Thick", 10], [2, "Thin", 5],
]

menu_pizza_size = [
    [1, "Small", 30], [2, "Medium", 40], [3, "Large", 50],
]

menu_basic_sauce = [
    [1, "Tomato", 5], [2, "Barbecue", 10],
]

menu_toppings = [
    [1, "Cheese", 5], [2, "Mushrooms", 3], [3, "Avocado", 7], [4, "Pineapple", 5], [5, "Bacon", 7], [6, "Chicken", 7], [7, "Fish", 6],
]

print("Menu Base")
for item in menu_pizza_base:
    print('{} {} - {:.2f}'.format(*item))

print("Menu Size")
for item in menu_pizza_size:
    print('{} {} - {:.2f}'.format(*item))

print("Menu Sauce")
for item in menu_basic_sauce:
    print('{} {} - {:.2f}'.format(*item))

print("Menu Toppings")
for item in menu_toppings:
    print('{} {} - {:.2f}'.format(*item))

order = input('\n\nPlease enter the numbers of the items you would like: ')

print("You ordered: ", order)
order_total = 0

for item in order:
    print(menu_pizza_base[int(item) - 1])
    print(menu_pizza_size[int(item) - 1])
    print(menu_basic_sauce[int(item) - 1])
    print(menu_toppings[int(item) - 1])