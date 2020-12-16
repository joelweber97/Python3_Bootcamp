
def eat(food, is_healthy):
    if not isinstance(is_healthy, bool):
        raise ValueError('is_healthy must be a bool')
    ending = 'because YOLO'
    if is_healthy:
        ending = 'because my body is a temple'
    return f'Im eating {food}, {ending}'
    
def nap(num_hours):
    if num_hours >= 2:
        return f'Ugh, I overslept. I didnt mean to nap for {num_hours} hours'
    return 'Im feeling refreshed after my 1 hour nap'
    
    
    
def is_funny(person):
    if person is 'tim': return False
    return True
    
from random import choice 
def laugh():
    return choice(('lol', 'tehe', 'haha'))