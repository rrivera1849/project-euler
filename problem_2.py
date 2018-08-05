
s = 2
a, b = 0, 2
c = b * 4 + a
while c < 4000000:
  s += c
  a = b; b = c;
  c = b * 4 + a

print(s)
