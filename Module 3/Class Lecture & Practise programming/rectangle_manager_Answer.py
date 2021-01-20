from rectangle import *

rectangles = list()

user_input = "y"

while user_input == "y":
    print("Please enter the details of a rectangle:  ")
    length = int(input("Enter the length:  "))
    width = int(input("Enter the width:  "))
    display_character = input("Enter a character to draw with:  ")
    rectangles.append(Rectangle(length, width, display_character))
    user_input = input("Do you wish to enter another rectangle? Enter y to continue:  ")
    print("-" * 70)

for current in rectangles:
    current.display()
    print()

