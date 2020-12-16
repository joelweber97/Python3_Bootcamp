


def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError as err:
        print(err)
        print('Cannot divide by zero')
    except TypeError:
        print('A and B must be integer or float values')
        
        
        

