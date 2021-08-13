def k_shingles(s, k, word_wise=False):
    if word_wise:
        s = s.split()
    for i in range(len(s) - k + 1):
        yield s[i:i+k]

print(list(k_shingles('11', 2)))