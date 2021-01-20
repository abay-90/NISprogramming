# import sys
# help()

# import keyword
#
# print('Python keywords:')
# for theword in keyword.kwlist: # kwlist contains a list of Python keywords
# 	print(theword, end=", ")
# print()
# 	# iskeyword returns True or False depending on whether a word is a keyword
# print('Noroff is a Python keyword: ', keyword.iskeyword('Noroff'))

#Practice 1
#create the below function in a seperate file and call the file calculatepay.py
# def hourly_pay(hours, rate):
#     return hours * rate
#
# def monthly_pay(years_experience, pay_notch):
#     return years_experience * pay_notch


#Practice 2
# it's also possible to provide an alias for the import,
# i.e. provide another name which you want to use when calling the functions.
# This is done by extending the import statement by adding as the_name_you_want.

# import calculatepay as pay
#
# hourly = pay.hourly_pay(40,10)   # use pay instead of calculatepay
# monthly = pay.monthly_pay(10,50)
#
# print("Hourly worker pay: ", hourly)
# print("Salary worker pay:  ", monthly)
#
# from calculatepay import hourly_pay as pay
#
# hourly = pay(40,10)   # use pay is now used like a local method name
#
# print("Hourly worker pay: ", hourly)

                    #System interrogation
# import sys
# help()

# import keyword
#
# print('Python keywords:')
# for theword in keyword.kwlist: # kwlist contains a list of Python keywords
# 	print(theword, end=", ")
# print()
# 	# iskeyword returns True or False depending on whether a word is a keyword
# print('Noroff is a Python keyword: ', keyword.iskeyword('Noroff'))


        #Class practice
# import keyword
#
# print('python keywords: ')
# for thewordNIS in keyword.kwlist:
# 	print(thewordNIS, end=', ')
# print()
# print('NIS is awesome but not a keyword in Python: ', keyword.iskeyword('NIS'))

        #Miscellaneous functions

    #Mathematics
# import math
#
# rounding = 2.3
# print("Ceiling of",rounding,": ",math.ceil(rounding))
# print("Floor of",rounding,": ",math.floor(rounding))
#
# base = 2
# exponent = 5
#
# print(base, "to the power of",exponent,": ",math.pow(base,exponent))
# print("The square root of 64 is: ", math.sqrt(64))

            #Random Numbers

# import random
#
# print('Random number in the range 0 to 1:', random.random())
# print('Random number in the range 0 to 100:', random.random() * 2)
# print('Select lottery numbers: ')
# # Chooses 6 non-repeating numbers in the range 1 to 50
#
# print('Your lucky numbers are: ', random.sample(range(1, 51),6))


#Decimal Numbers

# import decimal
#
# value_one = decimal(0.7)
# value_two = decimal(1.05)
# first_result = value_one * value_two
# second_result = value_one + first_result
#
# print('Value one: ', '%.2f' % value_one) # Shows the number with 2 floating point digits
# print('Value two: ', '%.2f' % value_two)
# print('First result: ', '%.2f' % first_result)
# print('Second result: ', '%.2f' % second_result)

#    # Time
# from datetime import *
#
# now = datetime.today()
# print('Today: ',now)
# print('Current time: ', now.hour, ':', now.minute, sep='')
# print('Today is a ', now.strftime('%A'),sep='')
# print('The month is ', now.strftime('%B'),sep='')


#Elapsed time with paused execution

# from time import *
#
# start = time()
# start_time = localtime(start)
# print("Started at: ", strftime("%X",start_time))
# for i in range(0,10):
#     print(i + 1)
#     sleep(1)
# # Pauses for a second
# end = time()
# difference = end - start
# print("The loop ran for", difference, "seconds.")




