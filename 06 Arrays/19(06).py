array1 = [2, 3, 2, 5, 8, 1, 9, 8]
array2 = []
unique = [digit for digit in array1 if digit not in array2]
print('Array:', *array1)
print('Unique elements: ', *unique)