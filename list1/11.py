def remove_neg(lst):
    return [x for x in lst if x >= 0]

print(remove_neg([-1, -2, 3, 99]))