a, b, c = int(input()), int(input()), int(input())
p = 1 / 2 * (a + b + c)
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print(s)