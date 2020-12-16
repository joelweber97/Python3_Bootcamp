import random


print('Rock....')
print('Paper....')
print('Scissors....')

#v3
p1 = input('Player 1 chooses: ').lower()
computer = ['rock', 'paper','scissors']
p2 = random.choice(computer)
print(f'computer plays {p2} ')
if p2 == p1:
    print('it is a tie')
elif p1 == 'rock':
    if p2 == 'scissors':
        print('p1 wins')
    else:
        print('computer wins')
elif p1 == 'paper':
    if p2 == 'rock':
        print('p1 wins')
    else:
        print('computer wins')
elif p1 == 'scissors':
    if p2 == 'rock':
        print('computer wins')
    else:
        print('p1 wins')
else:
    print('something went wrong')


'''
#V2
p1 = input('Player 1 chooses: ').lower()
p2 = input('Player 2 chooses: ').lower()


if p2 == p1:
    print('it is a tie')
elif p1 == 'rock':
    if p2 == 'scissors':
        print('p1 wins')
    elif p2 == 'paper':
        print('p2 wins')
elif p1 == 'paper':
    if p2 == 'rock':
        print('p1 wins')
    elif p2 == 'scissors':
        print('p2 wins')
elif p1 == 'scissors':
    if p2 == 'rock':
        print('p2 wins')
    elif p2 == 'paper':
        print('p1 wins')
else:
    print('something went wrong')
'''

'''
#V1
p1 = input('Player 1 chooses: ').lower()
p2 = input('Player 2 chooses: ').lower()


if p1 == 'rock' and p2 == 'scissors':
    print('P1 wins')
elif p1 == 'rock' and p2 == 'paper':
    print('P2 wins')
elif p1 == 'paper' and p2 == 'scissors':
    print('P2 wins')
elif p1 == 'paper' and p2 == 'rock':
    print('P1 wins')   
elif p1 == 'scissors' and p2 == 'rock':
    print('P2 wins')
elif p1 == 'scissors' and p2 == 'paper':
    print('P1 wins')
elif p1 == p2:
    print('It is a tie')
else:
    print('something went wrong')
'''
 
