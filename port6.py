import csv


def read_portfolio(filename, *, errors='warn'):
    '''
    Read CSV file  with name, date, shares, price data into a list of dicts
    '''
    portfolio = []

    if errors not in {'warn', 'silent', 'raise'}:
        raise ValueError("errors must be one of 'warn', 'silent', 'raise'")

    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)  # Skip the header
        for rowno, row in enumerate(rows, start=1):
            try:
                row[2] = int(row[2])
                row[3] = float(row[3])
            except ValueError as err:
                if errors == 'warn':
                    print('Row:', rowno, 'Bad row:', row)
                    print('Row:', rowno, 'Reason:', err)
                elif errors == 'raise':
                    raise  # Reraises the last exception
                else:
                    pass  # ignore
                continue
            # record = tuple(row)
            record = {
                'name': row[0],
                'date': row[1],
                'shares': row[2],
                'price': row[3]
            }
            portfolio.append(record)
    return portfolio


portfolio = read_portfolio('Data/portfolio.csv')

total = 0.0
for holding in portfolio:
    total += holding['shares'] * holding['price']
print('Total cost:', total)

'''
def holding_name(holding):
    return holding['name']


portfolio.sort(key=lambda holding: holding['name'])
portfolio.sort(key=holding_name)

import itertools

for name, items in itertools.groupby(portfolio, key=lambda holding: holding['name']):
    print('NAME: ', name)
    for it in items:
        print(' ', it)

by_name = {name: list(items) for name, items in itertools.groupby(portfolio, key=lambda holding: holding['name'])}
'''