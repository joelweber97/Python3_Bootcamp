
#this enforces types on whatever function we define.



def enforce(*types):   
    def decorator(f):   #this decorator is what is actually being returned
        def new_func(*args, **kwargs):   #
            newargs = []  #convert args into something more mutable
            for (a,t) in zip(args, types):      #zip together the args and the types of each args   
                                                #would return ('hello', str), ('3', int) 
                                                #we then cast the value as the type into a new list.
                newargs.append( t(a))           #append  type(arg) to newargs.   #newargs.append(str(val))
            return f(*newargs, **kwargs)
        return new_func
    return decorator


#tests to see if this arguments in this function are a string and an int, respectively.
#if they are not, the function above will try to convert them to a string and an int.
   
@enforce(str, int)
def repeat_msg(msg, times):
    for time in range(times):
        print(msg)
        


repeat_msg('hello', '3')
repeat_msg(3, 10.7) 