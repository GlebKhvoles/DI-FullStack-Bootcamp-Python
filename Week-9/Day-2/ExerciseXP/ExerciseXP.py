#Exercise1
def absolute(num):
    '''The abs() function returns the absolute value of the specified number.'''
    return abs(num)

def make_int(num):
    '''The int() function converts the specified value into an integer number.'''
    return int(num)

def do_input():
    '''The input() function allows user input.'''
    x = input('Enter your name')
    return x

print(make_int.__doc__)
print(do_input.__doc__)
print(absolute.__doc__)

#Exercise2
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
    def __int__(self):
        return self.amount
    def __str__(self):
        if self.amount > 1:
            return f'{self.amount} {self.currency}s'
        return f'{self.amount} {self.currency}'
    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if isinstance(other, Currency): #what if the type is not Currency at this case you need to handle it
            if self.currency == other.currency:
                self.amount += other.amount
            else:
                raise TypeError(f"Cannot add between Currency type {self.currency} and {other.currency}")

    def __iadd__(self, other):
        if isinstance(other, int):
            self.amount += other
        elif isinstance(other, Currency):
            self.amount += other.amount
        return self

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)
print(str(c1))
print(int(c1))
print(repr(c1))
c1 + 5
c1 + c2
print(c1)
c1 += 5
print(c1)
c1 += c2
print(c1)
c1 + c3
