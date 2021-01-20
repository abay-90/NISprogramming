

print("Opening thefile.txt")
# Opens "thefile.txt" in writable mode
# If the file doesn't exist, it is created
my_file = open("thefile.txt", "w")
print()
print("File methods and properties:")
# The name property provides the file system name of the associated file
print("name: ", my_file.name)
# The mode property provides details on which mode the file was opened as
print("mode: ", my_file.mode)
# The closed property returns true if the file is closed
print("closed: ", my_file.closed)
# The readable() method returns true if the file is readable
print("readable(): ", my_file.readable())
# The writable() method returns true if the file is writable
print("writable(): ", my_file.writable())
print()
print("Opening thefile.txt")
# Closes the file to release the resources
my_file.close()
print()
print("File methods and properties:")
print("closed: ", my_file.closed)