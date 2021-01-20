my_file = open("Abayfile.txt", "w")

# The \n escape character signifies new lines.
# The following string will be written to file as 3 separate lines.
write_me = "Hey there\nCongrats on writing & creating the file\nKeep going. \n"
my_file.write(write_me)

# Methode2
# Lines may also be written one at a time, by calling
# write() for each line to be written.
# my_file.write("Extra line 1\n")
# my_file.write("Extra line 2\n")
# my_file.write("Extra line 3\n")
#
# my_file.close()