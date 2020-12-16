
def get_unlimited_multiples(val = 1):
    num = val
    while True:
        yield num
        num += val
        
        
        
        
sevens = get_unlimited_multiples(7)
print([next(sevens) for i in range(15)])