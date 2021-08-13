def remove_too_long(lst):
    return [x for x in lst if len(x) <= 5]

print(remove_too_long(['foo', 'bar', 'aaaaaaa']))