from nltk import book
import random
import hashlib
import zlib

MAX_32_BIT_NUM = 2**32-1

PRIME = 4295081269

def jaccard(a, b):
    return (len(a.intersection(b)) / len(a.union(b)) ) if max(len(a), len(b)) > 0 else None

def k_shingles(tokens, k):
    for i in range(len(tokens) - k + 1):
        yield tokens[i:i+k]

s1 = set([zlib.adler32(token.encode('utf-8')) for token in book.text1.tokens if len(token) < 8])
s2 = set([zlib.adler32(token.encode('utf-8')) for token in book.text2.tokens if len(token) < 8])
s3 = set([zlib.adler32(token.encode('utf-8')) for token in book.text3.tokens if len(token) < 8])

def compare_counters(a, b):
    return sum(b[i] == value for i, value in enumerate(a)) / len(a)


hash_functions_coefs = list(zip(random.sample(range(1, MAX_32_BIT_NUM), 100), random.sample(range(1, MAX_32_BIT_NUM), 100)))

counter_gen = lambda s, coefs: [min((a*i + b) % PRIME for i in s) for a, b in coefs]

counters = [counter_gen(s, hash_functions_coefs) for s in [s1, s2, s3]]

print("\nMINHASH SIMILARITY --- JACCARD SIMILARITY")
print(compare_counters(counters[0], counters[1]), " --- ", jaccard(s1, s2))
print(compare_counters(counters[1], counters[2]), " --- ", jaccard(s2, s3))
print(compare_counters(counters[0], counters[2]), " --- ", jaccard(s1, s3))
