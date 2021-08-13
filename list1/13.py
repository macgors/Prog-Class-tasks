def find_longest(string_set):
    return max(string_set, key = len)

print(find_longest(["aaaaaa", "aaaaab", "a"]))