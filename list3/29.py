from itertools import combinations

def gen_humming_with_param(s, n):
    for indices in combinations(range(len(s)), n):
        yield replace_at_indices(s, indices)


def replace_at_indices(s, ixs):
    for i in ixs:
        s = s[:i] + ('0' if s[i] == '1' else '1') + s[i+1:]
    return s

print(list(gen_humming_with_param('11111', 4)))