#Main Task

# Create a script named editor.py
# In this script, prompt the user to enter a string of text.
# The following needs to happen until the user decides to exit the program, by pressing "e":
# Display the current version of the input string to the user.
# Ask the user to select an option to be applied to the string:
# 1. Uppercase
# 2. Lowercase
# 3. Titlecase
# 4. Remove front and back whitespaces
# 5. Exit program
# Update the string using the requested method or exit the program.


# 1, 2, 3 is done need to do 4 and 5
# Python String.strip()
# To remove the spaces present at start and end of the string, you can use strip() function on the string.

the_string = "This script is for the editor"

print("capitalize(): ", the_string.capitalize())
print("title(): ", the_string.title())
print("upper(): ", the_string.upper())
print("lower(): ", the_string.lower())
print("swapcase(): ", the_string.swapcase())

the_string = 'This script is for the editor'



# The functions quit(), exit(), sys.exit() and os._exit()
# have almost same functionality as they raise the SystemExit exception;
# by which the Python interpreter exits and no stack traceback is printed.

# Python program to demonstrate
# exit()

# for i in range(10):
#
#     # If the value of i becomes
#     # 5 then the program is forced
#     # to exit
#     if i == 5:
#         # prints the exit message
#         print(exit)
#         exit()
#     print(i)







