

###########################################
#we can pass funcs as args to other funcs
def sum(n, func):
    total = 0               #the function being passed into sum(n, func) is defined below when we call the function sum(10, square)
    for i in range(1, n+1):      #for each in the range we take the square of i and add it to the total
        total += func(i)    
    return total
    
def square(x):
    return x*x

def cube(x):
    return x*x*x

print(sum(10, square)) #should return the sum of the first 10 squares
#prints the sum of  (0^2, 1^2, 2^2, 3^2, 4^2, 5^2, 6^2, 7^2, 8^2, 9^2, 10^2)

print(sum(3, cube))  #now we are passing the cube function into the sum function
#prints the sum of (0^3, 1^3, 2^3, 3^3)
####################################

#nesting a function inside another function

from random import choice
#all greet() does is call get_mood()
def greet(person):
    def get_mood():
        msg = choice(('Hello there ', 'Go away ', 'I love you '))
        return msg
    
    result = get_mood() + person  #the get_mood() function is getting called here and we're passing in the argument from the greet() function.
    return result
    
print(greet('Toby'))

############################################

#A function returning another function
from random import choice
def make_laugh_func():
    def get_laugh():
        l = choice(('HAHA', 'LOL', 'TEHE'))
        return l
        
    return get_laugh    #running make_laugh_func doesn't return what's in the nested function.
                        #it returns the get_laugh function itself.

laugh = make_laugh_func()
print(laugh())



##############################################
#similar to above but working with an argument

from random import choice

def make_laugh_at_func(person):
    def get_laugh():
        laugh = choice(('HAHA', 'LOL', 'TEHE'))
        return f"{laugh} {person}"      #use the persons name defined in the outter function to return it in the inner function.
                                        #person isn't defined or passed into get_laugh but we have access to it in the inner function
        
    return get_laugh
    
laugh_at = make_laugh_at_func('linda')
print(laugh_at())


