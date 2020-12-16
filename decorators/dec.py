
#this takes in a function as an argument
#It also returns an nested function from inside.

def be_polite(fn):
    def wrapper():
        print('what a pleasure to meet you.')
        fn()
        print('have a great day')
    return wrapper
    
def greet():
    print('my name is colt')
#at this point the two functions above have nothing to do with each other
#until the greet function is fed into the be_polite function.

#greet is passed into be_polite
greet = be_polite(greet)
greet()
#this will print 3 lines
#what a pleasure to meet you
#my name is colt
#have a great day

#wrapping the wrapper function inside the be_polite function, saving it as a variable, and then calling that variable.
#we can also add another function
def rage():
    print('i hate you') 
polite_rage = be_polite(rage)
polite_rage()


