def is_in_array(n, arr):
    if n in arr:
        return n
    
number = int(input())
array = [15, 38, 7, 23, 14]

print(f'Number: {number}')
print('Array:', array)
print('Result: number', is_in_array(number, array), 'appears in the array')