
print('Rock....')
print('Paper....')
print('Scissors....')

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

 
