
#if an error is raised the whole thing will return True which will cause the entire thing to run again.
#if the number is entered correctly the else will run and break for the while loop so it will end and move on to the next bit of code


while True:
    try:
        num = int(input('Please enter a number: ')
    except ValueError:
        print('That is not a number')
    else:
        print('good job you entered a number')
        break
    finally:
        print('runs no matter what')
print('rest of game logic')
