#decorators that take an argument
#not working code


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


