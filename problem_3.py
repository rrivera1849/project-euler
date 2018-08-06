
import math
from utils import *

N = 600851475143
primes = sieve(int(math.sqrt(N)))

for p in primes[::-1]:
  if N % p == 0:
    print(p)
    break
