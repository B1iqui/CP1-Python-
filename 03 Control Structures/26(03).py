pin = '0805'
counter = 0
for i in range(3):
    password = input('Enter the PIN code: ')
    if password != pin:
        print('Incorrect')
        counter += 1
    elif password == pin:
        print('Correct')
        break
if counter == 3:
    print('Sorry, your payment card has been blocked.')