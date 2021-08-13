from nltk import book


def jaccard(a, b):
    return (len(a.intersection(b)) / len(a.union(b)))

res_dict = {}
for i, j in zip(book.text1.tokens, book.text1.tokens[1:]):
    res_dict[(i,j)] = jaccard(set(i), set(j))

print(res_dict)
    
