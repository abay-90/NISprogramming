description_one = "Description 1"
description_two = "Description 2"
price_one = "3456.89"
price_two = "563.45"

# Column 1 left justified
# Column 2 right justified
# Spaces for padding
print(description_one.ljust(20," "), price_one.rjust(10," "), sep="")
print(description_two.ljust(20," "), price_two.rjust(10," "), sep="")
print("-" * 30)
# Column 1 right justified
# Column 2 left justified
# Spaces for padding
print(description_one.rjust(20," "), price_one.ljust(10," "), sep="")
print(description_two.rjust(20," "), price_two.ljust(10," "), sep="")
print("-" * 30)
# Column 1 left justified
# Column 2 right justified
# . for padding
print(description_one.ljust(20,"."), price_one.rjust(10,"."), sep="")
print(description_two.ljust(20,"."), price_two.rjust(10,"."), sep="")
print("-" * 30)
# Column 1 center justified
# Column 2 center justified
# - for padding
print(description_one.center(20,"-"), price_one.center(10,"-"), sep="")
print(description_two.center(20,"-"), price_two.center(10,"-"), sep="")

