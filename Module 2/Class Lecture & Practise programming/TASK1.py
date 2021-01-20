import calculatepay

# hourly = calculatepay.hour_pay()40, 10)
# monthly = calculatepay.monthly_pay(10,50)
#
# print('Hourly worker pay: ', hourly)
# print('Salary worker pay: ', monthly)
# ### task2
# it's also possible to provide an alias for the import,
# i.e. provide another name which you want to use when calling the functions.
# This is done by extending the import statement by adding as the_name_you_want.

import calculatepay as pay

hourly = pay.hourly_pay(40,10)   # use pay instead of calculatepay
monthly = pay.monthly_pay(10,50)

print("Hourly worker pay: ", hourly)
print("Salary worker pay:  ", monthly)

from calculatepay import hourly_pay as pay

hourly = pay(40,10)   # use pay is now used like a local method name

print("Hourly worker pay: ", hourly)
