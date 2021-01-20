class Employee:
    def __init__(self, name):
        self.name = name

first = Employee("Freya")
second = Employee("Klaus")
third = Employee("Maia")
del second.name

print(first.name)
# print(second.name)
print(third.name)
