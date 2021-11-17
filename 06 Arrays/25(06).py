def minmax(array):
    new_array = []
    a = min(array)
    b = max(array)
    new_array.append(a)
    new_array.append(b)
    
    return new_array

a = [4, 2, 8, 4, 7, 9, 5]

print('Array: ', a)
print('Result:', minmax(a))