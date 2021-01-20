# #Lesson2 Prax 1
#
# from simpleStudent import *
#
# first_student = simpleStudent()
# simpleStudent.count += 1
#
# second_student = simpleStudent()
# simpleStudent.count += 1
#
# third_student = simpleStudent()
# simpleStudent.count += 1
#
# print("Number of students:  {}".format(simpleStudent.count))



class Employee:
    def __init__(self, name):
        self.name = name

first = Employee("Frey")
second = Employee("Klaus")


setattr(first,"name","Freya")

print(getattr(first,"name"))

delattr(second,"name")


if hasattr(second,"name"): #<-------does the object have the attribute name<
    print(getattr(second,"name"))
else:
    print("Second does not have attribute name")
