#a great use for decorators is timing.
#before we had to write lines to do timing for each thing we wanted to time.
#we can create a timing function and wrap that function around the thing we want timed.
from time import time
from functools import wraps
def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = time()
        result = fn(*args, **kwargs)
        end = time()
        print(f"executing {fn.__name__}")
        print(f"time elapsed {end - start}")
        return result
    return wrapper


#simple decorator thats easy to throw in front of any function we want timed.
@speed_test
def sum_nums_gen():
    return sum(x for x in range(90000000))  
print(sum_nums_gen())

@speed_test
def sum_nums_list():
    return sum([x for x in range(90000000)])
print(sum_nums_list())

