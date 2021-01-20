class Student:
    count = 0

    def __init__(self, name, surname):
        self.name = name    # Assign the received parameter's value
        self.surname = surname  # Assign the received parameter's value
        Student.count += 1
        self.number = Student.count
        self.grades = {}   # Subjects and their results (empty) (adding grades to student)

    def display(self): #<------- Display numbers, name & surname of student (blackbox concept)
        print("{}:\t{} {}".format(self.number, self.name, self.surname))
        print()
        if len(self.grades) == 0:
            print("\tNo subjects and results have been added")
        else:
            for key in self.grades:
                print("\t{}:\t\t{}".format(key, self.grades[key]))

            # Use self to call the calculate_average method
            print("\tAverange:\t{}".format(self.calculate_average()))

        print("-" * 50)