
"""Another useful module to import is the keyword module.
The keyword module allows a programmer to determine if a given function or variable name already exists as a keyword.
This module may be used to list all keywords or to test individual keywords by using the iskeyword() method."""

import keyword

print("Python keywords:")
for theword in keyword.kwlist:  # kwlist contains a list of Python keywords
    print(theword, end=", ")
print()
# iskeyword returns True or False depending on whether a word is a keyword
#print("Noroff is a Python keyword: ", keyword.iskeyword("Noroff"))
