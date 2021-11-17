def sep_even_odd(a):
    even_array = []
    odd_array = []
    for digit in a:
        if digit % 2 == 0:
            even_array.append(digit)
        else:
            odd_array.append(digit)
            
    return even_array + odd_array

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(sep_even_odd(array))