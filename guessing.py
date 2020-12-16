from random import randint

number = randint(1,10)
guess = int(input('Please enter a number from 1 to 10: '))
while guess != number:
    if guess < number:
        print('too low, guess again')
        guess = int(input())
    elif guess > number:
        print('too high, guess again')
        guess = int(input())
print('you got it')