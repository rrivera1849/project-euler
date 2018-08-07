
import math

def sieve(n):
  primes = []
  marked = [False] * (n+1)

  for p in range(2, n):
    if marked[p]:
      continue

    primes.append(p)
    for m in range(p*p, n, p):
      marked[m] = True

  return primes

def get_divisors(n):
    divisors = []

    for i in range(1, int(math.ceil(math.sqrt(n))) + 1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(int(n/i))

    return list(set(divisors))

def triangular(n):
    return (n * (n + 1)) / 2

def squareTriangular(n):
    intermediate = triangular(n)
    return intermediate * intermediate

def squarePyramidal(n):
    return (n * (n + 1) * (2*n + 1)) / 6
