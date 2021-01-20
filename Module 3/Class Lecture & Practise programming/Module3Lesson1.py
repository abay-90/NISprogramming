#Special Characters

# string = 'What's going on?'
# print(string)

# the_string_with_quotes = 'I\'m a developer'
# print(the_string_with_quotes)

#horizontal tab

# print("This demonstrates a \t horizontal tab")  #<------ actually prints a tab

#concatenation <---------- combining two variables (strings in the below example)
# symbol between two strings means to combine the two strings
#
# first_string = "I am combining "
# second_string = "these 2 strings."
# new_string = first_string + second_string
# print(new_string)
# print()
# # #concatenation and repetition
#
# repeat_me = "This string will repeat | "
# new_string = repeat_me * 3
# print(new_string)
#
# # Just as addition and multiplication may occur in the same equation
# # so too may concatenation and repetition be used in the same line.
# # adding * symbol and a number to a string, indicates how many times to repeat the string
#
# new_string = "| " + repeat_me * 3
# print(new_string)

#Slices
#Brings back a substring or subset of data in your string

# test_string = "This is my string"
# slice_of_test_string = test_string[3]
#
# print("test_string: ", test_string)
# print("slice at index 3: ",slice_of_test_string)

# More complicated string
#
# test_string = "This is my string"
# print("test_string: ", test_string)
# print("slice at index 5 up to index 10: ",test_string[5:10])
# print("slice at index 5 up to index 10, step 2: ",test_string[5:10:2])
# print("slice at index 5 up to the end of the string: ",test_string[5:])
# print("slice at index 5 up to 3 characters from the end: ",test_string[5:-3])

#Membership
#Search through a string for a specific value (e.g. similar to find (ctrl + f))
#
# test_string = "This is my string"
#
# # print("Membership inclusive:")
# # print("This" in test_string)
# # print("John" in test_string)
# # # print()
# print("Membership exclusive:")
# print("This" not in test_string)
# print("John" not in test_string)

# #Raw Strings

# print("This is a \t string") # Normal behaviour
# print(r"This is a \t string") # Interpreted as a raw string

#Docstrings

# def my_test_function():
#     '''This is a function to demonstrate the use of a docstring''' #<---------- remember to use 3 quotation marks
#     return
#
# print(my_test_function.__doc__) #<------remember to use 2 underscores before and after calling your doc method

#formatting strings
#formatting is applied using the format() method and curly brackets as placeholders.

#unindexed string
# # Define a string and create placeholders using {}.
# my_string = "{} sold {} items."
# # Call, the string's format method.
# # Pass as many arguments to the format method as there
# # are sets of {} in the string.  In this case 2.
# print(my_string.format("Olaf",20))
#
# # The same can be done on a string literal,
# # without using a pre-defined variable.
# print("This example requires {} argument(s).".format(1))
#
# #indexed string
# my_string = "{0} sold {1} items. {2} sold {3} items. {2} was the better salesperson than {0}"
#
# first_person = "Olaf"
# second_person = "Nina"
# first_sales = 10
# second_sales = 20
#
# # The interpreter looks at the list of arguments and assigns
# # them according to their index in the list of arguments as
# # the placeholder in the string.
# # The indexes for the arguments are as follows:
# # 0: first_person
# # 1: first_sales
# # 2: second_person - will be used twice according to the string
# # 3: second_sales
# print(my_string.format(first_person, first_sales, second_person, second_sales))

# Placeholders
#Python also allows individual placeholders to be formatted.
# Formatting determines how they are displayed.

print("f:  {0:f}".format(50.4756))
print(".2f:  {0:.2f}".format(50.4756))
print(".6f:  {0:.6f}".format(50.4756))
print("e:  {0:e}".format(50.4756))
print("b:  {0:b}".format(231))
print("o:  {0:o}".format(231))
print("x:  {0:x}".format(231))
print("X:  {0:X}".format(231))

#modifying strings

#change the case of the string
# the_string = "a king, named George, fell into the gorge."
#
# print("capitalize(): ", the_string.capitalize()) <----- changes 1st letter of sentence to upper case
# print("title(): ", the_string.title()) <---- first letter of every word is a capital
# print("upper(): ", the_string.upper()) <----- enitre string upper case
# print("lower(): ", the_string.lower()) <-----entire string lower case
# print("swapcase(): ", the_string.swapcase()) <----swaps upper to lower and lower to upper

#joining elements
# separator_one = ";"
# separator_two = ","
# separator_three = "###"
#
# the_list = ["1","2","3","4"]
#
# # Call join on the preferred separator and pass the list
# # whose elements need to be joined as an argument.
#
# print(";:",separator_one.join(the_list))
# print(",:",separator_two.join(the_list))
# print("###:",separator_three.join(the_list))

# splitting elements
# Python's split() method allows a string to be split according to a predefined delimiter.
#
# input_string = "this is the string to split"
#
# result_one = input_string.split()
# print("Default split (on spaces):")
# print(result_one)
# print()
#
# result_two = input_string.split("i")
# print("Split on i:")
# print(result_two)
# print()
#
# result_three = input_string.split("is")
# print("Split on is:")
# print(result_three)


# removing whitespace
#
# input_string = "   a string with horizontal whitespace   "
# # print(input_string)
# #
# # lstrip() removes leading/left whitespaces
# print("lstrip(): ", input_string.lstrip())
#
# # rstrip() removes trailing whitespaces (right)
# print("rstrip(): ", input_string.rstrip())
#
# # strip() removes leading and trailing whitespaces (left and right)
# print("strip(): ", input_string.strip())

# Replacement
#
# input_string = "Dear RECIPIENT, Please find attached a cheque to the amount of AMOUNT.  Kind regards, SENDER"
#
# input_string = input_string.replace("RECIPIENT", "John")
# input_string = input_string.replace("AMOUNT", "3000.00 NOK")
# input_string = input_string.replace("SENDER", "Management")
#
# print(input_string)
#
# Justification
#
# description_one = "Description 1"
# description_two = "Description 2"
# price_one = "3456.89"
# price_two = "563.45"
#
# # Column 1 left justified
# # Column 2 right justified
# # Spaces for padding
# print(description_one.ljust(20," "), price_one.rjust(10," "), sep="")
# print(description_two.ljust(20," "), price_two.rjust(10," "), sep="")
# print("-" * 30)
# # Column 1 right justified
# # Column 2 left justified
# # Spaces for padding
# print(description_one.rjust(20," "), price_one.ljust(10," "), sep="")
# print(description_two.rjust(20," "), price_two.ljust(10," "), sep="")
# print("-" * 30)
# # Column 1 left justified
# # Column 2 right justified
# # . for padding
# print(description_one.ljust(20,"."), price_one.rjust(10,"."), sep="")
# print(description_two.ljust(20,"."), price_two.rjust(10,"."), sep="")
# print("-" * 30)
# # Column 1 center justified
# # Column 2 center justified
# # - for padding
# print(description_one.center(20,"-"), price_one.center(10,"-"), sep="")
# print(description_two.center(20,"-"), price_two.center(10,"-"), sep="")

