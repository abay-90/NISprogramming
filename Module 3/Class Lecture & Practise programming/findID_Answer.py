#see the id of a specific item, use the id()

class stockItem:
    def __init__(self, name): #<---------constructor
        self.name = name #<----instance variable
        print('{} added to stock'.format(self.name)) #when stock item created, prints out stock item name to commmand line


item1 = stockItem('Toothbrush')
item2 =stockItem('Toothpaste')

#use id() to retrieve a object's id
print('item1 id: {}'.format(id(item1)))
print('item2 id: {}'.format(id(item2)))

