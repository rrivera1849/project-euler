
import math

def sieve(n):
  primes = []
  marked = [False] * (n+1)

  for p in range(2, n):
    if marked[p]:
      continue

    primes.append(p)
    for f in range(2, (n / p) + 1):
      marked[f*p] = True

  return primes


N = 600851475143
primes = sieve(int(math.sqrt(N)))

for p in primes[::-1]:
  if N % p == 0:
    print(p)
    break
