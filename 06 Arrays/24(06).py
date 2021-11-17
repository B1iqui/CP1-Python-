array = [10, 20, 30, 40, 50]
n = int(input('Enter any number: '))
for digit in array:
    if digit > n:
        print(digit, end = ' ')