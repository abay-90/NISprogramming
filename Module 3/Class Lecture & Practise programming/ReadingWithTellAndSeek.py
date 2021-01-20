# The file is opened using the readable mode
my_file = open("Textfile.txt", "r")

# Display all the contents of the file
print(my_file.read())
print("Position {}".format(my_file()))
print("Resetting postion to 50")
my_file.seek(20)
print("Position {}".format(my_file.tell()))
print()
# Display all the contents of the file again,
# But starting from position 50.
# This mean only a portion of the file will be read.

for line in my_file:
    # Suppress the new line at the end of the line,
    # since the line of text read from the file already;
    # contains a newline character at the end.
    print(line, end="")

my_file.close()
