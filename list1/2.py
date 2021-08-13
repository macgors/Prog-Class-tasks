import random
from typing import List

def mean(lst: List[int]) -> int:
    return sum(lst) / len(lst)

print(mean([random.randint(10, 90) for _ in range(20)]))