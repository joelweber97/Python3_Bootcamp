

def get_multiples(value = 1, num = 10):
    i = 1
    while i <= num:
        yield value * i
        i += 1
        
dm = get_multiples()
dm2 = get_multiples(2,3)
print(list(dm))
print(list(dm2))
dm3 = get_multiples(5, 100)
print(list(dm3))