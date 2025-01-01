# validate.py

"""
This is more proficient reusable code than the code we have in holding4.py which is more of a copy paste code.
we can have much better code than this as well
"""

class Typed(object):
    expected_type = object
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected {}'.format(self.expected_type))
        instance.__dict__[self.name] = value
class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class String(Typed):
    expected_type = str

class Holding(object):
    name = String('name')
    shares = Integer('shares')
    price = Float('price')
    def __init__(self, name, date, shares, price):
        self.name = name
        self.date = date
        self.shares = shares
        self.price = price

    def __setattr__(self, key, value):
        if key not in {'name','date','price','shares'}:
            raise AttributeError('No attribute {}'.format(key))
        super().__setattr__(key, value)
    @property
    def cost(self):
        return self.shares * self.price
#h = Holding('AA','2007-09-11',100,32.2)

class Spam():
    def __getattribute__(self, item):
        """
        calls for every get operation
        """
        print('Getting: ',item)

class Spam2():
    def __getattr__(self, item):
        """
        Fail Safe operation - If some attribute does not exists then this gets called and error gets suppressed
        calls for bad operation
        """
        print('Getting: ',item)