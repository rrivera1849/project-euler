
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
