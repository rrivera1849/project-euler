
import time

def find_largest(palindromes):
  for p in palindromes[::-1]:
    for q in reversed(range(100, 1000)):
      r = p / q
      if p % q == 0 and r > 99 and r < 1000:
        print(p)
        return

start = time.time()

palindromes = []
for a in range(1, 10):
  for b in range(0, 10):
    for c in range(0, 10):
      palindromes.append(int(str(a) + str(b) + str(c) + str(b) + str(a)))
      palindromes.append(int(str(a) + str(b) + str(c) + str(c) + str(b) + str(a)))

palindromes.sort()
find_largest(palindromes)

end = time.time()

print("Time Taken: {}".format(end - start))
