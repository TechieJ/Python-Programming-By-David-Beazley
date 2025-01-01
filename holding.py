class Holding(object):
    def __init__(self, name, date, shares, price):
        self. name = name
        self.date = date
        self.shares = shares
        self.price = price

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
#h = Holding('AA','2007-09-11',100,32.2)
#h.__dict__ # every attribute is part of dictionary and python is getting all info from here.
#h.__dict__['shares']
#you will not find methods being part of instance dictionary as those are part of class dictionary
#Holding.__dict__
#Holding.__dict__['cost']
#Holding.__dict__['cost'](h)