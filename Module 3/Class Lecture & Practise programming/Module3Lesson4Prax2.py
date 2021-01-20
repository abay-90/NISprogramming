class myBooks:
    def __init__(self, name):
        self.name = name
        print('{} is my book '.format(self.name))

    def __del__(self):  # <----method created in the class so requires the self parameter
        print('{} removed from stock. id: {}'.format(self.name, id(self)))


def test_scope():
    item1 = myBooks('jack and the beanstalk')

test_scope()

book2 = myBooks('charlie and the chocolate factory')
del book2

book3 = myBooks('Tom and Jerry')
