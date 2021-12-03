array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
for number in array:
    if number % 3 == 0:
        array[number] == 'THREE'
    if number % 5 == 0:
        array[number] == 'FIVE'
    if number % 3 and number % 5 == 0:
        array[number] == 'BINGO'
print(array)
        