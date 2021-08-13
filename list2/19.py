from nltk import book

res = set()

for i in range(9):
    res = res.union(set(getattr(book, f"text{i+1}").tokens))

print(res)