# The file is opened using the readable mode
my_file = open("../../../Downloads/0302_Python_fileshela_1/0302 Python fileshela/thecsvfile.csv", "r")

# readline is used to read all of a file's contents at once
file_contents = my_file.readlines()
print(file_contents)
print()
# The individual lines are stored as elements in a string-based list
for line in file_contents:
    print(line,end="")

my_file.close()
