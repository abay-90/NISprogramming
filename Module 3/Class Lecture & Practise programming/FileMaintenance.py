# Using the opreating system package and provides a method called isfile()
import os

# Creates an empty file and closes it
temp_file = open("tempfile.txt", "x") #<------- x argument creates an empty file
temp_file.close() #<----- closing it as we do not want to wrtie anything to it.

# Test if the file exists
if os.path.isfile("tempfile.txt"):
    print("File found - removing it.")
    # If it does, remove it
    os.remove("tempfile.txt")
