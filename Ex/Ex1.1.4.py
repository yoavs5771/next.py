from functools import reduce
def add(x, y):
    return int(x) + int(y)
def sum_of_digits(number):
    return int(reduce(add,list(str(number))))