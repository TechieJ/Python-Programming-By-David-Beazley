import sys
from abc import ABCMeta, abstractmethod


def print_table(objects, colnames):
    '''
    Make a nicely formatted table showing attributes from a list of objects
    '''
    # Emit table headers
    for colname in colnames:
        print('{:>10s}'.format(colname), end=' ')
    print()
    # Emit a row of table data
    for obj in objects:
        for colname in colnames:
            print('{:>10s}'.format(str(getattr(obj, colname))), end=' ')
        print()


def print_table(objects, colnames, formatter):
    '''
    Make a nicely formatted table showing attributes from a list of objects
    '''

    if not isinstance(TableFormatter):
        raise TypeError("Formatter must be a TableFormatter")

    formatter.headings(colnames)
    for obj in objects:
        rowdata = [str(getattr(obj, colname)) for colname in colnames]
        formatter.row(rowdata)


_formatters = {}


class TableMeta(ABCMeta):
    def __init__(cls, clsname, bases, methods):
        super().__init__(clsname, bases, methods)
        if hasattr(cls, 'name'):
            _formatters[cls.name] = cls


class TableFormatter(metaclass=TableMeta):
    def __init__(self, outfile=None):
        if outfile == None:
            outfile = sys.stdout
        self.outfile = outfile

    # Servers as design spec for making tables (use inheritance to customize)
    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass


class TextTableFormatter(TableFormatter):
    name='text'
    def __init__(self, outfile=None, width=10):
        super().__init__(outfile)  # Initialize parent
        self.width = width

    def headings(self, headers):
        for header in headers:
            print('{:>{}s}'.format(header, self.width), end=' ', file=self.outfile)
        print(file=self.outfile)

    def row(self, rowdata):
        for item in rowdata:
            print('{:>{}s}'.format(item, self.width), end=' ', file=self.outfile)
        print(file=self.outfile)


class CSVTableFormatter(TableFormatter):
    name='csv'
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))


class HTMLTableFormatter(TableFormatter):
    name = 'html'
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print('<th>{}</th>'.format(h), end='')
            print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
            print('<td>{}</td›'.format(d), end='')
        print('</tr>')


class QuotedTextTableFormatter(TextTableFormatter):
    # This is tightly coupled with text table formatter only
    def row(self, rowdata):
        quoted = ['"{}"'.format(d) for d in rowdata]
        super().row(quoted)


class QuotedMixin(object):
    # this is not coupled with any of the formatter class. This is more generic now.
    def row(self, rowdata):
        quoted = ['"{}"'.format(d) for d in rowdata]
        super().row(quoted)


class Formatter(QuotedMixin, CSVTableFormatter):
    # this will tie up mixin class with the formatter class
    pass

# python3 -i holding.py
# formatter = Formatter()
# print_table(portfolio, ['name','price'], formatter)
