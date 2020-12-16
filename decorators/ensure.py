#force restrictions on certain arguments
#this one ensures there are no keyword arguemnts in a given function.


#for example
#decorator that prevents a fn from being called with any kwargs or any numerical arguments
from functools import wraps

def ensure_no_kwargs(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError('No kwargs allowed')
        return fn(*args, **kwargs) 
    return wrapper  


@ensure_no_kwargs
def greet(name):
    print(f'hi there {name}')


greet('Tony')    #prints out hi there tony since there are no kwargs
greet(name = 'tony')  #raises a value error because name = 'tony' is a kwarg