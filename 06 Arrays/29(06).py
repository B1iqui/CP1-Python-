def is_subser(a1, a2):
    for digit in a1:
        if digit in a2:
            return True
        else:
            return False
    
array1 = [1, 2, 3]
array2 = [1, 2, 3]

print(is_subser(array1, array2))