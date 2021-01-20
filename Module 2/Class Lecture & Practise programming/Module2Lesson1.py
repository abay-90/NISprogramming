                                                    ##Loops
        #loop controlled by counter
# total = 0
#
# print('if statement output : \n')
#
# if total < 5:
#     print('Total: ', total)
#     total += 1


# total = 0
# print()
#
# print('\nwhile statement output:\n')
#
# while total < 5:
#     print('Total:', total)
#     total += 1
# print()

        #loop controlled by flag
# user_choice = input('Enter q to exit or another key to continue: ')
#
# while user_choice != 'q':
#     print('The user entered:', user_choice)
#     user_choice = input('Enter q to exit or another key to continue: ')
#
# print('\nThe user pressed q and the loop ended.')

        #nested loop
# outside_counter = 0
#
# while outside_counter < 3:
#     inside_counter = 0
#     while inside_counter < 3:
#         print('Outside counter: ', outside_counter, 'inside counter: ', inside_counter)
#         inside_counter += 1
#     outside_counter += 1

#         #for loop
# months = ['January','February','March', 'April', 'May', 'June', 'July']
# number_of_sales = [45, 59, 34]
# class_sizes = {'PRG': 30, 'NET': 40, 'NIX': 37}

    #Simple iteration over strings
# for item in months:
#     print(item, end=' ')
#     item = 'hello'
#     print(item)

# print()

# index = 0
# while index < len(months):
#     item = months[index]
#     print(item, end=' ')
#     index += 1

        #to modify anything in a data structure , use the while loop
        #to process things and display, use the for loop

    #Simple interation over integers
# for item in number_of_sales:
#     print(item, end=' ')
# print()
#
#     #Simple Iteration over a string, since a string is just a list of characters, is may be iterated over
# for item in 'the string':
#     print(item, end=' ')
# print()
#
#     #enumerate() allows the elements in a data structure to be listed along with its index in the data structure
# for item in enumerate(months):
#     print(item, end=' ')
# print()
#
#     #zip() allows the elements in the multiple data structure to be iterated at the same time
# for item in zip(months, number_of_sales):
#     print(item ,end=' ')
# print()
#
#     #Use key value combinations to iterate through a dictionary's items()
# for key, value in class_sizes.items():
#     print(key, ': ', value, sep=' ')
# print()

# #When a range() is provided with a single value, the single value constitututes the length.
# #i.e the range is from 0 to 1 less than the value specified
# print('range(10)', end=': ')
# for item in range(20):
#     print(item, end=', ')
# print()

# #When a range() is provided with 2 values, the first value constitutes the minimum value and the second the maximum.
# #The range is from the minimum value to the 1 less than the maximum value specified
# print('\nrange(1, 10)', end=': ')
# for item in range(0, 11):
#     print(item, end=', ')
#
# #When a range() is provided wih 3 values, the third value constitutes the step size.
# #A step size if 2 would iterate through every second value, 3 every third value and so forth
# print('\nrange(1, 10, 2)', end=': ' )
# for item in range(0, 50, 5):
#     print(item, end=', ')

    #break
#a loop that should iterate from 1 to 10
# for item in range(1, 11):
#     print('Item value:', item)
#     if input('Enter q to quit or any other key to continue: ') == 'q':
#         break

    #continue
# total = 0
# while total < 10:
#     total += 1
#     if total % 2 == 0:
#         print(total, ' is divisible by 2')
#     else:
#         continue
#         # break

# to comment block of code ctrl + /