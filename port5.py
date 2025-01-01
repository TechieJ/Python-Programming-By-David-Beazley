import csv


def read_portfolio(filename, *, errors='warn'):
    '''
    Read CSV file  with name, date, shares, price data into a list
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
                    raise   # Reraises the last exception
                else:
                    pass    #ignore
                continue
            record = tuple(row)
            portfolio.append(record)
    return portfolio

portfolio = read_portfolio('Data/portfolio.csv')

total = 0.0
for name,date, shares, price in portfolio:
    total += shares * price
print('Total cost:', total)
