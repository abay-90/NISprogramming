# Creating and naming a file.

print("Opening Abayfile.txt")
# Opens "Abayfile.txt in writable mode; Ab-raham ay-nalem.
# If the file doesn't exist, it is created
my_file = open("Abayfile.txt", "w")
print()
print("File methods and properties:")

# The name property provides the files system name of the associated file
print("name: ", my_file.name)

# The mode property provides details on which mode the file was opened as
print("mode: ", my_file.mode)

# The closed property returns true if the file is closed
print("closed: ", my_file.closed)

# The readable() methods returns true if the file is readable
print("readable(): ", my_file.readable())
print()
print("Closing Abayfile.txt")

# Close the file to release the resources
my_file.close()
print()
print("File methods and properties")
# Only to check the output here
print("closed: ", my_file.closed)
