#                     # Functions
#
# name = input('Please enter your name: ')
# amount = int(input('how many items do you wish to purchase: '))
# price = 10
# total = amount * price
# print(name, 'your total for ', amount, ' items is: ', total, sep=' ')
# print()
#
# name = input('Please enter your name: ')
# amount = int(input('how many items do you wish to purchase: '))
# price = 10
# total = amount * price
# print(name, 'your total for ', amount, ' items is: ', total, sep=' ')
# print()
#
# name = input('Please enter your name: ')
# amount = int(input('how many items do you wish to purchase: '))
# price = 10
# total = amount * price
# print(name, 'your total for ', amount, ' items is: ', total, sep=' ')
# print()
# price = 10

# def calculate_price(): # <--------- function header, below is the function body
#     name = input('Please enter your name: ')
#     amount = int(input('how many items do you wish to purchase: '))
#     global price
#     price = 10
#     total = amount * price
#     print(name, 'your total for ', amount, ' items is: ', total, sep=' ')
# #
# # #     # Take note of the indent. Everything in indent, is part of function
# #
# calculate_price()
# print(price)
#
#
# price = 10
#
# while input('Type y to calculate a users details:  ') == 'y':
#       calculate_price()

    #scope declaring local and global variables

# def calculate_price(): # <--------- function header, below is the function body
#     name = input('Please enter your name: ')
#     amount = int(input('how many items do you wish to purchase: '))
#     total = amount * price
#     print(name, 'your total for ', amount, ' items is: ', total, sep=' ')
#
# #     # Take note of the indent. Everything in indent, is part of function
# #
# price = 10
#
# while input('Type y to calculate a users details:  ') == 'y':
#     calculate_price()

    # functions with arguments
# def multiply (a, b):
#     result = a * b
#     return result
#
# answer = multiply(2, 6)
# print(answer)

# Define the function with the variable names between the brackets.
# The function parameters are provided with the defaut values.
# Any arguments passed to the function are received in the parameters in the sequence in which they are passed.
# The parameters serve as local variables.

# def with_one_argument(first):
#     print(first, end=' ')
# with_one_argument('with one argument')
# print()
#
# def with_two_arguments(first, second):
#     print(first, 'second - ', second)
# with_two_arguments('first arguments', 'second argument')

# print()
#
# When calling a function, provide as many arguments as the function has parameters.

# with_one_argument(10)
# with_two_arguments('me', 2)
#
# print()

# def display(one, two, three, four):
#     print('first: ', one)
#     print('second: ', two)
#     print('third: ', three)
#     print('fourth: ', four)
#
# print('call parameters in sequence:' )
# display(1,2,3,4)
# print()
# print('call by specifying parameter names: ')
# display(four=100, three=2000, two=2098, one=781)

    #Default values
# def display(one=1, two=2, three=3, four=4):
#     print('first: ', one)
#     print('second: ', two)
#     print('third: ', three)
#     print('fourth: ', four)
#
# print('Pass all arguments: ')
# display(1,2,3,4)
# print()
# print('Pass no arguments: ')
# display()
# print()
# print('Pass only the first argument: ')
# display(18)
# print()
# print('Pass the first argument and a named argument: ')
# display(38, four=100)
# print()

    #Return values
#
# def add_values(first_value, second_value):
#     return first_value + second_value
#
# # Assigning the returned value to a variable
# result = add_values(10, 20)
# print(result)
# # Using the returned values, in-line without declaring a variable
# print(add_values(50, 10))

# def calculator(calc_type, first_value, second_value):
#     if calc_type == 1:
#         print('adding values')
#         return first_value + second_value
#     elif calc_type ==2:
#         print('subtracting values')
#         return first_value - second_value
#     elif calc_type == 3:
#         print('Undefined')
#         return
#
# # print(calculator(1, 20, 10))
# # print(calculator(2, 20, 10))
# print(calculator(3, 20, 10)) # The return statement returns nothing
# print(calculator(4, 20, 10)) # No return statement matches this calc_type

    #function can return multiple values at once
# def calc_all(first_value, second_value):
#     addition = first_value + second_value
#     subtraction = first_value - second_value
#     division = first_value/second_value
#     multiplication = first_value * second_value
#     return addition, subtraction, division, multiplication # all 4 values are returned
#
# # Recycling the values seperately
# first, second, third, fourth = calc_all(20, 10)
# print(first, second, third, fourth)
# # Receiving all the values at once
# values = calc_all(10, 90)
# print(values)

    # Callbacks lambda keyword
# def subtraction_method(first_value, second_value):
#     return first_value - second_value

#using the method
# print(subtraction_method(30, 15))

# #Doing the same with the lambda expression (in-line expression)
# subtractor = lambda first_value, second_value: first_value - second_value
# print(subtractor(30, 15))
# #
# # def use_function_object(function_object, first_value, second_value):
# #     return function_object(first_value, second_value)
# #
# # #Creating the function objects
# # summing_machine = lambda first_value, second_value: first_value + second_value
# # subtractor = lambda first_value, second_value: first_value - second_value
# #
# # # Calling the same function with different results
# # print(use_function_object(summing_machine, 30, 15))
# # print(use_function_object(subtractor, 30, 15))





