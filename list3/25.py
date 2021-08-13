from nltk import book

def jaccard(a, b):
    return (len(a.intersection(b)) / len(a.union(b))) if max(len(a), len(b)) > 0 else None

text_sets = []
for i in range(9):
    text_sets.append(set(getattr(book, f"text{i+1}").tokens))

for i, text_set in enumerate(text_sets):
    print("<----------------->")
    for j, text_set2 in enumerate(text_sets[i:]):
        print(f"text{i+1} and text{j+i+1}: {jaccard(text_set, text_set2)}")