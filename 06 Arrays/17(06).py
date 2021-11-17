array1 = [4, 36, 12, 28, 9, 44, 5]
array2 = [5, 1, 36]

print(*[digit for digit in array1 if digit not in array2])