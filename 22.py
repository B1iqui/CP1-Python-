import random

comp_dice = random.randint(1, 6)
user_input = int(input('Enter number from 1 to 6: '))
if user_input < 1 or user_input > 6:
    print("You've picked wrond number, restart program and choose number from 1 to 6.")
elif user_input == comp_dice:
    print('True.2')
else:
    print(f'False. \nThe number was {comp_dice}!')