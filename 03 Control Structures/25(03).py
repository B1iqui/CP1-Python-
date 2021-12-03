a = int(input())
b = int(input())

print('*' * b)
for i in range(a - 2):
    print('*', ' ' * (b - 4), '*')
print('*' * b)