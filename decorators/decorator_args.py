
#this works with greet('joel') because only one argument is provided by greet
#and only 1 is needed in wrapper.
#however, order() has 2 arguments which causes an error because wrapper() only can take in 1
# def shout(fn):
    # def wrapper(name):
        # return fn(name).upper()
    # return wrapper
    

#to solve this issue we use *args/*kwargs
def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper

@shout
def greet(name):
    return f'Hi, im {name}'
    
@shout
def order(main, side):
    return f'Hi, id like to have {main} with a side of {side}.'

@shout
def lol():
    return 'lol'

#greet and order are both being decorated by shout
print(greet('joel'))

#order only works when using *args, **kwargs because theres two arguments 
#that are being passed into wrapper, which onnly takes 1 argument so it throws an error
print(order('chicken', 'rice'))

#now that we don't need a single argument for wrapper() to work, we can also
#create a function that requires no arguments.
@shout
def lol():
    return 'lol'
    
print(lol())