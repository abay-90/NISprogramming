                    # PlaceHolders
#     # using print()
# value_one = 50
# value_two = 70
# #
# if value_one > value_two:
#     print("Do something")
# else:
#     pass
# # print() # calling a print() method - it could also display a message

# print("Statement after ifs")
#
#
# def placeholder():
#     return
#
# if value_one > value_two:
#     print("Do something")
# else:
#     placeholder() # calling the placeholder function

# print("Statement after ifs")


                # Generators
    #Use yield function
a  = 100
b  = 150
c  = 120

# def my_first_yield():
#     increment = 0
#     while True: # <--------- this statement creates an infinite loop
#         yield increment # returns the value of increment and sets the next start point
#         increment += 1
#
# first_increment = my_first_yield()
# second_increment#  = my_first_yield()
#
# print('this is the first step before the yield is applied')
# print(next(first_increment)) # This is now executing the first yield statement
# print(next(first_increment)) # This is executing the second yield statement
# print(next(first_increment)) # This is executing the third yield statement
# print(next(first_increment)) # This is executing the third yield statement
# print(next(first_increment)) # This is executing the third yield statement
# print(next(first_increment)) # This is executing the third yield statement
# print(next(first_increment)) # This is executing the third yield statement
# print('this is the second incrementer')
# print(next(second_increment)) # This is executing the second yield statement

    # Another example fo the yield using the break statement
# def my_range(initial_value, increment):
#     i = initial_value
#     while True:
#         yield i
#         i += increment
#
# increment_one = my_range(0, 1)
# increment_two = my_range(0, 5)
#
# # print('first generator: ', end=' ')
# # for i in increment_one: # <----------- can use the generator functions in the for loop
# #     if i > 10:
# #         break
# #     else:
# #         print(i, end=', ')
#
# print()
# print('second generator: ', end=' ')
# for i in increment_two: # <----------- can use the generator functions in the for loop
#     if i > 30:
#         break
#     else:
#         print(i, end=', ')
# #
# #
# print(next(increment_two))

                    #     #Using Yield
# def simple_yield():
#     print('this is my first yield statement')
#     yield
#     print('this is my second yield statement')
#     yield
#     print(('this is my last yield statement'))
#
#
# first_yield_test = simple_yield()
# next(first_yield_test)  # Runs to first yield statement
# next(first_yield_test)  # Runs to second yield statement
# next(first_yield_test)  # Tries to run to third yield statement
#
#
# # # Since there is no more yield statements, the Python script will generate a run-time error.  Which #means the following statement will not execute.
# #
# print("This statement will not print")


               # Exceptions

# first_value = 10

# try:
#     print(second_value) # second_value is not defined and will give a run-time error
# except:
#     print('An error has occured because second_value does not exist')
#
# print()
#
    #NameError
# try:
#     print(second_value) # second_value has not been initialized and will result in a run-time error
# except NameError as msg: # The NameError exception is handled and its details are stored in a msg using the as keyword
#     print('An error has occured because second_value does not exist: ----> the system generated error message----> : ',msg)
#
# print()
#
#    #IndexError
# my_list = [1, 2, 3, 4] #list with 4 elements
#
# try:
#     for i in range(0,5): #loop with 5 iterations
#         print(my_list[i], end=' ') #<--------- trying to print the range with 5 interations
# except IndexError as msg:
#     print()
#     print('There is an index error:----> the system generated error message----> :', msg)
#
# print()
# #
#     #ValueError
# try:
#     a = int(input('Write your birth date: '))
# except ValueError as msg:
#     print('There is a value error: ----> the system generated error message----> : ', msg)
#
# print()

# my_values = [4, 5, 6, 7]
#
# try:
#     a = int(input('Enter a number : '))
#     index = 0
#     while index < a:
#         print(my_values[index])
#         index += 1
# except (ValueError, IndexError) as msg:
#     print('A value or an index error has occured:----> the system generated error message----> : ', msg)
#
#     #FinallyBlock
# y_values = [4, 5, 6, 7]

# try:
#     a = int(input('Enter a number : '))
#     index = 0
#     while index < a:
#         print(my_values[index])
#         index += 1
# except (ValueError, IndexError) as msg:
#     print('A value or an index error has occured:----> the system generated error message----> : ', msg)
# finally:
#     print('code executes and errors are handled because i am a boss like that')
# try:
#     a = 50
#     if a > 10: # Creates a ValueError object with a custom message
#         raise ValueError("The value is too high") # The raise keyword passes the Error to the except block
# except ValueError as msg:
# 	print("An error has occurred: ", msg)


            # Assertions
# try:
#     a = 50
#     assert type(a) is str, 'Debug error message: a is not an integer'
#     a = '50'
#     assert type(a) is int, 'Debug error message: a is not an integer' + str(type(a))
# except AssertionError as msg:
#     print('this will print the string message next to the assert -----> ', msg)