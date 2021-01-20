to_slice = input("Enter a string to slice:  ")

try:
    start_index = int(input("Enter a starting index:  "))
except:
    start_index = 0

try:
    end_index = int(input("Enter an ending index:  "))
except:
    end_index = len(to_slice)


if start_index < 0:
    start_index = 0

if end_index >= len(to_slice):
    end_index = len(to_slice)

print(to_slice[start_index:end_index])