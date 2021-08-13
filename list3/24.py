from nltk import book
from nltk.metrics import *

thresh_hold = 4
word = 'dog'
word_len = len(word)

res = []
for token in set(book.text1.tokens):
    token_len = len(token)
    if token_len <= word_len + thresh_hold and ( token_len < 4 or edit_distance(word, token) < 4):
        res.append(token)

print(res)