# The file is opened using the readable mode
my_file = open("../../../Downloads/0302_Python_fileshela_1/0302 Python fileshela/thefile.txt", "r")

# Display all the contents of the file
print(my_file.read())
print("Position {}".format(my_file.tell()))
print("Resetting position to 50")
my_file.seek(20)
print("Position {}".format(my_file.tell()))
print()
# Display all the contents of the file again, but
# starting from position 50.  That means only a
# portion of the file will be read.
for line in my_file:
    # Suppress the new line at the end of the line,
    # since the line of text read from the file already
    # contains a newline character at the end.
    print(line, end="")

my_file.close()
