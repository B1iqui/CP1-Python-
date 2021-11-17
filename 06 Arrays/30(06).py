import random

def rand_elem(array):
    return random.sample(array, 3)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(rand_elem(a))