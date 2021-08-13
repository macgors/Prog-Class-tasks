from numpy import dot
from math import sqrt

def cosine(a,b):
    return dot(a,b) / (sqrt(dot(a,a))*sqrt(dot(b,b)))

print(cosine((1,1,1), (-1,1,1)))