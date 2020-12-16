class GrumpyDict(dict):
    #don't need to define our own init. We can instead use the existing dict__init__()
    def __repr__(self):
        print('NONE OF YOUR BUSINESS')
        return super().__repr__()   #this will call the dictionary version of repr
        
    def __missing__(self, key):
        print(f'YOU WANT {key}, WELL IT AINT HERE')
        
    def __setitem__(self, key, value):
        print('you want to change the dictionary')
        print('ok fine')
        super().__setitem__(key, value)   #if we don't call this the k/v will not be set for data.
        #can call special dunder methods on parent classes. In this case super() is being calling __setitem__ on the dict class that was inherited by GrumpyDict
        
    def __contains__(self, item):   #this is supposed to return true or false if the value is contained in it.
        return 'No it aint in here'   
        
data = GrumpyDict({'first': 'Tom', 'animal':'cat'})
print(data)

print(data['city'])  #theres no city key so the __missing__ method will automatically be called and run on that key.


data['city'] = 'Tokyo' #now the city is tokyo
print(data)