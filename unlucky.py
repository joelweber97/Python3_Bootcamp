
'''
for i in range(1,21):
    if i == 4 or i == 13:
        print(f'{i} is unlucky')
    elif i % 2 == 0:
        print(f'{i} is even')
    elif i % 2 == 1:
        print(f'{i} is odd')
    else:
        print('something went wrong')
'''

for i in range(1,21):
    if i == 4 or i == 13:
        state = 'unluck'
    elif i % 2 == 0:
        state = 'even'
    elif i % 2 == 1:
        state = 'odd'
    print(f'{i} is {state}')