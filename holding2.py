class Holding(object):
    def __init__(self, name, date, shares, price):
        self. name = name
        self.date = date
        self.shares = shares
        self.price = price

    def get_price(self):
        '''
        This approach is being used in many other programming language
        However, this will not force user to use this approach as still user can directly set the attributes.
        '''
        return self.price

    def set_price(self, newprice):
        '''
        this approach is  being used at many other programming language
        However, this will not force user to use this approach as still user can directly set the attributes.
        '''
        if not isinstance(float):
            raise TypeError("Expected Float")
        self.price = newprice

    def __repr__(self):
        # representation of an object
        return 'Holding({!r},{!r},{!r},{!r})'.format(self.name, self.date, self.shares, self.price)

    def __str__(self):
        # runs with print statement
        return '{} shares of {} at ${:0.2f}'.format(self.shares, self.name, self.price)
    def cost(self):
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
