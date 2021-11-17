def is_median(n):
    average = sum(n) / len(n)
    return average

array = [1, 0, 9, 4, 6]
array1 = [6, 8, 3, 1, 0, 5, 7]

print(is_median(array))
print(is_median(array1))