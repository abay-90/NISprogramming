class Shape:
    count = 0

    def __init__(self, description):
        self.description = description
        Shape.count += 1

    def __str__(self):
        return "{0}\nArea:\t{1}\nVolume:\t{2}".format(self.description, self.area(), self.volume())

    def area(self):
        return 0

    def volume(self):
        return 0

