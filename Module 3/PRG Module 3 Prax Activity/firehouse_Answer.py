from fireman import *

fireman1 = Fireman("John",  "Doe", "12345", 20)
fireman2 = Fireman("Jane",  "Doe", "57890", 25)
fireman3 = Fireman("Jim",  "Doe", "11111", 23)

print("{0}:  {1} {2} ({3})".format(fireman1.staff_number, fireman1.name, fireman1.surname, fireman1.age))
print("{0}:  {1} {2} ({3})".format(fireman2.staff_number, fireman2.name, fireman2.surname, fireman2.age))
print("{0}:  {1} {2} ({3})".format(fireman3.staff_number, fireman3.name, fireman3.surname, fireman3.age))

print("Number of firemen: ", Fireman.count)