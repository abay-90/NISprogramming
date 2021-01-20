import math

def calculate_area_of_shape(shape, length=0, height=0, width=0, radius=0):
    if shape == "square":
        return length * length
    if shape == "rectangle":
        return length * width
    if shape == "cube":
        return length * length * 6
    if shape == "circle":
        # You could import Math and use math.Pi instead of 3.14
        return 3.14 * radius * radius
        # return math.pi * radius * radius
    if shape == "cylinder":
        # You could import Math and use math.Pi instead of 3.14
        return 2 * 3.14 * radius * height + 2 * 3.14 * radius * radius
        # return 2 * math.pi * radius * height + 2 * math.pi * radius * radius


if __name__ == "__main__":
    print("Square:  ", calculate_area_of_shape("square", length=10))
    print("Rectangle:  ", calculate_area_of_shape("rectangle", length=12, width=5))
    print("Cube:  ", calculate_area_of_shape("cube", length=10))
    print("Circle:  ", calculate_area_of_shape("circle", radius=8))
    print("Cylinder:  ", calculate_area_of_shape("cylinder", radius=9, height=15))

