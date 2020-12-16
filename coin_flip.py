from random import choice
from random import random


def coin_flip1():
    r = random()
    if random() > 0.5:
        return 'Heads'
    else:
        return 'Tails'


def coin_flip2():
    return choice(['Heads', 'Tails'])
    

print(coin_flip2())
print(coin_flip2())