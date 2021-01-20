class employee:
    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate

    def calculate(self):
        return self.hours * self.rate


class stockItem:
    def __init__(self, item_count, item_price):
        self.item_count = item_count
        self.item_price = item_price

    def calculate(self):
        return self.item_count * self.item_price


class myDog:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print('{} says Woof.'.format(self.name))


def call_calculate(the_object):
    print('Type of object: {}'.format(type(the_object)))
    try:
        print('Result: {}'.format(the_object.calculate()))
    except:
        print('The object does not have a calculate() method')
    print()

def call_talk(the_object):
    print('Type of object: {}'.format(type(the_object)))
    try:
        the_object.talk()
    except:
        print('The object does not have a talk() method')
    print()

employee = employee(10, 200)
stockitem = stockItem(100, 30)
dog = myDog('Roxy')

call_calculate(employee)
call_calculate(stockitem)
call_calculate(dog)

call_talk(employee)
call_talk(stockitem)
call_talk(dog)
