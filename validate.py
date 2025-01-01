# validate.py

"""
This is more proficient reusable code than the code we have in holding4.py which is more of a copy paste code.
we can have much better code than this as well
"""
class Integer(object):
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        instance.__dict__[self.name] = value

class Float(object):
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, float):
            raise TypeError('Expected float')
        instance.__dict__[self.name] = value

class Holding(object):
    shares = Integer('shares')
    price = Float('price')
    def __init__(self, name, date, shares, price):
        self.name = name
        self.date = date
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price
#h = Holding('AA','2007-09-11',100,32.2)