
def check_palindromic(i, j):
  prod = i * j
  if str(prod) == str(prod)[::-1]:
    return True

  return False

combinations = [(i, j) for i in range(100,1000) for j in range(100, 1000)]

candidates = []
for c in combinations:
  if check_palindromic(c[0], c[1]):
    candidates.append(c[0] * c[1])

print(max(candidates))
