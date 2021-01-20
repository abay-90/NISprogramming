from SimpleStudent import  *

# Creates a Student object and increments its count
first_student = SimpleStudent()
SimpleStudent.count  += 1

# Creates another Student object and increments its count
second_student = SimpleStudent()
SimpleStudent.count += 1

# Demonstrates that the value of count is shared amongst
# All Student instances
print("Number of students:  {}". format(SimpleStudent.count))

