n = int(input('Enter ammount in PLN: '))

counter = 0
counter_5zl = 0
counter_2zl = 0
counter_1zl = 0
while n != 0:
    if n >= 5:
        counter += n//5
        counter_5zl += n//5
        n %= 5
        
    elif n >= 2:
        counter += n//2
        counter_2zl += n//2
        n %= 2
        
    elif n >= 1:
        counter += n//1
        counter_1zl += n//1
        n %= 1
        
print(f'5 zl - {counter_5zl}\n2 zl - {counter_2zl}\n1 zl - {counter_1zl}')