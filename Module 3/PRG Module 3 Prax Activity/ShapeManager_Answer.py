from Square import *
from Rectangle import *
from Cube import *
from Box import *

shapes = list()

shapes.append(Square("Square 1", 10))
shapes.append(Rectangle("Rectangle 1", 20, 10))
shapes.append(Cube("Cube 1", 10))
shapes.append(Box("Box 1", 20, 10, 5))

print("Number of shapes: ", Shape.count)
print("-" * 50)

for current in shapes:
    print(current)
    print("-" * 50)

