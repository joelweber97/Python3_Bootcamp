
'''
from functools import wraps
def double_return(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        val = fn(*args, **kwargs)
        return [val, val]
    return wrapper
        
        
        
@double_return
def add(x,y):
    return x+y
    
    
@double_return
def greet(name):
    return 'Hi Im ' + name
    
print(greet('tony'))
print(add(3,4))

'''

'''
from functools import wraps
def ensure_fewer_than_three_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        length = len(args)
        if length < 3:
            return fn(*args, **kwargs)
        else:
            return 'Too many arguments!'
    return wrapper


@ensure_fewer_than_three_args
def add(*args):
    return sum(args)
    
print(add(1,2,3))
print(add(1,2))
'''
'''

from functools import wraps


def ensure_authorized(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs.get('role') == 'admin':
            return fn(*args, **kwargs)
        return 'Unauthorized'
    return wrapper


@ensure_authorized
def show_secrets(*args, **kwargs):
    return "Shh! Don't tell anybody!"



print(show_secrets(role='admin'))
print(show_secrets(role = 'nobody'))
'''


from functools import wraps
from time import sleep

def delay(val):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print(f'Waiting {val}s before running {fn.__name__}')
            sleep(val)
            return fn(*args, **kwargs)
        return wrapper
    return inner
    
    
@delay(3)
def say_hi():
    return 'hi'




print(say_hi())

