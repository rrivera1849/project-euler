
from utils import *

n = 1
while True:
    q = triangular(n)
    if len(get_divisors(q)) >= 500:
        print(q)
        break

    n += 1
