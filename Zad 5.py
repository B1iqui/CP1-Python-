def numpad():
    for x in range(0,3):
        for y in range(1, 4):
            print(f'{x*3 + y}', end = ' ')
        print()
numpad()