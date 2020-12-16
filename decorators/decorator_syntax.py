# @ sign syntactic sugar

def be_polite(fn):
    def wrapper():
        print('what a pleasure to meet you')
        fn()
        print('have a great day')
    return wrapper
    
@be_polite
def greet():
    print('my name is matt')
    
#we dont need to set greet=be_polite(greet) like we did in the dec script.
greet()

#the same goes for the rage function.
#we don't have to set rage = be_polite(rage).
#just give it the decorator and it will automatically run rage when we call rage()
@be_polite
def rage():
    print('i hate you')
    
rage()