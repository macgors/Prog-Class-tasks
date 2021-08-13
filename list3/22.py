def jaccard(a, b):
    return (len(a.intersection(b)) / len(a.union(b)) ) if max(len(a), len(b)) > 0 else None


print(jaccard(set([1, 2, 3, 4]), set([1,2,3,4])))