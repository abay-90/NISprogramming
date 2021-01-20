# The file is opened using the readable mode
my_file = open("../../../Downloads/0302_Python_fileshela_1/0302 Python fileshela/thefile.txt", "r")

# Display all the contents of the file
print(my_file.read())

#Method2
#want to have the output twice!
# Display all the contents of the file again
# The individual lines in a file may be processed
# using a for loop.
for line in my_file:
    # Suppress the new line at the end of the line,
    # since the line of text read from the file already
    # contains a newline character at the end.
    print(line, end="")

my_file.close()
