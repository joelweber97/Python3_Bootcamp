class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high
        
    def __iter__(self):  #needs to return an iterator
        return self
        
    def __next__(self):
        if self.current < self.high:
            num = self.current
            self.current += 1
            return num
        raise StopIteration
        #this sets the current value to the low defined in Counter(low,high)
        #sets num to that current value
        #addes one to the current value
        #and returns num
        #needs to be in this order otherwise the value will be incremented before the first value is printed.
        
        
    

# c = Counter(0,10)
# iter(c)   #calls __iter__ on the Counter (c) defined above

for x in Counter(0,10):
    print(x)