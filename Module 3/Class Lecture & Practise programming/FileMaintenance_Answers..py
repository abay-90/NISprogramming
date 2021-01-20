import os

# Creates an empty file and closes it
temp_file = open("tempfile.txt","x")
temp_file.close()

# Test if the file exists
if os.path.isfile("tempfile.txt"):
    print("File found - removing it.")
    # If it does, remove it
    os.remove("tempfile.txt")
