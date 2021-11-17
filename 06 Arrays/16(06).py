def star(n):
    for digit in array:
        if 10 <= digit <= 99:
            print(f'{digit}: {symbol * digit}')
        else:
            print(f'{digit}:  {symbol * digit}')
symbol = '*'
array = [12, 6, 4, 9, 3]

print(star(array))