from nltk.metrics import edit_distance
from nltk import book
from itertools import combinations_with_replacement
from collections import defaultdict
import time


def find_min_distance(tokens):

    len_lists = defaultdict(list)

    for token in tokens:
        len_lists[len(token)].append(token)

    min_relative_dist = float('inf')
    res = None, None 

    set_pairs = sorted(combinations_with_replacement(len_lists.keys(), 2), key=lambda x: x[0] + x[1], reverse=True)

    for len1, len2 in set_pairs:
        for token1 in len_lists[len1]:
            for token2 in len_lists[len2]:

                if token1 == token2:
                    continue

                curr_relative_dist = edit_distance(token1, token2)  / (len(token1) + len(token2))

                if curr_relative_dist <= min_relative_dist:
                    min_relative_dist = curr_relative_dist
                    res = token1, token2

                    if edit_distance(token1, token2)  == 1:
                        return (token1, token2), curr_relative_dist

    return res, min_relative_dist

tic = time.perf_counter()
res = find_min_distance(set(book.text2.tokens))
toc = time.perf_counter()

print(*res)
print(f"Total elapsed time: {toc - tic:0.4f} seconds")


# for token1, token2 in combinations(set(book.text2.tokens), 2):
#     curr_dist = edit_distance(token1, token2) / (len(token1) + len(token2))
#     if(curr_dist < min_dist):
#         min_dist = curr_dist
#         res = token1, token2
#         print(res)
