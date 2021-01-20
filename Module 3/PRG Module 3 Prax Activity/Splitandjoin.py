#Main task:

#Create a script named splitandjoin.py
#In this script, prompt the user to enter a string of text.
#Next ask the user for a character on which to split their text.
#Use this character to split their initial string. Display the elements of the split string to the user.
#Request text from the user to use in order to re-combine the string. Display the re-combined string to the user.

# Given a string, write a Python program to split the characters of the given string into a list.
#
# Examples:
# Input : Noroff
# Output : ['N', 'o', 'r', 'o', 'f', 'f']

#text = raw_input("prompt")  # Python 2
text = input("prompt")  # Python 3

import sys
print (sys.argv)

# Python3 program to Split string into characters
def split(word):
    return [char for char in word]

# Driver code
word = 'Noroff'
print(split(word))

