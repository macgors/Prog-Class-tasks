from statistics import mode 

def most_freq(sentence):
    return mode(sentence) if len(sentence) else None

print(most_freq([0, 1, 2, 2]))