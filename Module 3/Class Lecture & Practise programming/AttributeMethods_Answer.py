class Employee:
    def __init__(self, name):
        self.name = name

first = Employee("Frey")
second = Employee("Klaus")

# Set the attribute "name" of first to "Freya"
setattr(first,"name","Freya") #<-----changes the an attribute
# Get the attribute "name" of first
print(getattr(first,"name")) #<----- finds the name of an attribute

# Delete the attribute "name" of second
delattr(second,"name")

# Test if second has the attribute "name"
if hasattr(second,"name"): #<-------does the object have the attribute name<
    print(getattr(second,"name"))
else:
    print("Second does not have attribute name")
