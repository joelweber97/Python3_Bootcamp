#decorators that take an argument
#this particular example will make sure the first argument is 'burrito'

"""
#when we write
@decorator
def func(*args, **kwargs):
    pass
#we're really doing this
func = decorator(func)


#if we pass arguments into the decorator
#we write
@decorator_with_args(arg):
    def func(*args, **kwargs):
        pass
#what we're really doing is
func = decorator_with_args(arg)(func)
#which won't work
"""

from functools import wraps
#we need to add another layer to the standard decorator function
#in this case we'll call it inner and pass the function into it.
#then we'll define the wrapper function which takes the *args, **kwargs
def ensure_first_arg_is(val):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if args and args[0] != val:
                return f'Invalid! First arg needs to be {val}'
            return fn(*args, **kwargs)
        return wrapper
    return inner
    

@ensure_first_arg_is('burrito')
def fav_foods(*foods):
    print(foods)
#in the example above we are consturcting a decorator with that value ('burrito')
print(fav_foods('burrito', 'ice cream'))
print(fav_foods('ice cream', 'burrito'))
    
@ensure_first_arg_is(10)
def add_to_ten(num1, num2):
    return num1 + num2
    
print(add_to_ten(10,12))
print(add_to_ten(1,2))
    
