from simpleStudent import *

# Creates a Student object and increments its count
first_student = simpleStudent()
simpleStudent.count += 1
# Creates another Student object and increments its count
second_student = simpleStudent()
simpleStudent.count += 1


# Demonstrates that the value of count is shared amongst
# all Student instances
print("Number of students:  {}".format(simpleStudent.count))
