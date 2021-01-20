from TwoDimensionalShape import *


class Rectangle(TwoDimensionalShape):

    def __init__(self, description, length, width):
        super().__init__(description)
        self.length = length
        self.width = width

    def __str__(self):
        return "Rectangle is a {0}".format(super().__str__())

    def area(self):
        return self.length * self.width