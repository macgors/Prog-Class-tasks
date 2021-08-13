import functools

def calc(sentence):
    return functools.reduce(lambda x, y: 1 + x if y.isdigit() else x, sentence, 0), functools.reduce(lambda x, y: 1 + x if y.isalpha() else x, sentence, 0)

print(calc("123kk4 dd00 4k"))