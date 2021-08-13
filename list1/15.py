def custom_sorted(lst):
    return sorted([x for x in lst if isinstance(x, str)]) + sorted([x for x in lst if isinstance(x, int)])


print(custom_sorted(["a", "b", 1, 2, "s", -99]))
