def to_bin(a):
    return bin(int("".join(map(str, a))))

print(to_bin([1, 2, 3])[2:])
