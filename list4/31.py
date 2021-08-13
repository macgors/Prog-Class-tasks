from hashlib import sha1
import random
from itertools import combinations_with_replacement
import matplotlib.pyplot as plt
import time
import numpy as np
 

def task(n):
    def bit_strings(n):
        for _ in range(n):
            yield str(bin(random.getrandbits(100)))[2:] 

    return min(((i,j, sha1((i+j).encode('utf-8')).digest()) for i,j in combinations_with_replacement(bit_strings(n), 2)), key=lambda x: x[2])



xs = [50, 100, 200, 500, 700, 850, 1000, 1300, 1500, 2000, 2500, 3000, 4000, 5000, 6000, 8000, 10000]

ys = []
for x in xs:
    tic = time.perf_counter()
    task(x)
    tac = time.perf_counter()
    ys.append(tac-tic)


plt.ylabel('Execution time [seconds]')
plt.xlabel('n')
fit = np.polyfit(xs, ys, deg=3) 
p = np.poly1d(fit)
p_xs = [i for i in range(50, 10000, 10)]
plt.plot(p_xs,p(p_xs),"r--") 
plt.plot(xs, ys, 'o')

plt.show()
