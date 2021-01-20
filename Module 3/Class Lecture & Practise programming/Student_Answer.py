class Student:
    count = 0

    def __init__(self): #<---------- constructor.
                        # Self will receive a reference to the object to which the constructor is being called
        self.name = ""  # Assign to an instance variable (instance variables created by assigning variable to the self object
        self.surname = ""  # Assign to an instance variable
        Student.count += 1  # Assign to the class variable <----class attribute, so all students created will share same value
        self.number = Student.count  # Assign to an instance variable

        # every instance of student created, is a new instance variable

#so when creating the Student(), no arguments need to be passed to the () as the reference in memory will call the (self)
first_student = Student()  # no arguments are passed, self is implicit
first_student.name = "John"
first_student.surname = "Doe"

second_student = Student()
second_student.name = "Jane"
second_student.surname = "Doe"



print("{}:{} {}".format(first_student.number, first_student.name, first_student.surname))
print("{}: {} {}".format(second_student.number, second_student.name, second_student.surname))
print("Number of students:  {}".format(Student.count))

