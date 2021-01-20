
class myBooks:
    def __init__(self, name): #<---------contructor
        self.name = name #<----instance variable
        print('{} is my book '.format(self.name)) #when stock item created, prints out stock item name to commmand line


book1 = myBooks('jack and the beanstalk')
book2 = myBooks('charlie and the chocolate factory')

#use id() to retrieve a object's id
print('my first book location id: {}'.format(id(book1)))
print('my second book location id: {}'.format(id(book2)))