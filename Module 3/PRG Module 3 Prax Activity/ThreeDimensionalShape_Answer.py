from Shape import *


class ThreeDimensionalShape(Shape):

    def __init__(self, description):
        super().__init__(description)

    def __str__(self):
        return "Three-dimensional shape\n{0}".format(super().__str__())


