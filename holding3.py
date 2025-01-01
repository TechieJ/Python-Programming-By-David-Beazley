class Holding(object):
    def __init__(self, name, date, shares, price):
        self. name = name
        self.date = date
        self.shares = shares
        self.price = price

    @property
    def price(self):
        '''
        This approach is better than specified in holding2.py
        By adding property decorator, we are adding safety set the attributes correctly.
        However, there could tons of attributes in a larger program.
        '''
        return self._price

    @price.setter
    def price(self, newprice):
        '''
        This approach is better than specified in holding2.py
        By adding property decorator, we are adding safety set the attributes correctly.
        We can add lot of validation in this.
        However, there could tons of attributes in a larger program
        '''
        if not isinstance(newprice, float):
            raise TypeError("Expected Float")
        self._price = newprice

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, newshares):
        if not isinstance(newshares, int):
            raise TypeError("Expected int")
        self._shares = newshares

    def __repr__(self):
        # representation of an object
        return 'Holding({!r},{!r},{!r},{!r})'.format(self.name, self.date, self.shares, self.price)

    def __str__(self):
        # runs with print statement
        return '{} shares of {} at ${:0.2f}'.format(self.shares, self.name, self.price)

    @property
    def cost(self):
        '''
        By adding property decorator to the method, then it will behave as a compute attribute
        you will not need to add () while calling this method
        '''
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

import csv

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)  # Skip the header
        for row in rows:
            h = Holding(row[0],row[1],int(row[2]),float(row[3]))
            portfolio.append(h)
    return portfolio

portfolio = read_portfolio('Data/portfolio.csv')
#h = Holding('AA','2007-09-11',100,32.2)