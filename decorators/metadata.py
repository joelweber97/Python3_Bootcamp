

def log_function_data(fn):
    def wrapper(*args, **kwargs):
        """I am a wrapper function"""
        print(f"you are about to call {fn.__name__}")
        print(f"Here's your documentation: {fn.__doc__}")
        return fn(*args, **kwargs)
    return wrapper
   

@log_function_data
def add(x,y):
    """Adds two numbers together"""
    return x + y
    
    
print(add(10,30))
#you are about to call add
#here's your documentation: adds two numbers together
#40
#everything you expect it to print out correctly.
#the issue arrises when using the following:
print(add.__doc__)
#I am a wrapper function
print(add.__name__)
#wrapper
print(help(add))
#add.__doc__ should return the documentation for add() not for wrapper.

