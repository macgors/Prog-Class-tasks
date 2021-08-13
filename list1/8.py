from functools import reduce

def powset(lst):
    return reduce(lambda res, x: res + [subset + [x] for subset in res], lst, [[]])

print(powset([1,2,3]))