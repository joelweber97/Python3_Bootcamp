#first testing fibonachi using a regular function
#the memory required to store that list is massive
#a better option would be to create a generator that only
#stores 1 number at a time (using yield) and then moves on to the next
def fib_list(max):
    nums = []
    a,b = 0,1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a+b
    return nums


def fib_gen(max):
    x = 0
    y = 0
    count = 0
    while count < max:
        x, y = y, x + y
        yield x
        count +=1



# for n in fib_list(1000000):
    # print(n)
    
