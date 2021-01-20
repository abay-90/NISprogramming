class cat:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'A cat name {}.'.format(self.name)


class duck:
    def __init__(self, name):
        self.name = name


# Create a list to amend animals to store Cats and Ducks
animals = []
animals.append(cat('Åsta'))
animals.append(duck('Donald'))

#Run through all of the objects in animals.
#The system does not know what type of object is being processed.
#When a object is output, its str() method is called implicitly (automatically)
#This afain demonstrates polymorphism as the same method is called on all objects with different results

for current in animals:
    print('Object details: \t{}'.format(current))
