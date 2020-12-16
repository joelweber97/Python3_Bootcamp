from random import randint

number = randint(1,10)
while True:
    guess = int(input('Please enter a number from 1 to 10: '))
    if guess < number:
        print('too low, guess again')
        guess = int(input())
    elif guess > number:
        print('too high, guess again')
        guess = int(input())
    else:
        print('you got it')
        play_again = input('Do you want to play again (y/n)? ')
        if play_again == 'y':
            number = randint(1,10)
            guess = None
        else:
            print('thank you for playing')
            break