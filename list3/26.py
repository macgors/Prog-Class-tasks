from nltk import book
from itertools import combinations
import functools
from collections import defaultdict


def hamming(a, b):
    return functools.reduce(lambda acc, values: acc + 1 if values[0] != values[1] else acc, zip(a,b), 0)



len_lists = defaultdict(list)

for token in set(book.text1.tokens):
    len_lists[len(token)].append(token)

max_distance = -1
words = None, None

for length in sorted(len_lists.keys(), reverse=True):

    if length <= max_distance:
        break
    
    for token1, token2 in combinations(len_lists[length], 2):
        if hamming(token1, token2) > max_distance:
            max_distance = hamming(token1, token2)
            words = token1, token2
            if length <= max_distance:
                break

print(words, max_distance)