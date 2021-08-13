def func(lst, c):
    return [i for i in lst if i % c == 0 and i > lst[0] and i < lst[-1]]


print(func([3,1,2,3,4,5,6,7,8,9,7], 2))