#infinite generator

def current_beat():
    nums = (1,2,3,4)
    i = 0
    while True:
        if i >= len(nums): #if i is greater than len(nums), reset i back to 0 so it can keep going forever.
            i = 0
        yield nums[i]
        i += 1
        
        
        


print(current_beat())
counter = current_beat()
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

