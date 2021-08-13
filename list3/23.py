def jaccard_words(str_a, str_b):
    a = set(str_a.split())
    b = set(str_b.split())
    return (len(a.intersection(b)) / len(a.union(b))) if max(len(a), len(b)) > 0 else None

print(jaccard_words('a b c', 'a d'))