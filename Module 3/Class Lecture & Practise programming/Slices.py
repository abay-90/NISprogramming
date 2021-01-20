"""test_string = "This is my string"
slice_of_test_string = test_string[3]

print("test_string: ", test_string)
print("slice at index 3: ",slice_of_test_string)
"""

test_string = "This is my string"

print("test_string: ", test_string)
print("slice at index 5 up to index 10: ",test_string[5:10])
print("slice at index 5 up to index 10, step 2: ",test_string[5:10:2])
print("slice at index 5 up to the end of the string: ",test_string[5:])
print("slice at index 5 up to 3 characters from the end: ",test_string[5:-3])
