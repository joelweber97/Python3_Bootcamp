def yes_or_no():
    val = 'yes'
    while True:
        yield val
        val = 'no' if val == 'yes' else 'yes'
        
        
y = yes_or_no()
print(next(y))
print(next(y))
print(next(y))
