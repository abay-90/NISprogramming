"""# Define a string and create placeholders using {}.
my_string = "{} sold {} items."
# Call, the string's format method.
# Pass as many arguments to the format method as there
# are sets of {} in the string.  In this case 2.
print(my_string.format("Olaf",20))
# The same can be done on a string literal,
# without using a pre-defined variable.
print("This example requires {} argument(s).".format(1))
"""

my_string = "{0} sold {1} items. {2} sold {3} items. {2} was the better salesperson."
first_person = "Olaf"
second_person = "Nina"
first_sales = 10
second_sales = 20
# The interpreter looks at the list of arguments and assigns
# them according to their index in the list of arguments as
# the placeholder in the string.
# The indexes for the arguments are as follows:
# 0: first_person
# 1: first_sales
# 2: second_person - will be used twice according to the string
# 3: second_sales
print(my_string.format(first_person, first_sales, second_person, second_sales))
