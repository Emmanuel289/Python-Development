# A lazy recap of  some function definitions


def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
        among a, b and c.
        """
    d1 = abs(a - b)
    d2 = abs(a - c)
    d3 = abs(b - c)
    return min(d1, d2, d3)


# test the minimum difference function  Input1: (1,3,5) Expected return value: 2 Input2: (-3,-6,-11)
# Expected return value: 3

print(least_difference(1, 3, 5), least_difference(-3, -6, -11))


# Functions that call other functions

def mult_by_five(x):
    return 5 * x


def call(fn, arg):
    """call fn on arg"""
    return fn(arg)


def squared_call(fn, arg):
    """call fn on the result of calling fn on arg"""
    return fn(fn(arg))


# test function call on function

print("The result of applying the double function calls are '\n'",
      call(mult_by_five, 1),
      squared_call(mult_by_five, 1), sep='\n')


def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5


print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep='\n',
)
