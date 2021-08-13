def list_differences(a, b):
    return list(set(a) & set(b))

print(list_differences([1, 2, 5, 6, 99, "foo"], ["foo", "bar", 2, 99]))