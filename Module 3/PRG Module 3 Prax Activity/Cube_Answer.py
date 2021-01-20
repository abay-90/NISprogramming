from ThreeDimensionalShape import *


class Cube(ThreeDimensionalShape):

    def __init__(self, description, length):
        super().__init__(description)
        self.length = length

    def __str__(self):
        return "Cube is a {0}".format(super().__str__())

    def area(self):
        return self.length * self.length * 6

    def volume(self):
        return self.length * self.length * self.length

