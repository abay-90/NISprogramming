# The file is opened using the readable+ mode
# By running the code in a with block, the file will
# be released as the block exits scope.
with open("../../../Downloads/0302_Python_fileshela_1/0302 Python fileshela/thefile.txt", "r+") as my_file:
    # Move the file pointer to 50
    my_file.seek(50)
    # Overwrite the text at file pointer 50
    my_file.write("#####")
    # Return to the start of the file
    my_file.seek(0)
    # Display the file contents
    print(my_file.read())
    my_file.close()
