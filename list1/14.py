def alternate(lst1, lst2):
    return [x for y in zip(lst1, lst2) for x in y]
    #return sum(map(list, zip(lst1,lst2)), [])
    
print(alternate([1,3,5,7], [2,4,6,8]))