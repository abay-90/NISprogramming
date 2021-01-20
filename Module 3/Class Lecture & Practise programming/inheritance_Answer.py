# base class = parent/main class
# derivative class = child class
# when calling the base class from the derivative class, always use super() method


class Student:
    count = 0

    def __init__(self, name, surname):
        self.name = name  # Assign the received parameter's value
        self.surname = surname  # Assign the received parameter's value
        Student.count += 1
        self.number = Student.count
        self.grades = {}  # Subjects and their results (empty) (adding grades to a student)

    def display(self): #<---displays number, name and surname of student (blackbox concept)
        print("{}:\t{} {}".format(self.number, self.name, self.surname))
        print()
        if len(self.grades) == 0:
            print("\tNo subjects and results have been added")
        else:
            for key in self.grades:
                print("\t{}:\t\t{}".format(key, self.grades[key]))

            # Use self to call the calculate_average method
            print("\tAverage:\t\t{}".format(self.calculate_average()))

        print("-" * 50)

    def add_subject_and_mark(self, subject, mark):
        self.grades[subject] = mark

    def calculate_average(self):
        total = 0

        for key in self.grades:
            total += self.grades[key]

        return total / len(self.grades)

class nursingStudent(Student):

    #receives the name and surname expected by the base as well as hours used by nursingStudent
    def __init__(self, name, surname, hours):
        self.hours = hours #<----hours still needs to be assigned to the class instance
        #use super() to call the base class' __init__' which expects a name and surname
        super().__init__(name, surname) #<-----calls the base class constructor


    def display_extra(self): #<------- only exists for nursingStudent
        # derived class has access to all the variables of the base class.
        self.display()
        print('Hours worked: {}'.format(self.hours))
        print('_' * 50)

class engineeringStudent(Student):

    #receives the name and surname expected by the base as well as hours used by engineeringStudent
    def __init__(self, name, surname, registered):
        self.registered = registered #<----hours still needs to be assigned to the class instance
        #use super() to call the base class' __init__' which expects a name and surname
        super().__init__(name, surname) #<-----calls the base class constructor

    def display_extra(self): #<------- only exists for engineeringStudent
        # derived class has access to all the variables of the base class.
        self.display()
        print('Registered: {}'.format(self.registered))
        print('_' * 50)


normal_Student = Student('leonard', 'hofsteder')
nursing_Student = nursingStudent('amy','farafowler', 50)
engineering_Student = engineeringStudent('howard','wolowitz', True)


# even though add_subject_and_mark is part of the base class, it is also part of the derive clasess through the power of inheritance
# show everything in student is in our bases class
engineering_Student.add_subject_and_mark('NASA101', 50)
engineering_Student.add_subject_and_mark('Robot201', 73)

normal_Student.display()
nursing_Student.display_extra()
engineering_Student.display_extra()