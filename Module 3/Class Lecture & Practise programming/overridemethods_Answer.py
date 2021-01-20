class Student:
    count = 0

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        Student.count += 1
        self.number = Student.count
        self.grades = {}

    def display(self):
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
        self.hours = hours
        super().__init__(name, surname)

    def display(self):
        # the above method is the same as the base class method display()
        # the derived class method is overriding in the method in the base class
        super().display()
        print('Hours worked: {}'.format(self.hours))
        print('_' * 50)


class engineeringStudent(Student): #<-----derived class

    def __init__(self, name, surname, registered):
        self.registered = registered
        super().__init__(name, surname)


    def display(self):
        #the above method is the same as the base class method display()
        #the derived class method is overriding in the method in the base class
        super().display()
        print('Registered: {}'.format(self.registered))
        print('_' * 50)


normal_Student = Student('leonard', 'hofsteder')
nursing_Student = nursingStudent('amy','farafowler', 50)
engineering_Student = engineeringStudent('howard','wolowitz', True)
engineering_Student.add_subject_and_mark('NASA101', 50)
engineering_Student.add_subject_and_mark('Robot201', 73)

normal_Student.display()
nursing_Student.display()
engineering_Student.display()