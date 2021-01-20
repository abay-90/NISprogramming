from random import random

output = ""
for current in range(0, 100):
    print(current)
    output += str(int(random() * 500)) + ", "

my_file = open("randomnumbers.txt", "w")
my_file.write(output)
my_file.close()
