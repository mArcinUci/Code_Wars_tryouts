'''
This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:
eight(divided_by(three()))
'''

class Number:
    def __init__(self, value=None):
        self.value = value

    def __call__(self, *args):
        if args:
            # If called with arguments, treat as a function
            return args[0](self.value)
        else:
            # If called without arguments, return the value
            return self.value

def plus(x):
    return lambda y: x + y

def minus(x):
    return lambda y: y - x

def times(x):
    return lambda y: x * y

def divided_by(x):
    return lambda y: int(y / x) if y != 0 else 0

# Define numbers
zero = Number(0)
one = Number(1)
two = Number(2)
three = Number(3)
four = Number(4)
five = Number(5)
six = Number(6)
seven = Number(7)
eight = Number(8)
nine = Number(9)


'''
id_ = lambda x: x
number = lambda x: lambda f=id_: f(x)
zero, one, two, three, four, five, six, seven, eight, nine = map(number, range(10))
plus = lambda x: lambda y: y + x
minus = lambda x: lambda y: y - x
times = lambda x: lambda y: y * x
divided_by = lambda x: lambda y: y // x
'''

'''
def zero(cb=None): return cb(0) if cb else 0
def one(cb=None): return cb(1) if cb else 1
def two(cb=None): return cb(2) if cb else 2
def three(cb=None): return cb(3) if cb else 3
def four(cb=None): return cb(4) if cb else 4
def five(cb=None): return cb(5) if cb else 5
def six(cb=None): return cb(6) if cb else 6
def seven(cb=None): return cb(7) if cb else 7
def eight(cb=None): return cb(8) if cb else 8
def nine(cb=None): return cb(9) if cb else 9

def plus(n): return lambda x: x+n
def minus(n): return lambda x: x-n
def times(n): return lambda x: x*n
def divided_by(n): return lambda x: x//n
'''


'''
def plus(y): return lambda x: x+y
def minus(y): return lambda x: x-y
def times(y): return lambda x: x*y
def divided_by(y): return lambda x: x//y

# Number function generator
def nf_gen(n):
     return lambda f=None: n if not f else f(n)

zero, one, two, three, four, five, six, seven, eight, nine = map(nf_gen, range(10))
'''