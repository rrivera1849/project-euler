
def is_divisible(n):
  to_test = [3, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19]
  for i in to_test:
    if n % i != 0:
      return False
  return True

n = 20
while not is_divisible(n):
  n += 20

print(n)
