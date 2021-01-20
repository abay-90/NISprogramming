class Employee:
    def __init__(self, name):
        self.name = name

first = Employee("Frey")

for attribute in dir(first):
    print(attribute)

print()
print("Keys:")
for key in first.__dict__:
    print("{}:\t{}".format(key,first.__dict__[key]))
