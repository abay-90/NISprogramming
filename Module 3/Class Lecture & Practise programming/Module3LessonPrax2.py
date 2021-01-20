class myemployees:
    count = 0

    def __init__(self):
        self.name = ""
        self.surname = ""
        myemployees.count += 1
        self.number = myemployees.count


first_employee = myemployees()
first_employee.name = "Mia"
first_employee.surname = "Fossum"

second_employee = myemployees()
second_employee.name = "Siri"
second_employee.surname = "Berg"

third_employee = myemployees()
third_employee.name = "Kine"
third_employee.surname = "Nannestad"

print("{}: {} {}".format(first_employee.number, first_employee.name, first_employee.surname))
print("{}: {} {}".format(second_employee.number, second_employee.name, second_employee.surname))
print("{}: {} {}".format(third_employee.number, third_employee.name, third_employee.surname))
print("Number of students:  {}".format(myemployees.count))
