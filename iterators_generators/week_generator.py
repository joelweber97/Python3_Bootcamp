def week():
    d = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for i in d:
        yield i
        
        
days = week()
print(next(days))
print(next(days))