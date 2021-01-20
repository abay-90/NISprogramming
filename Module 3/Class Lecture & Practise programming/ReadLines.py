# The file is opened using the readable mode
my_file = open("CSVfile.csv", "r")

# readlines is used to read all of a file's contents at once
files_contents = my_file.readlines()
print(files_contents)
print()

# The individual lines are stored as elements in a string-based list
for line in files_contents:
    print(line,end="")

my_file.close()

