'''
def add_positive_numbers(x,y):
    assert x>0 and y>0, 'Both numbers must be positive!'
    return x + y
 
 
print(add_positive_numbers(1,3))

print(add_positive_numbers(0, 8))

print(add_positive_numbers(-3, -1))
'''

def eat_junk(food):
    assert food in [
        'pizza', 
        'ice cream', 
        'candy', 
        'fried butter'
        ], 'Food must be a junk food'
    return f"nom nom nom i am eating {food}"
    
    
food = input('enter a food please ')
print(eat_junk(food))