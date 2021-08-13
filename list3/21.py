def gen_humming(s):
    for i, c in enumerate(s):
        yield s[:i] + ('0' if c == '1' else '1') + s[i+1:]


print(list(gen_humming('1011')))